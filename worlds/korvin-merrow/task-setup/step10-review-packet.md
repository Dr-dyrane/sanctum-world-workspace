# Step 10 Review Packet - Task Setup for Healthcare_247_Merrow

Date: 2026-06-05. Prepared off-clock for Alexander's on-clock review. Nothing below is applied yet; every edit and every prompt requires your ruling. Platform flow reference: docs/world-pipeline-playbook.md section A2.

## 0. Status of assets

- World live: Healthcare_247_Merrow (world_d50c832ac6474a68ba982a77e28a6bbe), 26 world files synced.
- 6 task packages locked: TP/EO/Golden/GG KM01-KM06 under task-prompts/, expected-outputs/, goldens/, grader-guidance/ (all locked/).
- 7 task-context DOCX in file-review/task-files-holdback/ (E1-T1..E1-T6 + E2-T1).
- GOOD NEWS: the holdback files came through the pipeline repair loop clean. Zero EW/FI ID references remain in any of the 7 (the EW16-to-EW12 fix is moot - already resolved). Remaining issues are hint-surface, listed in section 3.
- Goldens: zero FI references - platform-ready content-wise. GG and EO files still carry FI-* IDs and need the section 4 translation before paste.

## 1. Task-to-file map (RLS entry reference)

| RLS Task | TP | Task date | Attach (task-specific files) |
|---|---|---|---|
| Task 1 | KM01 med rec / safety review | 05/24/2026 | discharge_medication_reconciliation_request_05242026.docx + medication_safety_handoff_addendum_05242026.docx |
| Task 2 | KM02 discharge summary | 05/24/2026 | discharge_summary_request_05242026.docx |
| Task 3 | KM03 readiness / care coordination | 05/24/2026 | discharge_readiness_care_coordination_request_05242026.docx |
| Task 4 | KM04 consultant synthesis | 05/24/2026 | consultant_synthesis_care_plan_request_05242026.docx |
| Task 5 | KM05 +7 follow-up | 05/31/2026 | post_discharge_followup_request_05312026.docx |
| Task 6 | KM06 +30 readmission-risk | 06/23/2026 | readmission_risk_review_request_06232026.docx |

## 2. DRAFT de-hinted platform prompts [A: edit and approve each - these must ship as YOUR words]

Why redrafted: the locked TP-KM Request sections fail the Section 4 checklist as platform prompts - they carry FI- IDs in the body (4.20), enumerate document types (4.27), bullet out the analytical steps (4.12), and in several places name the traps outright ("prednisone exposure, taper history", "the discharge-facing snapshot could be over-trusted", "whether family concerns reflect baseline knowledge"). The detailed scoping correctly lives in the in-world request memos (the attached task files); the prompt field should be the short conversational ask. Drafts derived from your locked text:

**Task 1 (KM01):**
> Korvin Merrow in 5W-318 is planned for discharge tomorrow morning, 5/24. I need his discharge medication reconciliation and medication-safety review done today. The formal request from Dr. Vossmere and the pharmacy handoff addendum are attached; everything else is in his chart. Work through the record and bring back a reconciliation note, organized by disposition, that pharmacy and the covering hospitalist can co-sign.

**Task 2 (KM02):**
> Korvin Merrow is going home tomorrow, 5/24, and I need his discharge summary drafted today. The drafting request with our standard section format is attached. Pull the full inpatient course from his chart, admission 5/18 through now, and write the summary the way the course actually evolved. Route the draft back to me for attending review and signature.

**Task 3 (KM03):**
> Before we finalize Korvin Merrow's disposition tomorrow we need the discharge readiness and care coordination assessment. Case management's request with the required headings is attached. Use the whole chart and tell us where the transition plan holds together and what still has to be resolved. This is the readiness assessment, not the disposition order.

**Task 4 (KM04):**
> We have had three consult services in on Korvin Merrow this week and I want one plan, not three. My request memo is attached. Write the consultant synthesis and interdisciplinary care plan ahead of the planned 5/24 discharge, organized by problem with a clear owner for each item. 450 to 700 words, attending register.

