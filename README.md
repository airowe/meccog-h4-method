# Method

MecCog Step 1 submission.

- **Team:** Groovy
- **Hypothesis:** H4, APOE4 adhesion to recycling receptors. "In some types of non-Alzheimer's, non-aged human brain cells, APOE4 adheres more tightly to some recycling receptors than APOE3, impeding recycling."
- **Starting reference:** Xian X, Pohlkamp T, Durakoglugil MS, et al. Reversal of ApoE4-induced recycling block as a novel prevention approach for Alzheimer's disease. Elife. 2018;7:e40048. PMID 30375977.
- **Submission date:** draft of 2026-11-23 (work began 2026-11-23)

This submission reuses the pipeline built for the team's H2 submission (`meccog-h2-method`). The scripts, the extraction brief and the conventions are inherited; the evidence is not. No H2 row was copied: every paper was re-read and re-extracted for H4's contrast, which is ApoE-to-receptor **binding** rather than receptor recycling.

---

## 1. Who did the work

A person and an agent (`both`). One human team leader set the task, the scope and the rules, approved each row change, and decided the coding questions the review raised. One orchestrating agent did the searching, screening, full-text retrieval, review and assembly, and handed per-paper extraction to sub-agents running the same model, each with one to seven papers and the same written brief (`prompts/EXTRACTION_BRIEF.md`). The orchestrator checked every sub-agent's rows against the sources before assembly; the checks are listed in section 5.

## 2. Model and version

- Orchestrator: `claude-opus-5-5` (Anthropic), run in Claude Code (desktop app).
- Extraction sub-agents (9) and blind referees (3): `claude-opus-5-5`, as sub-agents of the orchestrator in the same session.
- One sub-agent read publisher pages in the user's Chrome to obtain full text that no API served.

**Model safeguards stopped five runs**, which is unusual enough to record. Two sub-agents were stopped after writing complete, checker-clean output files (the Asaro extraction, and one file of the Guo/Cheng extraction, which was rewritten whole); two were stopped before writing anything; one orchestrator message was cut off mid-dispatch. Stopped work was initially not redone, following the team leader's standing rule; the leader later ruled that a stopped extraction may be re-run, and the four affected papers were re-extracted. Every re-run is noted in `state/decisions.md`.

## 3. How papers were found

One search round, on 2026-11-23, logged record by record in `state/ledger.jsonl` (303 records, each with a stage, a decision and a reason).

- **PubMed (NCBI E-utilities), 7 boolean queries** (`state/round1_queries.json` holds the exact strings), combining apoE isoform terms with: binding affinity / Kd / surface plasmon resonance against named receptors; endosomal pH and dissociation; receptor recycling; co-immunoprecipitation and pull-down against LRP1, ApoER2, LRP8, VLDLR, LDLR, sortilin and SorLA; apoE recycling and re-secretion; ApoER2/Reelin with surface, sequestration or trapping; heparan sulfate proteoglycan binding. 171 unique records.
- **Forward citations:** the full Europe PMC citation list of the starting reference (30375977), 97 records, not title-filtered.
- **Carry-over:** 28957663 (Zhao 2017) was added from the team's H2 evidence because no H4 query returned it, which is logged.
- **Screening:** 198 records excluded on title, 29 on abstract, 30 taken to full text. Each exclusion carries its reason.

A second search round was not run. The evidence map (`state/claims.md`) records why: the binding question is answered by the papers found, and the gaps that remain are literature gaps rather than search gaps (section 6).

## 4. How full text was obtained

- **Europe PMC `fullTextXML`** for open-access papers, converted to text by `scripts/totext.py`. Two requests returned 150-byte 404 stubs and were discarded rather than treated as empty papers.
- **Figure images** already held locally from the team's H2 work, for the 11 papers common to both hypotheses. Nothing was re-downloaded.
- **Publisher pages read in the user's Chrome**, text only, no file downloaded, for 9 papers that no API served (J Biol Chem, J Lipid Res, Am J Physiol, and two PMC author manuscripts). Routing note: `doi.org` links for Elsevier-hosted journals land on a bot check, while the journal's own `/article/.../fulltext` URL loads cleanly. Two of these captures hit a 50,000-character ceiling and lost the tail of the Discussion and the references; abstract, methods, results, legends and tables are complete in both, and no row quotes the missing tail.
- **Abstract only, full text not obtained**, for 7 papers behind paywalls or published as PDF only. Their rows carry `full_text_unavailable` provenance, location `Abstract`, and capped relevance and strength. 12 rows are affected.
- No CAPTCHA or bot check was ever clicked.

## 5. What a human checked

