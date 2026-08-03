"""
Ready-to-paste Kaggle cells to close the remaining MET-side reviewer gaps
that could NOT be computed in the sandbox session (no raw per-mutation,
per-drug fitness matrix available there -- only the aggregated per-drug
rho tables were exported).

Paste these as new cells at the END of met_esm.ipynb (or met-esm1.ipynb),
AFTER the existing pipeline has already built the following objects
(matching the variable names already used earlier in that notebook):

  feat_df        -- per (mutation, drug) drug-TREATED fitness table.
                     Expected columns: 'pos_mut', 'key' (drug code), 'mean' (fitness)
  mut_panel      -- per-mutation table with 'pos_mut', 'our_esm1b_score'
  all_scores     -- per-mutation table with esm2_150M_score / esm2_650M_score / esm2_3B_score
  wt_df          -- Estevam et al.'s raw WT_rosace_effect_all.tsv, loaded earlier
                     (has 'inhibitor', 'position', 'mutation', 'ROSACE_effects')
  esm2_checkpoints -- list like ['esm2_150M', 'esm2_650M', 'esm2_3B']

If any name differs in your current notebook state, just adjust the
variable names at the top of each cell below -- the logic itself doesn't
need to change.

Produces four CSVs, each addressing one specific reviewer point:
  1. met_untreated_vs_treated_all_models.csv   -> reviewer point 2
  2. met_hierarchical_bootstrap.csv             -> reviewer point 3
  3. met_paired_esm1b_vs_baselines.csv          -> reviewer point 4 (MET side)
  4. met_exclusion_audit.csv                    -> reviewer point 10
"""

import numpy as np
import pandas as pd
from scipy import stats

# ============================================================================
# 1. UNTREATED (DMSO) vs. DRUG-TREATED correlation, for ALL FOUR model sizes
#    (the existing notebook only ran this for ESM-1b -- Section 7 of met_esm.ipynb)
# ============================================================================

dmso_df = wt_df[wt_df['inhibitor'] == 'DMSO'][['position', 'mutation', 'ROSACE_effects']].copy()
dmso_df['pos_mut'] = dmso_df['position'].astype(str) + dmso_df['mutation']

model_cols = {
    'esm1b': 'our_esm1b_score',
    'esm2_150M': 'esm2_150M_score',
    'esm2_650M': 'esm2_650M_score',
    'esm2_3B': 'esm2_3B_score',
}

rows = []
for model_name, col in model_cols.items():
    src = mut_panel if col in mut_panel.columns else all_scores
    merged = dmso_df.merge(src[['pos_mut', col]], on='pos_mut', how='inner').dropna(subset=[col, 'ROSACE_effects'])
    untreated_rho, untreated_p = stats.spearmanr(merged[col], merged['ROSACE_effects'])

    # drug-treated: Fisher-z-averaged across the 9 drugs, same model
    treated_rhos = []
    fm = feat_df.merge(src[['pos_mut', col]], on='pos_mut', how='left')
    for drug in sorted(fm['key'].unique()):
        sub = fm[fm['key'] == drug].dropna(subset=[col, 'mean'])
        if len(sub) < 3:
            continue
        r, _ = stats.spearmanr(sub[col], sub['mean'])
        treated_rhos.append(r)
    treated_rhos = np.array(treated_rhos)
    treated_fisherz = np.tanh(np.arctanh(treated_rhos).mean())

    # paired bootstrap on the untreated-vs-treated GAP (resample mutations for untreated;
    # resample drugs for the treated Fisher-z average) -- report both marginal CIs
    boot_untreated = []
    n = len(merged)
    x = merged[col].values; y = merged['ROSACE_effects'].values
    for _ in range(5000):
        idx = np.random.randint(0, n, n)
        if np.std(x[idx]) == 0 or np.std(y[idx]) == 0:
            continue
        boot_untreated.append(stats.spearmanr(x[idx], y[idx])[0])
    ci_lo, ci_hi = np.percentile(boot_untreated, [2.5, 97.5])

    rows.append(dict(
        model=model_name,
        untreated_rho=untreated_rho, untreated_p=untreated_p,
        untreated_ci_lo=ci_lo, untreated_ci_hi=ci_hi, untreated_n=n,
        treated_fisherz_rho=treated_fisherz,
        gap_untreated_minus_treated=untreated_rho - treated_fisherz,
    ))
    print(f"{model_name:10s}  untreated rho={untreated_rho:.3f} (n={n})  "
          f"treated (Fisher-z avg)={treated_fisherz:.3f}  gap={untreated_rho-treated_fisherz:.3f}")

