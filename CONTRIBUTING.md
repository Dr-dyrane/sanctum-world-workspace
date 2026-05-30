# Contributing

This is a private working repository for Project Sanctum onboarding and future project work. Contributions should preserve clinical authorship, phase boundaries, and source integrity.

## Branch Naming

Recommended branches:

- `main`
- `james-carter-brainstorm`
- `james-carter-world-spec`
- `reviewer-fixes/<short-topic>`
- `autoqc-fixes/<short-topic>`

Use focused branches for reviewer or AutoQC fixes. Do not mix unrelated clinical design changes with infrastructure work.

## Commit Messages

Use checkpoint-style messages:

- `checkpoint: submit brainstorm for human review`
- `checkpoint: add world spec autoqc prompt`
- `checkpoint: address brainstorm autoqc findings`
- `docs: harden repository workflow`

Commits should be small enough to review and rollback.

## Review Checklist

Before committing:

- [ ] `project/STATUS.md` matches the true phase.
- [ ] Current work is allowed by the phase gate.
- [ ] No clinical content changed without Alexander's approval.
- [ ] No source material was blended into authored work without attribution.
- [ ] No secrets, credentials, browser exports, or real patient data were added.
- [ ] Official templates were used where required.
- [ ] AutoQC or reviewer feedback was recorded if relevant.
- [ ] Working tree is understood before RL Studio uploads.

## Clinical Content Rules

- Alexander is the physician expert and clinical source of truth.
- Do not change clinical facts, diagnoses, medication logic, traps, frictions, task concepts, dates, labs, or file plans without physician approval.
- Challenge weak clinical reasoning, but do not replace physician judgment.
- Separate frictions from traps.

## Phase Boundaries

- Do not draft World Spec content before Brainstorm receives GO.
- Do not write final task prompts unless the phase allows it and Alexander authors or dictates them.
- Do not write golden responses, grader guidelines, failure analysis, or preference labels during onboarding unless Alexander explicitly updates the project phase.
- Do not begin synthetic file generation or production task setup during onboarding.

## Reviewer Feedback

Record reviewer feedback in:

- `worlds/james-carter/reviewer-feedback.md`
- or a dated file under `worlds/james-carter/reviews/`

Keep the official feedback record in RL Studio. Slack can clarify, but RL Studio remains the source of truth.

## AutoQC Findings

For AutoQC:

- Save the full output locally when available.
- Separate pass items, warnings, failures, and reviewer notes.
- Apply only fixes that improve approval probability and preserve physician intent.
- Document disagreements for reviewer visibility.
- Re-run AutoQC after changes when required.