**Task 5 (KM05):**
> Korvin Merrow was discharged from Mercy Vale on 5/24 and is due for his post-discharge check-in around 5/31. Our clinic request is attached, and we hold his inpatient chart through the 5/23 documentation endpoint. Complete the early post-discharge follow-up assessment from the available record and fax the note back to the clinic.

**Task 6 (KM06):**
> The Office of Quality and Transitions of Care is running its thirty-day look-back on the Korvin Merrow admission, 5/18 through the planned 5/24 discharge. The review request memo is attached. The source record is the inpatient chart through 5/23 at 18:00; no post-discharge documentation exists. Complete the retrospective readmission-risk review per the memo.

Flagged judgment calls for you: (a) Task 4 "I want one plan, not three" implies disagreement exists - I think an attending would say exactly this and the memo says it anyway, but it brushes the friction; (b) Task 6 stating "no post-discharge documentation exists" repeats the memo's constraint - keep or cut.

## 3. Holdback DOCX candidate edits [A: rule per item; I apply after rulings, integrity-gated]

**E1-T1 discharge_medication_reconciliation_request (3 edits):**
1. P31 output format lists disposition categories including "unresolved provenance" - hands the agent the conclusion that something belongs there. Replace category list with: "continued / held with restart parameters / dose-modified / inpatient-specific". (The agent must DISCOVER that prednisone cannot be cleanly categorized.)
2. P20 "Perform source-hierarchy reconciliation for prednisone" names the method. Soften: "Reconcile prednisone across the available chart sources." (In-world plausible: the med rec note itself flags the dose as not verified.)
3. P24 teach-back enumeration includes "prednisone handling" - keep or drop "prednisone handling" from the list [A]. The rest of the enumeration (changed items, held items, warning signs) is standard teach-back language.

**E1-T4 consultant_synthesis_care_plan_request (4 edits - worst offender):**
1. "Frictions to preserve" heading uses design vocabulary and its bullet "Endocrinology and Primary Team have entered distinct positions on steroid interpretation" reveals the trap location. Replace heading with "Where services differ" and DELETE the bullet, keeping only the neutral instruction: "Note where consulting services have expressed differing clinical positions and explain the hospitalist's basis for any integrated plan."
2. P40 five-bucket action enumeration includes "(prednisone source reconstruction, rheumatology coordination, taper plan ownership; no numeric dose)" - this is most of the golden's structure plus trap coaching. Replace with: "The synthesis should explicitly name action items with an owner and a timeframe for each."
3. P22-26 "Required organization" per-problem descriptors carry coaching ("Hospital Medicine reconciling source hierarchy", "Mara Merrow's baseline collateral as documented stakeholder evidence"). Keep the five problem headings; strip the trailing descriptors to service names only.
4. Markdown residue: "---" rule paragraphs and the asterisk-wrapped signature line are template artifacts in a clinical memo. Remove the --- paragraphs; de-asterisk the signature.

**E1-T2 discharge_summary_request (1 edit):**
1. P10 Reason-for-Admission section embeds a full clinical recap (presentation details narrated in the request). Trim to match the register of the other section instructions: "1. Reason for Admission." plus one neutral sentence. The facts live in the chart; the memo should not pre-summarize them.

**E1-T3 discharge_readiness_request (2 edits):**
1. P13 "the 19-item home regimen" narrates the buried OT finding (regimen size is the discoverable evidence). Reword: "Patient's ability to manage the home medication regimen; teach-back status, as documented in the chart."
2. P14 "documented concerns" pointing at the family-concern evidence - soften to "family supervision capacity and availability, as documented" [A: borderline, a CM template might genuinely say this].

