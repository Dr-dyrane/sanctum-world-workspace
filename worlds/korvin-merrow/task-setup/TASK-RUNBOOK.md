# Per-Task RLS Runbook (Steps 10-11+) - run this for every task, clean-first

Derived from Task 1 (KM01) lived 6/5/2026: 9 AutoQC fails on first pass, all preventable. Follow in order; each checkbox is a place Task 1 broke. CANONICAL procedure - CODEX keep in sync with playbook A2/A3/A4. Per-task working files live in task-setup/platform/taskN/.

## A. Off-clock prep (Claude builds, physician rules)
- [ ] De-hint the task's request file(s) per task-setup/step10-review-packet.md section 3. Integrity-gate every docx (EOCD + styles.xml + opens). Keep last-valid copies.
- [ ] Confirm task files DO NOT duplicate any of the 26 world files (collision = blank trajectories). Check by filename against the synced world set.
- [ ] Draft the platform prompt in clinician voice (short; scoping lives in the attached memo, not the prompt). Physician edits + owns it - prompts must be writer-authored.
- [ ] Build grader guidelines from grader-guidelines-task1-v4.txt template (the /docs-aware version). Required structure, in this order: (1) Task context paragraph; (2) Golden reference - name the EXACT uploaded golden filename; (3) Must be present and correct; (4) Acceptable variation; (5) Penalize for. NO A/B/C labels, NO "Non-negotiables"/weighting/classification language, varied prose (not uniform bullet openings). Fabrication check: chart-sourced specifics (the grader has /docs/filesystem/) are CORRECT, not fabrication; penalize only specifics unsupported by the chart and not derivable from the golden. Copy-forward check: framed as per-medication reasoning vs reproduced list (golden-assessable). Expect the AutoQC Self-Contained warning and JUSTIFY it with the include_input_files evidence (see gotcha 5).
- [ ] Build the golden upload docx in committed chart register (clinical-voice-lessons.md): terse, first-person dispositions ("I would defer X; the AKI is too recent"), numbered by disposition to mirror the requested deliverable, ZERO meta-commentary paragraph, break parallel "should be X unless" stacks, drop coined modifiers. Physician reads + owns the committed calls. Keep golden v1 (locked-content) + v2 (shipped) side by side for the diff.

## B. On-clock RLS entry (1.1-1.4) - SAVE AFTER EVERY STEP
- [ ] 1.1 Pod = Vagus; Workflow = correct P0/P1 from approved list; Synthetic task base = No.
- [ ] 1.2 Prompt pasted. Save.
- [ ] 1.3 Add Files -> task docx -> **click "Save File Changes" (separate from top Save Changes)** -> refresh -> confirm files show UPLOADED, not "staged for upload." (Task 1: 3 fails came from skipping this.)
- [ ] 1.4 Grading Guidelines pasted; golden UPLOADED as file (not pasted). Confirm GG names the exact uploaded golden filename.
- [ ] Top Save Changes -> refresh -> eyeball all four sections survived.

## C. Task AutoQC (2.x)
- [ ] Run Task AutoQC. Rerun N failing ONLY (never full reruns).
- [ ] Expected residual = "Self-Contained Guidelines" warning (the /docs-aware fabrication check intentionally references the chart). JUSTIFY it in 2.2 with the include_input_files evidence - do not fix to golden-only (that mis-fires the fabrication check, per Taiga EL-2). If "No Weight Distribution" recurs despite no numeric weights and the native required sections passing, treat it as a variance/misfire only after checking the exact language; do not remove multi-path-defensibility language just to chase a clean board. Other structural guideline/golden/prompt flags: rebuild per A3, do not justify.
- [ ] 2.2 Notes (required even on pass): short resolution summary.
- [ ] Mark reviewed -> Run Taiga Trajectories & QA. CLOCK OFF during the run.

