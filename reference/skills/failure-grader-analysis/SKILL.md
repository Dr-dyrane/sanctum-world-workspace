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

Grader Analysis answers: "Did the grader score this correctly?" - what the grader got right, what it missed or mis-scored, and the concrete edit the grader guidelines need. It is not a defense of the number.

Do not explain how the task was built. Do not explain how the grading system works.

## Failure Analysis structure

Paragraph 1: State the failure. State what the response did. State why it was wrong.

Paragraph 2: Why it matters clinically. What consequence follows. Restate the central failure.

Pattern: wrong action, clinical significance, consequence.

Be specific (name the drug, lab, finding, and the consequence) and accessible: the 06_09 standard says the FA is read by non-medical engineers, so explain the mechanism, avoid unexplained jargon, and name the documents that verify the failure.

FAILURE-ONLY, by pod-lead override. The 06_09 template lists "What the Agent Got Right" as an FA component, but Ahmad (Trigeminus, more recent than 06_09) told us to cut it and focus on what the model did wrong. Keep our FAs failure-only unless the pod lead says otherwise.

## Grader Analysis structure (06_09 standard)

Four to six sentences total, kept as two short paragraphs so the local gate passes (it wants two; two short ones are still the single tight write-up the client asks for).

Paragraph 1: what the grader got RIGHT, named specifically - which non-negotiable it caught, that it did not let the polished rest inflate the score - and whether the score is fair.

Paragraph 2: where it fell short, labeled as a MISS (the grader never identified a failure) or a MIS-SCORE (it identified the failure but the number is off), stated concretely. Then a recommended edit in the "add X to the failure modes" form, not a vague concern.

Describe the grader-guideline content by its words; never name Section A, B, or C. Quote the rubric language when it matters.

Gate trap: the both-sides check bans the literal phrases "what the grader got right" and "what the model did well" anywhere in the file, including the Status line. Discuss what the grader judged correctly, but phrase it "the grader correctly identified" or "the grader caught," never "what the grader got right."

## Voice (the FA and the GA differ)

The FA and the GA review different objects, so they sit in different registers. Do not force them into the same voice.

FA voice: a physician reviewing a chart. Specific clinical reasoning, named drugs, labs, and findings, with the consequence stated. The 06_09 standard adds that the FA is read by non-medical engineers too, so write it so a general internist or a technically informed non-physician can follow: explain the mechanism, avoid unexplained jargon. Specific and accessible, not terse shorthand meant only for another attending.

GA voice: a reviewer auditing the grader, not the patient. Its subject is the scoring, so its natural vocabulary is the grader, the score, the band, what the grader caught and missed, and the failure mode to add. That is the correct register, not a lapse; forcing the GA into bedside prose reads wrong, and the 06_09 appendix examples are written exactly this way. Clinical voice is the FA's job, not the GA's.

What both share (the Alexander discipline): short, direct sentences; no AI transitions (Furthermore, Moreover, Notably); no narrating tool calls or the grading plumbing; name the clinical anchors specifically. verify_voice enforces the no-AI-transitions and no-scaffolding part on both.

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
