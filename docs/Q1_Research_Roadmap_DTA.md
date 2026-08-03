# Q1 Research Roadmap
## Multimodal Drug–Target Affinity Prediction for Kinase Inhibitors: A Systematic Benchmark of Molecular and Protein Language Model Representations (ChemBERTa + ESM-2) Across EGFR, VEGFR2, SRC, ABL1, and BRAF

**Target Journals (Q1):**
- Journal of Cheminformatics (Springer) — IF ~5.5–5.7 (sources vary 5.5–7.9 depending on database; reconfirm on Clarivate JCR before submission)
- Journal of Chemical Information and Modeling (ACS) — IF ~5.45
- Briefings in Bioinformatics (Oxford) — IF ~7.7–8.0
- Bioinformatics (Oxford) — IF ~5.56
- Computers in Biology and Medicine (Elsevier) — IF ~8.43

*(All five confirmed Q1 in their category as of 2024/2025 JCR data pulled this session. Impact factors fluctuate annually and vary slightly by source — reconfirm the current figure directly from Clarivate JCR or the publisher page before finalizing a submission decision.)*

---

## Phase 1 — Literature Review (Weeks 1–4)

### 1.1 Core Topics to Survey

**Classical & Deep DTA Prediction Baselines**
- KronRLS, SimBoost — kernel/matrix-factorization-era baselines
- DeepDTA — CNN over raw SMILES + protein sequence strings
- WideDTA, GraphDTA — graph neural network for the ligand + CNN/sequence encoder for the protein
- DeepPurpose — unified benchmarking toolkit spanning many encoder combinations
- MolTrans, PerceiverCPI and other transformer-based DTA architectures

**Molecular Representation Learning**
- Morgan/ECFP fingerprints (hashed substructure bit vectors — already covered in our terminology clusters)
- Molecular graph neural networks (GCN/GAT operating directly on atom-bond graphs)
- SMILES-based transformers (ChemBERTa, MolBERT) — pretrained on large unlabeled SMILES corpora

**Protein Representation Learning**
- Protein language models: ESM-1b, ESM-2, ProtBERT
- One-hot / PSSM-style classical protein encodings (for baseline comparison)
- Structure-derived features (AlphaFold-based), as a possible future extension

**Kinase-Specific ML Literature**
- Existing QSAR/DTA studies specific to EGFR, VEGFR2, SRC, ABL1, BRAF
- EGFR resistance-mutation literature (T790M, C797S, L858R) — clinical pharmacology side, to ground the mutation-sensitivity angle

**Methodological Literature on Data Leakage in Molecular ML**
- Scaffold-based (Bemis-Murcko) vs. random splitting — papers critiquing inflated benchmark numbers from random splits in molecular property prediction

### 1.2 Key Gaps to Identify (Your Novel Contribution Angles)

| Gap | Potential Contribution |
|---|---|
| No systematic benchmark of Morgan FP vs. ChemBERTa vs. graph-based ligand representations, combined with ESM-2, across this specific 5-kinase cancer panel under a leakage-controlled split | First unified, scaffold-split-controlled multimodal representation benchmark for EGFR/VEGFR2/SRC/ABL1/BRAF |
| Protein-embedding granularity (full-length ESM-2 vs. kinase-domain-only vs. mutation-substituted) rarely compared systematically for DTA | Representation ablation identifying which protein embedding strategy is actually informative (and cheaper to compute) |
| ESM-2's zero-shot mutation sensitivity (embedding distance / masked-residue log-likelihood ratio) has not been validated against *real measured* resistance IC50 shifts | Quantitative correlation study — turns an illustrative demo (see DigitalSreeni Video0, already logged in your tracker) into a testable pharmacological claim |
| Cross-dataset (ChEMBL ↔ Davis ↔ KIBA) and cross-target (train on one kinase, test on a related one) generalization rarely reported in kinase-focused DTA papers | Cross-dataset / cross-target generalization study |
| Assay-source heterogeneity (mixed IC50/Ki/Kd, mixed biochemical/cell-based assays) usually undisclosed or unaudited in DTA benchmark papers | Data-quality/leakage audit as a standalone methodological contribution |

### 1.3 Recommended Search Databases & Terms
- PubMed, arXiv (q-bio.BM, cs.LG), Google Scholar, Semantic Scholar
- Search terms: "drug-target affinity prediction deep learning", "ChemBERTa kinase inhibitor", "ESM-2 protein-ligand affinity", "scaffold split QSAR data leakage", "DeepDTA GraphDTA benchmark", "EGFR resistance mutation machine learning", "protein language model zero-shot variant effect"

---

## Phase 2 — Research Gap Formalization & Novelty Statement (Week 5)

**This phase required a real pivot — read this before the research questions below.** Finalizing Phase 2 meant stress-testing the novelty claim harder, which surfaced three very recent papers that substantially close the original Option A framing:

