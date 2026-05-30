# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is in Phase 1 World Building, but only steps 1-6 are in scope.

The Brainstorm for James Carter World has been completed, passed AutoQC, uploaded to RL Studio, and submitted for Human Review.

RL Studio:

- Task ID: `cyau8803`
- Status: `Ready for Plan Review`
- Brainstorm AutoQC: `51/51 passed`
- Human Review: pending

Current state: preparation only. World Spec drafting is not authorized.

## Locked Decisions

Locked from approved Brainstorm:

- Acute hospital medicine world, ED to inpatient admission.
- Multi-day hospitalization ending at Hospital Day 6 at 18:00 during discharge planning.
- Patient seed: 62-year-old male with T2DM, HTN, CKD stage 3, HFrEF, CAD, polypharmacy, PMR with prior chronic prednisone and recent taper.
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

## Decisions Remaining

Do not answer these without Alexander.

Identity/compliance:

- Final synthetic World Spec patient name.
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

Use these as post-GO interview priorities:

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

Wait for Brainstorm Human Review.

If reviewer returns GO:

1. Record the GO in local status/reviewer feedback.
2. Start the post-GO physician interview using `worlds/james-carter/world-spec-prep/post-go-interview-plan.md`.
3. Resolve identity/compliance decisions first.
4. Resolve timeline and source hierarchy.
5. Resolve task architecture before any prompts or Expected Output.
6. Resolve traceability/file strategy before any Section 3 file rows.
7. Ask Alexander for explicit approval before drafting the World Spec in the official template.

If reviewer returns SEND BACK:

1. Save exact reviewer feedback.
2. Classify required vs optional changes.
3. Compare to physician intent and source-of-truth criteria.
4. Apply only required fixes to Brainstorm.
5. Regenerate/upload only as authorized.
6. Do not begin World Spec.

## Hard Boundaries

Do not:

- draft the World Spec;
- populate the World Spec template;
- create Section 3 file inventory;
- create synthetic chart files;
- invent labs, vitals, medications, doses, dates, provider names, MRN, or patient name;
- write final task prompts;
- write golden responses;
- write grader guidelines;
- do failure analysis;
- change submitted Brainstorm content while Human Review is pending.

## Current Best Claude Task

If asked to help now, Claude should only support preparation:

- summarize current state;
- audit against AutoQC v6.3;
- prepare interview questions;
- critique proposed physician decisions;
- help maintain consistency with the approved Brainstorm.
