# World 3 (Marva Lydell) brainstorm reconciliation - Larry E review, 2026-06-20

Applies Larry's 06/20 brainstorm review to the canonical brainstorm (submission/Marva_Lydell_Brainstorm.md) for the World Spec phase. Spec-to-task divergence is legitimate (AGENTS.md guardrail 13), so these corrections land in the SPEC; the submitted brainstorm record is preserved. Do not re-upload the brainstorm for these.

## 1. Workflow remaps (Larry's three; verbatim discipline)

Name-check non-compliance is a recurring Major. The Step-10 string must be exact and the tier must match.

| Task | Was | Lock to | Why |
|---|---|---|---|
| 2 Discharge med rec | Medication Reconciliation (P0) | Discharge Medication Reconciliation (P0) | "Medication Reconciliation" is not the catalog string; the deliverable is a discharge med rec, so use the discharge-specific name verbatim. |
| 6 Cardiorenal follow-up letter | Specialty Consultation Note (P1) | Specialist Referral Letter and Documentation Preparation (P0) [or Specialist Referral Documentation (P0)] | The deliverable routes diuretic, renal, potassium, and anticoagulation decisions to owners, a referral/handoff letter, not the consultant's own consult note. Tier also moves P1 to P0. Same consult-vs-referral lesson as OV12. |
| 10 CDI query response | CDI Query Response Review (P1) | Clinical Documentation Improvement (CDI) Query Response Review (P0) | String is verbatim-correct; only the tier is wrong, P1 to P0. |

VERBATIM-CONFIRM (the one open input): Larry's exact strings for Tasks 2 and 6 ("Discharge Medication Reconciliation", "Specialist Referral Letter and Documentation Preparation") are NOT in our local 06/18 or 06/19 catalog copies (they carry "Medication Reconciliation at Care Transitions" P0, a misspelled "...Discharge Medication Reconcilliation" P1, and no "Specialist Referral" authoring workflow). Larry is reading a live/current Appendix A we do not hold locally. Confirm the exact string and tier on the live Step-10 sheet before locking. Task 10's tier also disagrees between our copies (Difficulty doc P0, Combined doc P1); Larry says P0, confirm at Step 10.

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
- Confirm the verbatim Step-10 strings and tiers for Tasks 2 and 6, and Task 10's P0, on the live sheet.
- Build Tasks 4 and 6 as true placeholders (section 2), never planted-false closures.
- Keep every trap in a task-level input; the world chart stays accurate.
