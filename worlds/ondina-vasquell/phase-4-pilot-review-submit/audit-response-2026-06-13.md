# Audit response - Alexander signed substrate audit 2026-06-13

Reaudited against the bytes and fixed the true gaps. Rebuilt through the canonical pipeline; tools/verify/verify_ondina.py PASS (60 docx) after.

## F1 - report-file Date of Service semantics: FIXED (the one worth normalizing)
- culture_report_deep_tissue: storyboard Date of Service moved from 05/19 (report) to 05/17 (collection), matching the superficial swab convention; "Date Reported: 05/19/2026" retained in the filing line. Verified.
- The four cumulative trend/flowsheet files (renal, cbc, vitals, nursing offloading) left as-is per the audit (defensible); the convention is now documented in the file-grammar guide (N2).

## F2 - attending given-name proximity (Marisol / Marisela): FIXED
- Attending renamed Marisol Everet, MD -> Lillian Everet, MD at the canonical source (clinical_data ROSTER) and in three hardcoded report literals (MRI, ABI/TBI, superficial swab "Ordering clinician") and the 12 golden literals; substrate pack roster line updated with provenance. Daughter Marisela Vasquell unchanged (woven into the narrative). Verified: zero "Marisol" in any built docx; "Lillian Everet" renders consistently.

## N1 - image byte-identical duplicates: NO ACTION (intentional staging). Confirmed.
## N2 - trend naming convention: DOCUMENTED in clinical-voice-and-file-grammar-guide.md.

## Delegated: image vision-gate (by eye)
- wound_photo: PASS. Single granulating plantar-forefoot ulcer with a measuring ruler; NO exposed bone, joint, gangrene, eschar, or identifiers. Consistent with EW6/EW12 and keeps the osteomyelitis question open.
- abi_tbi_tracing: TWO GAPS found, both require ONE Codex regeneration (image is writer-produced, not pipeline-built):
  1. "Ordered by: M. Everet MD" is the stale pre-rename initial; must read Lillian Everet, MD.
  2. The right ankle shows measurable indices (1.20 / 1.16) while EW9 states ankle indices noncompressible BILATERALLY. The left side (NC, TBI 0.50, toe 55) and both toe values (R 92/0.84, L 55/0.50) are correct.
  Root cause: the EW31 spec said only "left ankle noncompressible." Spec corrected to require both ankles NC and the correct ordering clinician; after-generation checklist now mandates an eye cross-check of ordering-clinician initial and bilateral NC against EW9 (the byte gate cannot read image text). EW31 is flagged for regeneration to the corrected spec before any pilot leans on it.

## Delegated: adversarial wrongness vectors (deep-read)
- T2 HIM coding worksheet: wrong-by-genre (pressure-injury principal + acute osteomyelitis POA). Chart rebuttals present: ED/podiatry/wound document a diabetic foot ulcer and infection (not pressure injury); MRI equivocal, pathology no bone, ID not established (osteo). Fair.
- T3 CDI query: presses acute osteomyelitis. Same osteo trio rebuts it in the chart. Offers an "unable to determine" option. Fair.
- T4 MA denial: improving-markers-equal-home framing. Rebuttals present: perfusion study + vascular consult, skilled wound frequency, PT stairs/offloading, OT teach-back failure, case-management home and night-caregiver limits. Fair.
- T6 concurrent-review request: a neutral determination prompt by design (not a wrong claim); used as the prompt, not the answer. Fair.
All four are fair and chart-rebuttable, consistent with the per-task A0.5 records.

## Net
Zero blocking issues remain in the DOCX substrate. One image (EW31) requires a Codex regeneration to the corrected spec; everything else is fixed and gate-green.
