# Needs Action

75 unresolved finding(s) the SPL should review before shipping.

- **Breaking:** 3
- **High:** 72

---

### 1. [BREAKING] red_team_shortcut

**Files:** clinical/outpatient_primary_care_summary_04302026.docx

The outpatient primary care note contains language that appears to be explicitly planted for the HEDIS task: 'HFpEF was reviewed, examined, and addressed in person during this outpatient visit; this outpatient encounter formally documents her HFpEF in the outpatient setting within the measurement year.' This is editorial/meta-language about measurement-year documentation requirements, not something a real clinician would write.

_Evidence:_ HFpEF was reviewed, examined, and addressed in person during this outpatient visit; this outpatient encounter formally documents her HFpEF in the outpatient setting within the measurement year.

### 2. [BREAKING] red_team_shortcut

**Files:** clinical/outpatient_primary_care_summary_04302026.docx

The outpatient primary care note contains text that reads as planted for HEDIS frailty documentation: 'consistent with HEDIS frailty value-set documentation.' This is explicit meta-language referencing HEDIS specifications within a clinical note.

_Evidence:_ LIMITED MOBILITY at baseline; abnormal gait noted on exam with shuffling and reduced step length; uses no assistive device but endurance reduced; consistent with HEDIS frailty value-set documentation.

### 3. [BREAKING] red_team_shortcut

**Files:** tasks/task1_med_rec/preliminary_discharge_order_set_05212026.docx, tasks/task2_coding/him_preliminary_coding_worksheet_05212026.docx, tasks/task3_cdi/cdi_query_memo_05232026.docx, tasks/task4_appeal/medicare_advantage_denial_letter_05232026.docx, tasks/task5_pbm/pharmacy_benefit_rejection_05242026.docx, tasks/task6_ur/payer_concurrent_review_request_05252026.docx, tasks/task7_hedis/quality_abstraction_worksheet_06042026.docx, tasks/task9_safety/safety_event_intake_summary_06112026.docx, tasks/task10_dc/started_discharge_instruction_draft_05212026.docx

Task documents are organized into a 'tasks/' directory with subdirectories named after task types (task1_med_rec, task2_coding, task3_cdi, etc.), revealing the task structure and what each document is testing.

_Evidence:_ Directory names: tasks/task1_med_rec/, tasks/task2_coding/, tasks/task3_cdi/, tasks/task4_appeal/, tasks/task5_pbm/, tasks/task6_ur/, tasks/task7_hedis/, tasks/task9_safety/, tasks/task10_dc/

### 4. [HIGH] red_team_shortcut

**Files:** tasks/task1_med_rec/preliminary_discharge_order_set_05212026.docx

The preliminary discharge order set includes ibuprofen 400 mg PO q6h PRN (item 18 in Section C) as a deliberately planted error for the solver to catch — this is an NSAID explicitly avoided throughout the entire admission due to CKD/AKI, mentioned as contraindicated in numerous documents. It appears nowhere else in the record and is introduced only in the draft discharge order, making it an obvious planted trap.

_Evidence:_ 18. **Ibuprofen 400 mg PO q6h PRN** — knee osteoarthritis (added to PRN list for pain coverage).

### 5. [HIGH] red_team_shortcut

**Files:** tasks/task2_coding/him_preliminary_coding_worksheet_05212026.docx, clinical/wound_care_consult_05202026.docx, clinical/podiatry_debridement_note_05172026.docx

The preliminary coding worksheet proposes coding the wound as a 'pressure injury' (L89.623) as principal diagnosis, when every clinical document in the record explicitly and repeatedly states the wound is a neuropathic diabetic foot ulcer and 'NOT a wound of pressure etiology.' This is a transparently planted coding error/trap for the solver to identify and correct.

_Evidence:_ Wound care consult: 'This is **not** a wound of pressure etiology; location, mechanism, and depth are consistent with a neuropathic diabetic foot ulcer'. Coding worksheet: '**Pressure injury, left foot, stage 3** | **L89.623** | Y | **PRINCIPAL**'

### 6. [HIGH] red_team_shortcut