**Automated checks, on 100% of rows:**

- **Quote:** every quote is a verbatim substring of the retrieved source (`scripts/check_rows.py`, self-test catches 6/6 seeded defects).
- **Statistic fields:** shape and value/provenance pairing valid; `~` only with `estimated_from_figure`; no P value estimated from a figure.
- **Official validator** (`validate_submission.py` from the challenge page): no errors.

**Orchestrator review:**

- Class 1 binding rows were spot-checked against the figure images before acceptance. Two Zhao 2017 rows were changed from `qualitative` to read-off Kd estimates because the axis is readable (Fig 5A, Kd about 54% lower with apoE4; Fig 5B, about 60%).
- **One double-count was caught and merged.** Mamotte 1999 had been filed as two rows, a paired IC50 ratio and an unpaired IC50 comparison, which are the same Hep G2 experiment reported two ways; filed separately they placed one experiment on both sides of the for/against count.
- A missing DOI that the validator rejected was found by exact-title match in Crossref (8808766, a 1996 J Lipid Res paper PubMed carries no DOI for).
- Rows that an extractor declined to file were checked rather than assumed correct: panels comparing only ApoE2, or a drug within one genotype, give no H4 row.

**Blind referee review (2026-11-23):** three referees re-coded 44 of the 89 rows across 24 papers, covering every class 1 binding row and every recycling or surface-level row that carries weight. Each referee could read only the source text, its figure images and the extraction brief; `rows/`, `reviews/`, `state/decisions.md` and `state/claims.md` were off limits. A leak check confirmed no prompt contained the recorded effect size, P or n it was asking about, and the same check fires when a value is planted deliberately. Verdicts: 26 pass, 3 revise, 0 reject; all three revisions are now resolved in `reviews/`.

- **One substantive error was found and corrected.** Mamotte 1999's Hep G2 row carried P < 0.05, which the source attaches to a one-sample test of the paired IC50 ratio against unity; the APOE4-vs-APOE3 group comparison is P < 0.08, which the authors call "marginally lower". The row now carries P < 0.08 and, under the non-significant-trend convention, is coded against. The direction still favours H4 and the authors' own one-tailed reading gives P < 0.05; both are recorded in the row.
- **Five misattribution traps were probed and our rows had already avoided all five**, each a case where a star belongs to a control contrast rather than to APOE4 vs APOE3: Xian 2018 Fig 2C and Pohlkamp 2021 Fig 4C/4D (Dunnett's post hoc, every bracket originates at the control bar), Cheng 2026 Fig 4 (the printed p = 0.004 compares two panels within ApoE4/4 cells), Prasad 2018 Fig 4F (no ApoE3 arm in the panel at all), Ji 1998 Fig 1A (the legend's p < 0.02 belongs to Fig 1B).
- Chen 2010 cuts the other way: its legend alone suggests vs-control stars, but the figure image shows real brackets between the ApoE3 and ApoE4 bars, and those P values are recorded.
- A referee confirmed Zhao 2017 Fig 5A/5B plot a **Kd** axis, so the lower ApoE4 bar means tighter binding. This is the easiest inversion in the set.

**A tool was built, trusted, and then thrown away.** `scripts/compare_referee.py` was written to compare referee codings with ours field by field. Its self-test passed, including planted errors, and it then reported 1 of 13 agreement on real data. Every disagreement was spurious: the normaliser took the first number in a referee's prose, turning "sVLDLr1-8" into 1-8, "ApoE4" into 4, and "three independent experiments" into something unequal to "3". The substantive values agreed throughout. A passing self-test did not show the tool measured the right thing on real input. It is retired, kept in the repo only as a loader, and the comparison was done by reading. Its agreement counts should not be quoted.

**Human (team leader):** set the scope, the hypothesis wording and the rules; approved every row change; and decided the scope and coding questions the review raised, including that the insulin receptor counts as a recycling receptor under H4 (the hypothesis says "some recycling receptors", and the insulin receptor recycles between the surface and the endosome). Three remaining proposals were delegated to the orchestrator and decided on the sources. No individual row was re-read by hand against the source papers. Rows most in need of a human check are those with `estimated_from_figure` in any field (19) or `full_text_unavailable` (12); each row's own `human_check` note in `rows/<key>.json` says what to look at.

## 6. Anything else

**29 papers, 89 findings, 39 of them against.** By directness class: 28 class 1, 2 class 2, 54 class 3, 5 class 4.

**H4 is compound, and its two halves are not equally supported.** The hypothesis asserts (B1) that ApoE4 adheres more tightly to a recycling receptor and (B2) that this impedes recycling. The evidence separates cleanly:

