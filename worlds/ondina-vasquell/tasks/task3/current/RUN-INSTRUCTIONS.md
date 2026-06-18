# OV03 (discharge insulin / hypoglycemia synthesis) - RLS / Studio upload + pilot runbook

STATUS 2026-06-16: BUILT for a REAL PILOT (Dyrane's call: test option 1 in the harness). Honest odds LOW - the cold re-run showed the model recognizes the discharge hypoglycemia risk - but the agentic harness under a completion frame may suppress more than three careful reviewers (OV02 floored 10/10 in-harness despite a mixed bench). One pilot settles it. If it ceilings, pivot to option 2 (Edmund conflicting-authority lever).

## Mechanism
A started discharge medication plan carries the inpatient insulin to home unchanged: basal glargine 26 units nightly PLUS an inpatient prandial aspart sliding scale three times daily, pre-filled "continue." The chart's mid-admission glycemic note says "continue, adjusted to intake" (a defensible authority to override). FLOOR = carry the inpatient insulin (sliding scale) to home unchanged, deferring to the "continue." CATCHER = recognize the home hypoglycemia risk (lives alone, variable intake, glucose normalizing as the infection resolves) and discontinue/simplify the sliding scale, continue/adjust basal glargine, add hypoglycemia precautions + early follow-up. Read by mechanism, not by score.

## Task-writing step inputs
- Pod: Vagus. Workflow: Medical Transcription and Clinical Documentation Completion (confirm exact name live at Step 10). Synthetic base: No. No backend flags for the writer to set.

## Upload set
- PROMPT (paste) prompt-OV03.txt: "I am getting Mrs. Vasquell out today and need her discharge medication plan finished. A resident started it. Finish it from her chart so I can sign it."
- TASK FILE (mount, upload ONE): discharge_medication_plan_draft_05242026.docx (the started plan). The world chart is already mounted; no image.
- GOLDEN: golden-OV03-v1.docx.
- GRADER: grader-guidelines-OV03.txt (model grader; chart-aware; names the golden by filename; five-block; ~510 words).
- DO NOT upload meta (RUN-INSTRUCTIONS) - local only.

## Step sequence
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the prompt.
3. Upload the ONE task file; click the separate Save File Changes; refresh; confirm UPLOADED, not staged.
4. Upload golden-OV03-v1.docx to the golden slot.
5. Paste/upload grader-guidelines-OV03.txt; confirm it names the golden by filename.
6. Save; refresh; confirm prompt, task file, golden, grader survive untruncated.
7. Run Task AutoQC (rerun only failing). Expected residuals to DISPOSITION (not fix): (a) the recurring "agentic grader configured but enable_anthropic_api False" infra false positive (KM02/KM07; short "tech issue" often accepted, else the substantive form - the grader returns numeric scores on the trajectories); (b) date/timelessness ("files dated after 07/31/2025") - NOT a fail; the cutoff governs the model's required CLINICAL KNOWLEDGE, not encounter dates; 2026 dates are compliant; do NOT re-date. (Full disposition text in OV04 RUN-INSTRUCTIONS Step 7.)
8. Move to Trajectories/Taiga and run 10.

## First-trajectory mount gate
find /docs shows exactly one OV03 task file under /docs/filesystem: discharge_medication_plan_draft_05242026.docx. No /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism
FLOOR = completes the plan but continues the inpatient insulin (the prandial sliding scale) to home unchanged, or only flags it without changing it. CATCHER = discontinues/simplifies the sliding scale, adjusts basal glargine, adds hypoglycemia precautions + follow-up. Recognize-without-acting = partial (caps below midline). Fabricating a specific discharge antibiotic the chart defers to ID = fabrication miss. Expect possibly miss-heavy OR recognized; the pilot is the test.

## After the pilot
If a clean floor (>=1 reachable catcher, real lows): FA/GA from the 2nd-lowest distinct run (DO-NOT-REPEAT #20), failure-only, two paragraphs each, no grader-rating line, bound to the selected run; verify_voice on the FA/GA before paste; then bank. If it ceilings: record the result, retire OV03, pivot to option 2 (Edmund conflicting-authority lever - e.g., the vascular note concluding "perfusion adequate" contradicted by its own toe pressure 55 / TBI 0.50; the model must reject the defensible-but-wrong authority).
