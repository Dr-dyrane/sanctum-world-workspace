# Phase 3 File Manifest - Ondina Vasquell reference files

SECOND PASS (style-matched to KM + header/footer leak fixed). Every file is a Mode A clone of a clean KM Epic-note base, body + chrome + header/footer rebuilt from the canonical clinical_data module to the KM design system (navy/blue/light-blue, masthead, blue bar, patient storyboard, PATIENT/ENCOUNTER block, blue table headers). Gates per file: scrub_all_metadata; verify_no_synthetic; verify_no_km_identifiers (NEW - catches Korvin/Merrow/KM-MRN/Mercy Vale in any part incl. headers/footers); zero banned characters; styles.xml preserved; world dates <= 05/21/2026 18:00.

Counts: 29 world (EW1-EW29), 3 supplementary (WS1-WS3), 9 task (E1-T*) = 41 DOCX. Plus EW30/EW31 images PENDING (Codex). Planned total 43 + 2 images.

## Mount placement (separation is load-bearing)

- world-files/ + supplementary-files/ -> shared world filesystem.
- task-files/ -> each E1-T travels ONLY with its keyed task; never in the shared world mount.

## Files

| Category | Filename | SHA256 (first 16) |
|---|---|---|
| World | abi_tbi_study_report_05192026.docx | 6c716dbab426f45a |
| World | admission_hp_05162026.docx | 039f88eace0a409d |
| World | antibiotic_plan_note_05192026.docx | 8f48dfed119eb4e0 |
| World | case_management_note_05202026.docx | 71a9d3bcb8ee2f29 |
| World | cbc_inflammatory_trend_05162026.docx | 11722d83b92859dc |
| World | culture_report_deep_tissue_05172026.docx | ef42935fc0c91903 |
| World | culture_report_superficial_swab_05162026.docx | 78a7026c0ff1669f |
| World | diabetic_eye_exam_result_03152026.docx | 8773ffc53021e228 |
| World | ed_physician_note_05162026.docx | 5e25a2bf1d8acb2a |
| World | endocrine_glycemic_note_05192026.docx | a0584e89c2550b28 |
| World | family_communication_note_05202026.docx | 1babe3cdbf71de45 |
| World | foot_pathology_report_05202026.docx | 83c4cba1f7416b96 |
| World | home_med_list_05162026.docx | 2fe0369551ce3ff3 |
| World | hospitalist_progress_hd2_05172026.docx | d2426ee1c4d34a9f |
| World | hospitalist_progress_hd4_05192026.docx | 9cb0f6b551262e86 |
| World | hospitalist_progress_hd6_05212026.docx | 0fdc78111e84ce0a |
| World | id_consult_note_05182026.docx | 3ef1ec46b625178e |
| World | mar_05162026_05212026.docx | caadd196a6c69061 |
| World | medication_hold_orders_05162026.docx | 4db04605a91788e1 |
| World | mri_foot_report_05182026.docx | fce08c411b0f0cce |
| World | nursing_offloading_flowsheet_05202026.docx | f3116cdeab3244b5 |
| World | ot_evaluation_05202026.docx | c8473714f4b91e8f |
| World | outpatient_primary_care_summary_04302026.docx | 1b0779a2432a8ffe |
| World | podiatry_debridement_note_05172026.docx | bc57070f74746bf3 |
| World | pt_evaluation_05202026.docx | 70e8e17a72ee6e01 |
| World | renal_lab_trend_05162026.docx | 83fb2ba59aa998a9 |
| World | vascular_consult_note_05192026.docx | c91df252faa8111f |
| World | vital_signs_flowsheet_05162026.docx | c60ba28bdb0c565c |
| World | wound_care_consult_05202026.docx | c179934cfe0748fb |
| Supplementary | diabetes_foot_care_education_05212026.docx | 93f4a0cef555dc2f |
| Supplementary | general_discharge_rights_notice_05212026.docx | e15facc07c8b3407 |
| Supplementary | nursing_shift_narrative_05182026.docx | 24a6885644d42f46 |
| Task | cdi_query_memo_05232026.docx | 2a16baf67a49f96f |
| Task | him_preliminary_coding_worksheet_05212026.docx | b9ec07989e94aade |
| Task | medicare_advantage_denial_letter_05232026.docx | 67fdfbb7ce63795d |
| Task | payer_concurrent_review_request_05252026.docx | ea3a9d4d4e7cdb5b |
| Task | pharmacy_benefit_rejection_05242026.docx | c8204628babff5cc |
| Task | preliminary_discharge_order_set_05212026.docx | 569275a8f55d516b |
| Task | quality_abstraction_worksheet_06042026.docx | f1c09728ac759f81 |
| Task | safety_event_intake_summary_06112026.docx | 87b8afbb33d61fc6 |
| Task | started_discharge_instruction_draft_05212026.docx | d482718dc893a2ea |