- **The recycling half (B2) is well supported.** Receptor surface levels and recycling fall with ApoE4 across Xian 2018 (Apoer2), Chen 2010, Pohlkamp 2021, Prasad 2018, Safieh 2024 and Asaro 2020 (sortilin recycling 50% lower).
- **The adhesion half (B1) is not.** Of 28 direct-binding findings, 9 support tighter ApoE4 binding and 19 run against it. Supporting: Zhao 2017 (insulin receptor, Kd about 54-60% lower, three assays agreeing), Calabuig-Navarro 2017 (VLDL1 dissociates from LDLR more slowly, P = 0.013), Yajima 2015 (apoE4 > apoE3 > apoE2 complex with LR11/SorLA, abstract only), Xian 2018 Fig 2D-E (more ApoE4 co-precipitates with Apoer2). Against: Chou 2006 and Lund-Katz 2001 (LDLR, flat null), Ruiz 2005 (VLDLR, LRP1 and LDLR, no discrimination), Ji 1998 (equal binding yet ApoE4 retained less), Na 2023 (ApoE4 binds LRP1 less), Guo 2025 (shared EC50), Mamotte 1999 (its own direct-binding null), and Xian 2018 Fig 1 itself.
- **The starting reference contains both.** Xian 2018 reports more ApoE4 retained with Apoer2 (Fig 2D-E) and, in the same paper, no ApoE3-vs-ApoE4 affinity difference (Fig 1). The authors frame their result as prolonged **retention** rather than higher affinity, and that distinction reconciles the two panels. It is the clearest statement in this literature that the adhesion claim and the recycling claim are separable.
- **The one receptor where ApoE4 clearly binds more tightly is not an LDLR-family receptor.** The insulin receptor and sortilin/SorLA carry the positive binding results; the LDLR-family receptors that H4's mechanism is usually told about come out null or reversed. Whether that is a real receptor-specific effect or an artefact of which systems have been studied is not answerable from this literature.

**Evidence gaps, in order of how much they matter:**

1. **No measurement of ApoE-receptor binding at endosomal pH exists anywhere in this set.** H4's mechanism requires the complex to fail to dissociate in the acidic endosome, and every binding assay found is at neutral pH or 4 degrees C. The pH rescues (NHE6 depletion, NHE inhibition, endosomal pH correction) are consistent with the mechanism but measure recycling, not adhesion. This is the single most useful experiment the hypothesis is missing.
2. **Human brain cells with endogenous APOE4 are essentially absent from the binding evidence.** Every B1 row is cell-free, non-brain (CHO, HuH7, HepG2, fibroblasts), rodent, or uses added recombinant ApoE. The one human iPSC astrocyte measurement (Guo 2025) is a null.
3. **The causal step from B1 to B2 is untested.** No experiment forces the ApoE-receptor complex apart and shows recycling restored.
4. **Particle-level and protein-level results are mixed together in this literature** and may not measure the same thing. Several positive results (Mamotte 1999, Calabuig-Navarro 2017, 8808766) compare whole VLDL particles from donors of different genotype, where apoE content and lipidation vary alongside the isoform.

**Weakest rows, stated plainly.** Cheng 2026 has one donor per genotype with age and Alzheimer's status fully confounded with APOE genotype (52-year-old healthy vs 87-year-old with LOAD), and GPC1 is a heparan sulfate proteoglycan rather than an LDLR-family receptor; its rows carry the lowest relevance in the submission (0.2) and say so. Fote 2022 rests on a legend reading "FDR<0.05 between APOE isoforms" that never names the pair, with all three isoforms present. Seven papers are abstract-only. These rows are kept rather than dropped because the challenge rules ask for the system to be recorded and the specifics to speak, not for findings to be excluded on the hypothesis's qualifiers.

## Code and prompts

- `scripts/` - search (`pm.py`, `citers.py`), text conversion (`totext.py`), row checking (`check_rows.py`, with `--selftest`), quote-position check (`quote_near_fig.py`), live state (`state.py`), assembly (`assemble.py`, with `test_assemble.py`), and the retired `compare_referee.py`.
- `prompts/EXTRACTION_BRIEF.md` - the brief every extraction sub-agent received.
- `rows/<key>.json` - every finding as extracted, with its provenance codes and its `human_check` note.
- `reviews/<key>.md` - one review per paper, with its verdict and the proposals raised against it.
- `state/` - `decisions.md` (every settled call and its reasoning), `claims.md` (the evidence map), `ledger.jsonl` (all 303 screened records), `round1_queries.json` (the exact search strings).
- Full texts and figure images are not in this repo (`.gitignore`), since they are publishers' copyright.
