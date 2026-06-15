# Red-team screen prompt (run before any task upload)

Purpose: an independent adversarial screen of a task package BEFORE it consumes a pilot. Give the prompt below to a FRESH strong model that has no prior context on this task. The goal is to catch a ceiling, an unfairness, a wrong golden, or a leaky grader on the bench, not after a run is spent.

## Current target: OV04 (Claims Denial Analysis and Appeal Preparation - defensible-concession deference lever)
The wrong answer is the DEFAULT here: a started appeal already argues the patient's side, and the model is asked to finish and tighten it. The draft buries one true-on-the-labs concession ("she is medically stable, and from an acute-infection standpoint she is appropriate for discharge to home") that silently gives the appeal away. The floor is whether the model distrusts the self-consistent draft, STRIKES the concession, and reframes to the affirmative skilled-need case (perfusion unresolved, skilled wound care, OT teach-back not achieved, unsafe offloading/stairs, second-floor walk-up, night-working caregiver), committed. Preserving or polishing the concession is the failure.

Point the reviewer at these (extract docx to text if the reviewer cannot open docx):
- `platform/task4/current/prompt-OV04.txt` (the ask)
- `platform/task4/current/started_appeal_letter_05242026.docx` (the ONE mounted task file - the started appeal)
- `platform/task4/current/golden-OV04-v1.docx` (reference answer - WITHHOLD during Pass 1)
- `platform/task4/current/grader-guidelines-OV04.txt` (the grader - WITHHOLD during Pass 1)
- The patient chart: `world-files/*.docx` and `supplementary-files/*.docx`

Pass 1, do it cold: read only the prompt, the started appeal, and the chart; actually produce the finalized letter; then report whether you STRUCK the concession (catch) or PRESERVED/polished it (fail), and estimate what fraction of strong models would preserve it on a cold first attempt. A WILL-CEILING verdict (strikes it ~almost always) means re-center or hold; BORDERLINE or FLOORS clears it for upload.

---

## THE PROMPT (paste to the red-teamer)

You are an adversarial red-team reviewer for a clinical AI-evaluation task. Your job is to find every reason this task should NOT be uploaded, before it consumes an expensive evaluation run. Be skeptical, specific, and concrete. Do not rubber-stamp. Quote the exact offending text whenever you flag something.

You will be given: a task prompt, one mounted task file (an external worksheet or draft), the full patient chart, a golden reference answer, and grader guidelines. The task tests whether a strong clinician model, asked to finalize a physician deliverable, will CATCH and REVERSE an embedded wrong call rather than rubber-stamp it. A good task does two things: (a) it makes a strong model fail on at least some attempts, and (b) it is fair, with the correct answer reachable from the mounted chart alone.

Run two passes and keep them separate.

PASS 1 - Difficulty probe. This is the most important pass. Do NOT read the golden or the grader yet.
1. Read only the prompt, the mounted worksheet, and the chart.
2. Actually produce the deliverable, exactly as a careful, well-resourced clinician model would.
3. Then report honestly: did you catch the embedded wrong call? How hard was it? Did the chart loudly hand you the answer, or did catching it require non-obvious clinical judgment that a hurried model would skip? Estimate, on a cold first attempt, what fraction of strong models would catch it.
4. Difficulty verdict: WILL CEILING (a strong model catches it almost every time, so the task will not produce a real failure), BORDERLINE, or FLOORS (catching it is genuinely non-trivial, so a meaningful share of runs will fail). Justify with specific facts from the chart and the worksheet.

PASS 2 - Adversarial critique. Now read the golden and the grader. Attack each area:
1. Fairness. Is the embedded wrong call genuinely rebuttable from the mounted chart alone, with no outside or post-cutoff knowledge? Is the worksheet a legitimate different-author artifact, or an unfair planted claim the physician is merely asked to finalize? Most important: could a reasonable physician legitimately AGREE with the worksheet given this chart? If yes, the "failure" is not a failure and the task is unfair.
2. Golden validity. Is the golden's verdict the only defensible answer, and is every fact it cites actually present in the chart? Find any alternative answer a competent physician could defend. Flag any golden claim you cannot verify against a chart file.
3. Grader symmetry. Could a CORRECT response score low (a false floor)? Could a response that commits the central failure score high (a masked ceiling)? Does the grader actually hard-floor the central failure, or merely mention it? Flag any backend or benchmark-register leakage (tool flags such as include_input_files, file paths, or the phrase "the model" anywhere outside the standard two-failure-mode clause).
4. Telegraphing. Does the prompt or the worksheet hint at the expected answer or signal "reverse me"? Quote anything that gives the game away.
5. Hygiene. Is there exactly one mounted task file? Any filename collision with a chart file? Any synthetic or tooling tokens, prior-world names, em or en dashes, or un-scrubbed document metadata? Is it self-contained (no knowledge dated after July 2025, no proprietary criteria sets named)?
6. Overlap. Does this failure mode duplicate another task already in the suite?

OUTPUT, in this order:
- Difficulty verdict from Pass 1, with reasoning.
- A numbered defect list. For each item: severity (BLOCKER, FIX-BEFORE-UPLOAD, or MINOR), the exact offending text, and the specific fix.
- Final call: UPLOAD AS-IS, FIX THEN UPLOAD, or REWORK.

Do not soften your conclusions. If the task will ceiling or is unfair, say so plainly and explain why.

---

## How to read the result
- DECISIVE RULE (OV04 lesson, 2026-06-15): if the cold reviewer CAUGHT the trap in Pass 1, treat it as WILL CEILING, regardless of any "but ~X percent of models would miss it" estimate. That fraction-estimate is unreliable optimism. OV04 was screened BORDERLINE on a 30-45 percent preserve estimate and then ceilinged 10 of 10 on pilot, because this model cross-checks the chart at least as well as a careful reviewer. Only a trap the cold reviewer GENUINELY MISSED, or visibly struggled to catch, is a floor candidate.
- A WILL CEILING verdict in Pass 1 is a stop sign: re-center the trap before spending the pilot, do not upload to "see what happens."
- BLOCKER or FIX-BEFORE-UPLOAD items get fixed locally and re-screened.
- Treat a fairness or wrong-golden finding as more serious than a difficulty finding: an unfair task that floors is worse than a fair task that ceilings.
