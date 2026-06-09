# Task-Level Context File Construction Ratification

Date: 2026-06-02

Status: LOCKED

## Scope

This ratification locks Task-Level Context File Construction for FI-T01 through FI-T07.

Locked path:

- `worlds/korvin-merrow/task-context-files/locked/`

Locked files:

- `FI-T01_discharge-medication-reconciliation-request-context.md`
- `FI-T02_discharge-summary-drafting-request-context.md`
- `FI-T03_discharge-readiness-care-coordination-request-context.md`
- `FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md`
- `FI-T05_early-post-discharge-follow-up-assessment-request-context.md`
- `FI-T06_patient-safety-readmission-risk-review-request-context.md`
- `FI-T07_medication-safety-handoff-task-context-addendum.md`
- `task-context-files-validation-review.md`

## Review Outcome

Reviewer A completed review with verdict:

- LOCK READY
- GO

Reviewer B completed review with:

- Clinical Architecture Status: STRONG
- Final Recommendation: GO WITH MINOR NOTES

True defects:

- NONE

Architecture defects:

- NONE

Governance defects:

- NONE

## Carry-Forward Watch Items

Carry-forward / future prompt-layer watch items are recorded in:

- `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md`

Recorded watch items include:

- FI-T01 vs FI-T07 differentiation must be preserved at prompt-construction time.
- FI-T02 discharge-summary prompt construction must preserve anti-transcription emphasis.
- FI-T03 / FI-T06 future deliverables must preserve physician voice or physician responsibility.
- FI-S construction remains a separate blocked phase.
- Task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, and submission artifacts remain blocked until explicit authorization.

## Ratification Decision

Task-Level Context File Construction is approved for lock.

Task-Level Context File Construction:

- Status: LOCKED

Task-Level Context Files:

- Status: COMPLETE

## Content Preservation

FI-T01 through FI-T07 and the validation review were moved from:

- `worlds/korvin-merrow/task-context-files/candidate-review/`

to:

- `worlds/korvin-merrow/task-context-files/locked/`

The move is a lifecycle lock move only. It does not rewrite FI-T content, add prompt-layer material, add expected outputs, add goldens, add grader guidance, add AutoQC responses, add DOCX artifacts, or add submission artifacts.

## Downstream Boundary

Do not create the following until Alexander explicitly authorizes the relevant phase:

- FI-S01 through FI-S04
- supplementary files
- task prompts
- expected outputs
- goldens
- grader guidance
- AutoQC responses
- DOCX artifacts
- RL Studio submission artifacts
- RL Studio uploads

## Next Eligible Phase

Supplementary File Architecture / Construction.
