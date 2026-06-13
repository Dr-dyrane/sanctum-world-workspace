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
- abi_tbi_tracing: FIXED and PASS after regeneration. Ordered by now reads Lillian Everet, MD; both ankle PT and DP rows are NC bilaterally; the ankle-brachial index row is noncompressible bilaterally; toe values are R 92 / 0.84 and L 55 / 0.50; no interpretation, adequate-perfusion, inadequate-perfusion, or revascularization text appears. The world-file and synthetic-file copies are byte-identical, grayscale 1240 by 1760 JPGs, EXIF length 0, SHA256 d0354413c690f53aae74ada2efd0de739c7acb84efafbaa92058873ca7ae4ef0.

## Delegated: adversarial wrongness vectors (deep-read)
- T2 HIM coding worksheet: wrong-by-genre (pressure-injury principal + acute osteomyelitis POA). Chart rebuttals present: ED/podiatry/wound document a diabetic foot ulcer and infection (not pressure injury); MRI equivocal, pathology no bone, ID not established (osteo). Fair.
- T3 CDI query: presses acute osteomyelitis. Same osteo trio rebuts it in the chart. Offers an "unable to determine" option. Fair.
- T4 MA denial: improving-markers-equal-home framing. Rebuttals present: perfusion study + vascular consult, skilled wound frequency, PT stairs/offloading, OT teach-back failure, case-management home and night-caregiver limits. Fair.
- T6 concurrent-review request: a neutral determination prompt by design (not a wrong claim); used as the prompt, not the answer. Fair.
All four are fair and chart-rebuttable, consistent with the per-task A0.5 records.

## Net
Zero blocking issues remain in the DOCX substrate or writer-produced media. EW31 has been regenerated to the corrected spec and eye-checked against EW9.
