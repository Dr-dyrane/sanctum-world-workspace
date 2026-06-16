# OV04 (CPAP/OSA over-closure) - RLS / Studio upload runbook

STATUS 2026-06-15 (v3, off-text CPAP-adherence finding, KM08-v7 pattern): v1 (propagation) was unfair (QA jqxv7246); v2 (disclosed-duty prompt) CEILED (job f52553ce, all 0.82-0.92). v3 retires the OSA over-closure and moves the floor OFF-TEXT: the draft OSA line is a plain true statement (continue home CPAP), the prompt reverts to plain "finish it from her chart so I can sign it" (fair via the placeholder Medications section, no telegraph), and the scored finding lives in a task-level CPAP compliance report image (poor adherence, residual AHI about 31) plus one quiet nursing breadcrumb. Floor = misses the report, calls OSA stable on home CPAP; catcher = reads it, flags undertreatment and routes sleep-medicine follow-up. Built; image generated and staged as cpap_compliance_report_05242026.jpg. Remaining: cold-bench on the built bytes, then pilot. v3 prereg: OV04-v3-pilot-preregistration.md. Earlier v1/v2 notes are SUPERSEDED.

## Task-writing step inputs (Studio, 1.1 Task Details + task fields)
- Pod: Vagus.
- Workflow: Medical Transcription and Clinical Documentation Completion (confirm exact name live).
- Created from a synthetic task base: No.
- Then prompt + task file + grader + golden (below).
- No backend flags for the writer to set. The QA Technical warning "agentic grader configured but enable_anthropic_api / model-access preflight is False" is a recurring infra FALSE POSITIVE, dispositioned at AutoQC (Step 7), not a task input you toggle.

## Upload set (what goes where)
- PROMPT (paste) prompt-OV04.txt, plain (reverted): "Dr. Renquist started Mrs. Vasquell's transition-of-care note for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart so I can sign it."
- TASK FILES (mount, upload THREE): transition_of_care_note_draft_05242026.docx (resident-started note); transfer_day_nursing_note_05242026.docx (quiet breadcrumb); cpap_compliance_report_05242026.jpg (CPAP compliance report image - carries the scored finding; generate via cpap-compliance-image-spec.md).
- GOLDEN: golden-OV04-v1.docx (v3 content; catches the adherence finding).
- GRADER: grader-guidelines-OV04.txt (model grader; chart-aware; names the golden by filename; mounted chart available; 537 words).
- DO NOT upload the meta files (prereg, A0.5, RUN-INSTRUCTIONS, cpap-compliance-image-spec.md) - local only.

## Step sequence (re-entry)
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the v3 prompt (above).
3. Upload the THREE task files: transition_of_care_note_draft_05242026.docx, transfer_day_nursing_note_05242026.docx, and cpap_compliance_report_05242026.jpg; click the separate Save File Changes (not just top Save); refresh; confirm each is UPLOADED, not staged.
4. Upload golden-OV04-v1.docx to the golden slot (unchanged).
5. Paste/upload grader-guidelines-OV04.txt; confirm it names the golden by filename.
6. Save; refresh; confirm prompt, all three task files, golden, and grader survive untruncated.
7. Run Task AutoQC (rerun only failing). Three expected residuals to DISPOSITION (not fix): (a) Self-Contained Guidelines - the grader needs the mounted chart to verify the finding; justify with the exact flagged text, do not flatten the grader. (b) Technical "agentic grader configured but enable_anthropic_api / model-access preflight is False" - recurring infra FALSE POSITIVE (KM02, KM07), not a writer-flippable flag; a short "tech issue" is often accepted (KM02), else give the substantive form (the grader returns numeric scores on the trajectories, so the warning reflects the linter's static config, outside the task definition). (c) Date / timelessness ("files dated after 07/31/2025" or "encounter after July 2025") - NOT a fail. The July-2025 cutoff governs the model's required CLINICAL KNOWLEDGE, not encounter or file dates (Instruction Doc line 1473; workspace-guardrails-lessons #15: "the knowledge cutoff is not the calendar"). Of the three independent date rules - after-world-close, no-future-vs-today (HARD), pre-July-2025 (SOFT) - only the SOFT preference is touched; 2026 dates are compliant (after snapshot, not future vs today June 2026). This task needs zero post-cutoff knowledge (A0.5 item-3). Disposition citing the shipped Healthcare_247 world and the 2026-dated reference example worlds; do NOT re-date the world ("do not reflexively redo compliant dates"). Save and verify.
8. Move to Trajectories/Taiga (this locks the fields) and run 10.

## First-trajectory mount gate (before trusting any score)
find /docs shows exactly these three OV04 task files under /docs/filesystem: transition_of_care_note_draft_05242026.docx, transfer_day_nursing_note_05242026.docx, and cpap_compliance_report_05242026.jpg. No /docs/.apps_data, no stale filename, no collision with a world file.

## Read by mechanism (not by score)
A FLOOR misses the CPAP report and treats obstructive sleep apnea as stable or controlled on home CPAP. A CATCHER reads the report, surfaces poor adherence and elevated residual apnea-hypopnea index, keeps obstructive sleep apnea open, continues home CPAP, and routes outpatient sleep-medicine follow-up for adherence and settings. Identify-without-action = partial. Refusing to finish = no credit.

## After the pilot
FA/GA from the 2nd-lowest distinct run (#20); pull the grading transcript first; two paragraphs each, no section names, no dashes, no grader-rating line. If the report is uniformly missed, make the report cleaner before re-pilot. If the task ceilings, quiet the breadcrumb or retire the lever rather than reusing the old propagation prompt.
