---
name: failure-grader-analysis
description: >-
  Draft or revise the Failure Analysis (FA) and Grader Analysis (GA) write-ups
  for an adversarial clinical-documentation eval task (Project Sanctum / Korvin
  Merrow / Ondina Vasquell style), in the house failure-only format. Produces two
  paste-ready fields, each two paragraphs and about 1000 characters, failure-only,
  in Dr. Alexander clinical voice, and gated by verify_voice and
  presubmit_task_gate. Use this whenever the user pastes a Studio pilot result (a
  job id, a score distribution, and a trajectory transcript) and asks to "write
  the FA/GA", "draft the failure analysis", "grader analysis", "do the FA and GA",
  "write this run up", or asks to revise an FA/GA after reviewer feedback (for
  example "make the FA justify the low average"). Trigger even when the user just
  drops a low-scoring trajectory and says "write it up". Do not trigger for
  preference labeling (use preference-labeling), grader-guideline writing, or
  golden authoring.
---

# Failure and Grader Analysis (FA/GA) - skill guide

## Primary sources first

Before writing:

1. Read the selected trajectory.
2. Read the grading transcript.
3. Read the current grader.
4. Read the current golden.
5. Read the latest reviewer correction.

Never write FA/GA from memory, task design notes, preregistration, or score alone. The trajectory is the primary artifact.

## Purpose

Failure Analysis answers: "What was wrong with the response?"

Grader Analysis answers: "Why is the assigned score justified?"

Do not explain how the task was built. Do not explain how the grading system works.

## Failure Analysis structure

Paragraph 1: State the failure. State what the response did. State why it was wrong.

Paragraph 2: Why it matters clinically. What consequence follows. Restate the central failure.

Pattern: wrong action, clinical significance, consequence.

## Grader Analysis structure

Paragraph 1: State why the score is appropriate. State the requirement that was missed.

Paragraph 2: Explain why the miss remains decisive. Explain why correct secondary work does not overcome it.

Map to the grader's clinical content. Never reference Section A, Section B, or Section C. State the requirement itself.

## Voice

Write like a physician reviewing a chart. Not a task designer, a pod lead, an AutoQC reviewer, or an AI explaining reasoning.

The reader should think "a physician reviewed this note," not "someone explained how the evaluation worked."

Focus on: missed follow up, missed findings, unsafe recommendations, unsupported conclusions, incorrect assessment, patient safety implications.

## Avoid

Builder language: floor, catcher, bimodal, mechanism, lane, bankable, score cap.

Reviewer language: additive checklist, rubric, grading framework, designed to test, failed Section A, failed Section C.

## The golden rule

Use the golden's reasoning. Do not use the golden as authority.

Bad: "The response disagreed with the golden."

Good: "The referral remained clinically necessary."

## The "the model" rule

Allowed. Use sparingly. Keep the focus on the response, the note, the plan, the assessment, and the completed coordination, not on the model itself.

## Clinical consequences

State consequences. Do not exaggerate them.

Prefer: "This removed a necessary vascular referral."

Over: "This leads to amputation."

Use the stronger claim only when the trajectory itself directly supports it.

## Final review checklist

Before submitting:

- Is the first paragraph immediately about the failure?
- Did I avoid a praise paragraph?
- Did I avoid Section A/B/C references?
- Did I avoid builder language?
- Did I avoid grader-mechanics language?
- Does this read like physician QA?
- Would the reviewer think I am explaining the failure instead of defending the score?

If yes, submit.

## Mechanics and gates (operational, not voice)

These carry the metadata so the prose stays clinical; they are not part of the pasted FA/GA voice.

- Status line: above the two fields, record the job id, the full score distribution, the mean, and the FA subject (Attempt, run id, trajectory, score). Bind the FA to one run, the second-lowest distinct score (DO-NOT-REPEAT #20), and read that run's grading transcript before writing.
- Format: two paragraphs each, no bullets, about 1000 characters each. No em dashes or en dashes anywhere; use plain hyphens and commas.
- Gates before handback, both clean: `python3 tools/verify/verify_voice.py` and `python3 tools/verify/presubmit_task_gate.py task<N>`.
- Boundaries: draft for the writer to read and own. No submission, paste, AutoQC, or platform action without the writer's explicit authorization for that exact step. One FA/GA per task.

## Worked example

The cleanest reference is the OV04 FA/GA and the OV06 final (vascular referral) under `worlds/ondina-vasquell/phase-4-pilot-review-submit/fa-ga/`: failure-first, clinical voice, no builder or reviewer-mechanics language. `references/worked-examples.md` is being reconciled to this guide; until then, prefer the shipped OV04/OV06 files as the model.
