# platform/task2 - paste-ready KM02 set for RLS Studio

KM02 = Hospital Discharge Summary Generation. These are the Task 2 platform-prep artifacts. Codex gate (6/6): golden v5 PASSED (identity band, comorbidities, culture/antibiotic, DOCX integrity, render). Grader and mounted draft cleaned of meta per Codex's holds. Clean pilot completed and was too easy: 10 trajectories scored 92-97, mean about 94.4, no true failure mode.

## CLEAN PILOT set (completed; historical baseline)
- prompt-task2.txt - paste into the prompt field (1.2). Pure clinician-voice body.
- golden-KM02-v5.docx - UPLOAD as the golden file (1.4), do not paste.
- grader-guidelines-task2.txt - paste into Grading Guidelines (1.4). Native structure (Task context / Golden reference / Must be present and correct / Acceptable variation / Penalize for), names golden-KM02-v5.docx, no weights or score bands, meta stripped.

The clean pilot ran with NO mounted task file (FI-T02 is un-mountable; it names the trap structure). Result: 92-97, mean about 94.4, no true penalties, no culture/disposition fabrication. Evidence: ../../task2/pilot-run-clean/ and ../../task2/KM02-pilot-failure-analysis.md.

## CURRENT NEXT SET: escalation
- escalation/prompt-task2-escalation.txt - replace the clean prompt.
- escalation/discharge_summary_draft_incomplete_05242026.docx - mount as the task file.
- Golden and grader stay unchanged: golden-KM02-v5.docx + grader-guidelines-task2.txt.
- escalation/README.md - current run instructions and fairness guardrail.

The older hold/discharge_summary_draft_incomplete.md remains the markdown extraction of the colleague draft. Use the DOCX in escalation/ for the platform run.

## RLS entry order (per TASK-RUNBOOK section B; SAVE AFTER EVERY STEP)
1.1 Pod = Vagus; Workflow = Hospital Discharge Summary Generation; Synthetic task base = No.
1.2 Clean pilot used prompt-task2.txt and is complete. Escalation: replace with escalation/prompt-task2-escalation.txt. Save.
1.3 Escalation: add escalation/discharge_summary_draft_incomplete_05242026.docx and click Save File Changes. Refresh and confirm uploaded.
1.4 Paste grader-guidelines-task2.txt; UPLOAD golden-KM02-v5.docx as a file (not pasted); confirm the grader names the exact uploaded golden filename. Top Save Changes, refresh, eyeball all sections.
2.x Run Task AutoQC. Rerun N failing ONCE before justifying (No Weight / No Formatting are often variance). 2.2 Notes even on pass.
3-5 Trajectories + Taiga QA per runbook.

## Change log
- Task AutoQC 2.1 fix (footer meta-language): "Meta-Language and Content Hygiene" flagged the "Synthetic training document" footer token. Resolved on the GOLDEN ONLY by stripping the token (footer now "Mercy Vale Regional Medical Center | Hospital Discharge Summary"); golden keeps the v5 filename, content otherwise unchanged and verified intact. Task AutoQC then PASSED (qcaud_36, 350). The WORLD is built and finalized and was NOT changed: the 6 world docx that carry the same footer are left exactly as built (live hashes unchanged), and the golden-only fix was sufficient for the pass. The builder (tools/generate_reference_files.py) was fixed so future goldens carry no synthetic footer. Do NOT re-open or re-sync the finalized world for this; if a reviewer ever requires the world footers changed, that is a pod-lead/EPM decision, not a task-level edit.

## Note for the final gate
The golden storyboard date label is plain "Date" (value 05/24/2026, fixed 6/7 per first review; matches the escalation in-world today and the mounted draft), which satisfies Abi's no-"Date / Anchor" rule. The runbook suggests "Date of Service"; if a reviewer prefers that exact wording it is a one-line builder change. Not blocking.

6/7 reseed note: the LIVE task uses escalation/prompt-task2-escalation.txt (in-world today = 05/24, finish-my-draft framing). The clean-pilot prompt was moved to hold/prompt-task2-CLEAN-SUPERSEDED.txt so it cannot be grabbed by mistake during re-upload. Golden re-dated to 05/24/2026 (sha 2dd3e0adb903).
