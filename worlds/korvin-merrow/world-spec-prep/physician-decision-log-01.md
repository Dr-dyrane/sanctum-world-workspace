# Physician Decision Log 01

Date recorded: 2026-05-31

Status: locked physician decisions for pre-Clinical Story Skeleton continuity.

Purpose: preserve Alexander's physician-originated decisions after World Spec kickoff and before Clinical Story Skeleton development. This is not a World Spec draft, not a file inventory, and not task prompt content.

## Source Context

- Approved Brainstorm: `worlds/korvin-merrow/active/brainstorm.md`
- Reviewer GO: `worlds/korvin-merrow/reviews/reviewer-go-01.md`
- World Spec kickoff packet: `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`
- Clinical logic file: `worlds/korvin-merrow/active/clinical-logic.md`

## Locked Temporal Architecture

- 6-day hospitalization.
- World close: Hospital Day 6 at 18:00.
- Discharge anchor after world close.
- +7 day post-discharge anchor.
- +30 day post-discharge anchor.

Operational meaning:

- The world-level chart closes at HD6 18:00.
- Tasks must be anchored after that world close.
- Post-discharge tasks may use +7 day and +30 day anchors, but must not depend on other tasks' outputs.

## Locked Underlying Clinical Story

- Mixed physiology world.
- Infection, steroid issues, CKD/HF, and polypharmacy interaction all contribute to the reasoning burden.
- This is not a single-diagnosis world.

Operational meaning:

- The correct reasoning should not collapse the case into "sepsis only" or "adrenal insufficiency reveal."
- The World Spec should preserve overlapping explanations and temporal reassessment.

## Locked Presentation Trigger

The presentation is triggered by:

- Progressive weakness.
- Poor oral intake.
- Near-fall/lightheadedness.
- Family-noticed confusion.
- Possible urinary symptoms.

Operational meaning:

- ED evaluation should remain realistic and undifferentiated.
- Urinary-source infection can be reasonable initially, but does not explain the whole hospitalization.

## Locked Clinical Evolution

- Approximately 3-week decline before presentation.

Operational meaning:

- The story should include subacute functional and physiologic decline before ED arrival.
- This should support the family's baseline concerns and discharge-readiness tension.

## Locked World Tone

- Medically improving.
- Operationally dangerous discharge.

Operational meaning:

- The patient can look better by vitals, labs, and infection treatment response.
- The danger is unsafe transition planning, unresolved functional decline, medication complexity, and source-of-truth ambiguity.

## Locked Primary Failure Target

The primary failure target is:

- Functional decline.
- Disposition safety.
- Discharge readiness reasoning.

Operational meaning:

- The hardest part is not naming a rare disease.
- The World should test whether an agent can integrate medical stabilization with real-world discharge safety.

## Locked Complexity Targets

- Exceed reviewer minimums.
- Target 12-15 comorbidities.
- Target 18-22 medications.

Operational meaning:

- The approved Brainstorm already expanded the burden and medication specificity.
- World Spec development should refine and possibly expand the comorbidity and medication lists within these targets, with Alexander approval.
- Medication expansion should support the existing cardiorenal, diabetes, steroid, neuropathy, bone-health, and discharge-reconciliation logic without adding unrelated noise.

## Boundaries

Do not use this log to:

- draft the World Spec;
- create the Clinical Story Skeleton;
- create final calendar dates;
- create a file inventory;
- write task prompts;
- create golden responses;
- create grader guidance;
- invent clinical values, lab values, vitals, provider names, MRN, or file names.

Next legal use:

- Use this as the locked decision source when Alexander explicitly starts Clinical Story Skeleton development.

