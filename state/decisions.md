# Settled decisions (H4)

Each entry: date, decision, reason. Re-opening one needs new evidence; add a new
dated entry that names the evidence rather than editing the old one.

## 2026-11-23 Set-up

- **Multiple hypotheses are allowed.** resources/rules.txt line 39: "You may submit
  for as many of the five hypotheses as you like"; one live submission per
  hypothesis, 50 papers max (official-rules.txt section 0).
- **H4 work lives in H4_work/; H2 is read-only.** Scripts, resources and the brief
  were copied from H2_work on 2026-11-23. Full texts and figures for 30375977,
  20547867, 34617884, 31796678, 28957663, 32588544, 29946028 were copied from
  H2_work/ft (not re-downloaded). H2 rows are not copied: every H4 row is
  re-extracted for the H4 contrast.
- **Script changes from H2:** paths H2_work -> H4_work, output H4_submission.xlsx,
  HYPOTHESIS = the H4 statement, ORDER emptied; assemble.py reads the template
  from H4_work/resources/submission_template.xlsx (a copy; never edited).
- **method.local.json copied from H2 unchanged.** Its Method URL and commit SHA
  still point at the H2 method repo; an H4 repo is a later step with the leader.
  Must be replaced before any H4 submission.

## Conventions inherited from H2 (H2_work/state/decisions.md, settled there)

- Effect column: unsigned percent, fold (`Nx`), `d=`/`r=`, `qualitative` or `N/A`.
  Decreases are positive magnitudes; direction goes in the description. Multi-value
  detail goes in the description as "Effect detail: ...".
- Log2FC rows carry the linear fold 2^log2FC, printed log2FC in the description.
- A P printed only on the figure panel is `printed_in_text`.
- A P tested only against a no-ApoE (or ApoE2) control is `N/A` /
  `not_found_in_source` when an ApoE3 arm exists and no E3-E4 bracket is drawn;
  the effect is read E4 vs E3 off the bars.
- No E3-vs-E4 bracket under selected-comparison tests (Sidak) = not shown, not a
  tested null. Stars with no legend key: `N/A` + `ambiguous_panel`.
- Non-significant trends are `against: true`, printed P kept, direction in
  human_check.
- A paper with no APOE3 arm is class 5, low relevance.
- One panel and one age/condition per row.
- System column: facts only (species, cell, age, treatment, assay); no
  "Deviation:" label and no judging words (H2 leader decision 2026-11-21).
- Carriers-vs-non-carriers comparators are accepted with the pooling stated in
  the row (Cataldo 2000 / McColl 2003 precedent).
- Model-system, aged and AD-tissue findings are relevant (rules.txt lines 75 and
  446): record the system, do not exclude for the hypothesis' qualifiers.

## H4-specific directness (2026-11-23, first build; open for the leader)

H4: A = APOE4 vs APOE3. B = APOE adheres more tightly to a recycling receptor
(B1), which impedes that receptor's recycling (B2). The hypothesis is compound, so:

- **Class 1:** APOE4 vs APOE3, and binding/adhesion between ApoE and a recycling
  receptor measured itself: affinity (Kd), co-immunoprecipitation amount,
  dissociation (especially at endosomal pH), or retention of ApoE together with
  the receptor in endosomes measured as a complex (e.g. co-IP from endosomal
  fractions). Strength 1-3.
- **Class 3:** APOE4 vs APOE3 with a surrogate of B: receptor recycling rate,
  receptor surface level, intracellular retention of the receptor, ApoE-receptor
  colocalisation by imaging, ApoE4 intracellular retention alone, ligand uptake.
  A recycling block alone is B2 without B1, so it is class 3 for H4 (unlike H2,
  where recycling is B itself). Strength 2-5 by how tightly the surrogate ties
  to adhesion (e.g. recycling block reversed by forcing dissociation = stronger).
- **Class 2 / 4:** a surrogate perturbation of A (receptor-binding-region mutant,
  structure corrector, NHE6 inhibition used to force ApoE4 dissociation, RAP
  competition), with B measured (2) or a surrogate measured (4). Explained in the
  description.
