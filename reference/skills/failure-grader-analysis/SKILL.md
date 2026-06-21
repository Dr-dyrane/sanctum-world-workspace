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

> CANONICAL (LOCKED): `docs/fa-ga-canonical.md` is the single standard, derived from the EXP 06_09 instruction doc, approved KM FA/GAs, and Vagus 2026-06-18 guidance. Read it first. If this guide or any skill-cache template disagrees, the canonical wins. The GA is a grader AUDIT and MUST name both what the grader identified correctly AND what it missed or mis-scored, then judge calibration. An affirm-only GA that ends "the score is justified" without the improvement move is incomplete and will be sent back.

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

Grader Analysis answers: "Did the grader score this correctly?" It is a grader audit: what the grader evaluated correctly, what it missed or mis-scored, why the score still holds, and the concrete edit the grader guidelines need. It is not a defense of the number, and it is not a second failure analysis.

Do not explain how the task was built. Do not explain how the grading system works.

## Failure Analysis structure

Paragraph 1: State the failure. State what the response did. State why it was wrong.

Paragraph 2: Why it matters clinically. What consequence follows. Restate the central failure.

Pattern: wrong action, clinical significance, consequence.

Be specific (name the drug, lab, finding, and the consequence) and accessible: the 06_09 standard says the FA is read by non-medical engineers, so explain the mechanism, avoid unexplained jargon, and name the documents that verify the failure.

FAILURE-ONLY, by pod-lead override. The 06_09 template lists "What the Agent Got Right" as an FA component, but Ahmad (Trigeminus, more recent than 06_09) told us to cut it and focus on what the model did wrong. Keep our FAs failure-only unless the pod lead says otherwise.

## Grader Analysis structure (06_09 standard)

This is a grader AUDIT, not a second failure analysis. Ahmad's correction (2026-06-17): do not re-narrate the model's failure here. Audit the grader against four questions:

1. What did the grader evaluate correctly? (the central failure it caught, and that it was not distracted by the otherwise complete rest of the response)
2. What did the grader miss?
3. Why is the score still reasonable?
4. How could the grader improve? (a concrete "add X to the failure modes" edit, not a vague concern)

About six to eight sentences across two short paragraphs (two so the local gate passes). Paragraph 1 carries (1) and (3): what the grader got correct and that the score holds. Paragraph 2 carries (2) and (4): the miss and the concrete fix. Label a shortfall as a MISS (the grader never identified the failure) or a MIS-SCORE (it identified the failure but the number is off). When the miss did not change the score (the failure already capped the run), say so, then give the case where the same gap would matter.

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

- Status line: above the two fields, record the job id, the full score distribution, the mean, and the FA subject (Attempt, run id, trajectory, score). Bind the FA to one run, the second-lowest distinct score in the latest valid run set (DO-NOT-REPEAT #20), and read that run's grading transcript before writing. If trajectories and QA are rerun, redo FA/GA from the latest run set.
- Format: two paragraphs each, no bullets, about 1000 characters each. No em dashes or en dashes anywhere; use plain hyphens and commas.
- Gates before handback, both clean: `python3 tools/verify/verify_voice.py` and `python3 tools/verify/presubmit_task_gate.py task<N>`.
- Boundaries: draft for the writer to read and own. No submission, paste, AutoQC, or platform action without the writer's explicit authorization for that exact step. One FA/GA per task.
- Writer score: FA must include Alexander's own score, not the trajectory score, and LEAD with `Overall Failure Score: X.XX / 1.0` (Output Score first per the 2026-06-20 template; this skill is superseded by fa-ga-canonical). Larry's 2026-06-18 guidance says FA/GA cannot be AI-authored. Use this skill only as scratch support; Alexander must own the final platform text.

## Worked example

The cleanest reference is the OV04 FA/GA and the OV06 final (vascular referral) under `worlds/ondina-vasquell/phase-4-pilot-review-submit/fa-ga/`: failure-first, clinical voice, no builder or reviewer-mechanics language. `references/worked-examples.md` is being reconciled to this guide; until then, prefer the shipped OV04/OV06 files as the model.
