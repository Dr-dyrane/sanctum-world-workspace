# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is in Phase 1 World Building, but only steps 1-6 are in scope.

The Brainstorm for Korvin Merrow World has been completed, passed AutoQC, uploaded to RL Studio, and returned SEND BACK from Human Review.

RL Studio:

- Task ID: `cyau8803`
- Status: `Writer Actions / Start Plan Fixes`
- Brainstorm AutoQC: `51/51 passed`
- Human Review: SEND BACK from Stacey S

Current state: Brainstorm reviewer remediation only. World Spec drafting is not authorized.

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

- Confirm comorbidity additions for Brainstorm remediation.
- Confirm medication names/doses for Brainstorm remediation.
- Confirm when to regenerate the final Brainstorm submission DOCX and reupload.
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

Wait for Alexander approval of comorbidity and medication decisions.

If Alexander approves the reviewer-remediation decisions:

1. Incorporate only approved comorbidity and medication specificity changes into Brainstorm.
2. Regenerate final Brainstorm submission DOCX.
3. Run final local QC.
4. Ask Alexander before RL Studio reupload.

If Alexander rejects or modifies any proposed decision:

1. Revise the decision brief or Brainstorm plan accordingly.
2. Do not reupload until approved.
3. Do not begin World Spec.

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
- change Brainstorm clinical content beyond reviewer-required remediation without Alexander approval.

## Current Best Claude Task

If asked to help now, Claude should only support preparation:

- summarize current state;
- audit against AutoQC v6.3;
- prepare interview questions;
- critique proposed physician decisions;
- help maintain consistency with the approved Brainstorm.
