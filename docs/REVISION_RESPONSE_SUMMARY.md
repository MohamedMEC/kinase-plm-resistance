# Response to Reviewer — Status of Each Point

This tracks the 12 major points plus presentation issues. Updated after rerunning the
MET-side analyses in the original Kaggle environment (real per-mutation/per-drug data),
which closed three points previously flagged as requiring that environment.

## Closed in this revision

**Point 1 — MET replication incomplete.** §2.1 retitled "Partial reproduction," language changed
from "confirms correct implementation" to "confirms repeatable, not correct." All 7 candidate
sources of the ρ=0.9199 gap you listed are now named explicitly (construct sequence, numbering,
masking convention, checkpoint version, precision, preprocessing, mutation filtering), with the
one we tested (scoring convention) distinguished from the six we haven't.

**Point 2 — untreated-vs-treated gap only shown for ESM-1b.** Closed via Kaggle rerun. Recomputed
for all four model sizes ($n=4{,}595$): ESM-1b $\rho=0.500$, ESM-2-150M $\rho=0.469$, ESM-2-650M
$\rho=0.500$, ESM-2-3B $\rho=0.500$, each roughly double its own drug-treated Fisher-z average
(gaps of 0.246–0.270). New §2.1b reports this directly. Three of the four untreated values round
to an identical 0.500 at 3 d.p.; the underlying values are distinct (0.49954, 0.50045, 0.50030)
and are reported without further rounding.

**Point 3 — MET Wilcoxon independence assumption.** Closed via Kaggle rerun. A hierarchical
bootstrap resampling mutations (not drug-rows), 10,000 resamples of the full 5,434-mutation
panel, confirms ESM-1b's advantage over ESM-2-150M (+0.040, 95% CI [0.025, 0.055]), ESM-2-650M
(+0.023, CI [0.011, 0.035]), and ESM-2-3B (+0.015, CI [0.005, 0.027]) — all CIs exclude zero.
Reported in §2.2, replacing the prior "we were not able to run this" disclosure.

**Point 4 (both halves) — baseline comparisons need formal tests.**
- *EGFR/ABL1 half:* paired bootstrap of ESM-1b vs. every other predictor, including all 3
  non-learned baselines individually — `egfr_abl1_paired_esm1b_vs_baselines.csv`. All 18
  comparisons cross zero.
- *MET half, closed via Kaggle rerun:* paired bootstrap of ESM-1b vs. all 8 MET baselines
  (`met_paired_esm1b_vs_baselines.csv`), BH-corrected across the 8 tests. Significant for 6 of 8:
  distance to reference ligand, distance to ATP pocket, aggregate stability estimate ($ddG\_all$),
  pocket volume, hydrophobicity, and polarity (all adjusted $p \leq 0.001$). NOT significant for
  BLOSUM62 (adjusted $p=0.237$) or the point-mutation stability estimate/$dddG$ (adjusted
  $p=0.087$). This softens the prior "exceeds every baseline" framing in §2.2 and Figure 2's
  caption to distinguish numerically-higher-but-not-confirmed (2 baselines) from
  statistically-confirmed (6 baselines).

**Point 5 — pooled MET correlation misleading.** Figure 2 caption and §2.2 text now explicitly
label it "descriptive," disclose the mutation-repetition-across-drugs issue, and point to the
per-drug analysis (Fig. 1) as primary.

**Point 6 — structural baseline not compound-specific.** Renamed throughout to "distance to
reference ligand," with an explicit paragraph in §3.3 explaining the mismatch (one reference
structure vs. many aggregated compounds per mutation) rather than implying compound-specificity.

**Point 7 — "genuinely matched" overstated.** Reworded to "document- and format-matched
observational pairs" everywhere, with the specific caveats (assay protocol, cell system,
construct, incubation time, lab conditions) spelled out in §2.3 and §4.1.

**Point 8 — EGFR/ABL1 underpowered, needs more diagnostics.** Added, all computed from the
corrected per-mutation CSV (`egfr_abl1_final_results_document_matched (1).csv`):
- Exact permutation tests (720 for EGFR, 362,880 for ABL1; Monte Carlo 200k for Combined) —
  `egfr_abl1_permutation_tests.csv`
- Leave-one-out / jackknife influence analysis — `egfr_abl1_leave_one_out.csv`
- Mutation-labeled scatterplots — Figure~\ref{figScatter} (ESM-1b and ESM-2-150M × ABL1/EGFR)
- Post-hoc power analysis — `power_analysis.csv` (the standout number: 8–13% power at n=6–15
  to detect a MET-sized effect; ~117 mutations needed for 80% power)

**Point 9 — combined n=15 questionable.** ABL1 and EGFR are now presented as the primary
within-kinase analyses; Combined is explicitly relabeled "secondary sensitivity check," with the
opposite-sign example (ESM-1b: ABL1 +0.233 vs. EGFR −0.543) stated directly as the reason.

**Presentation — Figure 3 clarity.** Regenerated with shaded background bands separating the
three groupings and explicit "(primary)" / "(secondary)" labels.

**Presentation — PDF metadata, "5,764 vs 5,434", conclusion scope, Figure 2 warning, intro/discussion
trims.** All addressed directly in the .tex.

## Still open

**Point 10 — itemized 5,764→5,434 MET exclusion audit.** Attempted via Kaggle rerun but the
audit script's "start (all scanned variants)" step reported `n_remaining=5434` instead of the
expected 5,764, with zero reduction from the "missing ESM-1b score" step
(`met_exclusion_audit.csv`). This means the variable the audit cell operated on (`mut_panel`) was
already pre-filtered to 5,434 rows before that cell ran — the actual 5,764→5,434 filtering
happens earlier in the pipeline, at a step not currently instrumented to log intermediate counts.
Closing this requires identifying the exact point where the raw 5,764-row scanned-variant panel
is first loaded (before any merge with model scores) and re-running the audit from there. §4.1
now states this explicitly rather than presenting a misleading "audit complete" result.

**Point 12 — public DOI-assigned repository.** Depositing code/data/checkpoints/seeds on Zenodo +
GitHub (or equivalent) is a publishing action, not a computation, and remains a pre-submission
task for the author.

## Summary

10 of 12 major points, plus all presentation issues, are closed in this revision. The two
remaining items (exclusion audit, public repository) are both well-specified and neither requires
new analysis — one requires locating an earlier step in the existing pipeline, the other is an
administrative deposit step.