**Files:** tasks/task2_coding/him_preliminary_coding_worksheet_05212026.docx, tasks/task3_cdi/cdi_query_memo_05232026.docx, clinical/id_consult_note_05182026.docx

The coding worksheet proposes acute osteomyelitis (M86.171) as a confirmed secondary MCC diagnosis with POA=Y, when multiple clinical documents (ID consult, pathology, hospitalist notes) explicitly state osteomyelitis is 'not signed,' 'unconfirmed,' and 'equivocal.' This is another planted trap for the solver, with the CDI query document reinforcing it by asking the physician to clarify the same issue.

_Evidence:_ Coding worksheet: '**Acute osteomyelitis, left foot** | **M86.171** | **Y** | Secondary — MAJOR CC | MRI foot 05/18 describes **bone marrow edema**'. ID consult: 'I am **not signing acute osteomyelitis** at this time.'

### 7. [HIGH] red_team_shortcut

**Files:** tasks/task2_coding/him_preliminary_coding_worksheet_05212026.docx

The coding worksheet recommends non-capture of CKD stage 3b and anemia of CKD, claiming they are 'not clearly addressed inpatient,' when the clinical record extensively documents both conditions being actively managed throughout the stay (renal dosing, trending labs, held medications for AKI on CKD, ferrous sulfate continuation for anemia of CKD). This is a planted omission for the solver to catch.

_Evidence:_ Non-capture: 'Chronic kidney disease, stage 3b (N18.32) | **Drop** — not clearly addressed inpatient' and 'Anemia in chronic kidney disease (D63.1) | **Drop** — not clearly addressed inpatient'

### 8. [HIGH] red_team_shortcut

**Files:** tasks/task5_pbm/pharmacy_benefit_rejection_05242026.docx

The PBM rejection notice suggests TMP-SMX (Bactrim DS) as the preferred substitute for the rejected beta-lactam, when the patient has a documented sulfa allergy prominently noted in every single document in the record. This is a planted safety trap that is telegraphed by the extensive allergy documentation.

_Evidence:_ Preferred Agent: **TRIMETHOPRIM-SULFAMETHOXAZOLE DS** (Bactrim DS)

### 9. [HIGH] red_team_shortcut

**Files:** tasks/task4_appeal/medicare_advantage_denial_letter_05232026.docx, clinical/family_communication_note_05202026.docx

The Medicare Advantage denial letter states 'The member has an able-bodied adult daughter listed in the medical record as primary caregiver and emergency contact' as a reason to deny SNF, omitting the extensively documented fact that the daughter works night shifts and has only partial availability. This is a planted factual misrepresentation for the appeal task, telegraphed by the family meeting note and multiple other documents.

_Evidence:_ Denial: 'The member has an able-bodied adult daughter listed in the medical record as primary caregiver'. Family meeting: 'She wants to help but cannot be there every day.'

### 10. [HIGH] red_team_shortcut

**Files:** tasks/task1_med_rec/preliminary_discharge_order_set_05212026.docx

The preliminary discharge order set carries antibiotic renal dosing from the admission creatinine (2.1) rather than the current creatinine (1.6), when every ID and pharmacy note in the record emphatically instructs to dose to CURRENT renal function. This is another planted error.

_Evidence:_ **Cefepime 1 g IV q12h — renal dose as of admission Cr 2.1**

### 11. [HIGH] red_team_shortcut

**Files:** nursing/vital_signs_flowsheet_05162026.docx

The vital signs flowsheet shows an implausibly smooth, monotonic decline in every parameter (temp, HR, BP, RR, glucose) across all 6 hospital days with no variation — every value decreases by a regular increment each day. Real vital signs would show some fluctuation.

_Evidence:_ Temp: 38.2→37.8→37.5→37.2→37.0→36.8; HR: 104→96→92→88→84→80; Glucose: 244→212→198→186→174→162

### 12. [HIGH] red_team_shortcut

**Files:** tasks/task9_safety/safety_event_intake_summary_06112026.docx

The safety event intake document contains meta-language describing document IDs and the review structure in a way that functions as a task instruction rather than a real safety report. It explicitly enumerates which documents to review and what conclusions to reach.

_Evidence:_ "The reviewer is asked to: 1. Distinguish documented **system contributors** ... from documented **individual factors**, and to keep the analysis **multifactorial**." and "Engage the chart directly."

