# Spec AutoQC Remediation Package v1 (qcaud_85: 26 fails)

Date: 2026-06-04. Authorizes the exact content for every spec fix. Canon-preserving: no new clinical facts; dates assigned below are chart-entry dates inside locked milestone windows. Items marked [A] need Alexander's one-word sign-off.

## 1. ID + filename scheme (convention b) - THE CASCADE

World-essential `EW#`, task-level `E#-T#` (file # of Task #), world-supplementary `WS#`. Spec filename: **`Alexander_World_Merrow_latest_6_4.docx`** [A: confirm writer first name for Writer_World_Patient pattern].

| Old | New ID | New filename (MMDDYYYY = chart-entry date within locked window) |
|---|---|---|
| FI-W01 | EW1 | ed_triage_initial_intake_05182026.docx |
| FI-W02 | EW2 | ed_provider_assessment_05182026.docx |
| FI-W03 | EW3 | admission_history_and_physical_05182026.docx |
| FI-W04 | EW4 | initial_medication_reconciliation_note_05182026.docx |
| FI-W05 | EW5 | pharmacy_refill_history_report_05182026.docx |
| FI-W06 | EW6 | outpatient_rheumatology_prednisone_provenance_05212026.docx (available HD4) |
| FI-W07 | EW7 | primary_care_outpatient_baseline_summary_05182026.docx |
| FI-W08 | EW8 | hospitalist_progress_hd1_hd2_05192026.docx |
| FI-W09 | EW9 | hospitalist_progress_hd3_05202026.docx |
| FI-W10 | EW10 | hospitalist_progress_hd4_05212026.docx |
| FI-W11 | EW11 | hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx |
| FI-W12 | EW12 | renal_infection_hemodynamic_trend_summary_05232026.docx |
| FI-W13 | EW13 | medication_administration_record_05232026.docx |
| FI-W14 | EW14 | nephrology_consultation_05212026.docx |
| FI-W15 | EW15 | cardiology_consultation_05212026.docx |
| FI-W16 | EW16 | endocrinology_consultation_05212026.docx |
| FI-W17 | EW17 | nursing_observation_flowsheet_summary_05232026.docx |
| FI-W18 | EW18 | physical_therapy_assessment_05202026.docx |
| FI-W19 | EW19 | occupational_therapy_assessment_05202026.docx |
| FI-W20 | EW20 | family_communication_care_conference_05222026.docx |
| FI-W21 | EW21 | case_management_social_work_discharge_note_05222026.docx |
| FI-W22 | EW22 | discharge_facing_plan_snapshot_05232026.docx |
| FI-T01 | E1-T1 | discharge_medication_reconciliation_request_05242026.docx |
| FI-T07 | E2-T1 | medication_safety_handoff_addendum_05242026.docx (kills the "Task 7" flag) |
| FI-T02 | E1-T2 | discharge_summary_request_05242026.docx |
| FI-T03 | E1-T3 | discharge_readiness_care_coordination_request_05242026.docx |
| FI-T04 | E1-T4 | consultant_synthesis_care_plan_request_05242026.docx |
| FI-T05 | E1-T5 | post_discharge_followup_request_05312026.docx |
| FI-T06 | E1-T6 | readmission_risk_review_request_06232026.docx |
| FI-S01 | WS1 | pci_stent_history_summary_05182026.docx |
| FI-S02 | WS2 | sleep_study_osa_history_summary_05182026.docx |
| FI-S03 | WS3 | home_support_equipment_reference_05222026.docx |
| FI-S04 | WS4 | problem_list_history_snapshot_05182026.docx |

## 2. Header table (new, top of spec)

| Field | Value |
|---|---|
| World Title / Number | Korvin Merrow World (RL Studio cyau8803) |
| Patient Name | Korvin Merrow (fictional) |
| World Type | Typical Clinical World |
| Setting | ED presentation -> acute inpatient hospitalization -> discharge / transition of care |
| Specialty / Workflow | Hospital Medicine (EM/IM); discharge, medication reconciliation, consultant synthesis, transition of care |
| Total Tasks | 6 |
| Project | Project Sanctum |
| Version | latest 6/4 |

## 3. Section 1.1 - merge to 2 paragraphs + composition sentence
Keep paragraphs 1-2; fold the world-close sentence into paragraph 2 and append: "The world comprises 22 essential world-level files, 7 essential task-level files, and 4 supplementary files: 33 unique files supporting 6 tasks." Delete paragraph 3 (downstream task list already lives in Section 2).

## 4. Section 1.2 additions
**Decision Friction Table** (move/copy from 1.5; 1.5 keeps prose only):

| Friction | Party A position (defensible) | Party B position (defensible) | Surfaces in |
|---|---|---|---|
| Cardiology vs Nephrology: restart timing | Preserve/restart HFrEF-CAD protective therapy when safe (EW15) | Protect renal recovery; avoid hypotension and premature restart (EW14) | EW10, EW13-EW15, 05/21-05/23 |
| Family vs Primary Team: discharge readiness | Patient not back to baseline; home-safety concern (EW20) | Medically improved; discharge planning defensible (EW11, EW22) | EW17-EW22, 05/20-05/23 |
| Endocrinology vs Primary Team: steroid risk | Steroid exposure/taper uncertainty clinically relevant (EW16) | Avoid over-attributing improvement-phase symptoms to adrenal risk (EW10-EW11) | EW6, EW10, EW16, 05/21-05/23 |

**Care Team Roster** [A: confirm "MD" credential for all six physicians]:

| Name | Credentials | Role | Service |
|---|---|---|---|
| Elian Vossmere | MD | Attending hospitalist | Hospital Medicine |
| Maris Caldrane | MD | Consulting attending | Cardiology |
| Iven Solthar | MD | Consulting attending | Nephrology |
| Nerea Veylorn | MD | Consulting attending | Endocrinology |
| Talia Quenor | MD | Primary care physician | Outpatient Primary Care |
| Soren Halvek | MD | Outpatient rheumatologist | Rheumatology |
| Mara Merrow | (family) | Caregiver / historian | Family |
Plus service roles: hospitalist resident, bedside nursing, PT, OT, case management, social work, pharmacy.

## 5. Section 2 - per-task additions (all six tasks)
Add four labeled lines to every task block:
- **Anchor:** T1/T2/T3/T4 = 05/24/2026; T5 = 05/31/2026; T6 = 06/23/2026
- **Workflow (exact tracker names):** T1 Discharge Medication Reconciliation; T2 Hospital Discharge Summary Generation; T3 Discharge Planning Documentation; T4 Interdisciplinary Care Plan Development and Documentation; T5 Transitional Care Management Documentation (TCM); T6 Patient Risk Stratification Assessment [A: tracker-name relabel for T5/T6 - labeling only, task logic unchanged]
- **Priority:** T1 P0, T2 P0, T3 P0, T4 P1, T5 P1, T6 P1 [A: confirm against tracker sheet]
- **Capability:** T1 medication-safety synthesis, source hierarchy, cardiorenal sequencing; T2 narrative fidelity and temporal synthesis without copy-forward; T3 disposition-safety judgment and functional-evidence integration; T4 consultant-conflict synthesis and priority arbitration; T5 post-transition reassessment under uncertainty; T6 retrospective risk stratification with outcome discipline
- **Time estimate:** T1 30-45 min (reconciles 10+ files incl. EW4-EW6, EW13-EW16); T2 30-45 min (full-course synthesis EW1-EW22); T3 25-40 min; T4 30-45 min; T5 25-35 min; T6 25-40 min [A: confirm]
- **Difficulty:** T1 Hard, T2 Medium-Hard, T3 Medium, T4 Hard, T5 Medium, T6 Medium-Hard. Add to 1.5: "Difficulty distribution: 2 Hard, 2 Medium-Hard, 2 Medium." [A: confirm]

**Expected Output spec line (append to each):** format + register + length:
- T1: headed reconciliation note, disposition-by-medication; pharmacist/hospitalist register; 450-700 words.
- T2: standard discharge summary sections (reason, course, consultants, meds, follow-up); attending register; 500-800 words.
- T3: discharge-readiness/care-coordination assessment with headed sections; interdisciplinary register; 400-650 words.
- T4: interdisciplinary care plan, problem/owner structure; attending synthesis register; 450-700 words.
- T5: outpatient follow-up assessment note (interval status, meds, plan); PCP register; 350-600 words.
- T6: quality/safety review memo with risk domains and mitigations; physician-reviewer register; 400-650 words.

**Draft Prompt voice fixes:**
- T5: replace anchor/rubric phrasing with: "Mr. Merrow is one week out from his discharge and is in clinic for post-hospital follow-up. Please review the hospitalization and discharge plan and give me your assessment of how his recovery is tracking, what needs monitoring or clarification, and what should change, based on his records."
- T6: end with: "...please review his hospitalization and transition plan and assess his readmission and safety risk based on what his record supports."

**Failure Design: add a 5th trap row per task (from locked secondary coverage), anchor every row to doc+date, and mark reuse.** Row format: Trap | anchored remediation citing EW/E#-T#/WS IDs + MM/DD/YYYY | "(shared world trap; primary in Task N)" where reused. Fifth rows:
- T1 + "Buried medication-management capacity evidence" - OT/nursing home-management findings (EW19 05/20, EW17 05/23) must inform teach-back/supervision; shared trap, also in T3.
- T2 + "Sepsis-anchor carry-forward" - early frame (EW2-EW3 05/18) must not narrate the whole course; reconcile against EW12 trends through 05/23; shared, primary here.
- T3 + "Family-concern minimization" - EW20 (05/22) longitudinal baseline observations are evidence, not anxiety; weigh vs EW11/EW22 (05/23); shared with T6.
- T4 + "Latest-note authority bias" - most recent consult note (EW14-EW16, 05/21-05/23 updates) is not automatically correct; synthesize trends EW12/EW13; shared mechanism with T1.
- T5 + "Premature closure on 'sepsis resolved'" - residual symptoms at +7 are not automatically benign; reassess against EW12 (05/23) baseline-anchored trends; shared with T2.
- T6 + "Medication-restart risk omission" - restart/hold decisions (EW13-EW15, 05/21-05/23) are core readmission-risk substrate; shared with T1/T4.

## 6. Section 3 - file plan rewrite
Apply section 1 IDs/filenames to all 33 rows. **Enrich Description column (builder-ready)** - every row gets: required content + structure + key facts carried + exclusions. Write from locked FI files (they exist; no invention). Pattern example, EW22: "One-page discharge-facing plan snapshot dated 05/23/2026 before 18:00: improvement summary, anticipated discharge 05/24, follow-up list, simplified medication framing. Must read reassuring and coherent while omitting unresolved functional/cognitive concerns (EW17-EW19), final restart decisions (EW13-EW15), and prednisone reconciliation (EW6). Exclude any post-world outcome." Apply the same depth to all rows. [Full 33-row text to be generated at patch time from each locked file's sections - mechanical, source-bound.]
**Pearls/Traps enrichment (3 flagged rows):** EW14/EW15/EW16 add "consultant chronology: recommendations evolve 05/19-05/23; date-of-note governs applicability (Task 2/4 chronology trap)"; EW21 add "cross-role disposition integration substrate (Task 4 disposition-siloing trap)"; EW12 add "monitoring-gap substrate: trends support reassessment; absence of scheduled post-discharge checks is the Task 5 monitoring-gap trap."

## 7. Formatting fixes
DOB display -> 02/18/1964. All display dates MM/DD/YYYY in spec. American English already. Spec filename per section 1.

## 8. Out of scope for spec edit (notes instead)
Prednisone dose/frequency (Trap #1 canon); Per-Task Reference Answer (platform-stage mismatch); transcript date formats (historical record). See autoqc-notes-draft.md.
