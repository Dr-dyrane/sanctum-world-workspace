---
name: fa-ga-canonical
description: >-
  Draft or revise the Failure Analysis (FA) and Grader Analysis (GA) write-ups
  for an adversarial clinical-documentation eval task (Project Sanctum / Korvin
  Merrow / Ondina Vasquell), in the LOCKED canonical format. Produces two
  paste-ready fields: a failure-only FA, and a grader-AUDIT GA that names what
  the grader got correct AND what it got wrong or could improve, then judges
  calibration. Use whenever the user pastes a Studio pilot result (a job id, a
  score distribution, a trajectory or grading transcript) and asks to write the
  FA/GA, draft the failure analysis, do the grader analysis, write up a run, or
  revise an FA/GA after reviewer feedback (for example the GA does not match the
  guidelines). Trigger even when the user just drops a low-scoring trajectory and
  says write it up. This is the corrected, canonical replacement for any older
  failure-grader-analysis skill; prefer it. Do not use for preference labeling,
  grader-guideline writing, or golden authoring.
---

# FA/GA Canonical - the locked write-up standard

This is the locked standard, derived from the Project Sanctum instruction document (EXP 06_09, Step 14) and every approved/delivered FA/GA (the two official source examples, KM task1-final rated Great, KM task9). Earlier skill versions encoded an affirm-only GA that just walks the score and ends "the score is justified." That is incomplete and gets sent back. Read this whole file before writing.

## The one rule that keeps getting missed
The GA is a GRADER AUDIT, not a second justification of the number. It must make two moves, and BOTH ARE MANDATORY:
1. What the grader got correct.
2. What the grader got wrong or could improve.
Then it judges calibration. An affirm-only GA (move 1 plus "the score is justified") is the recurring failure. If you wrote a GA with no improvement move, it is not finished.

## Primary sources first (never write from memory)
Before drafting, read in this order: (1) the selected trajectory output, (2) its grading transcript, (3) the current grader guidelines, (4) the golden. Do not infer the failure from the score or the output alone; KM task1 guessed four wrong failure modes, and the grading transcript showed the real miss. The golden's Section A names the non-negotiable move; the grader's failure-modes section names the central failure.

SAVE the run verbatim FIRST. When the pilot returns, copy the selected run exactly (the trajectory output and its grading transcript, as pasted from Studio) into the task's pilot/runs/ folder, named by job and attempt, and cite that file in the Status line, BEFORE writing a word of the FA/GA. The write-up must be derived from that saved primary source, not from chat memory. A run that lives only in the chat is gone at compaction; the next pass would be from memory, which is exactly where invented detail enters. Saved-run-first is what makes "never from memory" real and the FA/GA auditable.

## Run binding
Bind the FA to ONE run: the SECOND-lowest distinct score in the current valid run set (King P, 2026-06-14; supersedes the older "lowest run"). A single anomalous floor should not drive the analysis. If Taiga trajectories and QA are rerun, the prior FA/GA is stale. Redo FA/GA from the latest run set. If the strict second-lowest distinct has no full transcript, bind to the nearest run you do have and say so. The Status line is internal and is NOT pasted into Studio, so the submitted FA field must itself name the run: open the FA's first paragraph with "On trajectory N" (the 1-10 count, the same number as the attempt). Use that one identifier, not both attempt and trajectory, and not the run or trajectory hash; the hashes and the distribution stay in the Status line. The GA names the same run the same way ("The grader scored trajectory N at X"). End the FA with the exact writer-score line: "Overall Failure Score: X.XX / 1.0".