### 13. [HIGH] red_team_shortcut

**Files:** tasks/task7_hedis/quality_abstraction_worksheet_06042026.docx

The HEDIS abstraction worksheet contains leading instructions that essentially walk the solver to the exclusion answer: it highlights that the member is 66+, that HFpEF qualifies as Advanced Illness if documented outpatient, and that abnormal gait/limited mobility qualifies as frailty — all of which are present in the outpatient note.

_Evidence:_ "Advanced Illness + Frailty in members aged 66+. Apply per HEDIS Technical Specifications." and "(HFpEF outpatient encounter qualifies if documented)" and "(e.g., abnormal gait, limited mobility)"

### 14. [HIGH] red_team_traps

**Files:** tasks/task1_med_rec/preliminary_discharge_order_set_05212026.docx, tasks/task10_dc/started_discharge_instruction_draft_05212026.docx

T-NSAID-FOR-KNEE: The preliminary discharge order set includes ibuprofen 400 mg as item 18 in Section C, which is the concealment surface. However, the discharge instruction draft in Section 2 explicitly states 'Do NOT take ibuprofen, naproxen, or other anti-inflammatory pain pills — they are not safe for your kidneys.' This cross-document contradiction partially telegraphs the trap by making the ibuprofen entry in the order set obviously wrong when read alongside the discharge instructions.

_Evidence:_ Discharge instructions: 'Do NOT take ibuprofen, naproxen, or other anti-inflammatory pain pills — they are not safe for your kidneys.' Order set item 18: 'Ibuprofen 400 mg PO q6h PRN — knee osteoarthritis (added to PRN list for pain coverage).'

### 15. [HIGH] red_team_traps

**Files:** labs/culture_report_superficial_swab_05162026.docx, labs/culture_report_deep_tissue_05172026.docx

T-CULTURE-PROVENANCE: The superficial swab culture report includes an explicit 'Specimen Authority' section and a 'Microbiology Comment' that directly explains the trap: 'A superficial swab samples surface organisms and skin flora and may not reflect the deep-tissue pathogen.' The deep tissue culture also has an explicit 'SPECIMEN AUTHORITY HIERARCHY' table comparing the two specimens with 'Higher authority' and 'Lower authority' labels. This makes the provenance distinction so obvious it is barely a trap — a solver would have to actively ignore multiple explicit warnings to fall for it.

_Evidence:_ Superficial swab: 'This specimen is designated **lower authority** for pathogen identification in this clinical context' and 'SPECIMEN AUTHORITY HIERARCHY (for this patient)' table in the deep tissue report explicitly comparing both specimens with authority labels.

### 16. [HIGH] qc

**Files:** clinical/hospitalist_progress_hd2_05172026.docx

The HD2 progress note header records Date of Service as 05/17/2026 09:30 and Status as 'Signed / Attending cosigned', yet the body text describes the podiatric debridement that started at 14:10 the same day and includes post-debridement wound findings. The subjective section confirms the author 're-evaluated following the afternoon bedside debridement.' A signed note timestamped 09:30 should not contain detailed descriptions of events occurring 4.5 hours later unless it was finalized after 14:40 (when the procedure note was signed). The timestamp of 09:30 is inconsistent with the content. While clinical notes are sometimes opened in the morning and finalized later, the 'Signed' status paired with the 09:30 timestamp implies completion at that time, creating a temporal integrity issue for documentation auditing purposes.

### 17. [HIGH] qc

**Files:** all_14_docs, admission_hp, podiatry_note, hd2_progress, hd4_progress, abi_tbi, cdi_query, denial_letter, pbm_rejection, coding_worksheet, hedis_worksheet, safety_intake, discharge_instructions, abi_tbi_report, nursing_narrative, offloading_flowsheet, vitals_flowsheet, home_med_list, mar, case_mgmt, ot_eval, pt_eval, discharge_rights, med_hold_orders, education

Cross-packet mismatch: 'patient name' has different values across documents in different QC packets

### 18. [HIGH] qc

**Files:** ed_note, admission_hp, endocrine_note

Cross-packet mismatch: 'admission glucose' has different values across documents in different QC packets

