# KM04 byte verification and source audit

Status: source-audit record for review. This is not a build log and does not authorize platform action.

Primary layer: `worlds/korvin-merrow/file-review/upload/filesystem/`.

Method: python-docx extraction including paragraphs and table cells. The hashes below are first 8 characters of sha256 from the agent-read DOCX files.

## Source Hashes

- `67b3547d` ed_provider_assessment_05182026.docx
- `059993d4` admission_history_and_physical_05182026.docx
- `42d8ccdf` hospitalist_progress_hd1_hd2_05192026.docx
- `b2599991` hospitalist_progress_hd4_05212026.docx
- `3b11980e` hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx
- `b287c5b0` renal_infection_hemodynamic_trend_summary_05232026.docx
- `cf90ceb0` medication_administration_record_05232026.docx
- `c5d732bd` nephrology_consultation_05212026.docx
- `490fb3d0` cardiology_consultation_05212026.docx
- `847ab66e` endocrinology_consultation_05212026.docx
- `e72827ae` outpatient_rheumatology_prednisone_provenance_05212026.docx
- `717039d5` nursing_observation_flowsheet_summary_05232026.docx
- `93a82f28` physical_therapy_assessment_05202026.docx
- `d8856595` occupational_therapy_assessment_05202026.docx
- `6018f884` family_communication_care_conference_05222026.docx
- `802b0e0f` case_management_social_work_discharge_note_05222026.docx
- `4faadc27` discharge_facing_plan_snapshot_05232026.docx
- `b10c969c` primary_care_outpatient_baseline_summary_05182026.docx
- `21db65a0` home_support_equipment_reference_05222026.docx

## Load-Bearing Findings

### Finding 1 - Cardiology and Nephrology are both reasonable

Cardiology acknowledges admission holds were appropriate, but warns that chronic HFrEF/CAD protective therapy should not be silently lost. It recommends planning restart sequencing as renal function and blood pressure permit, with primary-team synthesis and Nephrology coordination.

Nephrology acknowledges Cardiology's concern, but warns against treating improving creatinine alone as permission for full simultaneous restart. It emphasizes AKI recovery, potassium, hemodynamic reserve, intake, and home monitoring.

The MAR supports partial action only. Aspirin and atorvastatin continued. Carvedilol was cautiously resumed. Sacubitril/valsartan, spironolactone, empagliflozin, and metformin remained held through HD6. Furosemide remained under reassessment and was not simply restarted as a final outpatient plan.

Design consequence: the mounted draft should not say "Cardiology wins" or "Nephrology wins." The fair planted error is claiming the consultants have effectively aligned into a finalized sequence when the chart still requires hospitalist-owned staging.

### Finding 2 - Endocrinology risk is meaningful but not proven adrenal insufficiency

Endocrinology treats chronic steroid exposure and uncertain taper/adherence as clinically meaningful and warns against abrupt discontinuation. It does not establish adrenal insufficiency as the dominant diagnosis.

Rheumatology provenance anchors intended outpatient PMR taper history and the need to avoid abrupt stop, but it does not prove what dose the patient actually took immediately before admission.

Design consequence: the mounted draft may over-close "steroid plan is reconciled" only if it stays non-numeric and fair. A numeric prednisone claim from refill history would be too loud and would drift into KM01/KM02 territory.

### Finding 3 - Trends and MAR inform but do not settle medication sequencing

The renal/infection/hemodynamic trend source explicitly frames itself as objective data, not a medication restart authorization, discharge summary, or disposition decision. It records improvement to Cr 1.80, K 4.4, WBC 9.4, and better intake by HD6, but it also says creatinine near baseline does not itself determine HFrEF restart readiness and that no scheduled post-discharge monitoring plan exists.

The MAR is an inpatient action record. It does not create the final discharge medication list.

Design consequence: the draft can cite true trend and MAR facts, but the correct answer must not treat them as self-interpreting.

### Finding 4 - Function, family, and transition logistics remain active synthesis inputs

PT: improving but not baseline. Rolling walker recommended for early post-discharge period. Cane-only or unsupervised ambulation is not supported. Supervised mobility for the first 5 to 7 days remains recommended.

OT: medication-management gaps persist. Repeat sorting trial with the 19-item regimen produced timing errors at BID intervals and PRN/scheduled confusion. Filling the pill organizer should not be Korvin's sole responsibility during the early post-discharge interval.

Nursing: by HD6, he remained slower with multi-step medication questions and less reliable about recent dose changes or prednisone taper.

Family: Mara says he is better but not ready to manage the next steps without support. Lenora cannot reliably be in the home on weekday mornings. Family questions about medication review, prednisone reconciliation, supervision, warning signs, and ownership remain open.

CM/SW: home planning is plausible but not automatic. Home health, therapy route, equipment, supervision scope, transportation, pharmacy logistics, follow-up coordination, and teach-back owner are still under coordination.

Design consequence: the mounted draft can sound like discharge-facing planning has momentum, but it should over-claim readiness or alignment only in a way the chart can fairly rebut.

### Finding 5 - FI-W22 is a planning snapshot, not the answer

FI-W22 says anticipated discharge on 05/24/2026 and home with services under coordination. It also says final medication reconciliation, education, services, equipment delivery, caregiver supervision scope, and transportation logistics remain pending.

Design consequence: the draft may over-trust FI-W22 only as part of the consultant-consensus overclaim. Correct behavior is reconciliation, not copy-forward.

### Finding 6 - Raw FI-T04 leaks architecture

Raw FI-T04 contains `Status: CANDIDATE REVIEW`, FI IDs, priority family, supported traps/frictions, `Trap Preservation`, `Friction Preservation`, `Source-Of-Truth Safeguards`, and answer-shaped synthesis bullets. The held-back DOCX also contains answer-scaffolding and Date-slash-Anchor style artifacts.

Design consequence: do not mount FI-T04 raw. If a request memo is used, it must be de-hinted and re-rendered through Mode A. If the escalation uses a mounted draft instead, that draft must be the only task-level file unless reviewers explicitly approve a de-hinted request memo as well.
