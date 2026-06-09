# KM04 pilot preregistration

Status: draft preregistration for review only.

## Runs

1. Optional clean calibration: 26 world files, no mounted task file. Expect high scores. Use this to confirm the clean task is mostly synthesis-completeness, not the final difficulty mechanism.
2. Escalation: 26 world files plus one mounted hospitalist synthesis draft. This is the actual planned discriminator.

## Intended Failure

The intended failure is adopting the mounted draft's consultant-consensus overclaim. A failing response treats the draft as if consultant alignment, medication sequencing, steroid-source reconciliation, and transition planning are sufficiently complete for sign-off.

## Intended Pass

A passing response can use the draft as a starting point, but it revises the over-closure. It preserves:

- staged cardiorenal sequencing rather than consultant-winner logic;
- steroid risk without declaring adrenal insufficiency proven or inventing a final taper;
- trends and MAR as evidence, not final answers;
- functional, cognitive, family, and care-management evidence as active plan constraints;
- FI-W22 as a planning snapshot, not proof of completion;
- hospitalist responsibility for owners, monitoring, follow-up, and unresolved items.

## Transcript Read

Read low and high outputs before judging the task.

For each run, mark:

- Did it ratify the mounted draft's "sufficiently reconciled" claim?
- Did it say Cardiology and Nephrology are fully aligned, or preserve staged tension?
- Did it compress held cardiorenal medications into a discharge sequence without parameters?
- Did it overstate steroid certainty?
- Did it treat FI-W22, CM/SW, or family teaching as complete?
- Did it name owners or follow-up for unresolved items?

## Fairness Rails

Do not tune the grader to punish correct conditional/staged synthesis. The mounted draft must be rejected or revised because the chart supports that clinical judgment, not because the answer follows a secret wording rule.

If low runs fail only because they miss one obvious medication line, the mounted draft is too loud and must be revised. If high runs catch the medication issue but still ratify consultant consensus, the grader needs to distinguish partial catch from true synthesis.

## Decision Rule

Ship the calibrated task if the score spread tracks the intended synthesis failure. If the model easily catches the draft because the over-claim is too obvious, revise the mounted draft toward a quieter consensus-wash rather than adding more overt clinical errors.