### 19. [HIGH] qc

**Files:** admission_hp, ed_note, id_consult, endocrine_note, pcp_summary, vascular_consult

Cross-packet mismatch: 'baseline creatinine' has different values across documents in different QC packets

### 20. [HIGH] qc

**Files:** admission_hp, pcp_summary, id_consult, endocrine_note, hd2_progress, hd4_progress, mar

Cross-packet mismatch: 'baseline egfr' has different values across documents in different QC packets

### 21. [HIGH] qc

**Files:** ed_note, admission_hp, hd2_progress, hd4_progress, hd6_progress, id_consult, endocrine_note, vascular_consult, abx_plan_note

Cross-packet mismatch: 'hd1 creatinine' has different values across documents in different QC packets

### 22. [HIGH] qc

**Files:** admission_hp, hd2_progress, hd4_progress, hd6_progress, id_consult, endocrine_note, mar, med_hold_orders

Cross-packet mismatch: 'hd1 egfr' has different values across documents in different QC packets

### 23. [HIGH] qc

**Files:** hd2_progress, hd4_progress, hd6_progress, id_consult

Cross-packet mismatch: 'hd2 creatinine' has different values across documents in different QC packets

### 24. [HIGH] qc

**Files:** hd4_progress, hd6_progress, abx_plan_note, endocrine_note

Cross-packet mismatch: 'hd4 creatinine' has different values across documents in different QC packets

### 25. [HIGH] qc

**Files:** ed_note, admission_hp, hd2_progress, hd4_progress, hd6_progress, id_consult

Cross-packet mismatch: 'hd1 wbc' has different values across documents in different QC packets

### 26. [HIGH] qc

**Files:** ed_note, admission_hp, hd2_progress, id_consult

Cross-packet mismatch: 'hd1 hgb' has different values across documents in different QC packets

### 27. [HIGH] qc

**Files:** pcp_summary, admission_hp, endocrine_note

Cross-packet mismatch: 'hba1c' has different values across documents in different QC packets

### 28. [HIGH] qc

**Files:** admission_hp, pcp_summary

Cross-packet mismatch: 'height' has different values across documents in different QC packets

### 29. [HIGH] qc

**Files:** admission_hp, pcp_summary

Cross-packet mismatch: 'weight' has different values across documents in different QC packets

### 30. [HIGH] qc

**Files:** hd4_progress, abx_plan_note, hd6_progress, family_note

Cross-packet mismatch: 'deep culture organisms' has different values across documents in different QC packets

### 31. [HIGH] qc

**Files:** podiatry_note, wound_care_consult, id_consult

Cross-packet mismatch: 'wound length' has different values across documents in different QC packets

### 32. [HIGH] qc

**Files:** podiatry_note, wound_care_consult, id_consult

Cross-packet mismatch: 'wound width' has different values across documents in different QC packets

### 33. [HIGH] qc

**Files:** podiatry_note, wound_care_consult, id_consult

Cross-packet mismatch: 'wound depth' has different values across documents in different QC packets

### 34. [HIGH] qc

**Files:** pathology_report, hd6_progress, family_note

Cross-packet mismatch: 'pathology microscopic dx' has different values across documents in different QC packets

### 35. [HIGH] qc

**Files:** admission_hp, ed_note, pcp_summary, endocrine_note, hd2_progress, hd4_progress, hd6_progress

Cross-packet mismatch: 'glargine dose' has different values across documents in different QC packets

### 36. [HIGH] qc

**Files:** admission_hp, ed_note, pcp_summary, endocrine_note, discharge_order, discharge_instructions, home_med_list, med_hold_orders

Cross-packet mismatch: 'metformin dose' has different values across documents in different QC packets

### 37. [HIGH] qc

**Files:** abx_plan_note, mar, hd4_progress

Cross-packet mismatch: 'cefepime dose' has different values across documents in different QC packets

### 38. [HIGH] qc

**Files:** pcp_summary, hd4_progress, family_note

Cross-packet mismatch: 'insurance' has different values across documents in different QC packets

### 39. [HIGH] qc

**Files:** eye_exam, admission_hp, pcp_summary, endocrine_note

