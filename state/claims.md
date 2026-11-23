# H4 evidence map

H4 = (B1) ApoE4 adheres more tightly to a recycling receptor than ApoE3, (B2)
impeding that receptor's recycling. Counts live in scripts/state.py, not here.
Status 2026-11-23: build complete and reviewed, 29 papers / 89 findings / 39 against,
validator clean. 28 class 1 (direct binding) findings: 9 support H4, 19 run against it.
Referee reviews in reviews/ (26 pass, 3 revise).

## Weakest link (next search target)

1. **Link 1 (B1) is answered, and the answer is mostly NO.** 28 direct-binding
   findings now exist. Supporting a tighter ApoE4 grip: 28957663 (insulin receptor,
   Kd ~54-60% lower, the strongest result in the set; the leader ruled 2026-11-23 that
   the insulin receptor counts as a recycling receptor under H4), 28276521 (slower VLDL1
   dissociation from LDLR), 10070023 (VLDL from E4/4 subjects competes better on
   human Hep G2, paired ratio 0.73, but P < 0.08 and so filed against under the
   non-significant-trend convention; direction still favours H4), 25482438 (apoE4>apoE3>apoE2 complex with
   LR11/SorLA, abstract only), 8808766 (VLDL-4/4 100% vs VLDL-3/3 82%, abstract
   only, untested), 30375977 Fig 2D-E (more ApoE4 co-IPs with Apoer2), 38279679 (bound but
   not catabolised, abstract only).
   Against: 39532095 Fig 1D (Kd 9 vs 16 nM, untested; authors call both high-affinity),
   16540478 and 11369796 (LDLR, flat null), 15863833 (VLDLR, LRP1 and LDLR,
   no discrimination), 12950167 (apoER2, pooled Kd range), 8632164 (rat astrocytes
   and neurons, similar binding), 30375977 Fig 1A-B (Apoer2, no affinity difference
   in the starting reference's OWN assay), 39532095 Fig 1A-C (LDLR, shared EC50),
   37060729 (ApoE4 binds LRP1 LESS), 10070023 (its own direct-binding null, and
   fibroblast and LDL nulls).
   Reading: the affinity difference H4 asserts is NOT a general property of ApoE4
   across LDLR-family receptors. Where it appears it is receptor-specific (insulin
   receptor, sortilin/SorLA) or particle-level rather than protein-level.
2. **No measurement of ApoE-receptor binding at ENDOSOMAL pH was found anywhere.**
   This is the sharpest gap: H4's mechanism needs the complex to fail to dissociate
   in the acidic endosome, and every binding assay in this set is at neutral pH or
   4 C. Xian 2018 and Pohlkamp 2021 instead rescue recycling by raising endosomal
   pH (NHE6), which is consistent with the mechanism but does not measure adhesion.
3. **Link 5, human brain cells with endogenous APOE4: still essentially empty.**
   Every B1 row is cell-free, non-brain (CHO, HuH7, HepG2, fibroblasts), rodent, or
   uses added recombinant ApoE. 39532095's human iPSC astrocytes give a null;
   43026723 has one donor per genotype with age and disease confounded.
4. **Link 4, the causal step B1 -> B2, is untested.** No experiment forces the
   ApoE-receptor complex apart and shows recycling restored; the rescues act on pH.

## Link 1: ApoE4 binds a recycling receptor more tightly (B1)
For: 28957663 Fig 5A/5B/5C (insulin receptor); 28276521 Table 1 VLDL1 kd2/K2 (LDLR).
Against/null: 30375977 Fig 1A-B (Apoer2, no affinity difference); 39532095 Fig 1C
(shared EC50), Fig 1A-B (cell binding, untested); 28276521 Table 1 LDL KA (E3/E4 binds
LESS). Not yet extracted: 16540478 (LDLR null), 15863833 (VLDLR/LRP1, no discrimination),
37060729 (LRP1 PLA, E4 binds less), 10070023, 8808766, 8632164, 38279679, 12950167.

## Link 2: ApoE4 stays with the receptor in endosomes (B1 in cells)
30375977 Fig 2D-E (co-IP, ~57% more ApoE4 with Apoer2); 32588544 Fig 5C/5D (sortilin-apoE
complex with transferrin); 34557909 Fig 7H/7I (sortilin complex in Rab5/Rab11);
38217595 Figs 5A/5B/6A (receptors in early endosomes); 34982109 Fig 7C (ApoE4 with Rab7).

## Link 3: the receptor's recycling is impeded (B2)
30375977 Fig 2C; 20547867 Fig 1A-C; 34617884 Fig 4C/4D; 29946028 Fig 2B; 38217595
Fig 4A/4B; 32588544 Fig 6E; 28957663 Fig 5H, S8B. Nulls: 30375977 Fig 2C (Lrp1, Ldlr,
IR, TfR), 28957663 S7C (surface LRP1), 38217595 Fig 8B (recycling endosome),
39532095 Fig 2C-D (surface LDLR). Not yet extracted: 15485881 (apoE recycling),
9593678 (apoE4 retained LESS), 17079794, 18369154.

## Link 4: releasing the complex rescues recycling
30375977 Fig 4E (NHE inhibitor); 34617884 Fig 4C (Slc9a6 knockout); 29946028 Fig 4F
(NHE6 rescue of surface LRP1). All act on endosomal pH, not on the complex itself.

## Link 5: human brain cells, endogenous genotype
Only 39532095 Fig 2C-D/2I (human iPSC astrocytes, and it is a null for E4 vs E3) and
43026723 (one donor per genotype, age and disease confounded).
