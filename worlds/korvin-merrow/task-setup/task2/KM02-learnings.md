# KM02 learnings (Task 2 retrospective) - 2026-06-07, awaiting first human review

Task 2 = Hospital Discharge Summary Generation. Clean pilot 94.4% (too easy) -> escalation 65% mean (good stumping) with a clean 0.35 FA subject. What it taught, for Tasks 3-6.

## 1. The forced slot is the whole game (headline, confirms THE LAW point 4 at n=2)
KM01 bit (0.78) because a medication reconciliation HAS a prednisone row the model must fill, and forcing a number is the error. KM02's clean discharge summary did NOT bite (94%) because the genre lets the model defer everything ("to be finalized"); there is no slot it must fill with a value it can get wrong. Difficulty in these evals lives in a FORCED move, not in completeness or correctness. A synthesis task with no forced slot, on a chart that coaches openness, will run high no matter how good it is. Verified at the byte level: prednisone flagged unverified in 8 files, culture pending in 4, chart internally consistent (no numeric conflict to resolve wrong).

## 2. When the genre has no forced slot, manufacture one with a mounted adversarial input
The colleague-draft (an authoritative half-finished attending draft with chart-contradicted closures planted in correct prose, framed "finish it for sign-out") converts the test from GENERATE a fabrication (careful models resist) to PROPAGATE a pre-written one (more models fail). The failure mode it measures is real and worth testing: over-trusting a handed document instead of verifying the source. ~half the runs propagated; the catch runs prove it is fair and catchable. This is the reusable difficulty lever for synthesis tasks.

## 3. Difficulty is empirical; ship the calibrated number, do not pre-soften
Aimed ~85%, landed ~65% (the draft was stickier than predicted). 65 is in the good band (<70); softening back to 85 would re-create the too-easy problem we just escaped. Run it, read the spread, ship at the honest number. Do not reach a target by docking the correct answer.

## 4. Verify on the AGENT-READ layer, every time (recurred twice this task)
I twice concluded facts from the FI-W markdown / .meta reference copies instead of file-review/upload/filesystem (the culture+antibiotic, then the chrome). The agent-read MAR (cf90ceb0) names ceftriaxone-to-cefpodoxime and the culture status; the markdown and reference copies do not. Gate: verify by hash on upload/filesystem, python-docx INCLUDING table cells, never the markdown.

## 5. Rules written after an error come out instance-shaped; write them at the class
Grader-config, markdown/docx layer, and the template miss each had a rule that fixed its own case and missed the sibling case until a reviewer caught it. The template gate I wrote after the golden miss did not stop me building the colleague-draft as a plain doc. Fix (now in the build gate): when adding a rule, ask "what CLASS does this error belong to" and write it there. The template/chrome standard covers EVERY artifact (golden, task file, draft), not just goldens; default all through the world builder.

## 6. Read the grader transcript before concluding (KM01 rule held)
The clean pilot's 92-97 spread was pure grader jitter (the 0.92's only noted issue was explicitly allowed); the escalation's lows were real propagation (run 7 verified). Reading the transcript, not the score, separated jitter from a real failure mode.

## 7. Process gotchas
- Bash mount serves TRUNCATED copies of freshly-written files (builder .py, source.md), silently dropping the last section from renders. Build from /tmp copies; verify the last section is present.
- Footer meta-language: "Synthetic training document" in a footer fails Task AutoQC "Meta-Language and Content Hygiene". Strip it; builder fixed. Golden-only fix sufficed; the finalized world was not re-opened.
- QA tech-issue has TWO boxes: the annotation field = exactly "tech issue" (narrative fails the Feedback AutoQC), the dedicated dismissal-reasoning field = a full sentence. And keep the dismissal sentence honest (KM02: 9 of 10 scored, run 8 was a grader tooling failure, not "all ten").
- FA/GA field cap ~1000 chars; match Task 1 length (FA ~984, GA ~840), two short paragraphs, no em dashes.

## 8. The multi-reviewer loop earned its keep
claude.ai red-team + Codex gate + verifying each claim against the primary bytes caught the culture/antibiotic fabrication, the footer, the chrome mismatch, and the FA length. The discipline that paid every time: go to the primary artifact (grading transcript, agent-read docx), do not infer from a summary or the latest reviewer.