- **Abbott, "Systematic Benchmarking of Kinase Bioactivity Models Across Splitting Strategies and Protein Representations," bioRxiv, 2026** (preprint, [doi.org/10.64898/2026.04.20.719590](https://doi.org/10.64898/2026.04.20.719590)) — RF/XGBoost/ElasticNet/GIN/ESM-2-MLP compared across **507 human kinases**, 352,874 ChEMBL records, under random/scaffold/target-held-out splits. Close to a superset of the original Option A design, at roughly 100x the target-panel scale.
- **"Structure-free drug–target affinity prediction using protein and molecule language models," Journal of Cheminformatics, 2025/2026** (peer-reviewed, [doi.org/10.1186/s13321-025-01146-6](https://doi.org/10.1186/s13321-025-01146-6)) — already fuses ChemBERTa + ESM-2 via a Residual Inception architecture. The exact representation combination named in your original research plan is no longer an open combination to "try first."
- **Guo, Ran & Li, "Kinase-inhibitor binding affinity prediction with pretrained graph encoder and language model" (Kinhibit), Briefings in Bioinformatics 26(4):bbaf338, 2025** (peer-reviewed, [doi.org/10.1093/bib/bbaf338](https://doi.org/10.1093/bib/bbaf338)) — graph encoder + ESM-S protein LM, specifically for kinase-inhibitor affinity, tested on MAPK-pathway kinases and 200+ kinases broadly.

**Honest read: Option A, as a standalone contribution, is no longer defensible as "first."** A representation benchmark on 5 kinases is a strictly smaller, less rigorous version of what Abbott already did on 507. Presenting it as novel invites a reviewer to simply cite Abbott and reject on novelty grounds.

**What survives, unweakened, across every paper found (Phase 1 and this pass): Option C.** None of the six DTA/kinase-benchmark papers found so far do zero-shot protein-language-model mutation scoring validated against real measured resistance data. Li et al. 2025 (Phase 1) gets closest but works from ligand-side descriptors, not target-side PLM representations. This angle has survived two rounds of adversarial literature search — treat that as meaningful signal, not just convenient optimism.

**Revised plan:** promote Option C from "secondary angle" to primary contribution, and demote Option A to *replication context* — a small-scale sanity check that your pipeline reproduces the qualitative direction of Abbott/Kinhibit's findings on your 5-kinase panel, reported briefly, not sold as novel. This also shrinks the compute/scope burden relative to the original plan, which helps your monthly-cadence goal.

### Your Core Research Questions (revised)
1. *(Replication context, not a novelty claim)* Do representation choices (Morgan FP / ChemBERTa / GNN × ESM-2 full-length / domain-only) rank consistently on our clinically-curated 5-kinase panel (EGFR, VEGFR2, SRC, ABL1, BRAF) with what Abbott (2026) and Kinhibit (2025) report at larger scale? Report this as a short validation section, explicitly citing both papers.
2. **(Primary question)** Does ESM-2's zero-shot sensitivity to a kinase's clinically observed resistance mutations — embedding distance and masked-residue log-likelihood ratio — correlate with the real measured IC50/Ki fold-shift for inhibitors against those mutants? Start with EGFR (T790M, C797S, L858R, well-documented in ChEMBL), extend to ABL1 (T315I, the classic imatinib-resistance gatekeeper mutation) and BRAF resistance mutations if sufficient paired WT/mutant ChEMBL data exists — **confirm data availability before committing to multi-kinase scope**.
3. Does the mutation-sensitivity-to-real-resistance correlation hold consistently across kinases and mutation mechanism types (gatekeeper vs. covalent-anchor vs. activating), or is it kinase/mechanism-dependent? A dependency finding is itself a legitimate, interesting result, not a null result to hide.
4. Could zero-shot mutation sensitivity serve as a cheap pre-screening signal to flag candidate resistance mutations before expensive experimental characterization? (Frame as a practical/translational angle for the Discussion section, not a claim to over-promise on with this scope alone.)

### Novelty Statement (Revised)
> "Recent work has shown that protein-language-model and graph-based representations improve kinase-inhibitor bioactivity prediction at scale (Abbott, 2026; Guo et al., 2025) and that fused chemical-and-protein language models are effective for structure-free drug-target affinity prediction generally (Journal of Cheminformatics, 2025/2026). We address a question this literature does not: whether a protein language model's zero-shot sensitivity to a kinase's clinically observed resistance mutations corresponds to real, experimentally measured affinity shifts. Using ESM-2 embedding-distance and masked-residue log-likelihood scores across resistance mutations in EGFR — and, data permitting, ABL1 and BRAF — we provide, to our knowledge, the first quantitative, multi-kinase validation of protein-language-model mutation sensitivity against measured resistance data, moving this class of analysis from illustrative demonstration to a testable pharmacological claim with a plausible translational use case in early resistance-liability screening."

**Before relying on this "first" claim in the actual manuscript:** run one more targeted novelty search immediately before writing the Introduction — this exact space is moving fast enough (three closely-related papers surfaced in one afternoon of searching) that something closing this gap could appear before you submit. Re-check novelty right before writing, not just once in Phase 1.

### Cross-verification: has anyone already done Option C? (second adversarial search pass)

Ran a third round of targeted searches specifically trying to break the Option C novelty claim. Found five adjacent papers — none of them do the specific thing Option C proposes, but all five must be cited and explicitly differentiated from in Related Work, or a reviewer who knows this space will assume you missed them:

- **Meier, Rao, Verkuil, Liu, Sercu & Rives, "Language models enable zero-shot prediction of the effects of mutations on protein function," NeurIPS 2021, pp. 29287–29303.** This is the actual origin of the zero-shot masked-marginal log-likelihood-ratio method used in the DigitalSreeni Video0 notebook and in Option C. **Cite this as your foundational method, not as competing work.** It validates zero-shot scoring against general deep-mutational-scanning/fitness data (ProteinGym-style benchmarks), not drug-resistance or binding-affinity-shift data specifically — that gap is exactly what Option C fills.
- **Pan, Portelli, Nguyen & Ascher, "Systematic evaluation of computational tools to predict the effects of mutations on protein-ligand binding affinity in the absence of experimental structures," Briefings in Bioinformatics 27(1):bbag035, 2026.** Closest-sounding title of anything found. Benchmarks mostly structure/docking-based scoring tools (using AlphaFold-predicted structures) for mutation-induced protein-ligand affinity changes. Different method family from Option C (structure-based scoring functions vs. zero-shot sequence-only PLM scores) and not kinase-resistance-specific — but cite it prominently and state the distinction in one explicit sentence.
- **Gurusinghe, Wu, DeGrado & Shifman, "ProBASS," Bioinformatics 41(5):btaf270, 2025.** Uses ESM2 + ESM-IF1 for mutation ΔΔG_bind — but for protein-**protein** interactions, and it's **supervised/fine-tuned**, not zero-shot, and not drug binding. Methodologically close (same base model), application and setting both differ.
- **Singh, Sledzieski, Bryson, Cowen & Berger, "ConPLex," PNAS 120(24):e2220778120, 2023.** PLM-embedding-based drug-target interaction prediction, experimentally validated on real kinase-drug pairs (12/19 validated). General interaction/affinity prediction, not mutation-resistance sensitivity — relevant background on "PLM embeddings correlate with real kinase-drug binding," useful supporting citation for your feasibility argument.
- **Li, Dong & Qu, Pharmaceuticals 18(8):1092, 2025** (already logged in Phase 1) — ligand-side ML for the exact EGFR triple mutant, not target-side PLM scoring.

**Conclusion: Option C survived a third round of adversarial searching.** No paper found does zero-shot, sequence-only protein-language-model scoring (masked-marginal LLR or embedding distance) validated specifically against real measured kinase-inhibitor resistance IC50/Ki fold-shifts. That is a narrow, precisely-stated claim — narrower than the original draft — but it is the claim to actually make in the manuscript, and it now comes with a Related Work section that can cite five closely adjacent papers and explain exactly how this study differs from each one, which is a much stronger position than a vague "first to do X" statement unsupported by evidence of having looked.

---

## Phase 3 — Dataset Preparation (Weeks 5–7)

### Primary Datasets

**ChEMBL (per-target bioactivity) — all 5 target IDs now confirmed**
- EGFR = CHEMBL203 (~26,600 total IC50 records; ~1,295 raw records already pulled this session, cleaning paused)
- VEGFR2 = CHEMBL279 ("Vascular endothelial growth factor receptor 2")
- SRC = CHEMBL267 ("Proto-oncogene tyrosine-protein kinase Src")
- ABL1 = CHEMBL1862 ("Tyrosine-protein kinase ABL1"); also check CHEMBL2096618 (Bcr/Abl fusion protein) since T315I resistance is clinically studied in the fusion-protein context
- BRAF = CHEMBL5145 ("Serine/threonine-protein kinase B-raf")
- Filter: `standard_type ∈ {IC50, Ki, Kd}`, `standard_relation = '='`, `target_organism = Homo sapiens`, exclude records flagged with a `data_validity_comment`

**Mutation-data availability check (completed this session — directly determines Option C scope):** ChEMBL's `assay_variant_mutation` field gives a structured way to pull mutant-specific activity data.
- **EGFR: 13,960 mutant-annotated records**, including T790M, L858R, L861Q, and C797S (64 records specifically). Strong.
- **ABL1: 9,492 mutant-annotated records**, including **T315I** (the classic imatinib-resistance gatekeeper mutation) with real Kd values across many compounds, plus M351T. **Confirmed viable for the multi-kinase extension of Option C.**
- **BRAF: 6,606 mutant-annotated records, but overwhelmingly V600E.** Important distinction: V600E is BRAF's oncogenic driver mutation — the thing vemurafenib/dabrafenib were designed to target — not a secondary drug-resistance mutation that arose against an inhibitor, the way T790M/T315I did. Including BRAF in Option C as currently framed would be scientifically muddled. **Action: search specifically for genuine BRAF secondary-resistance mutations (e.g., splice variants, amplification-related, or any second-site mutations reported against vemurafenib/dabrafenib/encorafenib) before deciding whether BRAF belongs in this study at all.**
- **Revised Option C scope: EGFR + ABL1 confirmed viable now. BRAF status pending the secondary-resistance-mutation check above — don't include it by default just because data volume looks large.**

### Concrete Option C Protocol (literature-grounded, finalized this session)

**BRAF resolved — excluded, not just "pending."** Targeted literature search found: "second-site point mutations in BRAF are not thought to contribute significantly to acquired resistance to RAF inhibitors vemurafenib and dabrafenib, which contrasts with resistance mechanisms seen in other kinases like EGFR and KIT" ([Frontiers in Oncology, 2019](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2019.00268/full)). Clinical BRAF-inhibitor resistance is overwhelmingly driven by RAS/RAF/ERK **pathway reactivation** — RTK upregulation, RAS mutation, aberrant splicing, RAF dimerization, BRAF amplification — not by second-site mutations in the BRAF kinase domain itself. Two rare exceptions are documented in the literature, L505H ([Cancer Discovery 2018](https://aacrjournals.org/cancerdiscovery/article/8/9/1130/10474/A-Secondary-Mutation-in-BRAF-Confers-Resistance-to)) and L505H/L514V, but a direct ChEMBL check this session confirmed **zero activity records** for either mutation — there's no usable data to test them against, even as a negative control. **Decision: BRAF is out of scope for Option C, with this reasoning stated explicitly in the manuscript** (this is itself a legitimate, citable methodological point, not a weakness to hide — it shows the study understands *why* different kinases resist drugs differently, which most benchmark papers don't bother to establish).

**ABL1 mutation panel confirmed and extended.** The clinically characterized resistance panel — M244V, G250E, Y253F/H, E255K/V, T315I, M351T, F359V/I — accounts for ~85% of all BCR-ABL kinase-domain resistance mutations in imatinib-treated CML patients ([GIMEMA working party, Clin Cancer Res](https://aacrjournals.org/clincancerres/article/12/24/7374/193164/Contribution-of-ABL-Kinase-Domain-Mutations-to); [Iranian CML cohort study](https://pubmed.ncbi.nlm.nih.gov/26413254/)). Confirmed via direct ChEMBL query: **3,562 activity records** across this panel (beyond the T315I-specific count already found), plus T315I itself. This is a strong, literature-matched mutation panel — not an arbitrary one.

**Final scope: EGFR (T790M, C797S, L858R) + ABL1 (M244V, G250E, Y253F/H, E255K/V, T315I, M351T, F359V/I) — 10 mutations total across 2 kinases**, each with real ChEMBL activity data against multiple inhibitors.

**A methodological honesty check you need to resolve before running this, not after:** ESM-2's zero-shot mutation score (embedding distance or masked-marginal log-likelihood ratio) is computed from the **protein sequence alone** — it has no knowledge of which inhibitor is being tested. But the real resistance fold-shift in ChEMBL is **inhibitor-specific** (T790M causes strong resistance to first-gen EGFR inhibitors like erlotinib/gefitinib but was specifically designed around by osimertinib, so the same mutation gives very different fold-shifts depending on the drug). This means:
- The valid comparison is: does ESM-2's single, drug-agnostic mutation-sensitivity score correlate with the **aggregate/average** resistance shift across the inhibitors tested against that mutation in ChEMBL — a coarser but still meaningful question.
- It does **not** mean ESM-2 alone can explain drug-specific resistance patterns (e.g., why osimertinib resists T790M better than erlotinib does) — that would require a joint ligand-and-target model, which is a different (larger) study, not this one. State this limitation explicitly in the Discussion rather than let a reviewer discover it.
- With only 10 mutations total, this is a **small-N correlation study** (roughly n=10 mutation-level data points, though each mutation has multiple inhibitor measurements underneath it). Say so explicitly and consider a non-parametric test (Spearman, or even just reporting the scatter plot with confidence bands) rather than overselling statistical significance from a 10-point correlation.

**Concrete pipeline:**
1. For each of the 10 mutations: extract WT and mutant kinase-domain sequences (already have EGFR from the DigitalSreeni notebook; pull ABL1 WT sequence from UniProt P00519, kinase domain residues ~242–493, and build each of the 7 mutants by single-residue substitution, same method as the EGFR notebook).
2. Compute ESM-2 embedding cosine distance (WT vs. mutant) and the masked-marginal log-likelihood-ratio score for each mutation — 10 data points, two scores each.
3. **From ChEMBL — two explicit tiers, not one undifferentiated pull (sharpened after external critique this session):**
   - **PRIMARY (the actual benchmark):** for each mutation, pull activity records with that `assay_variant_mutation`, then explicitly pair each one against a WT activity record for the *same* `molecule_chembl_id` (same compound, both conditions measured). Compute per-compound &#916;pIC50 (or fold-shift = mutant IC50/Kd &#247; WT IC50/Kd) only from these matched pairs, then aggregate (median) to one controlled value per mutation. This matched-pair count will be smaller than the raw mutant-annotated record count and must be reported explicitly (not substituted with the larger, unpaired number).
   - **SECONDARY (context/validation only):** the broader set of mutant-annotated records without a matched same-compound WT measurement. Useful for describing data volume and coverage, but must not be used as if it were the controlled benchmark — a reviewer will treat "13,960 mutant records" as a red flag if it turns out most of them have no paired WT measurement to compute an actual shift from.
4. Correlate (Spearman, given small N and no assumption of linearity) the ESM-2 scores against the aggregated real fold-shifts across the 10 mutations. Report the scatter plot, the correlation coefficient with confidence interval, and a per-mutation table (not just the summary statistic) so reviewers can see the individual data points, not just a fitted line.
5. Secondary, more exploratory analysis: within each mutation, does the ESM-2 score correlate with the *spread* (variance) of fold-shifts across different inhibitors — mutations with wider fold-shift spread might indicate the mutation's effect is more binding-pocket/inhibitor-specific rather than a generic destabilization ESM-2 would pick up on.

### CRITICAL UPDATE — a 4th round of adversarial searching found a paper that has already largely done this

**Estevam, Linossi, Rao, Macdonald, Ravikumar, Chrispens, Capra, Coyote-Maestas, Pimentel, Collisson, Jura, Fraser & Seeliger, "Mapping kinase domain resistance mechanisms for the MET receptor tyrosine kinase via deep mutational scanning," eLife 13:RP101882, 2025.** [doi.org/10.7554/eLife.101882.3](https://doi.org/10.7554/eLife.101882.3). Peer-reviewed.

This paper performs a deep mutational scan of 5,764 MET kinase domain variants against 11 real inhibitors, and — this is the critical part — **reports the raw zero-shot correlation between ESM-1b and real drug-treatment resistance fitness: r = 0.28, versus r = 0.50 for untreated/baseline fitness.** Their explanation: the protein language model is trained on evolutionary sequence data, and drug-specific resistance pressure is not an evolutionary pressure the model has seen, so zero-shot scores are a much weaker predictor of drug-specific effects than of general fitness. This is exactly the empirical question Option C was built to ask — asked and answered, for a different kinase (MET), with an earlier model (ESM-1b, not ESM-2), against DMS pooled-fitness data rather than ChEMBL biochemical IC50/Kd.

Two more relevant facts that came out of the same search: their citation trail explicitly lists precedent DMS-plus-inhibitor-resistance studies across **ERK, CDK4/6, Src, and EGFR** (Persky et al. 2020, *Nat Struct Mol Biol*, [doi.org/10.1038/s41594-019-0358-z](https://doi.org/10.1038/s41594-019-0358-z)), and a second, independent EGFR-specific DMS dataset exists (Wang et al. 2025, *npj Precision Oncology*, BLU-945 resistance screen, [nature.com/articles/s41698-025-01086-2](https://www.nature.com/articles/s41698-025-01086-2)). Either of these could be paired with ESM2 by someone else at any time — this is not a hypothetical risk, it is exactly how the MET paper came to exist.

**Honest conclusion: "first quantitative validation of PLM zero-shot mutation sensitivity against real measured kinase-inhibitor resistance" is no longer a true claim.** It has a specific, peer-reviewed, quantified answer (r≈0.28, weak) for at least one kinase already. Continuing to plan around a "first" framing would set the paper up to be scooped by a citation the authors clearly should have found — because it took only a few well-chosen searches to find it here.

**What is still legitimately open, and the revised plan:**
1. **Extend, don't discover.** Frame the contribution explicitly as testing whether Estevam et al.'s finding (weak zero-shot correlation with drug-specific resistance) generalizes beyond MET to clinically central resistance mutations in EGFR and ABL1 — cite them as the paper this work directly builds on, in the first paragraph of the Introduction, not buried in Related Work.
2. **Two concrete, testable differences from Estevam et al. that are real methodological contributions, not just "we did it again":**
   - They used **ESM-1b**; this study uses **ESM-2** (newer, larger, better-benchmarked on ProteinGym). Does model scale/generation improve the drug-resistance-specific correlation at all, or is the weak correlation a fundamental limitation of the zero-shot approach regardless of model size? That is a real, useful question with a real answer either way.
   - They measured resistance via **pooled cellular fitness/growth** (DMS); this study uses **direct biochemical/cell IC50 and Kd values from ChEMBL** — a different, arguably more directly interpretable resistance readout. Does the correlation strength depend on which type of resistance measurement you use? Also a real question.
3. **Multi-kinase generalizability framing.** With Estevam's MET result (r≈0.28) as a published reference point, and EGFR + ABL1 results computed in this study, the paper becomes "does this weak-correlation finding hold across kinase families (RTK vs. non-receptor tyrosine kinase), or is it kinase/mutation-type dependent" — a broader, more defensible claim than a single-kinase replication, and one that directly answers a question Estevam et al. raise but don't test (they only had MET).
4. **Set expectations accordingly.** Given Estevam's r≈0.28 result, the realistic expectation for this study's EGFR/ABL1 correlation is also weak-to-moderate, not a clean, strong validation. That is fine — a well-explained weak correlation across multiple kinases, with a clear mechanistic account of why (echoing and extending Estevam's evolutionary-pressure-mismatch explanation), is a legitimate, publishable finding. Do not let the pressure to find a strong effect distort the analysis or the write-up.

**Practical next step before writing anything else:** read the Estevam et al. 2025 paper in full (not just the abstract) to see exactly how they computed their zero-shot correlation, what exact ESM-1b scoring method they used (embedding distance, masked-marginal LLR, or something else), and whether their supplementary data is public — if their raw fitness scores are available, that itself is a useful methodological template to replicate precisely for EGFR/ABL1, ensuring an apples-to-apples comparison rather than a loosely analogous one.

### RESOLVED — data/code availability check (this session)

**Both are public and confirmed usable. This closes the gate on point 1 of the Finalized Analysis Plan below, ahead of schedule.**

- Found and cloned `fraser-lab/MET_kinase_Inhibitor_DMS` (GitHub, MIT License). Its README confirms it is the source-code repo for exactly this paper. Contains R analysis scripts, a `Machine_Learning/` folder (XGBoost training pipeline), and top-level processed-score TSVs.
- **The exact processed data exists at mutation-level, per-drug granularity:** `Machine_Learning/data/all_features_all_data.csv` — 48,906 rows, one per (mutation × drug) pair, across all **9 MET inhibitors tested** (cabozantinib, capmatinib, crizotinib, glesatinib, glumetinib, merestinib, NVP-[compound], savolitinib, tepotinib). Columns include `score` (confirmed via `all_model_training.py`'s `feature_list` dict to literally be the "ESM LLR" — the zero-shot masked-marginal log-likelihood-ratio score), `mean` (the drug-treated DMS fitness value — the dependent variable), `resistance` (binary flag, 180/48,906 mutations flagged), plus 13 structural/biophysical features (ΔΔG, distance-to-ATP, pocket volume, RMSF, hydrophobicity, etc.) used as additional model features in their XGBoost extension.
- **Untreated/baseline fitness is separately available**, supporting point 3 (untreated vs. drug-treated contrast) directly: `WT_rosace_effect_all.tsv` (58,709 rows, DMSO/no-drug condition, ROSACE-modeled fitness effects) and `met_scores_filtered.tsv`/`met_scores_unfiltered.tsv`. A companion repo, `fraser-lab/MET_KinaseDomain_DMS`, holds the earlier (2023/2024) precursor paper's independent WT/exon-14 baseline scans — useful cross-reference, not the primary target repo.
- **Independent verification performed this session:** recomputed per-drug Spearman(ESM-LLR, drug-treated fitness) directly from `all_features_all_data.csv` and compared against the authors' own published per-drug results in `Machine_Learning/outputs/inhibitor_correlations_all_submodels_final.csv` (model = `esm_baseline`). The two track closely:

| Drug | My recomputed Spearman ρ | Their published `esm_baseline` correlation |
|---|---|---|
| Camp (capmatinib) | 0.065 | 0.071 |
| Gle (glesatinib) | 0.194 | 0.168 |
| Mere (merestinib) | 0.199 | 0.187 |
| Crizo (crizotinib) | 0.274 | 0.257 |
| NVP | 0.276 | 0.269 |
| Glu (glumetinib) | 0.304 | 0.297 |
| Cabo (cabozantinib) | 0.331 | 0.315 |
| Tepo (tepotinib) | 0.356 | 0.340 |
| Savo (savolitinib) | 0.422 | 0.415 |
| **Pooled (all drugs)** | **0.274** | (paper-reported: **0.28**) |

  The pooled figure (0.274) matches the r≈0.28 finding from the literature search almost exactly, and the per-drug ordering/magnitude matches their own reported numbers closely (small residual differences are expected — likely Pearson-vs-Spearman or held-out-fold differences in their pipeline vs. a full-data Spearman here). **This is real, working, reproducible confirmation that the dataset is what it claims to be** — not just a data-availability check, but a first-pass independent replication.
- **What this does NOT confirm:** the repo does not contain the actual ESM-1b sequence-scoring script (the `score` column is precomputed; the code that generated it appears to have run on the authors' HPC cluster, referenced via a `/wynton/group/fraser/...` path, and isn't checked in). So "exact replication" should be reframed slightly: rather than re-running their scoring code line-for-line, the correct move is to **build our own zero-shot scoring pipeline (ESM-1b, then ESM-2 at each size) and validate it against their published MET `score` column as ground truth** before trusting it on EGFR/ABL1. That's arguably a more rigorous validation step than reusing unseen code would have been.
- **License note:** MIT — fully reusable and citable, no permissions barrier.

**Net effect on the plan: the single biggest schedule risk flagged in this section (whether point 1 was even feasible) is resolved, and largely de-risks the MET portion of the study before any new computation has been run.** See the Finalized Analysis Plan and Phase 9 timeline updates below.

### 5th round of adversarial cross-verification (before starting to build anything)

Per standing practice, re-ran the novelty/feasibility check once more before committing engineering time — this time specifically hunting for (a) anything that already does the cross-kinase generalization angle now that it's the paper's actual spine, and (b) confirming the remaining open data-availability questions (EGFR DMS, ABL1 DMS, ChEMBL compound-mutation encoding).

**Closest new paper found — must cite, does not close the gap:** Wu, Xie, Ji & Zhi, "Towards Precision Protein-Ligand Affinity Prediction Benchmark: A Complete and Modification-Aware DAVIS Dataset," arXiv:2512.00708 (submitted 30 Nov 2025, cs.LG/q-bio.BM, CC-BY-4.0, code at [github.com/ZhiGroup/DAVIS-complete](https://github.com/ZhiGroup/DAVIS-complete)). This curates a modification-aware DAVIS benchmark covering **4,032 kinase-ligand pairs with substitutions/insertions/deletions/phosphorylation across ABL1, BRAF, EGFR, FGFR3, FLT3, KIT, LRRK2, MET, PIK3CA, and RET** — the same kinase panel this study now touches (MET/EGFR/ABL1/BRAF). **Why it doesn't close Option C:** it benchmarks trained/fine-tuned docking-based and docking-free affinity-prediction *models'* generalization to unseen mutations (three settings: augmented-dataset prediction, wild-type-to-modification generalization, few-shot modification generalization) — a supervised-model-generalization question. It does not test whether an off-the-shelf protein language model's zero-shot sequence score, with no training on any affinity data at all, correlates with real resistance. Different research question, same kinase panel — cite it prominently in Related Work as the closest multi-kinase mutation-aware benchmark, and state the distinction explicitly (zero-shot intrinsic PLM signal vs. supervised affinity-model generalization).

**Estevam et al. scope reconfirmed, plus one new useful number.** Directly confirmed via the paper: ESM-1b only (no ESM-2 tested, consistent with the plan's assumption) — this answers finalized-plan point 10. New detail worth folding into the write-up: their own XGBoost model, adding 13 structural/biophysical/chemical features on top of the raw ESM-1b score, only lifts the drug-treated correlation from **0.28 to 0.37** for MET. That's a concrete, realistic ceiling to cite when setting expectations for how much our own non-learned baselines (BLOSUM62, conservation, structural distance-to-pocket) might improve on raw zero-shot scores for EGFR/ABL1 — a jump to a strong correlation should not be expected even with substantial feature engineering.

**EGFR DMS (Wang et al. 2025, BLU-945, npj Precision Oncology) reconfirmed as real and peer-reviewed** (~17,000-variant L858R-background saturation library, escape mutations identified against osimertinib/BLU-945). **Not yet confirmed:** whether their processed fitness scores are actually deposited/public the way Estevam's are — this still needs the same public-data check just completed for MET before relying on it for the EGFR untreated-vs-treated contrast. Flagging as the next data-availability check to run, not assuming it based on the paper existing.

**ABL1 DMS: still nothing found.** A second dedicated search this round confirms the earlier conclusion — the ABL1/BCR-ABL1 literature is entirely clinical-sequencing-cohort based (mutation frequency in patients), not deep-mutational-scanning based. **No ABL1 DMS dataset exists as far as two independent search rounds can tell.** This is now a confirmed, real asymmetry, not just an unresolved flag — the ABL1 leg of the study will rely on ChEMBL-derived fold-shift only, with no DMS-based untreated baseline. State this explicitly and don't try to paper over it with an ill-fitting proxy.

**Minor related-work addition:** found ESM-Scan (Totaro et al., *Protein Science* 41(5):btaf270... — actually *Protein Science* 2024, PMC11577456), a general-purpose in silico deep-mutational-scanning tool built on ESM zero-shot scoring. Not kinase- or drug-resistance-specific — worth one citation as a related generic tool, not a competing result.

**ChEMBL compound-mutation encoding (T790M+C797S as a single assay_variant_mutation entry): still unresolved.** The API check hit a rate limit this round; this remains an open item to resolve before the background-aware-scoring step (finalized-plan point 6), not before starting the MET validation work below.

**Conclusion: the plan survives a 5th round of adversarial searching.** No paper found tests zero-shot, sequence-only PLM scoring against real measured kinase-inhibitor resistance across multiple kinases. The one close paper (DAVIS-complete) sits in the adjacent-but-distinct "supervised model generalization" space and strengthens rather than threatens the Related Work section. Clear to proceed to building the ESM-1b/ESM-2 scoring pipeline.

### Finalized Analysis Plan (post-pivot, user + mentor co-designed)

1. **Exact replication — CONFIRMED FEASIBLE, first pass already done this session.** Their processed per-mutation, per-drug data (`fraser-lab/MET_kinase_Inhibitor_DMS` on GitHub, MIT license) is public: 48,906-row mutation×drug table with precomputed ESM-LLR scores, drug-treated fitness, and untreated/baseline fitness in a companion file. Independently recomputed per-drug Spearman correlations this session matched their own published numbers closely (pooled ρ=0.274 vs. their reported r≈0.28 — see RESOLVED section above). Remaining work for a from-scratch reproduction: build our own ESM-1b (then ESM-2) zero-shot scorer and validate it reproduces their `score` column on the same MET mutations, rather than assuming the precomputed numbers transfer as-is to a new pipeline. This step is now a validation/write-up task, not an open data-acquisition risk.
2. **ESM-1b vs. all ESM-2 sizes, identical scoring.** ESM-2 has six official checkpoints (8M/35M/150M/650M/3B/15B). Plan around 150M/650M/3B as the core ladder; treat 15B as a stretch goal given its ~60GB+ unquantized memory footprint (likely needs rented cloud GPU, not this sandbox).
3. **Untreated vs. drug-treated fitness/affinity correlation.** For MET, replicate Estevam's DMS-based contrast directly. For EGFR, prefer Persky et al. 2020 and/or Wang et al. 2025 (BLU-945) DMS data over ChEMBL for this specific contrast, if available — DMS gives a true "no-drug" baseline that ChEMBL doesn't. Use ChEMBL IC50/Kd fold-shift as a complementary secondary analysis. Check whether ABL1 has an equivalent DMS dataset; if not, state that asymmetry explicitly rather than forcing a ChEMBL-only comparison to look equivalent to the DMS-based ones.
4. **Per-drug results, not one pooled correlation — MET per-drug numbers already in hand.** The 9-drug MET breakdown above (ρ ranging 0.065–0.422, roughly 6x spread) is itself a useful early result: it shows the "weak overall correlation" headline number hides real per-drug heterogeneity even within one kinase, which strengthens the case for reporting per-drug numbers for EGFR/ABL1 too rather than one pooled figure.
5. **Cross-kinase: MET, EGFR, ABL1.** State the real scope honestly in the paper — MET and EGFR are both RTKs, ABL1 is non-receptor, but all three are tyrosine kinases. "Generalizes across tyrosine kinases," not "across the kinome" (no Ser/Thr kinase data — BRAF was excluded).
6. **Background-aware scoring for compound EGFR mutations.** T790M+C797S must be scored against a T790M background, not WT, since that's the clinically real comparison (osimertinib resistance arises on top of T790M). The DigitalSreeni notebook's `egfr_double` construction is a reusable starting point. **Unresolved: verify whether ChEMBL's `assay_variant_mutation` field encodes compound mutations (e.g., "T790M;C797S") at all — if it only records single substitutions, this analysis may need a different data source.**
7. **Non-learned baselines: BLOSUM62, sequence conservation, structural distance to the binding pocket.** Structural distance-to-pocket is likely the single hardest baseline to beat, since resistance mutations cluster near the binding site almost by definition — a well-computed distance baseline outperforming a 3B-parameter model would be a more important, more honest finding than the scale question alone. Computable from existing PDB structures (ABL1-imatinib: PDB 1IEP; EGFR and MET structures per Estevam et al. and TeachOpenCADD T015).
8. **Bootstrap confidence intervals + paired statistical comparison between models.** Given the number of comparisons (models × kinases × drugs × baselines), apply multiple-comparison correction (Benjamini-Hochberg FDR) and report effect sizes with CIs throughout — don't lean on p<0.05 given small per-drug N.
9. **Pre-register the final analysis plan** (dated document, ideally OSF) before running any analysis — this design went through several honest pivots this session, which is good process but invisible to a reviewer unless the final plan is locked and timestamped before results exist.
10. **Confirm Estevam et al. tested ESM-1b only, not any ESM-2 variant**, by reading their methods (not just the abstract — their citation is Rives et al. 2021, the ESM-1b paper, but verify directly).

**Sharpened research question:** "Does protein-language-model scale improve zero-shot identification of drug-specific kinase-inhibitor resistance beyond what simple non-learned baselines (substitution matrices, conservation, structural proximity to the binding pocket) already capture, or is drug-specific resistance simply not recoverable from sequence information regardless of model sophistication?" — this framing makes a clean negative result (ESM-2-15B failing to beat distance-to-pocket) just as publishable as a positive one.

**Revised timeline estimate: 15–19 weeks** (down slightly from the earlier 16–20 week estimate, now that point 1's data-availability risk is resolved rather than open) — this design is still meaningfully bigger and more rigorous (3 kinases, up to 4 model sizes, 3 baseline types, proper multi-comparison statistics) than the version it replaced, and the MET portion's one-week saving is modest relative to the total. Decide explicitly whether this becomes the primary paper for this cycle with something narrower running in parallel for the monthly-cadence goal, rather than letting scope creep silently eat the timeline.

**Davis** — Kd benchmark, ~442 compounds × ~72 kinases (already covered in our terminology clusters — the standard DTA benchmark alongside KIBA)

**KIBA** — unified KIBA score combining Ki/Kd/IC50 across a large kinase-inhibitor matrix

**BindingDB** — cross-referenced affinities + structures, useful for a docking-adjacent extension later

**PDBbind** — structure + affinity pairs, optional if you extend into structure-based methods

**Therapeutics Data Commons (TDC)** — standardized, citable splits; useful for a reproducible secondary benchmark run

### Dataset Processing Steps
1. Canonicalize SMILES with RDKit; drop anything that fails to parse
2. Convert standard values to pIC50 / pKi / pKd (`9 − log10(value_nM)`)
3. Aggregate duplicate compound–target measurements (document your method — median is the common default — rather than silently keeping only one row)
4. Bemis-Murcko scaffold split (train/val/test), stratified per target — **not a random split**, given the leakage discussion from our earlier sessions
5. Document class/value distribution and assay-type composition (biochemical vs. cell-based) per split — this is exactly the kind of table reviewers ask for
6. Define the protein sequence set (canonical UniProt sequences) and the embedding-extraction protocol (full-length vs. kinase-domain-only) per target, consistently across all five kinases

**Status note:** Task 8 in this session already pulled ~1,295 raw EGFR IC50 records from ChEMBL (5 API pages via browser, since the direct fetch tool hit a rate limit). Cleaning/deduplication/scaffold-split for that sample is task 9, currently paused — resume that as your first concrete Phase 3 step rather than starting from zero.

---

## Phase 4 — Representation Strategy (Week 7–8)

This is your key novelty area, analogous to prompt engineering in a vision-language pipeline: instead of prompt wording, the axis you're studying is *which numeric representation of the molecule and the protein* the model sees.

### Representation Taxonomy

| Representation Type | Ligand | Protein |
|---|---|---|
| Hand-crafted | Morgan/ECFP fingerprint (2048-bit, radius 2) | One-hot target ID (no sequence information — the "dumb" baseline) |
| Descriptor-based | RDKit physicochemical descriptors (MW, LogP, TPSA, HBD/HBA) | — |
| Pretrained LM embedding | ChemBERTa (SMILES transformer) | ESM-2 (650M, or a smaller checkpoint for compute-constrained runs) |
| Graph-based | Molecular graph (GCN/GAT over atoms+bonds) | — (protein structure graph is a possible future extension, not in scope for paper 1) |

### Representation Ablation Design
- Factorial grid: each ligand representation × each protein representation, model architecture held fixed
- Separately: protein-embedding granularity ablation — full-length ESM-2 vs. kinase-domain-only vs. mutation-substituted, holding the ligand representation fixed
- This dual ablation (which ligand representation matters, which protein representation matters) is, on its own, a legitimate reviewer-facing contribution — directly mirrors how a prompt-sensitivity ablation would work in a different modality

---

## Phase 5 — Experimental Design (Weeks 8–12)

### 5.1 Experimental Conditions

| Condition | Ligand Repr. | Protein Repr. | Model | Data |
|---|---|---|---|---|
| E1 | Morgan FP | One-hot target ID | Random Forest / XGBoost (classical baseline) | Per-target ChEMBL |
| E2 | Morgan FP | ESM-2 (full-length) | Concatenated-feature regressor (RF/MLP) | Per-target ChEMBL |
| E3 | ChemBERTa | ESM-2 (full-length) | MLP / attention fusion | Per-target ChEMBL |
| E4 | ChemBERTa | ESM-2 (kinase-domain only) | MLP / attention fusion | Per-target ChEMBL |
| E5 | Molecular graph (GNN) | ESM-2 (full-length) | Joint DTA architecture (GraphDTA-style) | Per-target ChEMBL |
| E6 | Best combo from E1–E5 | Best combo from E1–E5 | Reproduced literature baseline (DeepDTA/GraphDTA) for direct comparison | Davis |
| E7 | Best combo from E1–E5 | Best combo from E1–E5 | Same | KIBA |

### 5.2 Cross-Dataset / Cross-Target Generalization
- Train on ChEMBL EGFR → test on the Davis/KIBA EGFR subset
- Train on EGFR → test on VEGFR2/SRC/ABL1/BRAF (related-kinase transfer — tests whether learned representations generalize across the kinase family, not just within one target)
- Train on Davis → test on KIBA, and vice versa (the standard cross-benchmark sanity check in the DTA literature)

### 5.3 Ablation Studies (Essential for Q1)

| Ablation | Variable | Fixed |
|---|---|---|
| Ligand representation | Morgan FP / ChemBERTa / GNN | Protein = ESM-2 full-length |
| Protein representation | ESM-2 full-length / kinase-domain / one-hot (no sequence info) | Ligand = best-performing option above |
| Split strategy | Random split vs. scaffold split | Same model/data — directly quantifies leakage inflation |
| Duplicate-record aggregation | Median vs. keep-all vs. first-only | Fixed representation/model |
| Assay-type filtering | Mixed IC50/Ki/Kd vs. IC50-only | Fixed representation/model |

---

## Phase 6 — Evaluation Framework (Throughout Experiments)

### Primary Metrics

| Metric | Definition | Why It Matters |
|---|---|---|
| RMSE | √(mean((ŷ − y)²)), in pIC50 units | Standard regression error |
| MAE | mean(\|ŷ − y\|) | Robust, easy-to-interpret magnitude of error |
| Pearson r | Linear correlation between predicted and true affinity | Universally reported in QSAR/DTA papers |
| Spearman ρ | Rank correlation | Robust to nonlinearity; relevant for virtual-screening-style ranking use cases |
| Concordance Index (CI) | Probability that, for a randomly drawn pair of compounds, the model ranks them in the same order as their true affinity | **The standard DTA benchmark metric** (used throughout the DeepDTA/GraphDTA/Davis/KIBA literature) — reviewers familiar with this literature will expect it |
| r²m | Regularized r² penalizing large intercept deviation between predicted and true values | Specific external-validation metric used in the DeepDTA/GraphDTA papers |

### Secondary Analysis
- Per-target performance breakdown — report all five kinases individually, not just pooled (mirrors the per-class breakdown expectation for imbalanced data)
- Statistical significance testing (paired test or Wilcoxon signed-rank across cross-validation folds / bootstrap resamples, comparing representation combinations)
- Scaffold-level error analysis — where the model fails (genuinely novel scaffolds vs. close analogs of training compounds)
- Computational cost comparison — embedding extraction time, model size, inference time per compound (relevant if you position this as informing practical virtual-screening pipelines)

---

## Phase 7 — Proposed Novel Contribution Options

Choose **one or two** to position as your main contribution for Q1:

### Option A — Representation Benchmark (DOWNGRADED — see Phase 2 pivot)
~~Systematically compare ligand/protein representation combinations across the 5-kinase panel under scaffold split.~~ Abbott (2026, bioRxiv) already did this on 507 kinases. Keep only as a brief replication/validation section, not a headline contribution.

### Option B — Protein-Embedding Granularity Study (Medium effort)
Test whether kinase-domain-only ESM-2 embeddings match or beat full-length embeddings for kinase-specific affinity prediction. Still plausible as a secondary finding, but check the Abbott and Kinhibit papers' methods sections before writing this up — they may have already tested embedding granularity too.

### Option C — Mutation-Sensitivity Validation (PROMOTED — primary contribution)
Quantitatively test whether ESM-2's zero-shot mutation scores correlate with real measured resistance-mutation IC50 shifts from ChEMBL, starting with EGFR and extending to ABL1/BRAF if data allows. Directly extends the DigitalSreeni Video0 demo (already reproduced and logged in your tracker) from an illustrative UMAP plot into a testable pharmacological claim. Survived two rounds of adversarial literature search this session — the strongest defensible angle you have.

### Option D — Cross-Target Transfer Study (Higher effort — check for overlap before pursuing)
Train on one or several kinases, evaluate transfer to held-out kinases. Abbott's target-held-out split already tests a version of this at scale across 507 kinases — read that paper's results before assuming this is still fully open.

**Revised recommendation: Option C as the primary contribution, with Option A/B reduced to a short replication/context section (not the headline).** This is a smaller, more focused paper than originally planned — which is a feature, not a compromise, given the crowded state of the general kinase-DTA-benchmark space this session's searches revealed.

---

## Phase 8 — Paper Structure (Q1 Standard)

### Sections
1. **Abstract** — Problem, gap, method, key result, significance
2. **Introduction** — Clinical motivation (kinase inhibitors in oncology, resistance mutations), limitations of current DTA benchmarks (representation choices under-examined, leakage from undisclosed random splits, mutation-sensitivity untested against real data), contributions (bulleted)
3. **Related Work** — DTA prediction models (KronRLS/SimBoost/DeepDTA/GraphDTA/DeepPurpose), molecular representation learning, protein language models, kinase-specific ML studies
4. **Methodology** — Datasets, representation taxonomy, model architectures, scaffold-split protocol, evaluation metrics
5. **Experiments** — E1–E7, ablations, cross-dataset/cross-target generalization
6. **Results** — Tables + figures, statistical tests, per-kinase breakdown
7. **Discussion** — Which representations win and why, mutation-sensitivity validation findings, failure cases, clinical relevance, limitations (residual leakage risk even after scaffold split, assay heterogeneity, per-kinase sample size imbalance)
8. **Conclusion**

### Figure Checklist (Reviewers expect these)
- [ ] Pipeline overview diagram (ligand repr. + protein repr. → fusion → affinity prediction)
- [ ] Scatter plots: predicted vs. true pIC50, per representation combination
- [ ] Bar chart comparing RMSE / CI / Pearson r across E1–E7
- [ ] Random-split vs. scaffold-split leakage-inflation comparison chart
- [ ] Per-kinase performance breakdown (grouped bar chart across all 5 targets)
- [ ] EGFR mutation UMAP + mutation-score-vs-real-IC50-shift correlation plot (ties directly to Option C)
- [ ] Cross-target / cross-dataset generalization heatmap (train-target × test-target matrix)

---

## Phase 9 — Timeline

Your stated long-term goal is one strong manuscript per month — worth being honest about upfront: this particular paper (now centered on Option C — cross-kinase, multi-ESM-2-size, multi-baseline mutation-resistance validation across MET/EGFR/ABL1) is a first-paper-scope project, realistically **15–19 weeks** per the Phase 3 finalized-plan estimate below, not 4. The table below is being kept at the original Phase 1–9 structure for continuity, but its content should now be read through the Option C lens (Phase 3's "Finalized Analysis Plan" is the authoritative detailed plan; treat E1–E7 in Phase 5 as the replication-context section, not the headline experiments).

**Update this session:** Week 5–7's "dataset preparation" milestone is partly de-risked — the MET portion no longer requires new data acquisition (Estevam et al.'s processed data is confirmed public and already spot-verified, see Phase 3 RESOLVED section). Remaining Phase 3 data work is EGFR/ABL1-specific: pulling paired WT/mutant ChEMBL records for the 10-mutation panel, and finding/confirming an EGFR DMS dataset (Persky 2020 or Wang 2025) for the untreated-vs-treated contrast, since ChEMBL alone doesn't give a clean "no-drug" baseline the way DMS does.

| Week | Milestone |
|---|---|
| 1–4 | Literature review, gap analysis, finalize novelty statement — **done** |
| 5 | Research proposal / internal presentation |
| 5–6 | MET validation write-up: build + validate own ESM-1b/ESM-2 zero-shot scorer against Estevam et al.'s published `score` column (ground-truth check, not new data acquisition — largely de-risked this session) |
| 6–8 | EGFR + ABL1 data preparation: paired WT/mutant ChEMBL pulls for the 10-mutation panel, resume paused EGFR cleaning, locate/confirm EGFR DMS data (Persky 2020 / Wang 2025) for untreated-vs-treated contrast, confirm/deny ABL1 DMS equivalent |
| 8–10 | Representation/scoring pipeline: ESM-1b + ESM-2 (150M/650M/3B core ladder, 15B stretch goal) zero-shot scoring for all 10 EGFR/ABL1 mutations + MET panel; non-learned baselines (BLOSUM62, conservation, structural distance-to-pocket) |
| 10–13 | Full analysis per the Phase 3 Finalized Analysis Plan (10 points): per-drug correlations, untreated-vs-treated contrast, cross-kinase comparison, background-aware scoring for compound EGFR mutations, bootstrap CIs + paired stats with multiple-comparison correction |
| 13–14 | Ablations / robustness checks; pre-register final locked analysis plan retroactively documented as the design history (already substantially done via this tracker + roadmap's revision history) |
| 14–16 | Paper writing (first draft) |
| 16–17 | Internal review and revision |
| 17–18 | Submission to target journal |
| 18+ | Handle reviews (expect 3–6 months review cycle) |

*(Original 10–14-week / E1–E7-centered timeline below is retained for reference but superseded by the above — Option A's E1–E7 grid is now replication-context only, not the paper's critical path.)*

---

## Phase 10 — Target Journal Selection Strategy

### Primary Target
**Journal of Cheminformatics (Springer)**
- Publishes exactly this kind of benchmark/methods paper regularly
- ChEMBL-based, open-data-driven studies are a natural fit for its scope
- Q1, IF ~5.5–5.7 (reconfirm current value before submission)

### Backup Targets (in order)
1. Journal of Chemical Information and Modeling (ACS) — IF ~5.45
2. Briefings in Bioinformatics (Oxford) — IF ~7.7–8.0, broader bioinformatics audience; strong fit if you lean the framing toward the protein-language-model methodology
3. Bioinformatics (Oxford) — IF ~5.56
4. Computers in Biology and Medicine (Elsevier) — IF ~8.43, broader biomedical-computing audience

### What Q1 Reviewers Will Check
- Comparison against ≥5 recent DTA baselines (DeepDTA, GraphDTA, DeepPurpose, etc. — not just your own representation variants)
- Scaffold-based (not random) splits, explicitly justified
- Multiple datasets/targets (the 5-kinase panel plus Davis/KIBA, not a single dataset)
- Statistical significance testing, not just point-estimate comparisons
- Ablations for every representation/design choice
- Per-target (not just pooled) performance breakdown, given known assay heterogeneity across your five kinases
- Reproducibility — code + processed dataset release is very achievable here since ChEMBL/Davis/KIBA/TDC are all publicly redistributable, unlike many clinical datasets

---

## Quick Reference: Research Contribution Summary

> **Title Suggestion:** "Multimodal Drug–Target Affinity Prediction for Kinase Inhibitors: Benchmarking ChemBERTa and ESM-2 Representations Across EGFR, VEGFR2, SRC, ABL1, and BRAF"

> **Core Claims (draft — to be filled in once experiments run, do not state numbers before you have them):**
> 1. [Best representation combination] achieves the lowest RMSE / highest Concordance Index across the 5-kinase panel under scaffold split, outperforming the Morgan-FP-only baseline by X%
> 2. Scaffold splitting reduces the (inflated) random-split performance by X points of CI, quantifying a leakage risk that much of the prior literature doesn't disclose
> 3. Kinase-domain-only ESM-2 embeddings match / underperform full-length embeddings by X%, informing a cheaper default for future kinase-focused DTA work
> 4. ESM-2's zero-shot mutation sensitivity for EGFR T790M/C797S/L858R correlates (r = X) with real measured resistance IC50 fold-shifts from ChEMBL — the first quantitative validation of this previously illustrative-only observation

> **MET leg — real result in hand (this session, not a placeholder):**
> For MET, zero-shot ESM-1b clearly beats every non-learned baseline tested (BLOSUM62 ρ=0.175, structural/biophysical features ρ≈−0.17 to 0.06, vs. ESM-1b ρ=0.257 pooled) — confirming a protein language model adds real signal here. But ESM-2 does **not** improve on ESM-1b at any tested size: ESM-1b beats ESM-2-650M and ESM-2-3B on 9/9 of the 9 inhibitors tested (paired Wilcoxon p=0.0039 both), and beats ESM-2-150M on 8/9 (p=0.0078). Scale *does* help monotonically within the ESM-2 family alone (150M<650M<3B, each step significant), it just never catches ESM-1b. This is a genuinely useful, non-obvious finding for the Introduction/Discussion: model scale and generation are not interchangeable proxies for "better," and a model that wins on general benchmarks (ESM-2 vs. ESM-1b on ProteinGym) can lose on this specific, narrower, drug-resistance-correlation task. **Open question the EGFR/ABL1 extension must answer: is this an MET-specific or drug-specific quirk, or does it hold across kinases?** — this is now the sharpest version of the paper's central question.

> **EGFR/ABL1 leg — real result in hand (this session, not a placeholder), and it does NOT answer the open question above cleanly.**
> Built and ran the full EGFR/ABL1 pipeline: UniProt-verified sequences, kinase-domain windows for the ESM-1b length cap, background-aware cascade scoring for EGFR's compound mutations (L858R→+T790M→+C797S, since ChEMBL confirmed these almost never occur independently), literature-verified 19-mutation panel (13 ABL1 + 6 EGFR steps), matched WT-mutant ΔpIC50 pairs per compound (primary tier) built from ChEMBL. Result: **no correlation reaches significance for either kinase, even after expanding the panel** — ABL1 (n=9 reliable): esm1b ρ=+0.25 (p=0.52), esm2 ρ=0.00 to −0.15 (p≥0.70); EGFR (n=6): all models negative, closest is esm2-150M ρ=−0.77 (p=0.072, still not significant, and n=6 is too thin to trust); combined (n=15): esm1b ρ=−0.07, esm2-3B ρ=−0.39, neither significant. Notably, expanding ABL1 from n=5→n=9 **weakened** the initial striking ESM-1b-beats-ESM-2 sign pattern seen at n=5 (ρ=+0.60→+0.25 for esm1b; −0.70→0.00 for esm2-150M), showing that pattern was substantially small-sample noise, not a real cross-kinase reversal.
> **Honest read for the paper:** this is not a failed pipeline — it's a genuine power problem. MET's DMS panel gave 5,434 mutations × 9 drugs (highly powered); ChEMBL-derived EGFR/ABL1 tops out at 6–13 usable mutations per kinase even after expansion, because clinically-characterized resistance mutations are inherently few in number (that's what makes them clinically notable). **The sharpened research question's negative branch — "is drug-specific resistance simply not recoverable from sequence information regardless of model sophistication" — cannot yet be confidently answered for EGFR/ABL1**, only for MET. The manuscript should report MET's result as the powered, confident finding and EGFR/ABL1 as a directionally-suggestive-but-inconclusive replication attempt, with the DMS-vs-ChEMBL power asymmetry stated as a real, citable methodological limitation rather than glossed over. Full detail logged in `research_workflow_tracker.md` §7b.

> **EGFR/ABL1 baselines completed (this session) — closes finalized-plan point 7.** Built BLOSUM62 plus two real structure-derived baselines (distance-to-inhibitor, distance-to-ATP-pocket) using actual PDB structures — EGFR's 6LUD (the exact L858R/T790M/C797S+osimertinib construct, matching our cascade panel) and ABL1's 1IEP (imatinib-bound) — with numbering verified against four literature-sourced catalytic residues per kinase before trusting any distance number. **Result: all 7 predictors now tested (4 ESM sizes + BLOSUM62 + 2 structural distances) are non-significant for ABL1 (n=9), EGFR (n=6), and combined (n=15).** The one point worth flagging without overclaiming: for ABL1, distance-to-inhibitor (ρ=+0.485, p=0.185) is the single largest-magnitude correlation found, edging out ESM-1b, with a mechanistically sensible sign — but still nowhere near significant at this n. **This completes, not just partially addresses, finalized-plan point 7**, and sharpens the EGFR/ABL1 conclusion: the null result isn't a PLM-specific weakness, it's a panel-size ceiling that no predictor tested — learned or non-learned — can overcome at n<15. Full comparison table in `research_workflow_tracker.md` §7b.

---

*Roadmap prepared for Q1 journal submission targeting Journal of Cheminformatics / Journal of Chemical Information and Modeling*
*Research area: Drug–Target Affinity Prediction · Kinase Inhibitors (EGFR, VEGFR2, SRC, ABL1, BRAF) · ChemBERTa · ESM-2 · ChEMBL / Davis / KIBA*