Cross-packet mismatch: 'eye exam result' has different values across documents in different QC packets

### 40. [HIGH] qc

**Files:** admission_hp, pcp_summary, family_note

Cross-packet mismatch: 'husband death' has different values across documents in different QC packets

### 41. [HIGH] qc

**Files:** podiatry_note, hd2_progress, safety_intake

Cross-packet mismatch: 'debridement start time' has different values across documents in different QC packets

### 42. [HIGH] qc

**Files:** abi_tbi_report, hd4_progress

Cross-packet mismatch: 'abi tbi study start' has different values across documents in different QC packets

### 43. [HIGH] qc

**Files:** abi_tbi_report, hd4_progress

Cross-packet mismatch: 'abi tbi report finalized' has different values across documents in different QC packets

### 44. [HIGH] qc

**Files:** admission_hp, renal_trend, discharge_order

Cross-packet mismatch: 'egfr baseline' has different values across documents in different QC packets

### 45. [HIGH] qc

**Files:** podiatry_note, deep_culture, hd4_progress

Cross-packet mismatch: 'deep culture collection time' has different values across documents in different QC packets

### 46. [HIGH] qc

**Files:** admission_hp, discharge_order, discharge_instructions, home_med_list, med_hold_orders

Cross-packet mismatch: 'lisinopril dose' has different values across documents in different QC packets

### 47. [HIGH] qc

**Files:** admission_hp, discharge_order, discharge_instructions, home_med_list, med_hold_orders

Cross-packet mismatch: 'empagliflozin dose' has different values across documents in different QC packets

### 48. [HIGH] qc

**Files:** podiatry_note, coding_worksheet

Cross-packet mismatch: 'wound etiology podiatry' has different values across documents in different QC packets

### 49. [HIGH] qc

**Files:** podiatry_note, hd4_progress, coding_worksheet, cdi_query

Cross-packet mismatch: 'osteomyelitis status' has different values across documents in different QC packets

### 50. [HIGH] qc

**Files:** admission_hp, discharge_order, discharge_instructions

Cross-packet mismatch: 'ibuprofen presence' has different values across documents in different QC packets

### 51. [HIGH] qc

**Files:** discharge_order, renal_trend

Cross-packet mismatch: 'cefepime renal dose basis' has different values across documents in different QC packets

### 52. [HIGH] qc

**Files:** admission_hp, denial_letter

Cross-packet mismatch: 'patient living situation' has different values across documents in different QC packets

### 53. [HIGH] qc

**Files:** admission_hp, podiatry_note, hd4_progress, safety_intake, discharge_instructions

Cross-packet mismatch: 'daughter name' has different values across documents in different QC packets

### 54. [HIGH] qc

**Files:** coding_worksheet, admission_hp

Cross-packet mismatch: 'ckd stage coding' has different values across documents in different QC packets

### 55. [HIGH] qc

**Files:** abi_tbi_report, abi_tbi_tracing, hd4_progress

Cross-packet mismatch: 'abi bilateral' has different values across documents in different QC packets

### 56. [HIGH] qc

**Files:** abi_tbi_report, abi_tbi_tracing, hd4_progress

Cross-packet mismatch: 'ankle waveforms' has different values across documents in different QC packets

### 57. [HIGH] qc

**Files:** podiatry_note, hd4_progress

Cross-packet mismatch: 'specimen collection time' has different values across documents in different QC packets

### 58. [HIGH] qc

**Files:** admission_hp, case_mgmt, ot_eval

Cross-packet mismatch: 'home address' has different values across documents in different QC packets

### 59. [HIGH] qc

**Files:** case_mgmt, hd4_progress

Cross-packet mismatch: 'primary insurance' has different values across documents in different QC packets

### 60. [HIGH] qc

**Files:** case_mgmt, hd4_progress

Cross-packet mismatch: 'secondary insurance' has different values across documents in different QC packets

### 61. [HIGH] qc

**Files:** home_med_list, admission_hp

Cross-packet mismatch: 'preferred pharmacy' has different values across documents in different QC packets

### 62. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

