# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is in Phase 1 World Building, but only steps 1-6 are in scope.

The Brainstorm for Korvin Merrow World has been completed, passed AutoQC, uploaded to RL Studio, returned SEND BACK from Human Review, remediated, reuploaded, resubmitted, and approved by Stacey S.

RL Studio:

- Task ID: `cyau8803`
- Status: Brainstorm approved / ready for World Spec transition
- Brainstorm AutoQC: revised run `0 failed / 51 passed`
- Diagnostics reviewed: yes
- Human Review: GO from Stacey S
- Approval source: Slack / Stacey S
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current state: World Spec kickoff / ready for physician interview. World Spec drafting has not started and remains gated on physician interview decisions plus explicit Alexander authorization.

## Locked Decisions

Locked from approved Brainstorm:

- Acute hospital medicine world, ED to inpatient admission.
- Multi-day hospitalization ending at Hospital Day 6 at 18:00 during discharge planning.
- Patient seed: 62-year-old male with T2DM, HTN, CKD stage 3, HFrEF, CAD, hyperlipidemia, anemia of CKD, osteoporosis/osteopenia from chronic steroid exposure, obstructive sleep apnea, diabetic peripheral neuropathy, polypharmacy, PMR with prior chronic prednisone and recent taper.
- Presentation: AMS, progressive weakness, poor oral intake, reduced activity, borderline hypotension, AKI on CKD, possible urinary-source infection.
- Initial suspected sepsis treatment is appropriate.
- Complexity evolves from overlapping common hospital contributors, not from a single rare diagnosis.

Locked primary frictions:

1. Nephrology vs Cardiology.
2. Family vs Inpatient Medicine.
3. Emergency/Inpatient Medicine vs Endocrinology.

Locked world-level traps:

1. Steroid timeline/source-of-truth trap.
2. HF-AKI medication reconciliation and time-sensitive consultant trap.
3. Buried functional/cognitive status trap.
4. Sepsis anchoring after partial improvement trap.
5. Discharge plan source-hierarchy trap.

Approved rough task concepts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

Approved Brainstorm remediation additions:

- World Type: Typical Clinical World.
- Medication list: sacubitril/valsartan 24/26 mg BID; carvedilol 12.5 mg BID; furosemide 40 mg daily; spironolactone 25 mg daily; empagliflozin 10 mg daily; aspirin 81 mg daily; atorvastatin 40 mg nightly; metformin ER 500 mg BID; insulin glargine 18 units nightly; prednisone with inconsistent documented taper/dose; alendronate 70 mg weekly; calcium/vitamin D daily; ferrous sulfate 325 mg every other day; gabapentin 300 mg nightly.
- Active DOCX: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.

## Decisions Remaining

Do not answer these without Alexander.

Identity/compliance:

- Confirm when to reupload the revised Brainstorm and rerun AutoQC.
- Synthetic MRN format.
- DOB, age consistency, sex, allergies, code status, height, weight, BMI, and clinically relevant demographics.

Clinical scenario:

- Exact calendar dates for ED arrival, admission course, world snapshot, and task anchors.
- Key milestone list.
- Source-of-truth hierarchy for conflicting evidence.

Task architecture:

- Consolidation from current rough mappings to 3-5 distinct approved catalog workflows.
- Whether/how to include a healthcare administration deliverable.
- Final task independence, requester, anchor, and one-deliverable discipline.

Traceability/file strategy:

- Evidence provenance workflow.
- Later file modalities.
- Later trap substrate planning.
- No final file inventory yet.

## Verified World Spec Risks

Use these as future World Spec priorities only after Brainstorm GO:

- AutoQC 2.2: patient name must be unmistakably synthetic.
- AutoQC 2.3: MRN must be clearly synthetic.
- AutoQC 2.14: Decision Friction Table required when 2+ conflicts exist.
- AutoQC 2.18 and 2.48: clinical facts and Expected Output facts must trace to narrative or file rows.
- AutoQC 2.41: temporal architecture is a blocker gate.
- AutoQC 2.65: source-of-truth hierarchy required when authority traps are present.
- AutoQC 2.98: workflow names must match approved tracker exactly.
- AutoQC 2.107: final world must use 3-5 distinct catalog workflows.
- AutoQC 2.108: typical clinical/medical director worlds should include clinical and healthcare administration work products where appropriate.

## Next Legal Action

Use `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` for orientation.

Wait for Alexander to explicitly start the World Spec physician decision interview.

If Alexander starts the interview:

1. Read `project/STATUS.md`, `project/PASS_PLAN.md`, and `worlds/korvin-merrow/world-spec-prep/post-go-interview-plan.md`.
2. Run the World Spec physician interview sequence.
3. Do not populate the official World Spec template until Alexander authorizes drafting after the interview.

If Alexander has not started the interview:

1. Continue preparation-only activities.
2. Do not draft World Spec.
3. Do not create file inventory.

## Hard Boundaries

Do not:

- draft the World Spec before explicit Alexander authorization;
- populate the World Spec template before explicit Alexander authorization;
- create Section 3 file inventory before explicit authorization;
- create synthetic chart files;
- invent labs, vitals, medications, doses, dates, provider names, MRN, or patient name;
- write final task prompts;
- write golden responses;
- write grader guidelines;
- do failure analysis;
- change Brainstorm clinical content unless new reviewer feedback arrives and Alexander approves the response plan.

## Current Best Claude Task

If asked to help now, Claude should only support preparation:

- summarize current state;
- audit against AutoQC v6.3;
- prepare or refine post-GO interview questions;
- critique proposed physician decisions;
- help maintain consistency with the approved Brainstorm.

## Workspace Doctrine Note

The workspace contains overlapping prep and guideline docs. This is intentional but should now be treated as supporting reference material. The active cockpit for the World Spec transition is `WORLD_SPEC_KICKOFF.md`; the live state source is `project/STATUS.md`; exact AutoQC checks live in `reference/world-spec-guidelines/08_autoqc_master_index.md`; practical authoring flow lives in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