## DERIVED clinical values (physician-ratified 2026-06-13)

| Item | Value | Rationale |
|---|---|---|
| facility | Harbor Crest Regional Medical Center | synthetic facility, distinct from KM Mercy Vale |
| encounter ids | CSN-308852140, FIN-2207733, unit 6 South Medicine, room 6S-214 | synthetic plumbing |
| clinician NPIs | all 10-digit synthetic, non-registry | chart realism |
| HD1 vitals | T 38.2 C, HR 104, BP 148/82, RR 18, SpO2 96% RA, gluc 244 | febrile index event concordant with WBC 14.2 / temp 38.2 (substrate) |
| HD2 vitals | T 37.8 C, HR 96, BP 142/80, RR 18, SpO2 97% RA, gluc 212 | post-debridement, improving |
| HD4 vitals | T 37.2 C, HR 88, BP 138/78, RR 17, SpO2 97% RA, gluc 186 | narrowing trajectory |
| HD6 vitals | T 36.8 C, HR 80, BP 134/76, RR 16, SpO2 98% RA, gluc 162 | defervescence by snapshot (substrate) |
| creatinine intermediate | 1.5 base, 2.1 peak HD1, 1.9 HD2, 1.7 HD4, 1.6 HD6 | interpolated between ratified 1.5/2.1/1.6 |
| WBC intermediate | 14.2 HD1, 12.1 HD2, 10.4 HD4, 8.9 HD6 | interpolated between ratified 14.2/8.9 |
| CRP | 118 HD1, falling to 41 HD6 (mg/L) | inflammatory marker concordant with improving WBC |
| BUN / K | BUN 38 HD1 to 26 HD6; K 4.6 to 4.1 mEq/L | AKI-on-CKD concordant, no hyperkalemia gate |
| platelets / Hgb | platelets 318k; Hgb 9.8 stable (ratified) | anemia of CKD stays open |
| deep tissue culture | MSSA and Streptococcus agalactiae; MSSA oxacillin-S, clindamycin-S, TMP-SMX-S(not used, sulfa allergy) | typical limb-threat DFI deep culture; drives de-escalation and the sulfa-constrained PBM trap |
| superficial swab | mixed skin flora, no dominant pathogen - lower authority | culture-hierarchy trap substrate |
| wound dimensions | 3.0 x 2.2 x 0.8 cm plantar left forefoot, granulating base, scant serous drainage | post-debridement wound, no exposed bone (substrate) |
| toe pressure | TBI 0.50 affected side, absolute toe pressure 55 mmHg; ankle noncompressible ABI > 1.3 | ratified ABI/TBI; absolute toe pressure derived concordant with TBI 0.50 |
| eye exam | mild non-proliferative diabetic retinopathy, dilated exam 03/15/2026 | ratified milestone; finding concordant with A1c 8.6 |
| inpatient antibiotics | vancomycin (by level) + piperacillin-tazobactam 2.25 g q8h renally dosed from HD1; cefepime 1 g q12h renally dosed culture-directed | ratified empiric/step; doses renally adjusted for eGFR 38 |
