# Final Analysis Plan & Design History

**Compiled:** August 2, 2026
**Status:** Retrospective consolidation, compiled after primary analysis was run. Not a literal prospective OSF pre-registration. See "Honesty Statement" below before citing this as pre-registration in the manuscript.

---

## Honesty Statement

This document consolidates the analysis plan for the study below into a single, dated record. Most of its core elements — research question, datasets, model list, baseline list, statistical tests, and the reliability threshold — were genuinely decided and written down (in `Q1_Research_Roadmap_DTA.md`, Phase 3 "Finalized Analysis Plan," 10 points) **before** the EGFR/ABL1 computational pipeline was built and run, and before the MET validation pipeline was executed. That plan is reproduced faithfully in Section 3 below.

One material deviation from strict pre-specification: **the EGFR/ABL1 mutation panel was expanded mid-analysis**, after an initial n=5 (ABL1) / n=3 (EGFR) run showed underpowered, hard-to-interpret results. This is disclosed explicitly in Section 5 rather than folded silently into the "final" panel. The expansion criterion was independent of outcome — added mutations (EGFR L861Q/G719C/G719S; ABL1 F317L/F317I/H396P/Q252H) were selected because they are literature-documented driver or resistance mutations with real ChEMBL activity data, not because of which direction they would push the correlation — but this is still a data-dependent stopping/expansion decision and should be reported as such, not presented as if the final n was fixed in advance.

Where this document says a decision was "pre-specified," that claim is checkable against the dated Phase 3 section of the roadmap, which predates the relevant code being run (confirmed via the tracker's experiment log). Where a decision was made adaptively, it is labeled as such.

---

## 1. Research Question (locked)

> Does protein-language-model scale improve zero-shot identification of drug-specific kinase-inhibitor resistance beyond what simple non-learned baselines (substitution matrices, conservation, structural proximity to the binding pocket) already capture, or is drug-specific resistance simply not recoverable from sequence information regardless of model sophistication?

Secondary question, addressed via the untreated-vs-treated MET contrast: does a PLM's zero-shot score track general evolutionary/structural fitness constraint better than it tracks drug-specific resistance pressure (per Estevam et al. 2025's finding that this gap exists for MET)?

## 2. Datasets (pre-specified)

- **MET**: Estevam et al. 2025 (eLife 13:RP101882) deep mutational scanning data, `fraser-lab/MET_kinase_Inhibitor_DMS` (GitHub, MIT license). 5,764 kinase-domain variants × 9 inhibitors (cabozantinib, capmatinib, crizotinib, glesatinib, glumetinib, merestinib, NVP-compound, savolitinib, tepotinib). Drug-treated fitness (`mean` column) as the dependent variable; untreated/DMSO fitness (`WT_rosace_effect_all.tsv`) for the treated-vs-untreated contrast.
- **EGFR**: UniProt P00533, kinase-domain window (696–1018, ESM-1b-length-safe), mutations T790M/C797S/L858R (original panel) plus L861Q/G719C/G719S (expansion — see Section 5). ChEMBL target CHEMBL203.
- **ABL1**: UniProt P00519 isoform 1b (clinical numbering, 1130aa), kinase-domain window (92–643), mutations M244V/G250E/Y253F/Y253H/E255K/E255V/T315I/M351T/F359V/F359I (original panel) plus F317L/F317I/H396P/Q252H (expansion). ChEMBL target CHEMBL1862.

## 3. Models tested (pre-specified)

- ESM-1b (650M, Rives et al. 2021) — masked-marginal log-likelihood-ratio scoring (Meier et al. 2021, NeurIPS)
- ESM-2 at 150M, 650M, 3B (identical scoring method, held constant across sizes)
- Confirmed via direct reading of Estevam et al.'s methods: they tested ESM-1b only, never any ESM-2 variant — this is the specific model-scale extension this study contributes.

## 4. Baselines tested (pre-specified in kind; exact implementation finalized alongside execution)

- **BLOSUM62** substitution score (wt→mut), no structural information
- **Distance-to-inhibitor**: minimum heavy-atom distance from the mutated residue to the bound inhibitor, computed from real PDB structures — EGFR: 6LUD (L858R/T790M/C797S + osimertinib, chosen because it matches the cascade panel exactly), ABL1: 1IEP (WT + imatinib)
- **Distance-to-ATP-pocket**: minimum heavy-atom distance from the mutated residue to a validated set of four catalytic residues per kinase (EGFR: K745/E762/M793/D855; ABL1: K271/E286/M318/D381), sourced from independent literature search, not inferred from the same structures used for the inhibitor-distance baseline
- For MET only: Estevam et al.'s own precomputed structural/biophysical features (ΔΔG, distance-to-ATP, pocket volume, RMSF, hydrophobicity, polarity), reused rather than recomputed, since they were already validated by the original authors

Numbering convention for both EGFR and ABL1 structures was verified directly against known-invariant catalytic residue identities before any distance was trusted (documented in `research_workflow_tracker.md` §7b) — this is a methodological safeguard, not itself part of the pre-specified plan, added during execution because it is standard good practice for structure-based analysis.