## Failure Analysis - what the agent got wrong and why
Cover four things, in prose, organized by severity (clinical first, then administrative, then style):
1. What the agent got RIGHT - a brief competent baseline, one or two sentences, as the setup for the turn. Lead with it but keep it short. The FA stays failure-only; no standalone praise paragraph (Ahmad's override of the 06_09 "what got right" component).
2. What the agent got WRONG - the central failure as a turn: it had the contradicting evidence and failed anyway. Tie it to the golden.
3. Why it MATTERS - the clinical mechanism and the consequence. Quantify when you can. State the severity tier (a patient-safety failure is not a documentation preference).
4. The SCORE - tie the failure to the analyzed run's trajectory score and Alexander's own score. End with `Overall Failure Score: X.XX / 1.0`. That number is Alexander's score, not the trajectory score. The run distribution stays in the Status line.

Writing standards (all required, because non-physician engineers read this too):
- Be specific, not generic. Not "got the med list wrong" but "listed metformin as active despite Endocrinology holding it until creatinine returns to baseline, risking lactic acidosis."
- Name the document(s) a reviewer should open to verify.
- Separate clinical error from formatting preference; do not conflate.
- Write for a non-specialist; explain any jargon.

## Grader Analysis - how well the grader scored the work
Two short paragraphs (so the local gate passes). The structure:
- Paragraph 1, what the grader got CORRECT: name what it credited correctly and the central defect plus any secondary miss it caught. Map to the grader's own categories (the non-negotiables, the acceptable-variation boundary, the common failure modes) where natural. Affirming a sound grader IS analysis, not filler.
- Paragraph 2, what the grader got WRONG or could IMPROVE, then calibration. Give at least one concrete point: a miscalibration, a phrasing overstatement, or a distinct failure mode it should have named explicitly so it did not have to infer partial credit (label a shortfall a MISS if the grader never saw the failure, a MIS-SCORE if it saw it but the number is off). If the grader was genuinely sound, say so and still add the stricter-or-looser-reading caveat ("I would dock a full omission of a held medication harder, but the score is defensible"). For a real grader MISS (it never saw the failure), recommend a concrete rubric or failure-mode addition in Larry 3:10 form: name the missed issue, say why it matters, then "Recommend adding: ...". For a MIS-SCORE (it saw the issue but scored it wrong), recommend how the scoring guidance should be clarified. Close on calibration: the score is well placed; "a deep floor would overstate X, and a higher score would ignore Y" is an acceptable closer but does NOT replace the improvement move.

The grader RATING (Great / Good / Mediocre / Poor) is entered in the Studio field. Do NOT write it anywhere in the file, not even the Status line; the gate rejects a rating line. Tell the writer the rating separately.

WRITER'S SCORE (project guidance, 2026-06-18). Verbatim project guidance: "New Failure Analysis guidance. Please submit a score with your failure analysis about how you think the model did in your task. This score should be your own score, not the trajectory score, and will be compared against the agentic grader." Separately from the grader rating, submit your OWN score of how the model did on the task, alongside the FA: your independent 0.0 to 1.0 assessment of the model's performance, NOT the trajectory score, compared against the agentic grader. Score on the task's own logic (central failure caps low, partial credit for accurate items, no credit for refusing). It usually lands near the grader; when it diverges, say why in the GA's calibration move. The writer's score goes in the Studio score field AND inside the submitted FA field, because the Status line is internal and is not pasted into Studio. The FA must end with the exact required line: `Overall Failure Score: X.XX / 1.0`. Record it in the Status line too. It is the writer's own number, distinct from the banned grader-rating line (Great / Good / Mediocre / Poor), which never appears in the file, not even the Status line.

HUMAN OWNERSHIP. Larry's 2026-06-18 guidance says FA/GA cannot be AI-authored. Use this skill only to organize evidence and produce a scratch draft when Alexander asks. The final platform text must be read, owned, and rewritten or explicitly approved by Alexander before paste.

## Voice (FA and GA differ)
- FA voice: a physician reviewing a chart. Named drugs, labs, findings, the consequence stated. Specific and accessible.
- GA voice: a reviewer auditing the grader. Its subject is the scoring, so the grader, the score, what it caught and missed, and the failure mode to add are the right vocabulary, not bedside prose.
- Both share the Alexander discipline: short declarative sentences; no AI transitions (Furthermore, Moreover, Consequently, Notably, In addition); no scaffolding (OCR, directory listings, "the transcript shows", tool calls); name the clinical anchors.
- Short sentences, so a reader can catch a breath. One idea per sentence. Break any sentence joined by a semicolon, or by an "and" linking two clauses, into separate sentences. If you cannot say it aloud in one breath, split it. Aim for about 15 words or fewer. Not "No immunization history, administration, or review exists anywhere; the summary documents only the eye and foot exams" but "No immunization record exists anywhere in the chart. No history, no administration, no review."
- Plain clinical language, not compressed nomenclature. Write the way an attending speaks, not in stacked hyphenated tokens that read like a variable name or a rubric label. Say "only noted that the attending should decide on restart," not "added a decide-restart-versus-hold instruction." If a phrase looks like code or eval shorthand, rewrite it as speech.
- No essayistic framing or narrated grader effort. Do not announce a point with "The sharper point is", "The real issue is", or "What stands out is"; state it directly ("But the note still tells the attending to resume..."). Do not narrate the grader's mind with "labored over", "deliberated over", or "wrestled with"; say "the grader was unsure whether X counted" or "the grader read it as Y". These framings read as essay or fiction, not chart review, and are the most common residual AI-tone leak in an otherwise clean write-up.

## Gate traps (these hard-fail presubmit_task_gate.py and verify_voice.py)
- Failure-only phrasing. The both-sides check bans the literal strings "the grader credited", "it credited the", "credited the correct/useful/complete/model", "what the grader got right", and "what the model did well" anywhere in the file, including the Status line. Write "it gave appropriate credit for", "the grader correctly identified", or "it caught".
- No grader-section names. Do not write Section A/B/C; state the content.
- No grader-rating line anywhere in the file, including the Status line.
- Single-run rule (Abi 6/05). Analyze ONE run, named by its trajectory number ("On trajectory N"). Cite only that run's score and the writer's own score; do not mention other runs' scores or the distribution in the FA or GA body. The distribution lives in the Status line.
- No em dashes or en dashes. Plain hyphens and commas.
- Two paragraphs per field, no bullets, each field at or under about 1000 characters. Completeness of the components beats hitting the count, but stay under 1000 so the gate is clean.
- Self-check before handing back: run `python3 tools/verify/lint_fa_ga.py <the FA/GA file>` and clear every FAIL. It enforces this skill mechanically (opens "On trajectory N", single run only, `Overall Failure Score` line, two paragraphs, under 1000 chars, no dashes, no rating word, no banned phrases) and warns on semicolons and sentences over 24 words. Fix until it prints "clean".

## Avoid (builder and reviewer jargon)
floor, catcher, bimodal, mechanism, lane, bankable, score cap; rubric, grading framework, designed to test, additive checklist.

## Status line (metadata; carries the numbers so the prose stays clinical)
Above the two fields, record: the job id, the full score distribution, the mean, whether it is all-low or bimodal, and the FA subject (Attempt, run id, trajectory, score, with a note if it is not the strict second-lowest distinct). No rating line.

## Final checklist before handing back
FA: opens with "On trajectory N" (the 1-10 count); leads with a brief competent baseline; names the central failure as a turn; states the clinical mechanism, consequence, and severity tier; names the document(s); ends with `Overall Failure Score: X.XX / 1.0`; references only this run, never other runs' scores; failure-only.
GA: names what the grader got correct; names what it got wrong or could improve (NOT optional); judges calibration; no rating line.
Both: no section names, no banned credit phrases, no dashes, plain clinical speech, second-lowest distinct run, gates clean.
Self-check: `python3 tools/verify/lint_fa_ga.py <file>` prints "clean" (no FAILs) before you hand back.

Worked examples in `references/worked-examples.md`: the OV09 held-medication GA shows the grader-audit shape with the improvement move; the OV04 image FA/GA shows the simpler clinical form. Read them when a draft feels off-format.

## Boundaries
Draft for the writer to read and own. No submission, paste, or AutoQC without explicit authorization for that exact step. One FA/GA per task, bound to one run.
