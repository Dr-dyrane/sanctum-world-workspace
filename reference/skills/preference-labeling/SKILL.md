---
name: preference-labeling
description: >-
  Draft a preference label (PL) comparing two model transcripts, Transcript A vs
  Transcript B, for an adversarial clinical-documentation eval task (Project
  Sanctum / Korvin Merrow / Ondina Vasquell style). Scores the pair on the A1-B3
  scale against the task's golden and grader and produces a paste-ready label in
  the house format. Use this whenever the user pastes a Studio preference-labeling
  pair (for example "Transcript A 0.90 ... Transcript B 0.72", or "PREFERENCE
  LABELING, Annotated pairs 1 / 3"), or says "label this pair", "draft the PL",
  "preference label", "which output is better, A or B", "annotate the pair", "do
  the preference labeling", or is at Step 15 preference labeling. Trigger even
  when the user just drops two transcripts each with a score and does not say the
  words "preference label". Do not trigger for failure analysis or grader analysis
  (FA/GA), grader-guideline writing, or golden authoring.
---

# Preference Labeling

A preference label compares two model transcripts (A and B) for one eval task and
records which is better, by how much on the A1-B3 scale, and why, in a paste-ready
house format. The whole verdict turns on one thing: how each output handled the
task's central designed failure. Everything else (prose, formatting, length, step
count) is noise the grader is told to ignore, so you must too.

The output is a workspace backup file that the writer reads and owns. You draft it.
You never submit it, enter it on the platform, or run Preference Labels AutoQC
without the writer's explicit authorization for that exact step.

## Before you label: pin the central failure

Do not label from memory. The pair is decided against the task's central capped
failure, so read the task's own evidence first:

- The golden (`golden-<TASK>.docx`): the correct answer. Section A "must be present
  and correct" lists the non-negotiable moves.
- The grader guidelines (`grader-guidelines-<TASK>.txt`): Section C names the
  central failure to watch for and the patterns to reason about.
- The results / reconciliation record and the current FA/GA: these state what the
  floors did wrong and what the catcher did right, in this task's own words.

