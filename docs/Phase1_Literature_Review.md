# Phase 1 Literature Review
## Multimodal Drug–Target Affinity Prediction for Kinase Inhibitors

12 papers found and verified this session (title, authors, year, venue, DOI, peer-review status all checked against live sources — none invented). Organized by the topic structure from Phase 1.1 of the roadmap.

---

## 1. Classical & Deep DTA Prediction Baselines

These define the lineage your work sits in — any reviewer will expect you to compare against several of these, not just your own representation variants.

**KronRLS** — Pahikkala et al., "Toward more realistic drug–target interaction predictions," *Briefings in Bioinformatics* 16(2):325–337, 2015. [doi.org/10.1093/bib/bbu010](https://doi.org/10.1093/bib/bbu010). Peer-reviewed, Q1.
Kernel-based (Kronecker regularized least squares) baseline using compound similarity + Smith-Waterman protein similarity. Its own framing — that earlier DTI benchmarks were evaluated too simplistically — is directly relevant to your leakage/scaffold-split argument; worth citing for that framing, not just as a numerical baseline.

**SimBoost** — He, Heidemeyer, Ban, Cherkasov & Ester, "SimBoost: a read-across approach for predicting drug–target binding affinities using gradient boosting machines," *Journal of Cheminformatics* 9:24, 2017. [doi.org/10.1186/s13321-017-0209-z](https://doi.org/10.1186/s13321-017-0209-z). Peer-reviewed, Q1.
Gradient-boosting alternative to KronRLS; also proposes a prediction-interval variant (SimBoostQuant) for confidence estimation — worth considering if you want to report prediction uncertainty, which Q1 reviewers increasingly ask for.

**DeepDTA** — Öztürk, Özgür & Ozkirimli, "DeepDTA: deep drug–target binding affinity prediction," *Bioinformatics* 34(17):i821–i829, 2018. [doi.org/10.1093/bioinformatics/bty593](https://doi.org/10.1093/bioinformatics/bty593). Peer-reviewed, Q1. Code: [github.com/hkmztrk/DeepDTA](https://github.com/hkmztrk/DeepDTA).
The field's reference baseline — CNNs over raw SMILES characters and raw protein sequence characters, no hand-crafted features. This is the paper your E6/E7 "reproduced literature baseline" experiments in the roadmap should target first.

**WideDTA** — Öztürk, Ozkirimli & Özgür, arXiv:1902.04166, 2019. [arxiv.org/abs/1902.04166](https://arxiv.org/abs/1902.04166). **Preprint only — I found no peer-reviewed venue for this paper.** Cite it as a preprint explicitly if you reference it; don't present its "beat DeepDTA on KIBA" claim with the same weight as a peer-reviewed result.
Adds protein domains/motifs and word-level (not character-level) SMILES representation on top of DeepDTA.

**GraphDTA** — Nguyen, Le, Quinn, Nguyen, Le & Venkatesh, "GraphDTA: predicting drug–target binding affinity with graph neural networks," *Bioinformatics* 37(8):1140–1147, 2021. [doi.org/10.1093/bioinformatics/btaa921](https://doi.org/10.1093/bioinformatics/btaa921). Peer-reviewed, Q1. Code: [github.com/thinng/GraphDTA](https://github.com/thinng/GraphDTA).
First to represent the ligand as a molecular graph (GNN) rather than a SMILES string for DTA. Your E5 condition (GNN ligand representation) should be positioned against this directly.

**DeepPurpose** — Huang, Fu, Glass, Zitnik, Xiao & Sun, "DeepPurpose: a deep learning library for drug–target interaction prediction," *Bioinformatics* 36(22-23):5545–5547, 2020. [doi.org/10.1093/bioinformatics/btaa1005](https://doi.org/10.1093/bioinformatics/btaa1005). Peer-reviewed, Q1. Code: [github.com/kexinhuang12345/DeepPurpose](https://github.com/kexinhuang12345/DeepPurpose).
Not a single model but a benchmarking toolkit spanning many encoder combinations — genuinely useful as infrastructure for your own E1–E7 grid, not just a citation.

**MolTrans** — Huang, Xiao, Glass & Sun, "MolTrans: Molecular Interaction Transformer for drug–target interaction prediction," *Bioinformatics* 37(6):830–836, 2021. [doi.org/10.1093/bioinformatics/btaa880](https://doi.org/10.1093/bioinformatics/btaa880). Peer-reviewed, Q1.
Substructure-aware transformer that also leverages unlabeled molecular data via pretraining — conceptually the closest existing work to your ChemBERTa+ESM-2 combination, worth reading closely to make sure your Related Work section correctly differentiates your approach.

---

## 2. Molecular & Protein Representation Learning

**ChemBERTa** — Chithrananda, Grand & Ramsundar, arXiv:2010.09885, 2020. [arxiv.org/abs/2010.09885](https://arxiv.org/abs/2010.09885). **Preprint only — no peer-reviewed venue confirmed.**
RoBERTa architecture adapted to SMILES, pretrained on 77M SMILES strings. This is the exact molecular representation named in your original research plan — flag its preprint status explicitly when you cite it in Related Work, since a Q1 reviewer will notice if you cite it as if it were peer-reviewed.

**ESM-2 / ESMFold** — Lin, Akin, Rao, Hie, Zhu, Lu, Smetanin, Verkuil, Kabeli, Shmueli et al., "Evolutionary-scale prediction of atomic-level protein structure with a language model," *Science* 379(6637):1123–1130, 2023. [doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574). Peer-reviewed, published in *Science* (flagship AAAS journal — not JCR-quartile-ranked the way specialty journals are, since it's multidisciplinary, but unambiguously top-tier).
Up to 15B parameters; the paper's central finding is that atomic-level structural information emerges from sequence-only pretraining at scale. This is your protein representation backbone and also the direct source of the zero-shot variant-scoring capability used in the DigitalSreeni Video0 notebook.

---

## 3. Methodology — Data Leakage & Split Strategy

**MoleculeNet** — Wu, Ramsundar, Feinberg, Gomes, Geniesse, Pappu, Leswing & Pande, "MoleculeNet: a benchmark for molecular machine learning," *Chemical Science* 9(2):513–530, 2018. [doi.org/10.1039/c7sc02664a](https://doi.org/10.1039/c7sc02664a). Peer-reviewed, Q1 (RSC).
Established scaffold splitting as the standard, more realistic alternative to random splitting for molecular ML benchmarks. This is your primary citation for justifying the scaffold-split protocol in Phase 3/5 of the roadmap — cite it specifically for that methodological point, not just as a general benchmark reference.

---

## 4. Kinase-Specific / EGFR Resistance-Mutation Literature — Important Finding

This is the section that actually changes your novelty statement, so read it carefully.

**Li, Dong & Qu, "Predicting EGFR L858R/T790M/C797S Inhibitory Effect of Osimertinib Derivatives by Mixed Kernel SVM Enhanced with CLPSO," *Pharmaceuticals* 18(8):1092, 2025. [doi.org/10.3390/ph18081092](https://doi.org/10.3390/ph18081092). Peer-reviewed, Q1 (Pharmacology & Pharmacy, Chemistry-Medicinal).**

This paper already does machine learning (random forest, gradient boosting, and mixed-kernel SVM, tuned via a particle-swarm optimizer) to predict the inhibitory effect of osimertinib *derivatives* against exactly the triple-mutant EGFR (L858R/T790M/C797S) that the DigitalSreeni notebook and your Option C research gap are built around.

**What this means for your novelty statement:** the roadmap's Phase 2 novelty claim — "first quantitative validation of ESM-2 zero-shot sensitivity against real resistance IC50 shifts" — is narrower than it looked before this search, but not closed. This paper predicts activity from molecular descriptors of the *inhibitor* (structure-activity relationship on osimertinib derivatives), not from a *protein language model's* representation of the *mutant target*. Your angle — does ESM-2's embedding distance or masked-residue log-likelihood ratio for the mutation itself correlate with measured resistance — is a genuinely different question (target-side representation vs. ligand-side SAR) and still appears open. But you must cite this paper in Related Work and explicitly state that distinction, or a reviewer familiar with the EGFR-resistance ML literature will flag it as an overlooked prior work.

**Structural dynamics and kinase inhibitory activity of three generations of tyrosine kinase inhibitors against wild-type, L858R/T790M, and L858R/T790M/C797S forms of EGFR**, *Computers in Biology and Medicine*, 2022. [sciencedirect.com/science/article/pii/S0010482522005546](https://www.sciencedirect.com/science/article/pii/S0010482522005546). Q1 journal, but I could not confirm the exact DOI string or full author list from search snippets alone — **do not cite this without opening the actual article and confirming both.**
Reports comparative binding/inhibitory activity of erlotinib, gefitinib, afatinib, dacomitinib, and osimertinib against WT vs. mutant EGFR, with osimertinib and afatinib engaging hinge-region residues M790/M793/C797. Search snippets suggested specific IC50-like values (osimertinib ~12.79 nM vs. L858R/T790M, ~7.78 nM vs. the triple mutant) — **I flag these as unverified**, since I could not confirm from the snippet alone whether these are real experimental IC50s or values derived from the paper's own molecular dynamics simulations. This matters a lot for your Option C study: if you want a real experimental resistance fold-change as ground truth, you need the ChEMBL-sourced assay data directly (which is what Phase 3 of the roadmap already plans to pull), not a number lifted from this paper without reading the methods section.

---

## Revised Gap Table (post-literature-review)

| Gap | Status after this search | Contribution angle |
|---|---|---|
| Systematic multi-representation (Morgan FP / ChemBERTa / GNN) × (ESM-2 full-length / domain-only) benchmark across this specific 5-kinase panel | **Still open** — no paper found doing exactly this factorial comparison on EGFR/VEGFR2/SRC/ABL1/BRAF together | Option A, unchanged |
| ESM-2 zero-shot mutation sensitivity validated against real measured resistance IC50 shifts | **Narrower than initially framed** — Li et al. 2025 already does ML-based resistance prediction for this exact mutation, but from ligand-side descriptors, not target-side protein-LM representations. Must cite and explicitly differentiate. | Option C, refine framing: "target-representation-side" validation, distinct from existing ligand-SAR-side ML work |
| Scaffold vs. random split leakage quantification specific to kinase DTA (not just general MoleculeNet-style benchmarks) | Open — MoleculeNet established the general principle in 2018, but a kinase-DTA-specific leakage quantification (Ablation in Phase 5.3) doesn't appear to be commonly reported in the DTA papers surveyed here | Supports Option A |
| Cross-target (EGFR→VEGFR2/SRC/ABL1/BRAF) and cross-dataset (ChEMBL↔Davis↔KIBA) generalization for this representation set | Open | Option D, unchanged |

---

## Action Items Before Writing Related Work

1. Read the Li et al. 2025 *Pharmaceuticals* paper in full (not just the abstract/snippets) — confirm exactly what features and models they use, and write the one or two sentences that explicitly differentiate your target-representation approach from their ligand-SAR approach.
2. Open the *Computers in Biology and Medicine* 2022 paper directly to confirm the DOI, full author list, and whether the ~12.79/~7.78 nM figures are experimental or MD-derived, before using them anywhere.
3. Confirm WideDTA and ChemBERTa's preprint status hasn't changed (check for a later peer-reviewed version) immediately before submission — preprints do sometimes get published later.
4. Search specifically for VEGFR2, SRC, ABL1, and BRAF resistance-mutation or kinase-specific DTA literature (this session focused the mutation-specific search on EGFR only, since that's what the DigitalSreeni notebook covered) before finalizing the Related Work section.
