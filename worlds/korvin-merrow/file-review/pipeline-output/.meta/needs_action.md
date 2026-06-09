# Needs Action

95 unresolved finding(s) the SPL should review before shipping.

- **Breaking:** 11
- **High:** 84

---

### 1. [BREAKING] red_team_shortcut

**Files:** discharge_summary_request_05242026.docx, readmission_risk_review_request_06232026.docx, discharge_readiness_care_coordination_request_05242026.docx, consultant_synthesis_care_plan_request_05242026.docx, hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx

Multiple documents contain extensive meta-language acknowledging the documents are part of a constructed exercise. References to 'locked world record EW1–EW22', 'world close', 'world-close day', and 'world-close snapshot' explicitly reveal these are constructed scenario documents, not real medical records. A solver could use these references to understand the entire document architecture and locate specific answers by EW identifier.

_Evidence:_ Pull from the locked world record EW1–EW22; do not author beyond what those documents support

### 2. [BREAKING] red_team_shortcut

**Files:** discharge_summary_request_05242026.docx

The discharge summary request document explicitly maps EW identifiers to document contents and tells the solver exactly what each source contains and what clinical issues to find in each. This is a complete answer key mapping sources to findings.

_Evidence:_ Draw from EW1–EW3 and the baseline anchors in EW7... HD1–HD6 (EW8–EW11, with objective trend reconciliation against EW12)... prednisone, handle provenance through the rheumatology-led source hierarchy (EW6 outpatient rheumatology)... PT (EW18), OT (EW19), and nursing observations (EW17)... EW20... EW22

### 3. [BREAKING] red_team_shortcut

**Files:** readmission_risk_review_request_06232026.docx

The readmission risk review request explicitly names all eight risk domains the task is likely testing, complete with EW source identifiers and the specific frictions (F1, F3) to find. This telegraphs every 'trap' in the scenario.

_Evidence:_ Cardiorenal medication restart sequencing risk — Cardiology (Dr. Caldrane) vs Nephrology (Dr. Solthar) time-qualified addenda EW10–EW11 and EW15; trend substrate EW16... Prednisone source-error risk — Rheumatology provenance EW6 (Dr. Halvek)... Consultant-friction unresolved risk — Cardiology vs Nephrology (F1) and Endocrinology vs Primary Team (F3)

### 4. [BREAKING] red_team_shortcut

**Files:** consultant_synthesis_care_plan_request_05242026.docx

The consultant synthesis request document explicitly names three 'frictions' (F1, F2, F3) that are 'still live' and tells the solver exactly what they are and how to handle them. This is editorial/interpretive commentary that tells the reader what to conclude.

_Evidence:_ F1 — Cardiology vs Nephrology on restart timing... F2 — Family vs Primary Team on discharge readiness... F3 — Endocrinology vs Primary Team on steroid interpretation

### 5. [BREAKING] red_team_shortcut

**Files:** sleep_study_osa_history_summary_05182026.docx, problem_list_history_snapshot_05182026.docx, outpatient_rheumatology_prednisone_provenance_05212026.docx

Multiple documents contain explicit 'guardrails' sections that coach the reader on what NOT to conclude, effectively telling a solver what the traps are. The sleep study summary is particularly egregious, listing specific wrong conclusions to avoid.

_Evidence:_ This summary must not: explain the near-fall; explain functional decline; prove discharge is safe or unsafe; create an acute respiratory arc; create hidden hypoxemia or respiratory failure; replace functional, family, nursing, or care-coordination sources.

### 6. [BREAKING] red_team_shortcut

**Files:** sleep_study_osa_history_summary_05182026.docx

The sleep study document contains interpretive commentary telling the reader exactly how to weigh the document — that it is 'low-stakes chronic-reserve texture' and does not 'add new oxygen requirements, acute respiratory failure, updated sleep-study findings, a hidden cause of altered mental status, a definitive functional explanation.' Real documents do not coach readers on what conclusions to avoid.

_Evidence:_ This file does not add: new oxygen requirements; acute respiratory failure; updated sleep-study findings; a hidden cause of altered mental status; a definitive functional explanation.

### 7. [BREAKING] red_team_shortcut

**Files:** problem_list_history_snapshot_05182026.docx

The problem list snapshot contains the explicit guardrail 'No post-world information, discharge outcome, follow-up findings, task prompt, expected output, or grading material is contained in this snapshot.' This meta-language acknowledges the exercise structure.

