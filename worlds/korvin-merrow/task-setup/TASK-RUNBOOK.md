# Per-Task RLS Runbook (Steps 10-11+) - run this for every task, clean-first

Derived from Task 1 (KM01) lived 6/5-6/6/2026: AutoQC setup failures, Taiga rerun lessons, and Abi's first human review. Follow in order; each checkbox is a place Task 1 broke. CANONICAL procedure - CODEX keep in sync with playbook A2/A3/A4/A5 and `worlds/korvin-merrow/task-setup/reviews/task1-first-human-review-ao-2026-06-05.md`. Per-task working files live in task-setup/platform/taskN/.

GOVERNING PRINCIPLE: docs/reasoning-discipline.md (the verification gate). At every one-way door (expensive/irreversible commit) or any claim about WHY a system behaved a certain way, read the ground truth (config/transcript/output) BEFORE committing; state verified vs inferred. Stay fast everywhere else. Most of this runbook's "expected residual / justify vs fix" calls ARE one-way doors - verify first.

## A. Off-clock prep (Claude builds, physician rules)
- [ ] Decide whether task-context files are truly needed. They must frame the task, not teach the answer. Delete or avoid any file that tells the model step-by-step how to complete the deliverable.
- [ ] If task files are used, de-hint them per task-setup/step10-review-packet.md section 3 and run a realism scan: correct task date/anchor in every location, no "date/anchor" or "discharge anchor" project artifacts, realistic author/signature, no architecture/trap/source-package language, and no duplicate answer scaffolding. Integrity-gate every docx (EOCD + styles.xml + opens). Keep last-valid copies.
- [ ] Confirm task files DO NOT duplicate any of the 26 world files (collision = blank trajectories). Check by filename against the synced world set.
- [ ] Draft the platform prompt in clinician voice (short; scoping lives in the attached memo, not the prompt). Physician edits + owns it - prompts must be writer-authored.
- [ ] Build grader guidelines from grader-guidelines-task1-v5.txt template (mechanism-agnostic). Required structure, in this order: (1) Task context paragraph; (2) Golden reference - name the EXACT uploaded golden filename; (3) Must be present and correct; (4) Acceptable variation; (5) Penalize for. NO A/B/C labels, NO "Non-negotiables"/weighting/classification language, varied prose (not uniform bullet openings). Do not tell the grader whether or how to read `/docs`; judge output against the golden and grader guidelines.
- [ ] Build the golden upload docx in committed chart register (clinical-voice-lessons.md): terse, first-person dispositions ("I would defer X; the AKI is too recent"), numbered by disposition to mirror the requested deliverable, ZERO meta-commentary paragraph, break parallel "should be X unless" stacks, drop coined modifiers. Also make it look like the requested clinical deliverable: patient name, DOB, MRN/identifier when available, allergies, date, and appropriate signature block. Physician reads + owns the committed calls. Keep golden versions side by side for provenance.

## B. On-clock RLS entry (1.1-1.4) - SAVE AFTER EVERY STEP
- [ ] 1.1 Pod = Vagus; Workflow = correct P0/P1 from approved list; Synthetic task base = No.
- [ ] 1.2 Prompt pasted. Save.
- [ ] 1.3 Add Files -> task docx -> **click "Save File Changes" (separate from top Save Changes)** -> refresh -> confirm files show UPLOADED, not "staged for upload." (Task 1: 3 fails came from skipping this.)
- [ ] 1.4 Grading Guidelines pasted; golden UPLOADED as file (not pasted). Confirm GG names the exact uploaded golden filename.
- [ ] Top Save Changes -> refresh -> eyeball all four sections survived.

## C. Task AutoQC (2.x)
- [ ] Run Task AutoQC. Rerun N failing ONLY (never full reruns).
- [ ] Do not assume an expected residual. If "Self-Contained Guidelines" appears, read the exact flagged text and the current grader-guideline wording first. Keep reviewer-facing guidance mechanism-agnostic unless an AutoQC response specifically requires verified platform-mechanism evidence. If "No Weight Distribution" recurs despite no numeric weights and the native required sections passing, treat it as a variance/misfire only after checking the exact language; do not remove multi-path-defensibility language just to chase a clean board. Other structural guideline/golden/prompt flags: rebuild per A3, do not justify.
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
- [ ] Pull the GRADING TRANSCRIPT for the single lowest run BEFORE writing FA/GA. Do not infer the failure mode from the output alone.
- [ ] Grep the lowest-run output against the golden-required elements to find the discriminator fast. Use other runs only as internal calibration, not as the FA/GA subject.
- [ ] FA analyzes ONE run only: 2-3 sentences on what the model failed and 2-3 sentences on what the model did well.
- [ ] GA analyzes ONE run only: 2-3 sentences on what the grader got right when scoring the model output against the golden and grader guidelines, and 2-3 sentences on what it got wrong. Do not say "the grader went into the chart" in reviewer-facing GA.
- [ ] FA/GA = physician-authored, chart-register voice, FIRST PERSON where natural, NO em dashes (hyphens/periods only).
- [ ] A "too easy" mean (no sub-70) is not automatically weak - if the SPREAD tracks a real clinical competency (Task 1: medication-coverage completeness), the task discriminates and is worth keeping. Concentrate hard stumping in the synthesis tasks (KM04, KM06).
- [ ] Add a physician calibration line only if it helps the single-run review. It is optional, not a blocker.
- [ ] FA/GA AutoQC expected residual: "Human-Written (Grader Analysis)" fires as a FALSE POSITIVE because the check reads the AGENTIC GRADER's transcripts (grader_type: model, "Selected Grader: model"), which are machine-generated by design ("all 20 trajectories," rubric headers, emoji, "Let me evaluate against the grading criteria"). That is NOT the writer's GA. JUSTIFY, do not rerun (it's substantive text, not variance; rerun reproduces). Reusable justify text banked in Task 1 7.2 notes + task1/FA-GA-final.md. Expect it every task that uses the model grader.

## E. Recurring gotchas (Task 1 receipts)
1. "Save File Changes" in 1.3 is not the same as top Save Changes. Files staged but unsaved = No Missing Files / Prompt Self-Contained / References-Only fails.
2. Grader-guideline gate wants native structure, NOT the golden-response A/B/C format. A/B/C trips No Weight Distribution + Human-Written.
3. Golden reads LLM if it has parallel modal stacks, coined modifiers, or a self-reviewing closing paragraph. Chart register fixes it.
4. Golden filename in GG must match the uploaded file exactly (v2, not v1).
5. CORRECTED 6/6 after Abi review + transcript reconciliation: chart access may exist in the grader container, but reviewer-facing grader guidance and GA should be MECHANISM-AGNOSTIC. Do not instruct the grader to cross-check `/docs` unless a specific AutoQC dispute requires verified platform-mechanism evidence. Build Tasks 2-6 guidance from grader-guidelines-task1-v5.txt, NOT v3 or v4.
6. Control chars can hide in source text - scan and sanitize before DOCX build.
7. On any contested QC disposition that turns on platform behavior, read the primary transcript/config first, then use a cold-context Claude pass if useful.
8. No Weight Distribution can variance-misfire. If the guideline has no numeric weights, preserves the platform's native sections, and the companion structure checks pass, justify rather than flattening clinically useful acceptable-variation language.
9. Human review beats local optimism. Do not start Tasks 2-6 from Task 1 until Task 1's human-review pattern is resolved.
