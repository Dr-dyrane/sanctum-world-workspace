# World 3 (Marva Lydell) brainstorm reconciliation - Larry E review, 2026-06-20

Applies Larry's 06/20 brainstorm review to the canonical brainstorm (submission/Marva_Lydell_Brainstorm.md) for the World Spec phase. Spec-to-task divergence is legitimate (AGENTS.md guardrail 13), so these corrections land in the SPEC; the submitted brainstorm record is preserved. Do not re-upload the brainstorm for these.

## 1. Workflow remaps (Larry's three) - LOCKED to Larry 2026-06-20

Authority, corrected. Larry holds the latest workflow cut, and the 06/19 Combined doc in `reference/source/task-selection-categories/Sanctum_Task_Selection_Categories_Combined_06_19.docx` is canonical. The Sanctum Coach's live endpoint is BEHIND: the EPMs have not pushed the current cut to it, so its lane set, tiers, and delivered counts lag and are NOT our source of truth. An earlier pass this session treated that stale endpoint as authoritative and wrongly recommended holding the brainstorm originals; that is reversed here. Lock to Larry, corroborated by the canonical 06/19 doc where the lane already appears.

| Task | Brainstorm had | LOCK (Larry, latest) | Canonical 06/19 doc corroboration |
|---|---|---|---|
| 2 Discharge med rec | Medication Reconciliation (P0) | Discharge Medication Reconciliation (P0) | Lane present as "Medication Reconcilliation Documentation/Discharge Medication Reconcilliation" at P1 (doc line 341, misspelled). Larry's current cut is the clean name at P0. The deliverable is a discharge med rec, so the discharge-specific lane is right. |
| 6 Cardiorenal follow-up handoff | Specialty Consultation Note (P1) | Specialist Referral Letter and Documentation Preparation (P0) | Not yet in the 06/19 doc (nearest are Specialty Consultation Note P1 at line 453 and Care Coordination Referral Tracking and Closure). Larry's latest adds the referral-letter authoring lane at P0. The deliverable routes diuretic, renal, potassium, and anticoagulation decisions to owners, a handoff letter, not the consultant's own consult note. Same consult-vs-referral lesson as OV12. |
| 10 CDI query response | CDI Query Response Review (P1) | Clinical Documentation Improvement (CDI) Query Response Review (P0) | Lane present verbatim at P1 (doc line 181). Larry's latest bumps the tier to P0; string unchanged. |

The other W3 lanes are unchanged and corroborated in the 06/19 doc: Claims Denial Analysis and Appeal Preparation (P0, Tasks 1 and 7), Utilization Review Concurrent Stay Documentation (P1, Task 3), Medical Transcription and Clinical Documentation Completion (P0, Task 4), Post-Acute Care Coordination Documentation (P0, Task 5), Corrective Action Plan (CAP) Development and Tracking (P1, Task 8), HEDIS Medical Record Chart Abstraction and Review (P0, Task 9). With Larry's tiers the spread is eight P0 and two P1 (Tasks 3 and 8).

Why the endpoint disagreed (recorded so we do not repeat the error): the endpoint is the stale Coach cut. It lacks the Specialist Referral lane entirely, still shows Tasks 2 and 10 at the old P1, and carries a saturated "Medication Reconciliation at Care Transitions" that is not even the canonical lane. Saturation and tier are read off the canonical/Larry cut, never the endpoint.

## 2. Fairness pass on the traps (Larry's other point)

Larry's line: a fair trap is true missed/buried information the model must sort out, or a wrong element in a document the requester's job is to review and rebut. An unfair trap plants a false statement in the patient's own authoritative record and dings the model for trusting it, because the model presumes the record is accurate, like a real clinician. Verdict: the W3 traps are predominantly on the fair side, with two to build carefully.

Fair as designed:
- Synthesis traps (resting vs exertional oxygen, improving kidney vs medication readiness, volume vs transition readiness, home support overestimated, respiratory control over-closed): the findings are TRUE and buried; the model fails by not synthesizing, not by trusting a falsehood.
- Reviewable-external / subordinate wrongs (payer denials in Tasks 1 and 7; the continued-stay worksheet in Task 3; the abstractor worksheet in Task 9; the CDI query in Task 10; case-management vs vendor in Task 5; the initial event note in Task 8; the outside medication list in Task 2): these live in documents the requester is meant to review and rebut, not in the patient's authoritative chart. The model rebuts or reconciles, the fair pattern (OV06/08/09/10, KM CDI).

The two to build as TRUE PLACEHOLDERS, not planted-false closures (this is exactly Larry's "fix this incomplete note that has wrong information" line):
- Task 4 (transition note completion): the started note must leave oxygen, volume, and follow-up ownership genuinely OPEN (true placeholders) under an optimistic but not-false tone. Do NOT plant a false closure ("cleared for discharge", "oxygen delivered and teach-backed") that the model is dinged for not correcting. The model completes the open sections correctly; it is never asked to distrust a false statement.
- Task 6 (cardiorenal follow-up letter): the started letter must be a true placeholder/handoff the model completes by routing the open decisions, not a draft that falsely states the plan is settled and dings the model for accepting it.

Architecture rule (carry into the spec): the world chart, the authoritative inpatient record, stays accurate. Every wrong, conflict, or over-closure lives in a TASK-LEVEL input the requester reviews (a denial, a worksheet, an outside list, a started-draft placeholder), never planted-false in the world chart. The brainstorm already states this (the shared chart stays raw); the spec must hold it.

## 3. Process: Sanctum Coach for the spec

Larry: author the World Spec through Sanctum Coach (the new instructions require it). It is not in the repo; it is the Drive package Sanctum_Coach_2026-06-15.zip (drive.google.com/file/d/1YyEsN6MQIyrGYMImwiOWUQsvxnosPhCq/view; setup video drive.google.com/file/d/1otkSfdBTRtSQ-TeSa5sWYcJM_brVPer5/view). Set it up as a Claude Project on Opus 4.8 High, paste the INSTRUCTIONS file as the project prompt, add the zip contents plus the World Spec, and add the DataBank at template curation. Division of labor: this workspace prepares the inputs (this reconciliation, the fairness-vetted traps, the confirmed workflow strings); Sanctum Coach authors the spec and templates; the OV factory (bootstrap_world_factory, build_one, the gates) does the deterministic build and verification after.

## 4. To lock before the spec
- Workflow strings: LOCKED to Larry (section 1). Task 2 Discharge Medication Reconciliation P0; Task 6 Specialist Referral Letter and Documentation Preparation P0; Task 10 CDI Query Response Review P0. The 06/19 canonical doc corroborates Tasks 2 and 10; Task 6 is Larry's latest addition. Confirm Task 6's exact spelling and tier with Larry or the next doc cut.
- Temporal rule: the Coach curriculum's whole-timeline-before-July-2025 rule is Coach-stale (the Coach is behind, and OV shipped on 2026 dates). Treat as not binding; confirm the date policy against the canonical doc or Larry before changing Marva's July 2025 timeline.
- Build Tasks 4 and 6 as true placeholders (section 2), never planted-false closures.
- Keep every trap in a task-level input; the world chart stays accurate.
- Saturation: judge against the canonical or Larry cut, not the stale Coach endpoint (its counts lag).