_Evidence:_ No post-world information, discharge outcome, follow-up findings, task prompt, expected output, or grading material is contained in this snapshot.

### 8. [BREAKING] red_team_shortcut

**Files:** discharge_medication_reconciliation_request_05242026.docx

The discharge medication reconciliation request explicitly tells the solver the exact structure of the expected output and which EW documents to use for each section, functioning as an answer template rather than a realistic clinical document.

_Evidence:_ Please draw on, at minimum, the following chart sources: EW4... EW5... EW6... EW10... EW11... EW13... EW14... EW15... EW16... EW19... EW20

### 9. [BREAKING] red_team_shortcut

**Files:** post_discharge_followup_request_05312026.docx

The post-discharge follow-up request contains scope constraints that acknowledge the artificial nature of the exercise: 'The hospital record I have access to closes 2026-05-23 at 18:00. There is no post-discharge clinical file available to me... Your reassessment must be grounded in the hospitalization evidence only.'

_Evidence:_ The hospital record I have access to closes 2026-05-23 at 18:00. There is no post-discharge clinical file available to me

### 10. [BREAKING] red_team_shortcut

**Files:** discharge_readiness_care_coordination_request_05242026.docx

The discharge readiness request document explicitly lists all eight headed sections required and tells the solver exactly which clinical observations matter (evening confusion, executive slowing, 19-item regimen, Mara's quote about 'better than Monday'), effectively pre-analyzing the documents.

_Evidence:_ EW17 — Nursing observation flowsheet summary: intake trend, supervised ambulation, intermittent evening confusion noted HD1–HD4... EW19 — Occupational Therapy assessment: ADL/IADL findings, executive slowing under complexity, medication-organization errors... EW20 — Family communication record: Mara Merrow's... HD6 statement on the distinction between 'better than Monday' and ready to manage next steps

### 11. [BREAKING] red_team_shortcut

**Files:** home_support_equipment_reference_05222026.docx

The home support equipment reference document uses the phrase 'world close' — explicit meta-language acknowledging the constructed exercise.

_Evidence:_ Date / Anchor: HD5–HD6 through 05/22/2026 | World close 05/23/2026 18:00

### 12. [HIGH] qc

**Files:** readmission_risk_review_request_06232026.docx

(no description)

### 13. [HIGH] red_team_shortcut

**Files:** sleep_study_osa_history_summary_05182026.docx

The filename 'sleep_study_osa_history_summary_05182026.docx' combined with its extensive guardrails section telegraphs that OSA is a red herring / distractor document in the exercise, making it trivially easy for a solver to deprioritize it without reading.

_Evidence:_ sleep_study_osa_history_summary_05182026.docx

### 14. [HIGH] red_team_shortcut

**Files:** occupational_therapy_assessment_05202026.docx

The OT assessment contains explicit interpretive commentary coaching the reader on how to weigh the findings: 'The findings described above are subtle rather than dramatic and are easy to overlook... Reading any one of these sources in isolation is likely to understate the supervision need.' Real OT notes do not tell the reader that findings are 'easy to overlook.'

_Evidence:_ The findings described above are subtle rather than dramatic and are easy to overlook against the medical improvement trajectory... Reading any one of these sources in isolation is likely to understate the supervision need around the discharge medication list.

### 15. [HIGH] qc

**Files:** case_management_social_work_discharge_note_05222026.docx

Patient is 62 years old (DOB 02/18/1964, encounter date 05/18/2026) but is listed as having Medicare Part A & B primary coverage. Standard Medicare eligibility begins at age 65. Eligibility at 62 requires a qualifying disability (24+ months of SSDI) or ESRD, neither of which is documented in the chart. The problem list includes CKD stage 3 (not ESRD) and no disability determination appears anywhere. While there may be an undocumented disability pathway (e.g., HFrEF-related disability), this is not stated, creating an applicability gap that could affect insurance-dependent reasoning for home health eligibility screening, equipment authorization, and benefit verification.

### 16. [HIGH] qc

**Files:** medication_administration_record_05232026.docx

The MAR records prednisone as administered on all six hospital days but never specifies the numeric milligram dose given. While this is consistent with the intentional prednisone-uncertainty design theme, it creates a functional gap: a reader performing medication reconciliation or evaluating adequacy of stress-dose steroid coverage cannot determine what was actually administered. A real MAR would contain a specific dose. This is the single most significant ambiguity across all provided documents, as it affects clinical reasoning about steroid adequacy during acute illness. No must_contain or must_not_contain constraint addresses this specific gap.

### 17. [HIGH] qc

**Files:** consultant_synthesis_care_plan_request_05242026.docx, discharge_readiness_care_coordination_request_05242026.docx

Both request documents reference source files by EW identifiers without a formal crosswalk mapping EW numbers to document filenames. While most can be inferred contextually (e.g., EW14 = Nephrology, EW15 = Cardiology), the mapping is implicit. If a reader lacks the full document set or misassigns an EW number, they would retrieve the wrong source. No explicit EW-to-filename table is provided in any document.

### 18. [HIGH] qc

**Files:** medication_administration_record_05232026.docx

The MAR records prednisone as administered on all 6 hospital days but never specifies the dose given. A medication administration record typically requires a dose for every administered medication. No other provided document supplies this value. The reference chain (MAR → 'attending plan' → progress notes) terminates without a concrete numeric dose in any document. This appears to be an intentional design choice to maintain the 'no numeric prednisone dose asserted' constraint across the document set, but it creates a structurally anomalous MAR entry — a medication recorded as 'GIVEN' without a dose amount.

### 19. [HIGH] qc

**Files:** initial_medication_reconciliation_note_05182026.docx, medication_administration_record_05232026.docx

The ferrous sulfate every-other-day schedule breaks pattern between HD5 and HD6. If the on/off pattern is HD1-on, HD2-off, HD3-on, HD4-off, HD5-on, HD6-off, then HD5 should have been given (or held with reason) as an on-day and HD6 should have been NOT ORDERED as an off-day. Instead, HD5 shows HELD and HD6 shows GIVEN. This could be interpreted as a make-up dose, but the MAR does not use that terminology — HD6 is not flagged as 'make-up' or 'schedule shift.' The inconsistency is minor but represents a pattern break not explained by any provided document.

### 20. [HIGH] qc

**Files:** H&P, progress_HD1_HD2, HD3_progress, discharge_snapshot, discharge_summary_request

Cross-packet mismatch: 'attending hospitalist' has different values across documents in different QC packets

### 21. [HIGH] qc

**Files:** H&P, ED_triage, ED_provider, progress_HD1_HD2, discharge_snapshot, case_mgmt

Cross-packet mismatch: 'admission date' has different values across documents in different QC packets

### 22. [HIGH] qc

**Files:** H&P, PCI_summary, problem_list, cardiology, MedRec

Cross-packet mismatch: 'pci date' has different values across documents in different QC packets

### 23. [HIGH] qc

**Files:** H&P, sleep_summary

Cross-packet mismatch: 'sleep study date' has different values across documents in different QC packets

### 24. [HIGH] qc

**Files:** discharge_snapshot, discharge_summary_request, discharge_med_rec_request, discharge_readiness_request, med_safety_handoff, case_mgmt

Cross-packet mismatch: 'planned discharge date' has different values across documents in different QC packets

### 25. [HIGH] qc

**Files:** H&P, ED_provider, progress_HD1_HD2, trend_summary

Cross-packet mismatch: 'creatinine admission' has different values across documents in different QC packets

### 26. [HIGH] qc

**Files:** H&P, baseline_summary, trend_summary, ED_provider, progress_HD1_HD2

Cross-packet mismatch: 'creatinine baseline' has different values across documents in different QC packets

### 27. [HIGH] qc

**Files:** baseline_summary, H&P, ED_triage, trend_summary, med_safety_handoff

Cross-packet mismatch: 'dry weight' has different values across documents in different QC packets

### 28. [HIGH] qc

**Files:** med_safety_handoff, med_recon, pharmacy_refill, nephrology, MAR

Cross-packet mismatch: 'sacubitril/valsartan dose' has different values across documents in different QC packets

### 29. [HIGH] qc

**Files:** med_safety_handoff, med_recon, pharmacy_refill, nephrology, MAR, MedRec

Cross-packet mismatch: 'carvedilol dose' has different values across documents in different QC packets

### 30. [HIGH] qc

**Files:** med_safety_handoff, med_recon, pharmacy_refill, MAR, MedRec

Cross-packet mismatch: 'spironolactone dose' has different values across documents in different QC packets

### 31. [HIGH] qc

**Files:** med_safety_handoff, med_recon, pharmacy_refill, nephrology, MAR, MedRec

Cross-packet mismatch: 'empagliflozin dose' has different values across documents in different QC packets

### 32. [HIGH] qc

**Files:** med_safety_handoff, med_recon, pharmacy_refill, MAR, MedRec

Cross-packet mismatch: 'furosemide dose' has different values across documents in different QC packets

### 33. [HIGH] qc

**Files:** PCI_summary, med_recon, pharmacy_refill, cardiology, MAR, MedRec

Cross-packet mismatch: 'aspirin dose' has different values across documents in different QC packets

### 34. [HIGH] qc

**Files:** PCI_summary, med_recon, pharmacy_refill, cardiology, MAR, MedRec

Cross-packet mismatch: 'atorvastatin dose' has different values across documents in different QC packets

### 35. [HIGH] qc

**Files:** HD3_progress, readmission_risk_request

Cross-packet mismatch: 'morse fall scale score' has different values across documents in different QC packets

### 36. [HIGH] qc

**Files:** OT_assessment, discharge_med_rec_request, discharge_readiness_request, med_safety_handoff

Cross-packet mismatch: 'home medication item count' has different values across documents in different QC packets

### 37. [HIGH] qc

**Files:** H&P, discharge_snapshot, case_mgmt, home_support, SynthReq

Cross-packet mismatch: 'daughter name' has different values across documents in different QC packets

### 38. [HIGH] qc

**Files:** H&P, home_support, case_mgmt, PT

Cross-packet mismatch: 'exterior steps' has different values across documents in different QC packets

### 39. [HIGH] qc

**Files:** H&P, home_support, case_mgmt, PT

Cross-packet mismatch: 'home layout' has different values across documents in different QC packets

### 40. [HIGH] qc

**Files:** H&P, ED_triage, progress_HD1_HD2, HD3_progress, progress_notes, cardiology, family_conf

Cross-packet mismatch: 'code status' has different values across documents in different QC packets

### 41. [HIGH] qc

**Files:** H&P, PCI_summary, MedRec

Cross-packet mismatch: 'pci vessel' has different values across documents in different QC packets

### 42. [HIGH] qc

**Files:** discharge_snapshot, case_mgmt

Cross-packet mismatch: 'followup pcp window' has different values across documents in different QC packets

### 43. [HIGH] qc

**Files:** ED_triage, H&P, trend_summary, ED_Triage, HD1-2

Cross-packet mismatch: 'weight' has different values across documents in different QC packets

### 44. [HIGH] qc

**Files:** ED_triage, problem_list, ED_Triage

Cross-packet mismatch: 'height' has different values across documents in different QC packets

### 45. [HIGH] qc

**Files:** H&P, ED_provider, progress_HD1, trend_summary, nephrology_HD2, ED_Provider, HD1-2, HD3, HD4, HD5-6

Cross-packet mismatch: 'admission creatinine' has different values across documents in different QC packets

### 46. [HIGH] qc

**Files:** progress_HD2, trend_summary, HD1-2, HD3, HD4

Cross-packet mismatch: 'hd2 creatinine' has different values across documents in different QC packets

### 47. [HIGH] qc

**Files:** progress_HD3, trend_summary, nephrology_HD3, cardiology_HD3, HD3, HD4

Cross-packet mismatch: 'hd3 creatinine' has different values across documents in different QC packets

### 48. [HIGH] qc

**Files:** trend_summary, nephrology_HD4, cardiology_HD4, endocrinology_HD4, HD4, HD5-6

Cross-packet mismatch: 'hd4 creatinine' has different values across documents in different QC packets

### 49. [HIGH] qc

**Files:** trend_summary, nephrology_HD5, cardiology_HD5, HD5-6

Cross-packet mismatch: 'hd5 creatinine' has different values across documents in different QC packets

### 50. [HIGH] qc

**Files:** trend_summary, nephrology_HD6, cardiology_HD6, HD5-6

Cross-packet mismatch: 'hd6 creatinine' has different values across documents in different QC packets

### 51. [HIGH] qc

**Files:** H&P, trend_summary, nephrology, ED_Provider, HD1-2, HD3, HD4, HD5-6

Cross-packet mismatch: 'baseline creatinine' has different values across documents in different QC packets

### 52. [HIGH] qc

**Files:** H&P, progress_HD1, trend_summary, nephrology, ED_Provider, HD1-2

Cross-packet mismatch: 'admission bun' has different values across documents in different QC packets

### 53. [HIGH] qc

**Files:** H&P, progress_HD1, trend_summary, nephrology, ED_Provider, HD1-2, MAR

Cross-packet mismatch: 'admission potassium' has different values across documents in different QC packets

### 54. [HIGH] qc

**Files:** H&P, ED_provider, progress_HD1, trend_summary, nephrology, ED_Provider, HD1-2

Cross-packet mismatch: 'admission wbc' has different values across documents in different QC packets

### 55. [HIGH] qc

**Files:** H&P, ED_provider, progress_HD1, trend_summary

Cross-packet mismatch: 'admission glucose range' has different values across documents in different QC packets

### 56. [HIGH] qc

**Files:** H&P, problem_list

Cross-packet mismatch: 'psg date' has different values across documents in different QC packets

### 57. [HIGH] qc

**Files:** med_recon, pharmacy_refill, nephrology, MAR, MedRec

Cross-packet mismatch: 'metformin dose' has different values across documents in different QC packets

### 58. [HIGH] qc

**Files:** med_recon, pharmacy_refill, MAR

Cross-packet mismatch: 'insulin glargine home dose' has different values across documents in different QC packets

### 59. [HIGH] qc

**Files:** med_recon, pharmacy_refill, nephrology, MAR, MedRec

Cross-packet mismatch: 'gabapentin dose' has different values across documents in different QC packets

### 60. [HIGH] qc

**Files:** med_recon, pharmacy_refill, MAR, MedRec

Cross-packet mismatch: 'alendronate dose' has different values across documents in different QC packets

### 61. [HIGH] qc

**Files:** med_recon, pharmacy_refill, MAR, MedRec

Cross-packet mismatch: 'pantoprazole dose' has different values across documents in different QC packets

### 62. [HIGH] qc

**Files:** med_recon, pharmacy_refill, MAR, MedRec

Cross-packet mismatch: 'ntg dose' has different values across documents in different QC packets

### 63. [HIGH] qc

**Files:** med_recon, family_conf, discharge_readiness_req

Cross-packet mismatch: 'home medication count' has different values across documents in different QC packets

### 64. [HIGH] qc

**Files:** PT_assessment_HD3, PT_assessment_HD5, progress_HD3

Cross-packet mismatch: 'morse fall scale' has different values across documents in different QC packets

### 65. [HIGH] qc

**Files:** CM_SW, discharge_readiness_req

Cross-packet mismatch: 'pcp follow-up interval' has different values across documents in different QC packets

### 66. [HIGH] qc

**Files:** CM_SW, pharmacy_refill

Cross-packet mismatch: 'patient home address' has different values across documents in different QC packets

### 67. [HIGH] qc

**Files:** ED_triage, H&P, ED_Triage

Cross-packet mismatch: 'triage temperature' has different values across documents in different QC packets

### 68. [HIGH] qc

**Files:** ED_triage, H&P

Cross-packet mismatch: 'triage heart rate' has different values across documents in different QC packets

### 69. [HIGH] qc

**Files:** ED_triage, H&P

Cross-packet mismatch: 'triage respiratory rate' has different values across documents in different QC packets

### 70. [HIGH] qc

**Files:** ED_Triage, H&P

Cross-packet mismatch: 'triage hr' has different values across documents in different QC packets

### 71. [HIGH] qc

**Files:** ED_Triage, H&P, HD1-2

Cross-packet mismatch: 'blood pressure' has different values across documents in different QC packets

### 72. [HIGH] qc

**Files:** ED_Triage, H&P

Cross-packet mismatch: 'triage glucose' has different values across documents in different QC packets

### 73. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'sacubitril valsartan dose' has different values across documents in different QC packets

### 74. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'glargine home dose' has different values across documents in different QC packets

### 75. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'ferrous sulfate dose' has different values across documents in different QC packets

### 76. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'calcium vitd dose' has different values across documents in different QC packets

### 77. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'acetaminophen dose' has different values across documents in different QC packets

### 78. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'peg dose' has different values across documents in different QC packets

### 79. [HIGH] qc

**Files:** MedRec, MAR

Cross-packet mismatch: 'senna dose' has different values across documents in different QC packets

### 80. [HIGH] qc

**Files:** ED_Triage, H&P, ED_Provider, PT

Cross-packet mismatch: 'near fall date' has different values across documents in different QC packets

### 81. [HIGH] qc

**Files:** H&P, MedRec, HD4, SynthReq

Cross-packet mismatch: 'rheumatologist' has different values across documents in different QC packets

### 82. [HIGH] qc

**Files:** HD5-6, SynthReq

Cross-packet mismatch: 'discharge target' has different values across documents in different QC packets

### 83. [HIGH] qc

**Files:** HD5-6, SynthReq

Cross-packet mismatch: 'case manager' has different values across documents in different QC packets

### 84. [HIGH] qc

**Files:** HD5-6, SynthReq

Cross-packet mismatch: 'social worker' has different values across documents in different QC packets

### 85. [HIGH] identity_consistency

**Files:** discharge_facing_plan_snapshot_05232026.docx, home_support_equipment_reference_05222026.docx, discharge_readiness_care_coordination_request_05242026.docx, case_management_social_work_discharge_note_05222026.docx, family_communication_care_conference_05222026.docx, admission_history_and_physical_05182026.docx

The patient's adult daughter is consistently named 'Lenora Merrow-Halsey' across five documents but is extracted as 'Lenora Merrow' (without the hyphenated married surname) in the discharge-facing plan snapshot; this should be reconciled to the canonical hyphenated form 'Lenora Merrow-Halsey' for identity consistency.

_Evidence:_ {"discharge_facing_plan_snapshot_05232026.docx": "Lenora Merrow (referenced as 'Lenora')", "home_support_equipment_reference_05222026.docx": "Lenora Merrow-Halsey", "discharge_readiness_care_coordination_request_05242026.docx": "Lenora Merrow-Halsey", "case_management_social_work_discharge_note_05222026.docx": "Lenora Merrow-Halsey", "family_communication_care_conference_05222026.docx": "Lenora Merrow-Halsey", "admission_history_and_physical_05182026.docx": "Lenora Merrow-Halsey"}

### 86. [HIGH] certifier.formatting_consistency

**Files:** (unspecified)

hospitalist_progress_hd1_hd2_05192026.docx uses a plain-text (non-table) letterhead format with pipe `|` as the inline separator — verbatim: `Hospital Medicine | 5 Harbor Crest Way, Bridgehollow, PA 15211` and `*Main: (412) 555-0143 | Confidential | Medical Records*` — while the companion HD3 and HD4 hospitalist progress files from the same author and service use a proper 2-column table header (org name / dept / address / phone in the left cell; Confidential / Medical Records in the right). The patient demographics block also uses a labeled format (`PATIENT Korvin Merrow, 62 y | SEX Male | DOB 02/18/1964 | MRN KM-6427819`) instead of the standard unlabeled all-caps format used across HD3, HD4, and every specialty consult (`KORVIN MERROW 62 y | Male | DOB 02/18/1964 | | | MRN KM-6427819`).

_Suggested fix:_ Replace the plain-text header with a 2-column table matching hospitalist_progress_hd3_05202026.docx: left cell contains 'MERCY VALE REGIONAL MEDICAL CENTER' / 'Hospital Medicine' / '5 Harbor Crest Way, Bridgehollow, PA 15211' / 'Main: (412) 555-0143' on separate lines; right cell contains 'Confidential' / 'Medical Records'. Also replace the patient block row from 'PATIENT Korvin Merrow, 62 y | SEX Male | DOB 02/18/1964 | MRN KM-6427819' to the standard format 'KORVIN MERROW 62 y | Male | DOB 02/18/1964 | | | MRN KM-6427819' matching HD3/HD4.

### 87. [HIGH] certifier.formatting_consistency

**Files:** (unspecified)

hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx also uses a plain-text (non-table) letterhead, but with middle-dot · as the separator — verbatim: `Hospital Medicine · 5 Harbor Crest Way, Bridgehollow, PA 15211` and `*Main: (412) 555-0143 · Confidential · Medical Records*` — a different separator character from HD1–HD2 (which uses `|`) and a different structure from HD3/HD4 (which use a table). The patient demographics block further mixes · and | within the same row: `PATIENT Korvin Merrow, 62 y · Male · DOB 02/18/1964 | MRN KM-6427819 · FIN KM-2026-051877`.

_Suggested fix:_ Replace the plain-text header with a 2-column table matching hospitalist_progress_hd3_05202026.docx (same fix as HD1–HD2 above). Replace the patient demographics row with the standard unlabeled all-caps format: 'KORVIN MERROW 62 y | Male | DOB 02/18/1964 | | | MRN KM-6427819', eliminating the mixed ·/| separators.

### 88. [HIGH] certifier.formatting_consistency

**Files:** (unspecified)

nursing_observation_flowsheet_summary_05232026.docx uses a middle-dot · as the inline address/phone separator inside its letterhead table's left cell — verbatim: `5 Harbor Crest Way, Bridgehollow, PA 15211 · Nursing: (412) 555-0143` — while every other non-consult Mercy Vale service document (admissions H&P, MAR, med rec, PT assessment, case management, family conference, problem list, readmission risk) uses `|` or a line break to separate address from phone. The · style is the deliberate format for specialty consult documents (Cardiology, Nephrology, Endocrinology) but not for nursing/medicine service documents.

_Suggested fix:_ In the left cell of the header table, change `5 Harbor Crest Way, Bridgehollow, PA 15211 · Nursing: (412) 555-0143` to place address and phone on separate lines (line break) or use a pipe separator: `5 Harbor Crest Way, Bridgehollow, PA 15211 | Nursing: (412) 555-0143`, consistent with the format used by other Mercy Vale non-consult service documents such as physical_therapy_assessment_05202026.docx.

### 89. [HIGH] certifier.specialized_doc_authenticity

**Files:** (unspecified)

The initial endocrinology consultation note (HD4 / 05/21/2026) has no physical examination section. The section labeled '***Clinical context.***' contains only laboratory values, vital-sign ranges, and subjective/nursing observations ('Patient reports fatigue and low stamina; nursing notes intermittent evening slowing') — not a practitioner-performed bedside examination. Both peer inpatient consultations include formal physical exam sections (Cardiology: 'Physical Examination (05/19/2026)' with cardiovascular, pulmonary, JVP, and extremity findings; Nephrology: similar implicit exam data). A physical examination is a structural non-negotiable of an inpatient initial consultation note.

_Suggested fix:_ Insert a '***Physical Examination (05/21/2026).***' subsection immediately after the '***Clinical context.***' paragraph and before '***Endocrine interpretation.***'. At minimum document: general appearance (alert/ill-appearing), skin (relevant to chronic steroid exposure — e.g., no striae, no skin fragility noted, no moon facies), cardiovascular and pulmonary status (e.g., regular rate and rhythm, lungs clear), and any focused endocrine-relevant findings (e.g., no thyromegaly, no lymphadenopathy). If the consultation was records-based without direct examination, state that explicitly: 'Patient not directly examined for this addendum; this note represents a chart and data review.' Either a brief exam or an explicit records-review statement is required to meet genre structure.

### 90. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

Finding #2: The MAR records prednisone as administered on all six hospital days with no numeric milligram dose. Every row reads "GIVEN — interim inpatient steroid coverage per attending plan" — no dose amount is stated anywhere across HD1–HD6. This creates a functional gap for any reviewer performing medication reconciliation or evaluating steroid adequacy, since the MAR is the authoritative record of what was actually administered.

_Suggested fix:_ In the prednisone STEROID section, for each of HD1–HD6, append the numeric dose administered to the action cell (e.g., change "GIVEN — interim inpatient steroid coverage per attending plan" to "GIVEN [X mg] — interim inpatient steroid coverage per attending plan"). If a fixed dose cannot be asserted due to the intentional provenance uncertainty, add a parenthetical note in the table header such as "(dose per attending verbal order — see progress notes; no fixed numeric dose entered pending rheumatology reconciliation)" so the absence of a number is explicitly flagged rather than silently absent.

### 91. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

Finding #4: Duplicate of finding #2 — the same MAR entry confirms prednisone was recorded as "GIVEN" with no dose on any of the six hospital days. The reference chain (MAR → 'attending plan' → progress notes) terminates without a concrete numeric dose in any document that the MAR itself cites.

_Suggested fix:_ Same fix as finding #2: add the numeric dose given (or an explicit placeholder with a cross-reference to the authoritative source) to each of the six HD Action rows so that the MAR does not show a medication as GIVEN without any dose quantity. For example, amend each note row to read "Home taper unverified; interim dose [X mg] per attending verbal order; source reconstruction ongoing" rather than leaving the dose field blank.

### 92. [HIGH] certifier.trap_integrity_premature-or-delayed-cardiorenal-restart

**Files:** (unspecified)

Nephrology HD4 addendum enumerates the exact parameter categories from the trap's reveal surface: "Each reintroduction should be tied to specific, verifiable parameters (creatinine/eGFR trajectory, serum potassium, blood pressure including standing if obtainable, oral intake, and weight) rather than to a calendar day or to global 'improvement.'" This is nearly verbatim the trap's reveal surface, allowing a task-doer to extract the gating framework directly without synthesizing it from the consultant tension.

_Suggested fix:_ Remove the explicit enumeration '(creatinine/eGFR trajectory, serum potassium, blood pressure including standing if obtainable, oral intake, and weight)' from the HD4 addendum. Replace with language that defers parameter definition to a joint discussion among Nephrology, Cardiology, and the primary team without naming the categories. For example: 'Restart sequencing should be staged and parameter-gated rather than simultaneous. Each reintroduction should be gated against verifiable clinical parameters to be jointly defined with Cardiology and the primary team — not against a calendar day or a global impression of improvement.'

### 93. [HIGH] certifier.trap_integrity_premature-or-delayed-cardiorenal-restart

**Files:** (unspecified)

Nephrology HD5 addendum names sacubitril/valsartan as the first restart candidate at a reduced dose and specifies the monitoring cadence: "It is reasonable to consider a low-dose reintroduction of sacubitril/valsartan in the near term if blood pressure reserve and serum potassium remain favorable and oral intake is stable… Suggest reintroduction at a dose below the home regimen, with creatinine, potassium, and seated/standing blood pressure rechecked within 24–48 hours of the first dose." This resolves the 'which drug first' sequencing question and the monitoring interval — both key elements of the correct synthesis path.

_Suggested fix:_ Remove the specific identification of sacubitril/valsartan as the first restart candidate and remove the '24–48 hours' monitoring instruction. Replace with language that acknowledges improving renal parameters without committing to an agent or timeline. For example: 'Renal recovery continues to trend favorably. As the clinical picture stabilizes, the primary team should initiate sequencing discussions with Cardiology to identify the appropriate first candidate for reintroduction and the parameter thresholds that would govern that decision. Nephrology will provide input on renal and electrolyte readiness as that discussion proceeds.'

### 94. [HIGH] certifier.trap_integrity_functional-evidence-omission

**Files:** (unspecified)

The HD3 hospitalist note explicitly declares PT/OT findings 'central rather than supplementary' and names the OT medication-gap finding: 'PT and OT findings are being treated as central rather than supplementary...medication-management gap on OT testing is directly relevant to home safety.' This is a physician summary that directly counters the trap's 'easy to skip in favor of physician summaries' mechanism — a solver reading only HD3 already knows PT/OT are indispensable AND that OT found a medication-management gap, without needing to open the OT carrier file.

_Suggested fix:_ Replace 'PT and OT findings are being treated as central rather than supplementary. The team has communicated to Mara that medical improvement is real but not sufficient on its own, and that the medication-management gap on OT testing is directly relevant to home safety.' with neutral deference: 'PT and OT assessments are in progress; findings are documented in the respective therapy notes and will inform discharge readiness planning.' Remove the 'central rather than supplementary' framing and the explicit OT medication-gap reference.

### 95. [HIGH] certifier.trap_integrity_functional-evidence-omission

**Files:** (unspecified)

The T3 task request's required section headings enumerate sub-topics that map precisely to PT and OT carrier-file contents: 'Functional readiness — functional mobility findings from the inpatient course, current fall risk, ADL and IADL status relative to baseline, assistive-device plan.' and 'Medication-management capacity — Patient's ability to manage the 19-item home regimen; teach-back status; as documented in the chart.' These sub-items name the exact categories documented in the PT assessment (fall risk / Morse Fall Scale, assistive device) and OT assessment (ADL/IADL, medication management), making it structurally difficult for a solver to omit functional evidence from T3 — directly weakening the trap's 'easy to skip' mechanism.

_Suggested fix:_ Broaden the sub-topic language so it describes a category of information without pre-mapping it to carrier file contents. Replace section 1's enumerated sub-items with: 'Functional readiness — describe the patient's current functional status and any limitations documented during the hospitalization.' Replace section 2 with: 'Cognitive readiness — describe the patient's cognitive and attention status based on available sources.' Replace section 3 with: 'Medication-management capacity — describe the patient's ability to manage his home regimen as documented.' This preserves the section structure while restoring the need for the solver to find and synthesize the carrier-file evidence independently.