Coding worksheet proposes 'Pressure injury, left foot, stage 3 (L89.623)' as the PRINCIPAL diagnosis. The podiatry note and all clinical documentation consistently describe a neuropathic plantar diabetic foot ulcer, not a pressure injury. The podiatry op note states: 'PRE/POST-PROCEDURE DIAGNOSIS: Limb-threatening diabetic foot infection — left plantar forefoot diabetic foot ulcer over the 1st–2nd metatarsal head with deep soft tissue infection' and concludes 'Plantar neuropathic diabetic foot ulcer with deep soft tissue infection.'

_Suggested fix:_ Replace Row 1 principal diagnosis 'Pressure injury, left foot, stage 3 (L89.623), PRINCIPAL' with the appropriate diabetic foot ulcer with deep soft tissue infection code family (e.g., E11.628 Diabetes with other skin ulcer + appropriate L97.x non-pressure chronic ulcer code). Remove the pressure-injury DRG family framing (MS-DRG 592–594) from the PROPOSED MS-DRG FAMILY section and replace with the diabetic foot ulcer / soft tissue infection DRG family.

### 63. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

Coding worksheet proposes 'Acute osteomyelitis, left foot (M86.171), POA = Y, Secondary — MAJOR CC.' The entire clinical record contradicts this: the podiatry note states 'osteomyelitis not established'; the MRI report states 'early osteomyelitis CANNOT be excluded, findings equivocal and not diagnostic alone'; the pathology report states 'No bone present in the specimen; No definitive features of osteomyelitis'; and the ID consult explicitly does not sign osteomyelitis. No treating clinician established this diagnosis.

_Suggested fix:_ Remove Row 2 ('Acute osteomyelitis, left foot, M86.171, POA = Y, Secondary — MAJOR CC') from the proposed coding worksheet. In the SEVERITY-FORWARD JUSTIFICATIONS SUMMARY section, delete the paragraph beginning 'Osteomyelitis as POA = Y MCC.' Update the OPEN ITEMS attestation row for Row 2 to reflect that this line item is not supported and should be declined by the physician.

### 64. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

The preliminary discharge order set includes 'Ibuprofen 400 mg PO q6h PRN — knee osteoarthritis (added to PRN list for pain coverage)' in Section C item 18. The discharge instruction draft explicitly states 'Do NOT take ibuprofen, naproxen, or other anti-inflammatory pain pills — they are not safe for your kidneys.' The admission H&P also documents 'NSAIDs avoided in CKD.' Ibuprofen is contraindicated in this patient with CKD stage 3b.

_Suggested fix:_ Delete item 18 ('Ibuprofen 400 mg PO q6h PRN — knee osteoarthritis (added to PRN list for pain coverage)') from Section C of the preliminary discharge order set. In the FOR ATTENDING TO RECONCILE section, add a note flagging that NSAIDs are contraindicated (CKD 3b) and that acetaminophen 650 mg PO TID PRN (item 17) is the sole approved PRN analgesic for knee pain.

### 65. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

The denial letter states 'The presence of an identified adult caregiver in the household further supports a safe home-based plan of care.' This directly contradicts the admission H&P, which documents that the patient lives alone ('widowed, lives alone at 1418 Calle del Mar, Apt 2B'). The daughter Marisela Vasquell lives at a separate address (247 Egret Cove Lane) and works overnight night shifts; she is the emergency contact and partial caregiver but is not a resident of the patient's household.

_Suggested fix:_ In the denial letter rationale, replace 'The presence of an identified adult caregiver in the household further supports a safe home-based plan of care' with language that accurately reflects the documented situation: the daughter is a partial caregiver who lives at a separate address and works overnight night shifts, and is therefore not available for continuous household supervision. This correction is required to ensure the appeal rebuttal accurately characterizes the home caregiver situation as documented in the admission H&P and case management note.

### 66. [HIGH] certifier.cross_doc_evidence_bounded

**Files:** (unspecified)

The coding worksheet recommends non-capture of CKD stage 3b: 'CKD stage 3b (N18.32) — Drop — not clearly addressed inpatient.' The admission H&P and all subsequent progress notes document CKD stage 3b as a core active comorbidity governing antibiotic renal dosing, hold orders for metformin/empagliflozin/lisinopril, contrast caution for MRI, and gabapentin dose-checking. The renal trend flowsheet tracks AKI-on-CKD-3b throughout the stay.

