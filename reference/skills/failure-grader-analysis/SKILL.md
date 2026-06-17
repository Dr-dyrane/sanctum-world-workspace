---
name: failure-grader-analysis
description: >-
  Draft or revise the Failure Analysis (FA) and Grader Analysis (GA) write-ups
  for an adversarial clinical-documentation eval task (Project Sanctum / Korvin
  Merrow / Ondina Vasquell style), in the KM7-10 house format. Produces two
  paste-ready fields, each two paragraphs and about 1000 characters, failure-only,
  in Dr. Alexander clinical voice, and gated by verify_voice and
  presubmit_task_gate. Use this whenever the user pastes a Studio pilot result (a
  job id, a score distribution, and a trajectory transcript) and asks to "write
  the FA/GA", "draft the failure analysis", "grader analysis", "do the FA and GA",
  "write this run up", or asks to revise an FA/GA after reviewer feedback (for
  example "make the FA justify the low average", "follow the KM task 7-10 style").
  Trigger even when the user just drops a low-scoring trajectory and says "write
  it up". Do not trigger for preference labeling (use preference-labeling),
  grader-guideline writing, or golden authoring.
---

# Failure and Grader Analysis (FA/GA)

The FA and GA are the two write-ups the writer pastes into Studio for one floored
eval task. The FA says what the model did wrong on a low run and why it matters
clinically. The GA says whether the grader scored that run correctly. Both turn on
one thing: the task's central designed failure. Everything else (prose polish,
length, step count, formatting) is noise the grader is told to ignore, so you
ignore it too.

The output is a workspace draft the writer reads, owns, and pastes. You draft it.
You never submit it, enter it on the platform, or run AutoQC without the writer's
explicit authorization for that exact step.

## Before you write: pin the central failure

Do not write from memory. The score is capped on the task's central failure, so
read the task's own evidence first:

- The golden (`golden-<TASK>.docx`): the correct answer. Section A "must be present
  and correct" names the non-negotiable move.
- The grader guidelines (`grader-guidelines-<TASK>.txt`): Section C names the
  central failure and the patterns to reason about.
- The pilot record and any prior FA/GA: these state what the floors did wrong, in
  the task's own words, plus the score distribution and the job id.