Write down, in one sentence, the central golden move and the central failure (for
example: "discontinue the carried-forward inpatient enoxaparin at discharge; the
failure is continuing or soft-pedaling it"). That sentence governs the verdict.

## Method

1. Pin the central failure (above). The grader caps the score on it, so the
   preference is mostly a question of who handled it better.
2. Read both final outputs end to end, not just the summary line.
3. Frame the pair. This sets the ceiling on the margin:
   - both-pass (both above the floor band),
   - both-floor (both in the floor band),
   - pass-vs-floor,
   - catch-vs-miss (one makes the golden move, the other does not).
4. Compare on the central item first, then walk the seven sections.
5. Pick the tier with the conservative-margin calibration below.
6. Write the label using `references/pl-format-template.md`.

## The A1-B3 scale and the button

| Tier | Meaning | Button |
|---|---|---|
| A1/B1 | Slightly better; a narrow point | plain A or plain B (no plus) |
| A2/B2 | Better; avoids a discrete error the other makes | A+ or B+ (one plus) |
| A3/B3 | Much better; the other falls for the central designed trap or misses a critical finding | A++ or B++ (two plus) |

The rating lives in two places only: the `VERDICT` line of the file and the Button
you select on the platform. It is never a line of pasted text (see the format
section). Do not use A4/B4 or three-plus language unless new pod guidance restores it.

## Conservative-margin calibration (the part that matters most)

This is where most PLs go wrong, by inventing a bigger gap than the evidence
supports. Hold to these:

- Decide on the central failure, never on prose polish, formatting, length, or
  step count. State the decider explicitly in guardrail form so an edit cannot
  drift it onto style.
- The cap rule: if neither output makes the golden's affirmative move on the
  central item (neither catches the trap), cap the margin at one plus. Two pluses
  means one caught the designed trap and the other fell for it. When
  both only partially handle it, the most you are seeing is "less wrong," which is
  one plus at most, and often plain.
- Both-floor pairs are severity comparisons. Default to tier 1 (plain). Go to
  tier 2 only if one output is materially safer as a clinical result, a genuinely
  safer order or decision, not merely milder or better-hedged wording.
- Discrete error vs degree. A discrete factual or clinical error that one side
  makes and the other avoids earns one plus. A difference only of caution,
  emphasis, or completeness, with no discrete error, stays plain.
- Use the grader as evidence, not gospel. Align with its direction unless it made
  a clear error. The score gap hints at magnitude (a 0.05 gap is plain, a 0.15 to
  0.20 gap is usually one plus), but the central-item reasoning governs, not the
  raw number.
- Be fair to the loser. Credit a correct principle even in the worse output; do
  not penalize a side for being right about something. The decider is the outcome
  on the central item, not who phrased the principle more nicely.

## The seven sections

- Preferred output: which one, and the single sentence that decides it.
- Justification: why this tier. Carry the central-item argument and the cap
  reasoning (why not a higher or lower tier).
- Prompt adherence: did both answer the requested workflow and format. Usually a tie.
- Correctness: clinical accuracy against the golden, the central item above all.
  Usually the deciding dimension.
- Completeness: coverage of the required items and any secondary catches.
- Methodology: how each read and reconciled the chart.
- Quality and clarity: organization and readability. The grader is told not to
  weight formatting, so this is usually neutral; say so.
- Summary: restate the preference, the tier, and why it is not one step higher or
  lower.

## Clinical voice (Dr. Alexander voice DNA)

The justification prose must read like a physician doing chart review, not an AI
explaining what it did. This is enforced repo-wide by `tools/verify/verify_voice.py`
(see `docs/alexander-voice-dna.md`), which checks every PL.

- State the omission, why it matters clinically, and the consequence. Short
  declarative sentences. "The note missed the poor CPAP adherence. This affects the
  OSA assessment and follow up."
- Name the clinical mechanism, not the eval plumbing. "The compliance report was an
  image file the model never opened or reviewed" is fine. Narrating OCR, directory
  listings, tool calls, binarizing, or "the transcript shows" is scaffolding the
  gate flags; do not write it.
- No banned AI transitions: Furthermore, Moreover, Consequently, Notably, In
  addition, salient finding, critical insight, robust analysis, comprehensive
  review. These hard-fail the gate.
- Keep the house PL structure and the scoring logic; the voice applies to the prose
  inside it.

## The house format (three easy ways to get it wrong)

Copy `references/pl-format-template.md` and fill every field. Three recurring breaks:

- No "Scale Selection" line in the pasted Comments box. The scale selection lives
  in the `VERDICT` line of the workspace backup and the Button. The pasted comment
  starts at "Preferred output:". If Studio exposes a separate scale control, set it
  there. Do not add a second pasted "Scale Selection" line.
- No em dashes or en dashes anywhere, in this file or any deliverable. Use plain
  hyphens and commas. (Run a quick scan for the characters before you finish.)
- No eval-scaffolding narration in the prose (OCR, directory listing, tool calls,
  "the transcript shows"); use the clinical mechanism instead. Run
  `python3 tools/verify/verify_voice.py` before finishing; it must come back clean
  (no banned transitions, no scaffolding warns on the PL).

## Guardrails to put in every label

End every label with a short numbered "Guardrails (must survive any edit)" block:

1. State the preferred output and the Button.
2. Name the decider (the central-item handling) and forbid drifting it onto style.
3. Justify the tier, and explicitly why not one step up or down.
4. Record the single deciding gap (the discrete error, or the degree difference)
   so a later edit cannot lose it.
5. List the items both got right so they are not mistaken for differentiators.
6. Note which PL of three this is and that the pairs are distinct trajectories.

## Boundaries

- Draft for read and own only. No submission, platform entry, or PL AutoQC without
  the writer's explicit authorization for that exact step.
- Three PLs per task, each on a distinct trajectory pair. The pairs are
  Studio-selected; you do not choose them.
- Related but separate: the FA/GA subject is the second-lowest run, not the lowest
  (DO-NOT-REPEAT #20). That rule is about FA/GA, not PL; PL pairs are whatever
  Studio shows you.

## Worked examples

`references/worked-examples.md` has five labeled pairs covering the patterns you
will hit most: a both-floor severity call (plain), a one-plus from a discrete
error, a plain-A from a degree-only difference, and a one-plus where the loser
endorses the trap and floors. Read it when a pair feels borderline between tiers.