## D. Trajectories + Taiga QA (3-5)
- [ ] 3.1 Confirm batch has 10 completed trajectories, each with a %. Record the spread. Calibration: <70% = good stumping, >70% = maybe too easy; the number is not the verdict - read the outputs.
- [ ] Export trajectory outputs into task-setup/taskN/trajectories/vX/ + README with trap-by-trap read.
- [ ] 3.2 Trajectory AutoQC - expect pass.
- [ ] 4 Taiga QA: Fetch QC Report -> respond to EVERY Env Linter + Data Quality flag. Tech issue -> thumbs down + exactly `tech issue` (Task 1 recurring example: `enable_anthropic_api`). Substantive -> thumbs down + thorough professional rebuttal (client-visible). NEVER thumbs up (= go back and fix). Save each (paper-airplane) -> refresh to confirm.
- [ ] 5 Run Taiga QA Feedback AutoQC; address flags in 5.2 (copy exact line, then response).
- [ ] Pull/read the grading transcript for low-scoring trajectories before FA/GA; do not infer failure mode from trajectory prose alone. Task 1 receipt: the apparent 0.78 "underscore" became a true metformin-omission finding once transcripts were read.
- [ ] Verify fabrication-candidate specifics in trajectories against the 26 world files BEFORE FA.
- [ ] THEN Start Failure Analysis & Grader Analysis (never write FA/GA before clicking that button).

## D2. Failure Analysis & Grader Analysis (Task 1 lessons)
- [ ] Pull the GRADING TRANSCRIPT for each low run BEFORE writing GA. Do not infer the failure mode from the output alone (Task 1: working-draft guessed 4 wrong failure modes; real miss was a single dropped medication, only visible in the transcript).
- [ ] Grep low-run vs a high-run output for each golden-required medication/element to find the discriminator fast.
- [ ] FA is a single task-level field (10k char). GA is PER-TRAJECTORY: rate Poor/Fair/Good/Great + Explanation, and you can rate "Great" when the grader did real chart verification and caught a genuine miss (affirming a correct grader IS the analysis).
- [ ] FA/GA = physician-authored, chart-register voice, FIRST PERSON where natural, NO em dashes (hyphens/periods only).
- [ ] A "too easy" mean (no sub-70) is not automatically weak - if the SPREAD tracks a real clinical competency (Task 1: medication-coverage completeness), the task discriminates and is worth keeping. Concentrate hard stumping in the synthesis tasks (KM04, KM06).
- [ ] Add the physician calibration line the grader cannot self-assess (e.g. is the deduction size fair for the error's real-world severity).
- [ ] FA/GA AutoQC expected residual: "Human-Written (Grader Analysis)" fires as a FALSE POSITIVE because the check reads the AGENTIC GRADER's transcripts (grader_type: model, "Selected Grader: model"), which are machine-generated by design ("all 20 trajectories," rubric headers, emoji, "Let me evaluate against the grading criteria"). That is NOT the writer's GA. JUSTIFY, do not rerun (it's substantive text, not variance; rerun reproduces). Reusable justify text banked in Task 1 7.2 notes + task1/FA-GA-final.md. Expect it every task that uses the model grader.

## E. Recurring gotchas (Task 1 receipts)
1. "Save File Changes" in 1.3 is not the same as top Save Changes. Files staged but unsaved = No Missing Files / Prompt Self-Contained / References-Only fails.
2. Grader-guideline gate wants native structure, NOT the golden-response A/B/C format. A/B/C trips No Weight Distribution + Human-Written.
3. Golden reads LLM if it has parallel modal stacks, coined modifiers, or a self-reviewing closing paragraph. Chart register fixes it.
4. Golden filename in GG must match the uploaded file exactly (v2, not v1).
5. CORRECTED 6/5 (Taiga EL-2 evidence): the Taiga grader IS handed the chart - include_input_files=true mounts /docs/filesystem/ with all source files (confirmed in grader transcripts). So write the fabrication + copy-forward checks to CROSS-CHECK /docs (chart-sourced specifics are correct, not fabrication), and JUSTIFY the AutoQC "Self-Contained Guidelines" warning with the include_input_files evidence rather than fixing to golden-only. Golden-only anchoring is factually wrong here and mis-fires the fabrication check on legitimate chart specifics (the low-detail golden contains none of them). Build Tasks 2-6 guidance from grader-guidelines-task1-v4.txt (the /docs-aware version), NOT v3.
6. Control chars can hide in source text - scan and sanitize before DOCX build.
7. On any contested QC disposition that turns on platform behavior, run a cold-context Claude pass before deciding (A4).
8. No Weight Distribution can variance-misfire. If the guideline has no numeric weights, preserves the platform's native sections, and the companion structure checks pass, justify rather than flattening clinically useful acceptable-variation language.