- **Against:** ApoE4 binding equal to or weaker than ApoE3 for a recycling
  receptor; no recycling difference; nulls and non-significant trends.
- "Recycling receptor" is read broadly as an endocytic receptor that returns to
  the surface (LDLR family: LDLR, LRP1, VLDLR, Apoer2/LRP8; sortilin/SorLA;
  heparan sulfate proteoglycans noted as co-receptors). Binding studies of
  receptors with no recycling role are excluded.

## 2026-11-23 Round 1 extraction

- Extractor group C (32588544, 34557909, 39532095, 43026723) was stopped by a model
  safeguard before writing any rows. Per the leader's instruction its work is NOT
  redone; the four papers stay out of ORDER pending the team leader. Its read-only
  notes (useful if the leader approves a re-run): 39532095 Fig 1D SPR KD lipApoE4
  9 nM vs lipApoE3 16 nM, Fig 1C HTRF shared EC50 ~13 nM, Fig 2B/2D surface LDLR
  E3 ~ E4 (stars only vs ApoE2 / no ApoE), Fig 2I internalised ApoE E4 > E3 with a
  star; 32588544 Fig 6E sortilin recycling ~50% lower with apoE4 (n=9, P<.05) and the
  text says both isoforms bind sortilin equally (cited SPR, not measured there);
  43026723 one donor per genotype, age/disease confounded (52 y healthy vs 87 y LOAD),
  legend p=0.004 is within E4/4, not E3 vs E4. All unverified by a person.
- 2026-11-23, team leader: "approve all three fetches". (a) Europe PMC fullTextXML
  fetched: 28276521, 41102453, 34982109 OK; 18369154 and 37060729 returned 150-byte
  404 stubs (deleted) and are read on the PMC page in Chrome instead. (b) figure
  images: none fetched yet (Europe PMC bin is Cloudflare-blocked; figures read in
  Chrome where needed). (c) 9 publisher pages plus the 2 PMC pages read in Chrome,
  text only, no file download.
- 2026-11-23: 41102453 (Greda 2025) left out of ORDER, rows file kept. Its only
  extractable row is neuronal respiration/etomoxir sensitivity on apoE3 vs apoE4
  medium (class 4); it measures no ApoE-sortilin binding, sortilin surface level or
  recycling (those statements cite the group's earlier papers, refs 14/15). Not a
  B or B' readout for H4. 34982109 kept (2 class 3 rows, ApoE4 internalisation and
  late-endosome retention of ApoE, strength 4).
- 2026-11-23, team leader: "re-run extraction on the four stopped papers" (32588544, 34557909, 39532095, 43026723). Re-dispatched as two extractors.
- 2026-11-23: Asaro re-extractor (32588544, 34557909) stopped by a model safeguard after writing both rows files (check_rows clean: 5 and 2 findings). Not redone. Open: 26 system cells in 7 rows files still end with a 'Deviation:' label (the brief carried the old H2 line); a bulk removal was blocked by the permission layer, pending the leader.
- 2026-11-23, team leader (relayed): "Yes, strip and fix". 'Deviation:' label removed from the system cells listed above, facts kept; brief line fixed. Backup in state/backup_rows_pre_deviation/. check_rows clean.
  (26 cells: 28276521 x3, 28957663 x7, 29946028 x5, 31796678 x2, 34982109 x2, 38217595 x6, 41102453 x1. 39532095/43026723 were being written by an extractor at the time and are checked separately.)

## 2026-11-23 Extraction stopped: safeguard pattern

- Five model-safeguard stops on H4 extraction this session (group C; Asaro re-extractor,
  after writing both files; Guo's first file write, rewritten whole; one orchestrator
  message mid-dispatch; the 15485881/9593678/16540478 extractor, before any write).
  No stopped agent's work was redone. No more extractors dispatched in this session.
- 16 candidate papers have text in ft/ and NO rows: 15485881, 9593678, 16540478,
  15863833, 17079794, 11369796, 10070023, 18369154, 37060729 (full text, read in
  Chrome); 8808766, 12969990 (abstract only, PDF-only / paywalled); 12950167,
  18359298, 38279679, 8632164, 25482438 (abstract only, paywalled).
