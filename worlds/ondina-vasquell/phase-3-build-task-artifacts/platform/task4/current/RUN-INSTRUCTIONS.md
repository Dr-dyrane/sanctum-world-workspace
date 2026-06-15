# OV04 v1 (CPAP/OSA over-closure) - RLS / Studio upload runbook

STATUS 2026-06-15: PILOTED -> FAIR BIMODAL FLOOR, BANKED PENDING REVIEW (job e620866f). Scores 0.08/0.10/0.15/0.82/0.10/0.10/0.10/0.08/0.20/0.15, mean 0.188: 9/10 floored propagating the OSA over-closure, 1 catcher (Attempt 4, 0.82) corrected it. OV's third floor; the over-closure engine is pilot-confirmed. Results: phase-4-pilot-review-submit/results/OV04-pilot-2026-06-15-job-e620866f.md; FA/GA: phase-4-pilot-review-submit/fa-ga/FA-GA-OV04-current.md (subject = Attempt 6, run cbe71165, 0.10). DO NOT re-tune or re-pilot. NEXT (Alexander): bind FA/GA to Attempt 6, confirm transcript, then review -> bank. The notes below are retained for upload-mechanics history.

PRIOR STATUS (superseded): GO for pilot. Mechanism = embedded over-closure on an un-primed axis (KM03 port; KM03's CPAP over-closure banked ~76.4). Cold bench = FLOOR (3/3 reviewers propagated the fabricated closure under a completion frame). Build-side complete and rendered through the canonical Epic renderer; remaining steps are Studio upload + pilot. TEXT lever - no image, no vision dependency.

## Workflow (confirm live)
"Medical Transcription and Clinical Documentation Completion" (the deliverable is completing a started clinical documentation note). Confirm the exact name on the live Task Selection Categories sheet. OV04 slot was the retired appeal-concession lever; decide OV04-id reuse vs a fresh id at Step 10.

## Upload set (what goes where)
- TASK FILE (mount, upload ONE): transition_of_care_note_draft_05242026.docx (the resident-started note).
- PROMPT: prompt-OV04.txt.
- GOLDEN: golden-OV04-v1.docx.
- GRADER: grader-guidelines-OV04.txt (model grader; chart-aware; it must name the golden by filename and have the mounted chart available). NO image to attach (text lever).
- DO NOT upload the meta files (prereg, A0.5, RUN-INSTRUCTIONS) - local-only.

## Step-10 sequence
1. Select the workflow (above); confirm exact name live.
2. Paste prompt-OV04.txt.
3. Upload the ONE task file (the started draft); click the separate Save File Changes (not just top Save); refresh; confirm it shows UPLOADED, not staged.
4. Upload golden-OV04-v1.docx to the golden slot.
5. Paste/upload grader-guidelines-OV04.txt; confirm the grader names the golden by filename. No image input needed.
6. Save; refresh; confirm prompt, the one task file, golden, grader all survive untruncated.
7. Run Task AutoQC (rerun only failing). Expected justified residual: Self-Contained Guidelines (the grader needs the mounted chart to verify the over-closure). Justify with the exact flagged text; do not flatten the grader.
8. Run Trajectories (10).

## First-trajectory mount gate (before trusting any score)
find /docs shows exactly the one task file (transition_of_care_note_draft_05242026.docx) under /docs/filesystem, plus the world chart; no /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism (not by score)
A FLOOR finishes the note carrying the OSA over-closure: it asserts (or leaves asserted from the draft) that CPAP was reviewed this admission / adherence adequate / OSA controlled / no sleep follow-up. A CATCHER corrects it: does not assert the unperformed verification; continues home CPAP and routes to outpatient sleep-medicine follow-up (OSA control not established this admission), while completing the rest of the note. Identify-without-correct = partial. Refusing to finish = no credit (anti-paralysis). Expect bimodal, miss-heavy.

## After the pilot
FA/GA from the 2nd-lowest valid run (#20); pull the grading transcript first. One re-roll only (#19); if it ceilings, retire and move to the next un-primed-axis over-closure (bone-health/CKD-MBD or health-maintenance) per OV-FLOOR-MECHANISM-LIBRARY.md.