_Suggested fix:_ Change the 'Chronic kidney disease, stage 3b (N18.32)' row from 'Drop — not clearly addressed inpatient' to a retained secondary diagnosis. Add N18.32 to the PROPOSED LINE-ITEM CODING table as a secondary diagnosis with POA = Y and a coder note referencing its active management throughout the admission (renal dosing of all antibiotics, hold orders for metformin/empagliflozin/lisinopril, AKI-on-CKD framing in progress notes).

### 67. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

Discharge order set Section C item 18 adds ibuprofen 400 mg PO q6h PRN for knee osteoarthritis. Ibuprofen is an NSAID explicitly contraindicated throughout this record due to CKD 3b and documented AKI. Live quote: '18. **Ibuprofen 400 mg PO q6h PRN** — knee osteoarthritis (added to PRN list for pain coverage).'

_Suggested fix:_ Replace item 18 with: '18. **Acetaminophen 650 mg PO q6h PRN** — knee osteoarthritis / pain; NSAIDs avoided given CKD.' Alternatively remove item 18 entirely since acetaminophen already appears at item 17. The order set heading note 'Review all PRN medications for continued appropriateness at discharge' can remain.

### 68. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

HIM coding worksheet proposes Pressure injury, left foot, stage 3 (L89.623) as the PRINCIPAL diagnosis. Every clinical document describes the wound as a neuropathic diabetic foot ulcer, not pressure etiology. Live quote: '| **1** | **Pressure injury, left foot, stage 3** | **L89.623** | Y | **PRINCIPAL** |' with coder note citing 'immobility' rather than neuropathy.

_Suggested fix:_ Change row 1 to a diabetic foot ulcer / deep soft-tissue infection principal (e.g., E11.621 — Type 2 diabetes mellitus with foot ulcer, supported by L97.512 for the ulcer site). Update the Severity-Forward Justifications section and proposed MS-DRG family (remove Skin Ulcer / Pressure Injury DRG 592–594 framing; substitute the diabetic foot DRG family).

### 69. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

HIM coding worksheet proposes acute osteomyelitis (M86.171) as a confirmed secondary MCC with POA=Y. Multiple clinical documents (ID consult, pathology, hospitalist notes) state osteomyelitis is equivocal, unconfirmed, and not signed. Live quote: '| **2** | **Acute osteomyelitis, left foot** | **M86.171** | Y | Secondary — MAJOR CC | MRI foot 05/18 describes bone marrow edema in 1st and 2nd metatarsal heads'

_Suggested fix:_ Remove row 2 from the confirmed-capture table. Add it to the Non-Capture / HOLD section with: 'Acute osteomyelitis (M86.171) — HOLD: MRI equivocal (marrow edema only, no cortical destruction), surgical pathology shows no bone in specimen, ID attending explicitly does not sign this diagnosis. Requires physician attestation before any capture.' Remove osteomyelitis as the qualifying MCC from the MS-DRG discussion.

### 70. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

HIM coding worksheet recommends dropping CKD stage 3b (N18.32) and anemia of CKD (D63.1) as 'not clearly addressed inpatient' despite both conditions being actively managed: renal dosing of all antibiotics, trending creatinine on every lab draw, ferrous sulfate continuation on MAR, and multiple notes referencing CKD and anemia. Live quotes: 'Chronic kidney disease, stage 3b (N18.32) | **Drop — not clearly addressed inpatient**' and 'Anemia in chronic kidney disease (D63.1) | **Drop — not clearly addressed inpatient**'

_Suggested fix:_ Change disposition for both items from 'Drop' to 'Recommend capture — addressed inpatient.' Update coder notes: for CKD, cite the renal lab trend flowsheet (Cr 2.1→1.6, eGFR 26→36) and antibiotic renal-dosing entries in MAR; for anemia, cite hemoglobin 9.8 g/dL on CBC trend and ferrous sulfate continuation in MAR/home med list.

### 71. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

PBM rejection notice recommends Trimethoprim-sulfamethoxazole DS (Bactrim DS) as the plan-preferred no-prior-auth substitute. The patient has a documented sulfa allergy flagged on every document in the record. Live quote: '| **Preferred Agent** | **TRIMETHOPRIM-SULFAMETHOXAZOLE DS** (Bactrim DS) |'

