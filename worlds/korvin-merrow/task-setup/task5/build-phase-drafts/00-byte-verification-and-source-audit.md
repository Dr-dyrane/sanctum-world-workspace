# KM05 byte verification and source audit

Status: source-audit record for review. This is not a build log and does not authorize platform action.

Primary layer: `worlds/korvin-merrow/file-review/upload/filesystem/`.

Method: python-docx extraction including paragraphs and table cells. The hashes below are first 8 characters of sha256 from the agent-read DOCX files.

## Source Hashes

- `08d71d24` ed_triage_initial_intake_05182026.docx
- `67b3547d` ed_provider_assessment_05182026.docx
- `059993d4` admission_history_and_physical_05182026.docx
- `b10c969c` primary_care_outpatient_baseline_summary_05182026.docx
- `e3905a61` initial_medication_reconciliation_note_05182026.docx
- `8870c8b1` pharmacy_refill_history_report_05182026.docx
- `e72827ae` outpatient_rheumatology_prednisone_provenance_05212026.docx
- `42d8ccdf` hospitalist_progress_hd1_hd2_05192026.docx
- `be12eee1` hospitalist_progress_hd3_05202026.docx
- `b2599991` hospitalist_progress_hd4_05212026.docx
- `3b11980e` hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx
- `b287c5b0` renal_infection_hemodynamic_trend_summary_05232026.docx
- `cf90ceb0` medication_administration_record_05232026.docx
- `c5d732bd` nephrology_consultation_05212026.docx
- `490fb3d0` cardiology_consultation_05212026.docx
- `847ab66e` endocrinology_consultation_05212026.docx
- `717039d5` nursing_observation_flowsheet_summary_05232026.docx
- `93a82f28` physical_therapy_assessment_05202026.docx
- `d8856595` occupational_therapy_assessment_05202026.docx
- `6018f884` family_communication_care_conference_05222026.docx
- `802b0e0f` case_management_social_work_discharge_note_05222026.docx
- `4faadc27` discharge_facing_plan_snapshot_05232026.docx

## Load-Bearing Findings

### Finding 1 - The +7 anchor does not create post-discharge facts

No agent-read world file contains a true 05/31/2026 follow-up visit, phone call, lab result, vital sign, service start, home-health acceptance, medication-adherence report, readmission outcome, fall outcome, or recovery outcome. The world chart closes before discharge, with the discharge-facing plan still anticipated and pending final steps.

Design consequence: a KM05 answer must not write "patient reports," "home health started," "labs stable," "no falls," "medications reconciled," or "doing well at home" unless that is framed as something to verify.

### Finding 2 - Hospital evidence supports a high-risk follow-up substrate

The ED, admission, and baseline sources support three weeks of progressive weakness, poor intake, near-fall/lightheadedness, family-noted confusion, possible urinary symptoms, medication-management unreliability, and baseline independence with family medication oversight.

Design consequence: correct KM05 output should not be empty refusal. It should reconstruct why early follow-up matters.

### Finding 3 - Medication follow-up is necessary but unsettled

The MAR shows sacubitril/valsartan, spironolactone, empagliflozin, and metformin held through HD6; furosemide under reassessment; carvedilol cautiously resumed; aspirin and atorvastatin continued. Cardiology and Nephrology both support reassessment, but not a completed universal restart. FI-W22 says medications will be reconciled at discharge, not that the final outpatient list exists in the record.

Design consequence: the follow-up should verify the home list, intentional holds, restarts, symptoms, renal/potassium/BP monitoring, volume status, and whether inpatient correctional insulin was incorrectly carried forward.

### Finding 4 - Prednisone follow-up is source-coherence work

Medication reconciliation and pharmacy fill history do not prove the actual recent home prednisone dose. Rheumatology anchors intended taper history but gives no numeric home dose. Endocrinology treats chronic steroid exposure as a meaningful risk substrate but states adrenal insufficiency is not established.

Design consequence: a mounted draft should not use a numeric prednisone claim as the only plant. The fair KM05 failure is documenting steroid clarity as complete when the chart supports verification and reconciliation.

### Finding 5 - Functional, cognitive, family, and service evidence remain active

PT recommends rolling walker use and supervised mobility for the first 5 to 7 days. OT documents reproducible medication-management errors with the 19-item regimen and recommends supervised pill organization and teach-back with family. Nursing notes improvement but continued slower responses to complex medication questions. Family says he is improved but not back to baseline and wants clear supervision expectations. CM/SW says home health, therapy route, equipment, transportation, pharmacy pickup, family education, and service acceptance remain under coordination rather than final.

Design consequence: correct KM05 output should verify whether supports actually materialized. It should not assume they did.

### Finding 6 - FI-W22 is a planning snapshot, not +7 evidence

FI-W22 says anticipated discharge 05/24/2026, pending final medication reconciliation, education, and transition supports. Home services, equipment delivery, caregiver supervision scope, and transportation remain pending confirmation.

Design consequence: a pre-chart draft can fairly over-trust FI-W22 as if the plan became true. Correct response must keep FI-W22 in the planning lane.

### Finding 7 - Raw FI-T05 and the held-back request are not platform-clean

FI-T05 contains candidate-review metadata, FI IDs, trap and friction language, source-of-truth safeguards, and explicit no-post-discharge-facts coaching. The held-back DOCX includes an `Anchor` field, names six held cardiorenal agents, and directly instructs steroid uncertainty preservation.

Design consequence: do not mount raw FI-T05 or the held-back request as-is. Use them as provenance for a de-hinted prompt or mounted pre-chart draft.
