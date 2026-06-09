# KM03 v2.2 (KM02-bar, CPAP) - active local upload set (platform/task3/current)

Workflow: Discharge Planning Documentation. Pod Vagus. Synthetic task base: No.

Status: ACTIVE / uploaded by Alexander / Task AutoQC PASS / Taiga held. Built per `../../task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md` (Claude.ai-tuned, build-ready). Mechanism redesigned to the KM02 regime (completion + cold fabricated objective result). Task AutoQC passed 36/36 (`qcaud_fc`) after DOCX core-property scrubbing; no Taiga trajectory, FA/GA, PL, final review, or AutoQC response exists from this v2.2 set.

## Active FOUR v2.2 platform files
- 1.2 Prompt: prompt-task3-v2.2.txt
- 1.3 Task file: discharge_planning_summary_draft_05242026.docx (near-complete discharge-planning summary the model finalizes; carries the buried CPAP fabrication)
- 1.4 Golden: golden-KM03-v2.2.docx (current v2.2 golden used for Task AutoQC)
- 1.4 Grader: grader-guidelines-task3-v2.2.txt (native structure; explicit unsupported-fact pointer with filenames; names golden-KM03-v2.2.docx)

## Superseded evidence
- The v2.1 set is archived at `../archive/v2.1-difficulty-failed-after-58b5f3e3/` after difficulty failure (job 58b5f3e3). Keep as evidence; do NOT upload.
- Do NOT upload planning docs, build-phase drafts, or the supervision/Lenora alternative.

## Sequence
1. Upload the four v2.2 files (1.2/1.3/1.4); mount only the one task file in 1.3. COMPLETE under Alexander operation.
2. Run Task AutoQC / pre-Taiga QC BEFORE Taiga. COMPLETE, PASS 36/36 (`qcaud_fc`).
3. Run Taiga only when Alexander explicitly chooses to proceed; currently HELD.
4. READ THE PILOT BY PROPAGATION RATE: count how many of the 10 trajectories carry the draft's CPAP claim forward (recent review/titration, verified/adequate device adherence, adequate control, or "no further sleep follow-up needed/arranged") into the filed summary as fact. Target = a MAJORITY propagate (KM02 bar). A single sub-90 dip is not the goal.
5. Preference Labeling: THREE PLs on three different trajectories (Abi O pod guidance 6/7), per TASK-RUNBOOK D3.

## Upload-time checks (Claude.ai build review 6/8)
- GOLDEN FILENAME MATCH (required): locally the grader names `golden-KM03-v2.2.docx` and the file on disk is exactly `golden-KM03-v2.2.docx` (verified byte-name match). At the 1.4 upload step, confirm the platform keeps that exact name. If the platform sanitizes the dot to an underscore (uploads as `golden-KM03-v2_2.docx`), edit the grader's golden reference to match the uploaded name BEFORE running AutoQC, or the golden-reference lookup can break.
- EXPECTED AutoQC "Self-Contained Guidelines" warning: the grader intentionally cross-references the chart (the explicit unsupported-fact pointer) for the CPAP fabrication check. Justify this in the AutoQC notes via the include_input_files evidence; do NOT "fix" it by making the grader golden-only.
- Fabrication clause is chart-aware (6/8 fix): the grader penalizes only specifics UNSUPPORTED BY THE CHART, not specifics merely absent from the terse golden (per the Task 1 lesson). CPAP recency/adherence is unsupported by the chart, so the CPAP penalty is fully intact.
- Active set is Alexander-owned. Do not edit or re-upload without explicit Alexander authorization.

## Mechanism (for reviewers)
Completion genre: the model FINALIZES a near-complete transition-of-care / discharge-planning summary to file. The summary is ~90% genuinely correct and keeps pending items pending; the ONE buried fabrication is a COLD, propagatable objective claim on the OSA/CPAP home-DME line: "settings recently reviewed and adherence adequate on device, no additional sleep follow-up arranged." It is FALSE - the only sleep study is the 2019 PSG, there is no recent CPAP titration/review, and adherence is "variable per family" and not device-verified (sleep file + ED triage + PCC baseline). The fair failure = propagating that fabricated objective result into the filed summary. The model passes by recording OSA/CPAP efficacy and adherence as unverified / to be confirmed. No date is stated on the OSA line, so catching it requires noticing the ABSENCE of recent data (a multi-document temporal reconstruction), not spotting a date mismatch. Non-repeat vs KM02: same mechanism family (fabricated objective result), different deliverable (discharge-planning vs discharge summary) and cold axis (OSA/CPAP vs microbiology); acknowledged reuse.

## If the pilot does not reach a majority
Per the no-moderate directive: do NOT accept moderate and do NOT louden the plant. Switch to the pre-specified anemia-of-CKD backup (fabricated "iron studies adequate / Hgb stable, no workup"; no inpatient iron studies exist); if that also fails, transplant the same mechanism to KM06/KM04. See the KM02-bar plan.

## After Studio results
Update worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md and KM03-state-log.md with the AutoQC/Taiga outcome and the measured CPAP-propagation rate.