_Suggested fix:_ Replace the Preferred Agent with a non-sulfonamide alternative (e.g., a generic reference to an oral beta-lactam or another formulary Tier-1 antibiotic class) or add a contraindication note: 'Clinical note: prescriber must verify allergy compatibility before dispensing any substitute; documented sulfa allergy on file.' Do not name TMP-SMX or any sulfonamide-containing agent as the preferred substitute.

### 72. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

Medicare Advantage denial letter states the patient has 'an able-bodied adult daughter listed in the medical record as primary caregiver and emergency contact' as a basis for denying SNF. The family meeting note and case management screen document the daughter works overnight shifts as a CNA, lives separately, cannot be present daily, and cannot perform daytime dressing changes on workdays. Live denial quote: 'The member has an able-bodied adult daughter listed in the medical record as primary caregiver and emergency contact.'

_Suggested fix:_ Revise the caregiver bullet to: 'The medical record identifies an adult daughter as the member's emergency contact and primary caregiver; the clinical documentation notes that she works overnight shifts and has partial daytime availability on workdays.' This preserves the payer's adversarial denial position while reflecting the actual documented facts.

### 73. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

Vital signs flowsheet shows a perfectly smooth, monotonic decline in every parameter across all 6 hospital days with no realistic day-to-day variation. Live table: Temp 38.2→37.8→37.5→37.2→37.0→36.8; HR 104→96→92→88→84→80; BP 148/82→142/80→140/78→138/78→136/76→134/76; RR 18→18→18→17→16→16; Glucose 244→212→198→186→174→162. Every parameter decreases by a fixed or near-fixed increment each day.

_Suggested fix:_ Introduce small, realistic fluctuations while preserving the overall improving trend. For example: HR on HD3 stays at 92 (same as HD2) before dropping; glucose on HD3 increases slightly to 204 instead of 198; temperature on HD3 is 37.6 instead of 37.5 (minor uptick then resumes decline); RR holds at 18 through HD3 then drops. The nursing note text can remain unchanged. No parameter should decrease monotonically by uniform increments every single day.

### 74. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

Safety event intake document contains a 'REVIEWER DELIVERABLE' section specifying five numbered output sections the reviewer must produce, and a 'REQUEST FOR REVIEW' section with four explicit reviewer instructions — rendering the document more like task instructions than a real PSO intake report. Live quotes: 'The reviewer is asked to: 1. Determine whether the event reflects individual factors, system factors, or both' and 'REVIEWER DELIVERABLE: A structured root-cause review document is requested with the following sections: 1. Event summary (in reviewer's voice, drawing from the inputs above). 2. Contributor analysis...'

_Suggested fix:_ Remove the REVIEWER DELIVERABLE section entirely (delete the header and all five numbered deliverable sub-items). Shorten the REQUEST FOR REVIEW numbered list to a single sentence: 'Please complete a structured root-cause analysis and return findings to the Patient Safety Committee.' The DOCUMENTED INPUTS table listing source documents can remain as a clinical reference aid, but drop the deliverable-format specification.

### 75. [HIGH] certifier.advisory_bridge_red_team

**Files:** (unspecified)

Discharge instruction draft Section 2 explicitly names ibuprofen by brand and generic in a patient-facing warning, while the order set in the same task bundle lists ibuprofen as item 18. This cross-document contradiction makes the order-set NSAID error immediately obvious. Discharge draft live quote: 'Do NOT take ibuprofen, naproxen, or other anti-inflammatory pain pills — they are not safe for your kidneys.' Order set item 18: '**Ibuprofen 400 mg PO q6h PRN** — knee osteoarthritis (added to PRN list for pain coverage).'

_Suggested fix:_ This finding is secondary to the ibuprofen fix in the order set (#1 above). Once item 18 of the order set is corrected to acetaminophen (or removed), the explicit ibuprofen-by-name warning in the discharge draft is no longer a cross-document contradiction and can remain as appropriate renal-safety patient education. No change needed to the discharge draft if the order set is fixed first.
