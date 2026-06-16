# OV05 (off-text med-reconciliation finding via home-med-bottle photo) - RLS / Studio upload runbook

STATUS 2026-06-16: RETIRED - CEILINGED at pilot (job eb1665ba, 0.88-0.95, 10/10 caught the ibuprofen). DO NOT re-pilot. Cause: the medication-reconciliation genre PRIMES the model to examine every med source, so the bottle photo was not off-text (the model OCR'd it hard every run). Files retained for history; slot task5 reopens for a distinct-structure against-the-grain lever (#5 offloading). See results/OV05-v1-pilot-2026-06-15-job-eb1665ba.md and OV-FLOOR-MECHANISM-LIBRARY section 6. (Original build note kept below for history.)
STATUS 2026-06-15: BUILT, gates green (verify_ondina + presubmit task5), image in mount. Mechanism = off-text finding, reusing the proven OV04-v3 / KM08-v7 engine: a started SNF transfer medication reconciliation lists the EMR-verified home meds (no ibuprofen) and leaves the discrepancy + verification sections open; a task-level home-medication-bottle photo (the daughter brought the bottles) shows an OTC ibuprofen NOT on the list - a nephrotoxin in AKI on CKD (chart: NSAIDs avoided). Plain prompt; fair via construction (the bottles are a real source a reconciliation must use). FLOOR = reconcile off the EMR list, never open the photo; CATCHER = open it, catch and stop the ibuprofen. Cold design-bench = plausibly bimodal (OV04-v3 shape). NEXT: pilot 10, then FA/GA from the 2nd-lowest distinct run + catcher read.

## Task-writing step inputs (Studio, 1.1 Task Details + task fields)
- Pod: Vagus.
- Workflow: Medical Transcription and Clinical Documentation Completion (confirm exact name live).
- Created from a synthetic task base: No.
- No backend flags for the writer to set.

## Upload set (what goes where)
- PROMPT (paste) prompt-OV05.txt: "Dr. Renquist started Mrs. Vasquell's medication reconciliation for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart so I can sign it."
- TASK FILES (mount, upload THREE): medication_reconciliation_snf_transfer_draft_05242026.docx (started deliverable); transfer_day_nursing_note_05242026.docx (quiet breadcrumb); home_medication_bottles_05242026.jpg (the photo - carries the scored finding).
- GOLDEN: golden-OV05-v1.docx (captures and stops the unlisted ibuprofen).
- GRADER: grader-guidelines-OV05.txt (model grader; chart-aware; names the golden by filename; 540 words).
- DO NOT upload the meta files (prereg, A0.5, abi-mode-review, med-bottle-image-spec, RUN-INSTRUCTIONS) - local only.

## Step sequence
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the prompt.
3. Upload the THREE task files; click the separate Save File Changes (not just top Save); refresh; confirm UPLOADED, not staged.
4. Upload golden-OV05-v1.docx to the golden slot.
5. Paste/upload grader-guidelines-OV05.txt; confirm it names the golden by filename. No backend flag to set.
6. Save; refresh; confirm prompt, the three task files, golden, and grader survive untruncated.
7. Run Task AutoQC (rerun only failing). Three expected residuals to DISPOSITION (not fix): (a) Self-Contained Guidelines - the grader needs the mounted chart to verify the finding; justify with the exact flagged text, do not flatten the grader. (b) Technical "agentic grader configured but enable_anthropic_api / model-access preflight is False" - recurring infra FALSE POSITIVE (KM02, KM07); a short "tech issue" is often accepted, else the substantive form (the grader returns numeric scores on the trajectories, so it is the linter's static config, outside the task definition). (c) Date / timelessness ("files/narrative dated after 07/31/2025") - NOT a fail; the July-2025 cutoff governs the model's required CLINICAL KNOWLEDGE, not encounter/file dates (Instruction Doc line 1473; workspace-guardrails-lessons #15 "the knowledge cutoff is not the calendar"); 2026 dates are compliant; do NOT re-date. (Full disposition text in OV04 RUN-INSTRUCTIONS Step 7.)
8. Move to Trajectories/Taiga (this locks the fields) and run 10.

## First-trajectory mount gate (before trusting any score)
find /docs shows exactly these three OV05 task files under /docs/filesystem: medication_reconciliation_snf_transfer_draft_05242026.docx, transfer_day_nursing_note_05242026.docx, and home_medication_bottles_05242026.jpg. No /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism (not by score)
A FLOOR finalizes the reconciliation from the EMR home list and never opens the bottle photo, so it misses the unlisted OTC ibuprofen and states or implies no NSAID use. A CATCHER opens the photo, identifies the ibuprofen that is not on the list, and stops it as a nephrotoxin in AKI on CKD (continue acetaminophen for pain). Identify-without-stop = partial. Refusing to finish = no credit (anti-paralysis). Expect bimodal, miss-heavy.

## After the pilot
FA/GA from the 2nd-lowest distinct run (DO-NOT-REPEAT #20, King P 6/14); pull the grading transcript first; failure-only; two paragraphs each; no grader-rating line; bind to the selected run in Studio. Catcher read: confirm a high run genuinely opened the photo and caught the ibuprofen (not a spurious high score). Grader-rating field: Great if it independently verified (checked whether the model opened the image) and caught the real miss; otherwise Good. Then bank (clears Abi lens 7 if bimodal with a catcher).
