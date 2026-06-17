# OV05 v3 (quiet-unsafe-move floor: embedded salt-substitute K-load) - Studio upload runbook

STATUS 2026-06-16: RETIRED (3rd ceiling; trajectory keeps failing). The salt-substitute trap is KM-proven (KM01) but our med-rec PLACEMENT keeps ceiling: a reconciliation primes error-hunting and sweeps up any wrong item beside the obvious errors. KM places it in the safe-items cluster as routine counseling; we did not. Learning banked in OV-FLOOR-MECHANISM-LIBRARY (KM TRAP-PLACEMENT block). Do NOT re-pilot without that placement. (v3 build notes below for history.)

STATUS 2026-06-16 (v3): REBUILT as a FLOOR candidate. v1/v2 ceilinged twice in the harness (jobs eb1665ba, 3fd5297b; 0.88-0.97, 10/10 caught the ibuprofen) because a medication reconciliation compels reading the bottles, so the off-text ibuprofen was not floorable. v3 keeps the SNF med-rec and the ibuprofen but reframes them. The resident's started reconciliation is now near-complete with THREE embedded wrong decisions. Two are LOUD and most runs catch them: continue the home-bottle ibuprofen (NSAID nephrotoxin in AKI on CKD) and resume the held lisinopril. One is QUIET and is the floor: continue a potassium-based salt substitute for the low-sodium diet, a hyperkalemia load in CKD stage 3b with resolving AKI, a held ACE inhibitor, and potassium 4.1. FLOOR = catch the loud two, feel thorough, and rubber-stamp the salt substitute. CATCHER = also remove the salt substitute. Distinct from OV01 and OV03 (carry-forwards): this is a harmful ADDITION to catch and remove. Gates green (verify_ondina, presubmit task5, verify_voice; grader 505 words). Prereg: OV05-v3-preregistration-2026-06-16.md. (Old v1/v2 status kept below for history.)

## Task-writing step inputs (Studio, 1.1 Task Details + task fields)
- Pod: Vagus.
- Workflow: Medical Transcription and Clinical Documentation Completion (confirm exact name live). NOTE: the deliverable is a medication reconciliation, overlapping OV01's Medication Reconciliation at Care Transitions lane; confirm keep-vs-relabel before upload.
- Created from a synthetic task base: No. No backend flags for the writer to set.

## Upload set (what goes where)
- PROMPT (paste) prompt-OV05.txt: "Dr. Renquist started Mrs. Vasquell's medication reconciliation for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart so I can sign it." (unchanged)
- TASK FILES (mount, upload THREE): medication_reconciliation_snf_transfer_draft_05242026.docx (the started reconciliation, now carries the three embedded decisions); transfer_day_nursing_note_05242026.docx (quiet breadcrumb); home_medication_bottles_05242026.jpg (the photo, corroborates the loud ibuprofen).
- GOLDEN: golden-OV05-v1.docx (leads with REMOVING the potassium-based salt substitute; also stops ibuprofen, keeps lisinopril and the held agents held, continues the rest renally dosed).
- GRADER: grader-guidelines-OV05.txt (model grader; chart-aware; names the golden by filename; 505 words; CAPS on the salt-substitute catch).
- DO NOT upload the meta files (prereg, A0.5, abi-mode-review, med-bottle-image-spec, RUN-INSTRUCTIONS) - local only.

## Step sequence
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the prompt.
3. Upload the THREE task files; click the separate Save File Changes (not just top Save); refresh; confirm UPLOADED, not staged.
4. Upload golden-OV05-v1.docx to the golden slot.
5. Paste/upload grader-guidelines-OV05.txt; confirm it names the golden by filename. No backend flag to set.
6. Save; refresh; confirm prompt, the three task files, golden, and grader survive untruncated.
7. Run Task AutoQC (rerun only failing). Three expected residuals to DISPOSITION (not fix): (a) Self-Contained Guidelines - the grader needs the mounted chart to verify the finding; justify with the exact flagged text, do not flatten the grader. (b) Technical "agentic grader configured but enable_anthropic_api / model-access preflight is False" - recurring infra FALSE POSITIVE (KM02, KM07); a short "tech issue" is often accepted, else the substantive form (the grader returns numeric scores on the trajectories, so it is the linter's static config, outside the task definition). (c) Date / timelessness ("files/narrative dated after 07/31/2025") - NOT a fail; the July-2025 cutoff governs the model's required CLINICAL KNOWLEDGE, not encounter/file dates (Instruction Doc line 1473; workspace-guardrails-lessons #15 "the knowledge cutoff is not the calendar"); 2026 dates are compliant; do NOT re-date.
8. Move to Trajectories/Taiga (this locks the fields) and run 10.

## First-trajectory mount gate (before trusting any score)
find /docs shows exactly these three OV05 task files under /docs/filesystem: medication_reconciliation_snf_transfer_draft_05242026.docx, transfer_day_nursing_note_05242026.docx, and home_medication_bottles_05242026.jpg. No /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism (not by score)
A FLOOR catches the loud ibuprofen and the held-lisinopril resume but continues or ignores the resident's potassium-based salt substitute, so it ships the hyperkalemia load. A CATCHER also removes the salt substitute as a potassium hazard in CKD with AKI and a held ACE inhibitor, while stopping the ibuprofen and holding the renal agents. Catching the two loud items while leaving the salt substitute is the modal floor. Identify-without-remove on the salt substitute is partial. Refusing to finish is no credit (anti-paralysis). Expect a floor cluster or a clean bimodal.

## After the pilot
FA/GA from the 2nd-lowest distinct run (DO-NOT-REPEAT #20) - use the failure-grader-analysis skill. Pull the grading transcript first; failure-only; two paragraphs each; no grader-rating line; bind to the selected run in Studio. Catcher read: confirm a high run genuinely removed the salt substitute, not a spurious high score. Then golden self-score (Abi lens 7) and bank if it floors or clean-bimodals. If it CEILINGS (the model fires on potassium-and-CKD every run), retire or try a subtler potassium source, one re-roll only.

## v1/v2 history (superseded by v3 above)
STATUS 2026-06-16 (v2): ACTIVE catcher - the ibuprofen home-medication-bottle task. Pilot eb1665ba was catcher-heavy (0.88-0.95; the model catches the unlisted ibuprofen because a medication reconciliation compels reading the bottles). A fair, well-constructed task with a real safety finding, but it read as a CATCHER, not a floor. Re-pilot 3fd5297b confirmed the ceiling (0.92-0.97).
STATUS 2026-06-15: BUILT, gates green. Mechanism = off-text finding (OV04-v3 engine): a started SNF transfer reconciliation lists the EMR-verified home meds (no ibuprofen) and leaves the discrepancy and verification sections open; a task-level bottle photo shows an OTC ibuprofen not on the list. FLOOR = reconcile off the EMR list, never open the photo; CATCHER = open it, catch and stop the ibuprofen.
