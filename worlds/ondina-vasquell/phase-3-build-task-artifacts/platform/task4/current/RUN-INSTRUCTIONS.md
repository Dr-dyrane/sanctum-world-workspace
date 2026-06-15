# OV04 (CPAP/OSA over-closure) - RLS / Studio upload runbook

STATUS 2026-06-15 (v2, fairness re-pilot REQUIRED): the v1 build piloted bimodal twice (job e620866f, catcher 0.82; confirming re-pilot job 4623db0c, catcher 0.85), but QA jqxv7246 (data_quality) raised undisclosed_constraints - the OSA over-closure is pre-drafted content under a finish-only prompt (the AO/KM08 planted-claim class). Dyrane approved the prompt-disclosure fix: the PROMPT now discloses a verify-and-correct duty; golden, grader, and the started draft are UNCHANGED. v2 prereg locked (OV04-v2-pilot-preregistration.md); v1 A0.5 corrected. Because trajectory/taiga locks the editable fields after AutoQC, the prompt edit means going BACK to the task-writing step, re-running AutoQC, and re-piloting (edit-in-place on the existing OV04 task, not a fresh id). After the re-pilot: re-derive FA/GA from the new 2nd-lowest distinct run and re-read a catcher. Any earlier "do not re-pilot" note is SUPERSEDED.

## Task-writing step inputs (Studio, 1.1 Task Details + task fields)
- Pod: Vagus.
- Workflow: Medical Transcription and Clinical Documentation Completion (confirm exact name live).
- Created from a synthetic task base: No.
- Then prompt + task file + grader + golden (below).
- No backend flags for the writer to set. The QA Technical warning "agentic grader configured but enable_anthropic_api / model-access preflight is False" is a recurring infra FALSE POSITIVE, dispositioned at AutoQC (Step 7), not a task input you toggle.

## Upload set (what goes where)
- PROMPT (paste) prompt-OV04.txt, the v2 corrected text:
  "Dr. Renquist started Mrs. Vasquell's transition-of-care note for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart, and correct anything in it the record does not support, so I can sign it."
- TASK FILE (mount, upload ONE, UNCHANGED): transition_of_care_note_draft_05242026.docx (the resident-started note).
- GOLDEN (UNCHANGED): golden-OV04-v1.docx.
- GRADER (UNCHANGED): grader-guidelines-OV04.txt (model grader; chart-aware; names the golden by filename; mounted chart available). NO image (text lever).
- DO NOT upload the meta files (prereg, A0.5, RUN-INSTRUCTIONS) - local only.

## Step sequence (re-entry)
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the v2 prompt (above).
3. Upload the ONE task file (the started draft); click the separate Save File Changes (not just top Save); refresh; confirm UPLOADED, not staged.
4. Upload golden-OV04-v1.docx to the golden slot (unchanged).
5. Paste/upload grader-guidelines-OV04.txt; confirm it names the golden by filename. No image input.
6. Save; refresh; confirm prompt, the one task file, golden, grader all survive untruncated.
7. Run Task AutoQC (rerun only failing). Two expected residuals to DISPOSITION (not fix): (a) Self-Contained Guidelines - the grader needs the mounted chart to verify the over-closure; justify with the exact flagged text, do not flatten the grader. (b) Technical "agentic grader configured but enable_anthropic_api / model-access preflight is False" - recurring infra FALSE POSITIVE (KM02, KM07), not a writer-flippable flag. Disposition with a substantive, fact-referenced justification (NOT a bare "tech issue", which failed QA feedback in KM07): the agentic grader has model access at grading time and returns numeric scores on the trajectories (every OV04 pilot scored all ten, 0.10 to 0.85); the warning reflects the linter's static configuration context, outside the task definition. Save and verify.
8. Move to Trajectories/Taiga (this locks the fields) and run 10.

## First-trajectory mount gate (before trusting any score)
find /docs shows exactly the one task file (transition_of_care_note_draft_05242026.docx) under /docs/filesystem, plus the world chart; no /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism (not by score)
A FLOOR finishes the note carrying the OSA over-closure: it asserts (or leaves asserted from the draft) that CPAP was reviewed this admission / adherence adequate / OSA controlled / no sleep follow-up. A CATCHER corrects it: does not assert the unperformed verification; continues home CPAP and routes to outpatient sleep-medicine follow-up (OSA control not established this admission), while completing the rest of the note. Identify-without-correct = partial. Refusing to finish = no credit (anti-paralysis). Expect bimodal, miss-heavy, but note the disclosed duty may compress the floor.

## After the pilot
FA/GA from the 2nd-lowest distinct run (#20); pull the grading transcript first; two paragraphs each, no section names, no dashes, no grader-rating line. Stopping rule (v2): if the disclosed-duty prompt ceilings (all runs catch, meaning over-disclosed), move the over-closure into an open item the model completes (KM08 v5 placeholder route) rather than re-rolling the same prompt; if it stays bimodal with a catcher near 0.85, re-derive FA/GA and bank.