- Open for the leader:
  1. The "Deviation:" label is still on 8 rows in 39532095 and 43026723 (written
     under the old brief line). The approved cleanup covered the other 26 only.
  2. Whether to extract the 16 in a fresh session (recommended, given the stops).
  3. Heeren 2004 (15485881): 4 C surface binding with no receptor identified or
     measured; class 1 or class 3? The paper attributes the apoE4 effect to low-pH
     membrane behaviour, not receptor adhesion, which argues class 3.
  4. Ji 1998 (9593678): are HSPG retention rows in scope? decisions.md admits HSPG
     as a co-receptor only. The paper is against-H4 either way (apoE4 retained LESS,
     with equal beta-VLDL binding and uptake).
- 2026-11-23, team leader: "Keep trying here" (after the five safeguard stops). Re-dispatching extraction in this session, two papers per agent, writing each rows file before moving to the next paper.
- 2026-11-23, team leader (relayed, two decisions):
  1. "Yes, strip them" — the last 8 'Deviation:' labels (39532095 x6, 43026723 x2)
     removed, facts kept, backups in state/backup_rows_pre_deviation/, check_rows
     clean. No rows file carries the label now.
  2. "Keep, re-runs fine" — the re-extracted rows from the four safeguard-stopped
     papers stay in the build, and safeguard-stopped extractions MAY be re-run when
     needed. This overrides the original brief's "do not redo a stopped agent's
     work". Every re-run must be reported to the user and logged here.
- 2026-11-23: 10070023 (Mamotte 1999) rows 1 and 2 merged into one. Both reported the SAME Hep G2 VLDL experiment (paired IC50 ratio 0.73, P<0.05 vs unity; unpaired IC50 3.7 vs 6.1, P<0.08); filing them separately put one experiment on both sides of the for/against count. The unpaired values are kept in the description as Effect detail. Backup: state/backup_rows_pre_deviation/10070023.json.premerge.
- 2026-11-23: 8808766 (J Lipid Res 1996) DOI 10.1016/s0022-2275(20)39161-6 added; PubMed carries no DOI for it, found by exact-title match in the Crossref API. The validator rejects an empty DOI on a paper row.
- 2026-11-23, team leader: "Yes, run reviews" (confirmed directly in this session and
  relayed). H2 format: reviews/<key>.md per paper, verdict pass/revise/reject, proposed
  row changes listed with evidence and NOT applied; every row change needs the leader's
  approval first. Downloads and commits still need the leader's OK. A safeguard-stopped
  referee may be re-run (2026-11-23 ruling), and each re-run is reported.
- Review design: referees are blind to our rows (they may read only ft/, figs/ and the
  brief; rows/, reviews/, decisions.md and claims.md are off limits). Leak control on the
  89 prompts: 0 contain this row's recorded eff/p/n; the detector fires on a planted value.
  scripts/compare_referee.py has a self-test (2/2 planted errors caught, missing row
  flagged) so a clean comparison is a real negative result.
- 2026-11-23: scripts/compare_referee.py RETIRED as a verdict tool. Its self-test passed
  (planted errors caught) yet it reported 1/13 agreement on real data, all spurious: the
  eff/n normaliser takes the first number in a referee's prose, so "sVLDLr1-8" -> 1-8,
  "ApoE4" -> 4, "three independent experiments" != "3". The substantive values agreed.
  Same family as the H2 detector failures: a passing self-test does not show the tool
  measures the right thing on real input. Referee comparison is done by READING the
  items. The script stays only as a loader; do not quote its agreement counts.

## 2026-11-23 Referee reviews (blind)

- Three blind referees re-coded 44 of 89 rows across 24 papers: every class 1 binding
  row, every recycling/surface row that carries weight. They could read only ft/, figs/
  and the brief. 20 review files in reviews/.
- Verdicts: 17 pass, 3 revise. ONE substantive error found, in 10070023 (Mamotte 1999):
  our Hep G2 row carries P<0.05, which the source attaches to a one-sample test of the
  IC50 ratio against UNITY; the E4-vs-E3 group comparison is P<0.08 ("marginally lower").
  Verified at source. NOT applied: proposals in reviews/10070023.md, and the against flag
  must be decided with the P because the non-significant-trend convention would flip it.
