# Per-Task RLS Runbook (Steps 10-11+) - run this for every task, clean-first

Derived from Task 1 (KM01) lived 6/5/2026: 9 AutoQC fails on first pass, all preventable. Follow in order; each checkbox is a place Task 1 broke. CANONICAL procedure - CODEX keep in sync with playbook A2/A3/A4. Per-task working files live in task-setup/platform/taskN/.

## A. Off-clock prep (Claude builds, physician rules)
- [ ] De-hint the task's request file(s) per task-setup/step10-review-packet.md section 3. Integrity-gate every docx (EOCD + styles.xml + opens). Keep last-valid copies.
- [ ] Confirm task files DO NOT duplicate any of the 26 world files (collision = blank trajectories). Check by filename against the synced world set.
- [ ] Draft the platform prompt in clinician voice (short; scoping lives in the attached memo, not the prompt). Physician edits + owns it - prompts must be writer-authored.
- [ ] Build grader guidelines GOLDEN-ONLY from grader-guidelines-task1-v3.txt template. Required structure, in this order: (1) Task context paragraph; (2) Golden reference - name the EXACT uploaded golden filename; (3) Must be present and correct; (4) Acceptable variation; (5) Penalize for. NO A/B/C labels, NO "Non-negotiables"/weighting/classification language, varied prose (not uniform bullet openings). Fabrication + copy-forward checks anchored to the GOLDEN, never "the source documents."
- [ ] Build the golden upload docx in committed chart register (clinical-voice-lessons.md): terse, first-person dispositions ("I would defer X; the AKI is too recent"), numbered by disposition to mirror the requested deliverable, ZERO meta-commentary paragraph, break parallel "should be X unless" stacks, drop coined modifiers. Physician reads + owns the committed calls. Keep golden v1 (locked-content) + v2 (shipped) side by side for the diff.

## B. On-clock RLS entry (1.1-1.4) - SAVE AFTER EVERY STEP
- [ ] 1.1 Pod = Vagus; Workflow = correct P0/P1 from approved list; Synthetic task base = No.
- [ ] 1.2 Prompt pasted. Save.
- [ ] 1.3 Add Files -> task docx -> **click "Save File Changes" (separate from top Save Changes)** -> refresh -> confirm files show UPLOADED, not "staged for upload." (Task 1: 3 fails came from skipping this.)
- [ ] 1.4 Grading Guidelines pasted; golden UPLOADED as file (not pasted). Confirm GG names the exact uploaded golden filename.
- [ ] Top Save Changes -> refresh -> eyeball all four sections survived.

## C. Task AutoQC (2.x)
- [ ] Run Task AutoQC. Rerun N failing ONLY (never full reruns).
- [ ] Expected residual = "Self-Contained Guidelines" warning ONLY IF guidelines reach into the chart. With golden-anchored checks (step A) it should not fire. If any guideline/golden/prompt flag fires, fix per A3 - do not justify structural flags, rebuild them.
- [ ] 2.2 Notes (required even on pass): short resolution summary.
- [ ] Mark reviewed -> Run Taiga Trajectories & QA. CLOCK OFF during the run.

## D. Trajectories + Taiga QA (3-5)
- [ ] 3.1 Confirm batch has 10 completed trajectories, each with a %. Record the spread. Calibration: <70% = good stumping, >70% = maybe too easy; the number is not the verdict - read the outputs.
- [ ] Export trajectory outputs into task-setup/taskN/trajectories/vX/ + README with trap-by-trap read.
- [ ] 3.2 Trajectory AutoQC - expect pass.
- [ ] 4 Taiga QA: Fetch QC Report -> respond to EVERY Env Linter + Data Quality flag. Tech issue -> thumbs down + exactly `tech issue`. Substantive -> thumbs down + thorough professional rebuttal (client-visible). NEVER thumbs up (= go back and fix). Save each (paper-airplane) -> refresh to confirm.
- [ ] 5 Run Taiga QA Feedback AutoQC; address flags in 5.2 (copy exact line, then response).
- [ ] Verify fabrication-candidate specifics in trajectories against the 26 world files BEFORE FA.
- [ ] THEN Start Failure Analysis & Grader Analysis (never write FA/GA before clicking that button).

## E. Recurring gotchas (Task 1 receipts)
1. "Save File Changes" in 1.3 is not the same as top Save Changes. Files staged but unsaved = No Missing Files / Prompt Self-Contained / References-Only fails.
2. Grader-guideline gate wants native structure, NOT the golden-response A/B/C format. A/B/C trips No Weight Distribution + Human-Written.
3. Golden reads LLM if it has parallel modal stacks, coined modifiers, or a self-reviewing closing paragraph. Chart register fixes it.
4. Golden filename in GG must match the uploaded file exactly (v2, not v1).
5. Self-Contained warning = FIX (golden-anchor the checks), not justify. The Taiga grader grades golden-primary (instruction doc ~line 2387), it is not handed the chart.
6. Control chars can hide in source text - scan and sanitize before DOCX build.
7. On any contested QC disposition that turns on platform behavior, run a cold-context Claude pass before deciding (A4).