Write down, in one sentence, the central golden move and the central failure (for
example: "discontinue the carried-forward inpatient sliding scale at discharge; the
failure is sending it home unchanged"). That sentence governs both write-ups.

## Run-binding (which trajectory the FA describes)

The FA is bound to ONE run, named in the Status line, and it describes that one
trajectory only. The CURRENT rule is the second-lowest DISTINCT score, not the
absolute lowest (OV / DO-NOT-REPEAT #20), so a single anomalous floor does not
drive the analysis. This changed from the older KM practice, which bound to the
single lowest run, so the KM7-10 examples you copy use the lowest while the current
OV standard is second-lowest distinct. Read the grading transcript for the bound run
before you write (the KM01 rule: do not infer the failure from the output alone).
Bind to a run you have a full transcript for, and if it is not the strict
second-lowest distinct, say so in the Status line and offer to rebind.

## The house format (KM7-10)

Copy `references/fa-ga-format-template.md` and fill every field. The shape:

- A `Status` line with the job id, the full score distribution, the mean, and the
  FA subject (Attempt, run id, trajectory, score). This carries the metadata so
  the prose does not have to.
- `## Failure Analysis`: exactly two paragraphs, about 1000 characters, no bullets.
- `## Grader Analysis`: exactly two paragraphs, about 1000 characters, no bullets.

KM7's own fields run about 1035 and 1081 characters, so "about 1000" is the target,
not a hard 1000. Aim at or just under 1000 so the gate stays clean; matching KM at
~1050 is acceptable if trimming would cost real content.

### Failure Analysis: the two moves

Always open paragraph one by naming the bound run by its number: "On trajectory
10..." or "On Attempt 10...", matching the FA subject in the Status line. Never use
a numberless opener like "On this trajectory." The FA describes that ONE trajectory
only. Never compare runs, never write "the two lowest," and keep all cross-run
material out of the FA entirely; the run distribution and calibration belong in the
GA, not the FA (Abi house rule: one trajectory, not all).

FAILURE-ONLY (pod lead Ahmad G, 2026-06-16, Trigeminus). Do NOT open with a
competent-baseline paragraph. The earlier KM7-10 shape led with what the model did
well; Ahmad cut that for the OV world: "we don't need this at all, it should just
focus on what the model doesn't do well." Lead paragraph one with the failure
itself, named specifically and tied to the golden, and give the model no credit
paragraph anywhere.

You may still show that the model had the evidence and failed anyway, but FRAME it
as failure, not praise: "it closed the referral even after reading the perfusion
study and quoting the toe pressures" is failure-framing; "it read the study well" is
the credit paragraph Ahmad rejects. Write it as one connected argument, not a
staccato list of "It did X. It did Y." sentences; it should sound like an attending
naming what went wrong, not a balanced review.

Paragraph two carries the clinical detail Ahmad asks for: spell out the mechanism and
the consequences in several sentences, in Alexander voice, building to the harm. Name
what the wrong move does to the patient (a limb-threat foot discharged with no
vascular follow-up, the path to a nonhealing ulcer and amputation) and add any
secondary failures (it folded the closure into the attending verification as a
confirmed item). End by naming the central failure. Err toward MORE detail when the
pod lead asks for it, even past about 1000 characters; the gate length note is
non-blocking. Keep the run distribution OUT of the FA ("drives the floored runs from
0.08 to 0.50" is cross-run language that belongs in the GA); the FA stays on one
trajectory.

### Grader Analysis: the two moves

Paragraph one says the score is appropriate for an otherwise usable deliverable
that misses the central item, then walks how the grader got there: it set the
output against the golden, found the failure, applied the cap rule (the rubric says
the central miss caps the score low however complete the rest is), gave appropriate
credit for the accurate parts, and flagged the secondary errors.

The GA EVALUATES what the grader did; it does not ADVISE the grader what it should
have done. This is AO's KM10 correction: a GA that mostly tells the grader how to
score is wrong even with the right verdict. Judge the grader's actual number against
this run's output and the golden, say whether it identified the central failure,
applied the cap, credited the right parts, and calibrated the score, and do not
narrate the grader's exploration ("the grader went into the chart").

Explain WHY the low score holds despite the competent parts (pod lead Ahmad G,
2026-06-16). A reviewer will ask why a run that did several things well still scores
0.1; answer it head on. The rubric is safety-weighted, not additive: a critical miss
caps the score because it makes the deliverable unsafe to sign, so the competent
parts do not lift it off the floor. Use the catchers as proof: the runs that got the
central call right scored high (0.82 to 0.88) on the same competent work, so the
whole distance between the floor and the catchers is the weight of that one decision.
A higher score would imply the deliverable is usable when it is not. Say this; do not
leave the low number unexplained.

Paragraph two confirms the calibration holds across the run set (every trajectory
that made the miss landed in the same band, so the grader is keying on the safety
miss and not surface quality), then closes with the KM calibration sentence: "a
deep floor would overstate an otherwise complete plan, and a high score would
ignore [the hazard], so the band is well placed." End with "the score is justified".

## Clinical voice (Dr. Alexander DNA)

The prose must read like a physician doing chart review, not an AI explaining what
it did. This is enforced repo-wide by `tools/verify/verify_voice.py` (see
`docs/alexander-voice-dna.md`).

- State the omission, why it matters clinically, and the consequence. Short
  declarative sentences. "A mealtime sliding scale is an inpatient tool. Sent home
  to a patient who lives alone, it is a hypoglycemia hazard."
- Name the clinical mechanism, not the eval plumbing. Narrating OCR, directory
  listings, tool calls, or "the transcript shows" is scaffolding the gate flags.
- No banned AI transitions: Furthermore, Moreover, Consequently, Notably, In
  addition, salient finding, critical insight, robust analysis, comprehensive
  review. These hard-fail the gate.

## Gate-enforced guardrails (the format traps)

`presubmit_task_gate.py` checks the FA/GA fields. The recurring breaks:

- Failure-only, no both-sides crediting. The gate rejects the phrases "the grader
  credited", "it credited the", and "credited the correct / useful / complete /
  model". Write "gave appropriate credit for" or "credit was warranted for"
  instead. Leading the FA with the competent baseline is fine; naming the grader as
  crediting things is what trips it.
- No grader-rating line in prose. The rating (Great, etc.) lives in the Studio
  field, not in the pasted text. Do not write "Recommended grader rating: ...".
- No grader-section names. Do not write "Section A / B / C"; state the content.
- Two paragraphs each, no bullets, each field about 1000 characters.
- No em dashes or en dashes anywhere. Use plain hyphens and commas. Avoid the
  banned glyphs the gate lists.
- One trajectory only (Abi house rule). The FA and GA describe a single run. Never
  compare runs or write "the two lowest"; the only cross-run sentences are the
  across-trajectory line in FA paragraph two and the calibration line in GA
  paragraph two.
- Never narrate the grader's exploration ("the grader went into the chart") and
  never use first-person "what I missed." Describe the model's behavior and the
  grader's scoring, not the eval mechanics (Abi/AO house rules).

## Run the gates before you hand it back

Both must come back clean (a slight over-1000 char note is acceptable if you match
KM, but prefer under):

```
python3 tools/verify/verify_voice.py
python3 tools/verify/presubmit_task_gate.py task<N>
```

verify_voice must show no banned transitions and no scaffolding warns on the FA/GA.
presubmit must show PASS for the task with no both-sides, section-name, glyph,
rating-line, or two-paragraph flags on your file.

## Boundaries

- Draft for read and own only. No submission or AutoQC without the writer's
  explicit authorization for that exact step.
- One FA/GA per task, bound to one run (second-lowest distinct by default).
- Related but separate: preference labeling compares two trajectories and uses the
  A4-B4 scale (use the preference-labeling skill). Golden authoring and
  grader-guideline writing are their own steps; this skill does not do them.

## Worked examples

`references/worked-examples.md` has the OV03 discharge-insulin FA/GA in full and a
condensed KM7 example on a different task, so you can see the same shape twice.
Read it when a draft feels off-format or you are unsure how much detail to carry.