- Traps the referees probed that our rows had ALREADY avoided: Xian Fig 2C (Dunnett's,
  stars vs control only), Pohlkamp Fig 4C/4D (same), Cheng Fig 4 (p=0.004 is within
  ApoE4/4), Prasad Fig 4F (no ApoE3 arm), Ji Fig 1A (p<0.02 belongs to Fig 1B). All five
  already N/A or correctly scoped in our rows.
- Open scope question, leader's call: 28957663's receptor is the INSULIN RECEPTOR, not
  LDLR-family. It is the strongest pro-H4 binding result in the submission (4 rows).
  Whether it counts as a "recycling receptor" under H4 decides whether those rows belong.
- Not re-coded: the 7 abstract-only papers and a few low-weight rows (45 of 89). An
  abstract has no panel to re-read, so a blind pass adds little; their review files say so.
- 2026-11-23, team leader: "Yes, fix it". 10070023 Hep G2 row corrected: p '<0.05' ->
  '<0.08' (the printed E4/4-vs-E3/3 group comparison; the P<0.05 is a one-sample test of
  the paired ratio against unity). against false -> true, following mechanically from the
  non-significant-trend convention in this file, not as a separate judgement. Direction
  still favours H4 and the authors' one-tailed reading gives P<0.05; both recorded in
  human_check. Backup: state/backup_rows_pre_deviation/10070023.json.pre_p_fix.
  Rebuilt: 29 papers, 89 findings, 38 against; validator passes. Class 1 balance moves
  from 11 for / 17 against to 10 for / 18 against.
- STILL OPEN for the leader (proposals in reviews/, none applied): (1) does the INSULIN
  RECEPTOR count as a recycling receptor under H4 - decides whether 28957663's 4 rows,
  the strongest pro-H4 binding evidence, belong at all; (2) 39532095 Fig 1D for-vs-against
  (printed 16 vs 9 nM favours H4; authors call both high-affinity; our row and the referee
  disagree); (3) 15863833 Fig 1E-F LRP (1.1 vs 1.7 nM nominally favours H4, authors say no
  discrimination); (4) 34982109 rows rest on a legend that never names the compared pair;
  (5) 43026723 single-donor age/disease confound and GPC1 is not LDLR-family.
- 2026-11-23, team leader (relayed), three review answers:
  1. 10070023 Hep G2 "P<0.08, against" — already applied earlier this session on the
     leader's direct approval; no further change. Ratio test kept in the description.
  2. 28957663 insulin receptor "Yes, keep it" — the insulin receptor COUNTS as one of
     H4's recycling receptors. Reasoning: H4 says "some recycling receptors", and the
     insulin receptor recycles between the cell surface and the endosome. The 4 rows
     stay as coded. This settles the scope question the blind referee raised and keeps
     the strongest pro-H4 binding evidence (Kd 54-60% lower, Fig 5A/5B/5C/5H) in the set.
  3. 39532095 Fig 1D "Against" — against false -> true. Printed KDs (9 nM lipApoE4 vs
     16 nM lipApoE3) run the H4 way but are untested, and the authors frame both as
     high-affinity with the real contrast against ApoE2. Matches the blind referee.
     Both KDs and the authors' framing kept in the description.
  Backup: state/backup_rows_pre_deviation/39532095.json.pre_1d_fix.
  NOT decided, still open: 15863833 Fig 1E-F (LRP 1.1 vs 1.7 nM) and 34982109 (legend
  never names the compared pair). Also open: 43026723 confound/GPC1 scope.
