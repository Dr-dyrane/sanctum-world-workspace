# Phase 3 File Manifest - Ondina Vasquell reference files

Every file is a Mode A clone of a clean KM Epic-note base, body rebuilt from the canonical clinical_data module, metadata scrubbed (core + app + custom), verified zero synthetic/tool tokens in any part, zero banned characters, styles.xml preserved. World files dated at or before the 05/21/2026 18:00 snapshot; task files carry their own post-snapshot anchor dates.

Counts: 29 world (EW1-EW29), 3 supplementary (WS1-WS3), 9 task (E1-T*) = 41 DOCX. Plus 2 Codex-generated images PENDING: EW30 wound_photo_05202026.jpg, EW31 abi_tbi_tracing_05192026.jpg (see codex-image-prompts.md). Total planned world set 31 + 3 supplementary + 9 task = 43.

## Mount placement (separation is load-bearing)

- world-files/ and supplementary-files/ -> shared world filesystem, visible to every task.
- task-files/ -> each E1-T file travels ONLY with its keyed task input set; never in the shared world mount, or it would pre-answer its task.
- EW30/EW31 images -> shared world filesystem with the EW set once generated.

## Files

| Category | Filename | SHA256 (first 16) |
|---|---|---|
| World | abi_tbi_study_report_05192026.docx | 64bccb1fae1d919e |
| World | admission_hp_05162026.docx | 44cd8c93acc0d462 |
| World | antibiotic_plan_note_05192026.docx | a32fb202ded82dfa |
| World | case_management_note_05202026.docx | cc08ca30937a261e |
| World | cbc_inflammatory_trend_05162026.docx | 50f1b7659cc77c8e |
| World | culture_report_deep_tissue_05172026.docx | 9bb0112a5e092198 |
| World | culture_report_superficial_swab_05162026.docx | dc99855e061379ff |
| World | diabetic_eye_exam_result_03152026.docx | d2a6c74f57a5beba |
| World | ed_physician_note_05162026.docx | 74ebb6a16fcfddba |
| World | endocrine_glycemic_note_05192026.docx | b39c7a9084705a0b |
| World | family_communication_note_05202026.docx | 3b9a337deb5aff9d |
| World | foot_pathology_report_05202026.docx | 511c9b7eab149f72 |
| World | home_med_list_05162026.docx | c80007587d6bcc10 |
| World | hospitalist_progress_hd2_05172026.docx | f74e07a933fafe12 |
| World | hospitalist_progress_hd4_05192026.docx | 2439715c2af44bc7 |
| World | hospitalist_progress_hd6_05212026.docx | 486aae4d1cc39384 |
| World | id_consult_note_05182026.docx | 60edf3d7d7356309 |
| World | mar_05162026_05212026.docx | bae45ee98c1f17e8 |
| World | medication_hold_orders_05162026.docx | 103a8db12ad031f1 |
| World | mri_foot_report_05182026.docx | 6b4b73159d91f06c |
| World | nursing_offloading_flowsheet_05202026.docx | f50141ad1b7f34b5 |
| World | ot_evaluation_05202026.docx | 0bb123dd5c3c56f1 |
| World | outpatient_primary_care_summary_04302026.docx | 605a7f30c09d8ff6 |
| World | podiatry_debridement_note_05172026.docx | 738461449542bc92 |
| World | pt_evaluation_05202026.docx | e8a2c4d8f391d2e4 |
| World | renal_lab_trend_05162026.docx | 9094a9f71599dcc6 |
| World | vascular_consult_note_05192026.docx | c53b1fdc5fa8aac1 |
| World | vital_signs_flowsheet_05162026.docx | 037e99157cb546ed |
| World | wound_care_consult_05202026.docx | 952aa9454318f29e |
| Supplementary | diabetes_foot_care_education_05212026.docx | 4e320caf8ea9d555 |
| Supplementary | general_discharge_rights_notice_05212026.docx | a79a7ca2bf47d669 |
| Supplementary | nursing_shift_narrative_05182026.docx | 22c48807b386a942 |
| Task | cdi_query_memo_05232026.docx | 38ea478f1eba1a09 |
| Task | him_preliminary_coding_worksheet_05212026.docx | d9ea6671ff7b7392 |
| Task | medicare_advantage_denial_letter_05232026.docx | 7defd1628c4191f7 |
| Task | payer_concurrent_review_request_05252026.docx | f6afda4d448e9a7f |
| Task | pharmacy_benefit_rejection_05242026.docx | 07fabc62dded7157 |
| Task | preliminary_discharge_order_set_05212026.docx | 4132326189904059 |
| Task | quality_abstraction_worksheet_06042026.docx | d768440846d7b016 |
| Task | safety_event_intake_summary_06112026.docx | b12aad4aec9e87b8 |
| Task | started_discharge_instruction_draft_05212026.docx | 9c69fb6833d974d8 |

## DERIVED clinical values - for Alexander one-pass ratification

Load-bearing anchors are already ratified (substrate pack). The texture values below were generated clinically-concordant per decision 12 to render full charts; they are NOT yet ratified. Strike or approve in one pass.

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
| toe pressure | TBI 0.5 affected side, absolute toe pressure 38 mmHg; ankle noncompressible ABI > 1.3 | ratified ABI/TBI; absolute toe pressure derived concordant with TBI 0.5 |
| eye exam | mild non-proliferative diabetic retinopathy, dilated exam 03/15/2026 | ratified milestone; finding concordant with A1c 8.6 |
| inpatient antibiotics | vancomycin (by level) + piperacillin-tazobactam 2.25 g q8h renally dosed from HD1; cefepime 1 g q12h renally dosed culture-directed | ratified empiric/step; doses renally adjusted for eGFR 38 |

## Synthetic external issuers (task files)

| Role | Name | Note |
|---|---|---|
| MA plan | Meridian Advantage Health Plan | synthetic Medicare Advantage payer |
| PBM | CoreScript Pharmacy Benefits | synthetic pharmacy benefit manager |
| HIM coder | Marisol Everet, MD | HIM lead Corwin Adeyle, RHIA, CCS (ratified roster) |