**E1-T5 post_discharge_followup_request (2 edits):**
1. P13 enumerates the six held cardiorenal agents by name and dose - hands over the held-med discovery. Reword: "Held versus restarted cardiorenal agents; identify tolerance signals that should be checked at this visit."
2. P15 "preserve documented uncertainty rather than asserting a dose or taper step not supported" - coaches the exact golden behavior on the prednisone trap. Reword: "Review steroid instructions for clarity using available outpatient specialist records and inpatient documentation."

**E1-T6 readmission_risk_review_request (1 edit):**
1. P8-P9 state the no-post-discharge-data constraint twice in a row (authoring artifact). Merge into one sentence. The eight risk domains stay - standard QI review structure, realistic register [A: confirm leave].

**E2-T1 medication_safety_handoff_addendum (0 edits proposed):**
This file is BY DESIGN the scoping instrument for Task 1 - it lists focus items without resolving them ("This addendum lists items; it does not resolve them"). Its enumeration is your intended task scaffold, and each item defers to the chart. P17-18 prednisone item is in-world plausible (med rec note flags it). Recommend ship as-is [A: confirm].

## 4. FI-to-filename translation (mechanical; I run after your sign-off on the map)

GG-KM01..06 and EO-KM01..06 carry FI-* IDs that mean nothing to the platform grader. Translation map (filenames as they exist in the live world):

FI-W01 ed_triage_initial_intake_05182026.docx | FI-W02 ed_provider_assessment_05182026.docx | FI-W03 admission_history_and_physical_05182026.docx | FI-W04 initial_medication_reconciliation_note_05182026.docx | FI-W05 pharmacy_refill_history_report_05182026.docx | FI-W06 outpatient_rheumatology_prednisone_provenance_05212026.docx | FI-W07 primary_care_outpatient_baseline_summary_05182026.docx | FI-W08 hospitalist_progress_hd1_hd2_05192026.docx | FI-W09 hospitalist_progress_hd3_05202026.docx | FI-W10 hospitalist_progress_hd4_05212026.docx | FI-W11 hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx | FI-W12 renal_infection_hemodynamic_trend_summary_05232026.docx | FI-W13 medication_administration_record_05232026.docx | FI-W14 nephrology_consultation_05212026.docx | FI-W15 cardiology_consultation_05212026.docx | FI-W16 endocrinology_consultation_05212026.docx | FI-W17 nursing_observation_flowsheet_summary_05232026.docx | FI-W18 physical_therapy_assessment_05202026.docx | FI-W19 occupational_therapy_assessment_05202026.docx | FI-W20 family_communication_care_conference_05222026.docx | FI-W21 case_management_social_work_discharge_note_05222026.docx | FI-W22 discharge_facing_plan_snapshot_05232026.docx | FI-S01 pci_stent_history_summary_05182026.docx | FI-S02 sleep_study_osa_history_summary_05182026.docx | FI-S03 home_support_equipment_reference_05222026.docx | FI-S04 problem_list_history_snapshot_05182026.docx | FI-T01..T06 = the six request files (section 1) | FI-T07 medication_safety_handoff_addendum_05242026.docx

[A: confirm map.] Output goes to task-setup/platform/taskN/ as grader_guidelines.txt and golden upload files - locked/ originals untouched.

## 5. Execution order (your clock, batched)

1. Review sections 2-4, rule on every [A]. (Est. 30-40 min)
2. I apply holdback edits + run translations + build golden DOCX uploads + run Section 4 writer self-QC on the final prompts; report back. (Off-clock)
3. RLS entry, one task at a time: Create Task -> problem statement = task name -> Add Files per section 1 map -> paste prompt -> paste grader guidelines -> UPLOAD golden as file -> SAVE AFTER EVERY STEP. (Est. 40-60 min for all 6, batched)
4. Run agent: correct version, latest model, Run (~1 hr platform time, clock OFF). Then Run All QA -> wait 10-20 min -> Fetch QC Report.
5. QC findings loop per playbook A2 discipline.

Calibration reminder: trajectory scores under 70 percent mean the tasks are stumping the model properly; over 70 means too easy. Your traps were built for exactly this.
