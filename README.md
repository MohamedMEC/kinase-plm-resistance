# Does Protein-Language-Model Scale Improve Zero-Shot Identification of Kinase-Inhibitor Resistance?

Code, notebooks, processed results, and manuscript source for a study testing zero-shot
masked-marginal scoring from ESM-1b and three ESM-2 sizes (150M, 650M, 3B) against
measured kinase-inhibitor resistance data for MET, EGFR, and ABL1, benchmarked against
non-learned structural and sequence baselines.

## Repository structure

```
repo/
├── manuscript/          Manuscript source (sn-jnl LaTeX) and bibliography
│   ├── manuscript_sn.tex
│   └── sn-bibliography.bib
├── notebooks/            Kaggle/Colab notebooks used for scoring and analysis
│   ├── 00_rdkit_intro_demo.ipynb
│   ├── 01_met_esm_scoring.ipynb
│   ├── 02_met_esm_validation.ipynb
│   ├── 03_egfr_abl1_esm_scoring.ipynb
│   └── Video0_future_drug_discovery_KAGGLE.ipynb
├── scripts/               Standalone analysis / figure-generation scripts
│   ├── met_baseline_and_gap_bootstrap_CORRECTED.py   <- authoritative bootstrap procedure
│   ├── met_baseline_bootstrap_round1_SUPERSEDED.py    <- earlier, methodologically flawed version, kept for provenance
│   ├── figure3_forest_plot_generate.py
│   └── rdkit_demo.py
├── results/                Processed result tables (CSV) referenced in the manuscript
└── docs/                   Planning, literature review, and revision-history notes (not part of the manuscript)
```

## Reproducing the analysis

1. **MET scoring and validation** — run `notebooks/01_met_esm_scoring.ipynb`, then
   `notebooks/02_met_esm_validation.ipynb`. These reproduce ESM-1b/ESM-2 zero-shot
   masked-marginal scores against Estevam et al.'s MET deep mutational scanning panel
   (`fraser-lab/MET_kinase_Inhibitor_DMS`, MIT license).
2. **Corrected MET bootstraps** — run `scripts/met_baseline_and_gap_bootstrap_CORRECTED.py`
   inside the same kernel/session as the MET scoring notebook (it expects `feat_df`,
   `mut_panel`, `wt_df`, and the model-score columns to already be in memory). This produces:
   - `met_paired_esm1b_vs_baselines_v2.csv` — shared-mutation cluster bootstrap, ESM-1b vs.
     each of the 8 non-learned baselines (all 8 significant, BH-adjusted p ≤ 0.001).
   - `met_untreated_vs_treated_gap_ci.csv` — bootstrap CI for the untreated-vs-treated
     fitness gap, all 4 model sizes.
   `scripts/met_baseline_bootstrap_round1_SUPERSEDED.py` is the earlier, methodologically
   weaker version (mutations resampled independently per drug rather than sharing one
   resampled index set across drugs) — kept only for transparency about what changed
   between revisions, not used for any number reported in the manuscript.
3. **EGFR/ABL1 scoring and analysis** — run `notebooks/03_egfr_abl1_esm_scoring.ipynb`.
   Produces the permutation tests, leave-one-out analysis, and paired-baseline bootstrap
   in `results/egfr_abl1_*.csv`.
4. **Figures** — `scripts/figure3_forest_plot_generate.py` regenerates Figure 3 from
   `results/figure3_source_data.csv`. Figures 1, 2, 4, and 5 were generated inline within
   the notebooks above from the corresponding result tables.

## Data sources

- MET deep mutational scanning data: `fraser-lab/MET_kinase_Inhibitor_DMS` (GitHub, MIT
  license), from Estevam et al. 2025, eLife (DOI 10.7554/eLife.101882.3).
- EGFR (UniProt P00533) and ABL1 (UniProt P00519, isoform 1b) sequences: UniProt.
- Bioactivity data: ChEMBL.
- Crystal structures: RCSB PDB, accessions 6LUD (EGFR) and 1IEP (ABL1).

## Known gaps in this deposit

Three source-data files cited in the manuscript as `\texttt{...}` were generated during
earlier analysis passes and were not retained in this working copy:
`met_baseline_comparison.csv` (Figure 2 source data — point-estimate pooled correlations
per baseline), `met_full_model_drug_correlation_table.csv` (Figure 1 source data — per-drug,
per-model correlation table), and `egfr_abl1_final_results_document_matched.csv` (the
document-and-format-matched EGFR/ABL1 pairing table). These need to be re-exported from
the Kaggle/Colab session that originally produced them before the deposit is fully
complete — the notebooks in `notebooks/` contain the code that generates them, they just
weren't saved as standalone CSVs alongside the other result tables.

## Package versions

Record the exact package and model-checkpoint versions used (ESM/fair-esm or transformers
version, torch version, numpy/pandas/scipy/statsmodels versions) here before archiving —
this was flagged as an open reproducibility item and should be filled in from the actual
Kaggle/Colab environment rather than assumed.

## Citation

If you use this code or these results, please cite the associated manuscript (citation
details to be added once a DOI is assigned) and the underlying MET dataset
(Estevam et al. 2025, eLife, DOI 10.7554/eLife.101882.3).