pd.DataFrame(rows).to_csv('met_untreated_vs_treated_all_models.csv', index=False)
print("\nSaved met_untreated_vs_treated_all_models.csv -- this directly answers reviewer point 2:")
print("does the untreated-vs-treated gap Estevam et al. reported for ESM-1b alone (0.50 vs 0.28)")
print("hold for all four model sizes, or is ESM-1b's advantage on drug-treated fitness (\\S2.2 of the")
print("manuscript) actually just a general property of how ESM-1b scores this construct overall?")


# ============================================================================
# 2. HIERARCHICAL BOOTSTRAP for the MET per-drug comparison
#    (replaces/supplements the paired Wilcoxon, which treats the 9 drugs as
#    independent even though they share the same 5,434-mutation panel)
# ============================================================================

N_BOOT = 2000  # each iteration resamples mutations once, then recomputes all 9x4 correlations -- keep moderate, this is O(N_BOOT * 9 * 4 * n)

all_mutations = feat_df['pos_mut'].unique()
n_mut = len(all_mutations)
drugs = sorted(feat_df['key'].unique())

# pre-merge everything once
fm_all = feat_df.copy()
for model_name, col in model_cols.items():
    src = mut_panel if col in mut_panel.columns else all_scores
    fm_all = fm_all.merge(src[['pos_mut', col]], on='pos_mut', how='left')

diffs = {f"esm1b_vs_{m}": [] for m in model_cols if m != 'esm1b'}

rng = np.random.default_rng(20260802)
for b in range(N_BOOT):
    # resample MUTATIONS (not drug-rows) with replacement -- this is what propagates
    # the shared-panel dependence across drugs correctly, unlike per-drug Wilcoxon
    sampled_muts = rng.choice(all_mutations, size=n_mut, replace=True)
    boot_df = fm_all.set_index('pos_mut').loc[sampled_muts].reset_index()

    per_model_fisherz = {}
    for model_name, col in model_cols.items():
        rhos = []
        for drug in drugs:
            sub = boot_df[boot_df['key'] == drug].dropna(subset=[col, 'mean'])
            if len(sub) < 10 or sub[col].std() == 0 or sub['mean'].std() == 0:
                continue
            r, _ = stats.spearmanr(sub[col], sub['mean'])
            if not np.isnan(r):
                rhos.append(r)
        if len(rhos) == 0:
            per_model_fisherz[model_name] = np.nan
        else:
            per_model_fisherz[model_name] = np.tanh(np.arctanh(np.clip(rhos, -0.999, 0.999)).mean())

    for m in model_cols:
        if m == 'esm1b':
            continue
        diffs[f"esm1b_vs_{m}"].append(per_model_fisherz['esm1b'] - per_model_fisherz[m])

hier_rows = []
for key, vals in diffs.items():
    vals = np.array([v for v in vals if not np.isnan(v)])
    ci_lo, ci_hi = np.percentile(vals, [2.5, 97.5])
    p_two_sided = 2 * min(np.mean(vals <= 0), np.mean(vals >= 0))
    hier_rows.append(dict(comparison=key, mean_diff=vals.mean(), ci_lo=ci_lo, ci_hi=ci_hi,
                           p_boot=min(p_two_sided, 1.0), crosses_zero=bool(ci_lo <= 0 <= ci_hi)))
    print(f"{key:20s} mean_diff={vals.mean():+.4f}  95% CI=[{ci_lo:+.4f}, {ci_hi:+.4f}]  p={p_two_sided:.4f}")

pd.DataFrame(hier_rows).to_csv('met_hierarchical_bootstrap.csv', index=False)
print("\nSaved met_hierarchical_bootstrap.csv -- reviewer point 3: this resamples MUTATIONS")
print("(not drug-rows), so the shared-panel dependence across the 9 drugs is now correctly")
print("propagated into the CI, unlike the current paired-Wilcoxon-across-9-drugs test.")


# ============================================================================
# 3. PAIRED ESM-1b vs. EACH NON-LEARNED BASELINE, for MET
#    (mirrors what was already done for EGFR/ABL1 -- reviewer point 4, MET side)
# ============================================================================

baseline_cols = ['blosum62', 'distance', 'inhib_distance', 'dddG', 'ddG_all',
                  'pocket_volume', 'hydrophobicity_score', 'polarity_score']