- 2026-11-23, team leader: "Let it decide" — the last three review proposals delegated
  to this session. All three decided on the source and the established conventions:
  1. **15863833 Fig 1E-F (LRP): kept against: true, no value change.** Source: "apparent
     Kd values of 1.6, 1.7, and 1.1 nM for the apoE2, apoE3, and apoE4 isoforms". The
     apoE4 value is nominally tighter, but there is no statistical test, n = 2 duplicate
     averages, and the authors say twice that the receptors "do not discriminate between
     apoE isoforms". Coding an untested gap as support would attribute to the paper a
     claim it declines to make. Both Kd values stay in the description.
  2. **34982109: kept, relevance -> 0.3, strength -> 5.** The Fig 7A-B legend says
     "FDR<0.05 between APOE isoforms" without naming the pair, and all three isoforms are
     in the experiment, so an APOE2-vs-APOE3 bar would satisfy the wording without bearing
     on H4. No figure is saved to resolve it. Kept because the ranked direction is stated
     in the text; cut because the statistic cannot be attached to the H4 contrast.
  3. **43026723: kept, relevance -> 0.2 (lowest in the submission).** One donor per
     genotype with age and disease confounded (GM23976, 52 y healthy vs AG10788, 87 y
     LOAD), and GPC1 is an HSPG, not an LDLR-family recycling receptor. Kept because the
     challenge rules say to record the system and let the specifics speak rather than
     exclude on the hypothesis's qualifiers; the confound makes the values uninterpretable
     for H4, which the rows now state.
  Pattern: none of the three was dropped. The rules favour recording a finding with its
  limitations stated over removing it, and relevance is the lever for "real but weak".
- 2026-11-23: README draft error caught before anything was published. The LR11/SorLA
  paper (25482438) was written as "Kitamura 2015"; the first author is Yajima R (2015,
  Biochem Biophys Res Commun). The name was invented, not misread. All other author
  names in the README were then verified against PubMed esummary and are correct.
  Lesson for any future README: verify every author attribution against the record,
  not from memory. A public method document is exactly where a fabricated citation
  does the most damage.
- 2026-11-23, team leader: "Yes, commit". ~/Projects/meccog-h4-method initialised on
  branch main and the first commit made: 6153357c81738fb9f8672e8be5d43739d6933a83,
  "docs: add H4 method description and evidence rows", 75 files, 3912 insertions.
  Pre-commit checks: .gitignore excludes method.local.json, *.xlsx, ft/ and supp/;
  0 staged files matched those patterns; 0 matches for any contact detail or email in
  the staged content. Conventional Commits, no AI mention, no Co-Authored-By line.
  NOT done, still needs the user: creating the GitHub repo, adding a remote, pushing,
  and updating method.local.json (it still carries the H2 method URL and SHA, so the
  H4 submission would currently name the wrong method).
- 2026-11-23, team leader: "Yes, create and push". Public repo created and pushed:
  https://github.com/airowe/meccog-h4-method (public, matching the H2 precedent and the
  rules' requirement that the method be public). Remote HEAD matches local
  6153357c81738fb9f8672e8be5d43739d6933a83. Verified after publishing: 80 paths public,
  0 matching ft/, supp/, *.xlsx or method.local.json. No full texts, figure images,
  spreadsheets or contact details were published.
  STILL OPEN: method.local.json must be updated to the new URL and SHA before any
  submission; it currently names the H2 repo.

## method.local.json pointed at the H4 repo (2026-11-23)

`method.local.json` still carried H2's method reference: URL
`https://github.com/airowe/meccog-h2-method`, SHA `8e46b886...`. Submitting the
H4 spreadsheet with those would have named the wrong repository and a commit
containing none of this work.

Updated with the user's explicit approval to:
- Method URL: https://github.com/airowe/meccog-h4-method
- Commit SHA: 6153357c81738fb9f8672e8be5d43739d6933a83

SHA verified against both local HEAD and `refs/heads/main` on the remote before
the rebuild, not copied from memory.

Rebuilt `~/Documents/Alzheimers/H4_submission.xlsx`: 29 papers, 89 findings,
39 against (unchanged). Method sheet re-read from the written file and confirmed
to carry both new values. Official validator: "SUBMISSION VALID — no problems
found." check_rows.py: clean, exit 0, and its --selftest still catches 6/6
seeded defects (an empty pass is only meaningful alongside the control).

No evidence row was touched. This was the last blocker on the submission side;
submission itself remains the team leader's, and has not been attempted.