## 5. Deviation: mutation panel expansion (disclosed, not pre-specified)

**Original panel (pre-specified):** EGFR T790M/C797S/L858R (3 mutations/cascade steps); ABL1 M244V/G250E/Y253F/Y253H/E255K/E255V/T315I/M351T/F359V/F359I (10 mutations). This is the panel described in Phase 3's "Concrete Pipeline" before execution began.

**What happened:** initial correlations on this panel used only the subset clearing the ≥10-matched-pairs reliability threshold — n=5 for ABL1, n=3 for EGFR. These were judged too underpowered to interpret (single-digit n, results highly sensitive to individual data points).

**Adaptive decision:** panel expanded by searching the literature for additional, independently-documented EGFR driver mutations (L861Q, G719C, G719S — confirmed via WebSearch as legitimate activating mutations, same category as L858R, not selected for expected correlation direction) and ABL1 resistance mutations (F317L/F317I — confirmed dasatinib-resistance; H396P, Q252H — confirmed imatinib-resistance via case-report literature), then rerunning the identical pipeline. This raised the reliable-n to 9 (ABL1) and 6 (EGFR).

**Why this is disclosed rather than hidden:** the initial n=5 ABL1 result showed a sign pattern (ESM-1b positive, ESM-2 negative) that superficially resembled an interesting cross-kinase reversal of the MET finding. Expansion weakened this pattern substantially (ESM-1b ρ dropped from +0.60 to +0.25; ESM-2-150M from −0.70 to 0.00), consistent with the initial pattern being largely small-sample noise. Reporting only the final n=9/n=6 numbers without disclosing this history would hide a meaningful part of the story — that the "interesting" early result did not survive more data. The manuscript should report both stages briefly, framed as a worked demonstration of why n=5 correlations shouldn't be trusted, not as two independent studies.

## 6. Statistical methods (pre-specified)

- Spearman rank correlation (ρ) between each predictor and the outcome (MET: drug-treated DMS fitness; EGFR/ABL1: median matched-pair ΔpIC50), given no assumption of linearity and small-to-moderate N
- Reliability threshold: matched_pairs ≥ 10 for EGFR/ABL1 (chosen ad hoc, stated as such, not derived from a power calculation)
- Per-drug correlations for MET (not pooled first), aggregated via Fisher-z transform, matching the critique that pooling across drugs before computing correlation would obscure per-drug heterogeneity
- Paired Wilcoxon signed-rank test for model-vs-model comparisons (MET: ESM-1b vs. each ESM-2 size, across the 9 drugs)
- Bootstrap 95% CIs (10,000 resamples, percentile method) added for the EGFR/ABL1/combined correlations, computed post hoc after the point estimates were already known — this is a transparency addition, not a pre-specified test, and confirms rather than changes the conclusion (every CI crosses zero)
- Benjamini-Hochberg FDR correction was planned (finalized-plan point 8) but not applied to the EGFR/ABL1 results, since nothing reached nominal significance (α=0.05) to begin with — correction cannot make a non-significant result more or less significant, only adjusts which of several *significant* results survive multiple comparisons

## 7. Locked results (as of this document's date)

**MET (powered, significant):** ESM-1b beats ESM-2 at every tested size (vs. 650M and 3B: 9/9 drugs, paired Wilcoxon p=0.0039 both; vs. 150M: 8/9, p=0.0078). ESM-1b beats all non-learned baselines (pooled ρ=0.257 vs. BLOSUM62 ρ=0.175, structural/biophysical features ρ≈−0.17 to 0.06). Scale helps monotonically within ESM-2 alone, never catches ESM-1b.

**EGFR/ABL1 (underpowered, null across every predictor tested):** all 7 predictors (4 ESM sizes, BLOSUM62, distance-to-inhibitor, distance-to-ATP-pocket) non-significant for ABL1 (n=9 reliable), EGFR (n=6), and combined (n=15); every 95% bootstrap CI crosses zero. Largest point estimate: ABL1 distance-to-inhibitor, ρ=+0.485 (p=0.185, 95% CI [−0.32, +1.00]).

## 8. Interpretation locked for the manuscript

MET is the paper's powered, confident finding. EGFR/ABL1 is reported as an honest generalization check that the available clinically-characterized mutation panel (6–15 usable mutations even after literature-justified expansion) cannot resolve, for any predictor tried — framed as a genuine DMS-vs-ChEMBL statistical-power asymmetry, not a failure of the PLM approach specifically. This asymmetry (DMS: many mutations, few drugs; ChEMBL: few characterized mutations, many drugs per mutation) is itself a citable methodological point about why these two data sources aren't interchangeable for this class of cross-model comparison.

---

*Companion documents: `Q1_Research_Roadmap_DTA.md` (full roadmap and revision history), `research_workflow_tracker.md` (experiment log, bug log, adversarial novelty-search log), `egfr_abl1_final_results_with_baselines.csv` (full results table), `egfr_abl1_bootstrap_cis.csv` (bootstrap CI table), `met_esm.ipynb` (MET validation notebook).*