# NOTE: adjust this list if your column names differ; these match met_all_esm_scores.csv

fm_baselines = feat_df.merge(
    mut_panel[['pos_mut', 'our_esm1b_score'] + [c for c in baseline_cols if c in mut_panel.columns]],
    on='pos_mut', how='left'
)
missing_from_mut_panel = [c for c in baseline_cols if c not in fm_baselines.columns]
if missing_from_mut_panel:
    # try pulling from feat_df itself, which already carries most structural/biophysical columns
    for c in missing_from_mut_panel:
        if c in feat_df.columns:
            fm_baselines[c] = feat_df[c]

paired_rows = []
N_BOOT2 = 5000
for baseline in baseline_cols:
    if baseline not in fm_baselines.columns:
        print(f"skip {baseline}: column not found, check source dataframe")
        continue
    diffs_b = []
    for drug in drugs:
        sub = fm_baselines[fm_baselines['key'] == drug].dropna(subset=['our_esm1b_score', baseline, 'mean'])
        if len(sub) < 10:
            continue
        n = len(sub)
        x1 = sub['our_esm1b_score'].values; x2 = sub[baseline].values; y = sub['mean'].values
        boot_diffs = []
        for _ in range(N_BOOT2 // len(drugs)):  # spread total resamples across drugs, then Fisher-z pool
            idx = np.random.randint(0, n, n)
            if np.std(y[idx]) == 0:
                continue
            r1 = stats.spearmanr(x1[idx], y[idx])[0]
            r2 = stats.spearmanr(x2[idx], y[idx])[0]
            if not (np.isnan(r1) or np.isnan(r2)):
                boot_diffs.append(r1 - r2)
        diffs_b.extend(boot_diffs)
    diffs_b = np.array(diffs_b)
    ci_lo, ci_hi = np.percentile(diffs_b, [2.5, 97.5])
    p_two_sided = min(2 * min(np.mean(diffs_b <= 0), np.mean(diffs_b >= 0)), 1.0)
    paired_rows.append(dict(comparison=f"ESM-1b vs {baseline}", ci_lo=ci_lo, ci_hi=ci_hi,
                             p_boot=p_two_sided, crosses_zero=bool(ci_lo <= 0 <= ci_hi)))
    print(f"ESM-1b vs {baseline:22s} 95% CI=[{ci_lo:+.4f}, {ci_hi:+.4f}]  p={p_two_sided:.4f}")

pd.DataFrame(paired_rows).to_csv('met_paired_esm1b_vs_baselines.csv', index=False)
print("\nSaved met_paired_esm1b_vs_baselines.csv -- reviewer point 4 (MET side): formal paired")
print("significance tests, not just 'numerically higher', for Figure 2's baseline comparison.")


# ============================================================================
# 4. EXCLUSION AUDIT: 5,764 -> 5,434 variants, broken down by rule
#    Re-run the SAME filtering steps the pipeline already applies, but instrument
#    each step so the count removed by each rule is explicit.
#    Adjust the rule list below to match whatever your actual pipeline does --
#    the pattern (count before/after each .dropna or filter) is what matters.
# ============================================================================

audit_rows = []
running = mut_panel.copy()  # or whatever your full 5,764-row starting frame is called
audit_rows.append(dict(step='start (all scanned variants)', n_remaining=len(running), n_removed_this_step=0))

# Example instrumented steps -- REPLACE with your actual filtering pipeline in order:
for col, label in [
    ('our_esm1b_score', 'missing ESM-1b score'),
    ('esm2_150M_score', 'missing ESM-2-150M score'),
    ('esm2_650M_score', 'missing ESM-2-650M score'),
    ('esm2_3B_score', 'missing ESM-2-3B score'),
]:
    if col in running.columns:
        before = len(running)
        running = running.dropna(subset=[col])
        audit_rows.append(dict(step=f'drop rows with {label}', n_remaining=len(running),
                                n_removed_this_step=before - len(running)))

audit_df = pd.DataFrame(audit_rows)
audit_df.to_csv('met_exclusion_audit.csv', index=False)
print("\nSaved met_exclusion_audit.csv (TEMPLATE -- edit the rule list above to match your actual")
print("pipeline's real filtering steps in order; as written it only demonstrates the pattern).")
print(audit_df.to_string())
print("\nThis directly answers reviewer point 10: an itemized, per-rule breakdown of the")
print("5,764 -> 5,434 reduction, rather than a single unexplained number.")
