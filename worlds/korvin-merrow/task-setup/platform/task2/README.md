# platform/task2 - paste-ready KM02 set for RLS Studio

KM02 = Hospital Discharge Summary Generation. These are the live, platform-ready artifacts. Codex gate (6/6): golden v5 PASSED (identity band, comorbidities, culture/antibiotic, DOCX integrity, render). Grader and mounted draft cleaned of meta per Codex's holds.

## CLEAN PILOT set (use these three; NO task file)
- prompt-task2.txt - paste into the prompt field (1.2). Pure clinician-voice body.
- golden-KM02-v5.docx - UPLOAD as the golden file (1.4), do not paste.
- grader-guidelines-task2.txt - paste into Grading Guidelines (1.4). Native structure (Task context / Golden reference / Must be present and correct / Acceptable variation / Penalize for), names golden-KM02-v5.docx, no weights or score bands, meta stripped.

The clean pilot runs with NO mounted task file (FI-T02 is un-mountable; it names the trap structure). Expect the clean run to land high (~80-85%) because the chart coaches openness from three directions.

## HOLD (escalation only - do not mount for the clean pilot)
- hold/discharge_summary_draft_incomplete.md - the colleague-draft, clinical-only (meta split out). Mount this ONLY if the clean pilot confirms it is needed to reach the difficulty target, and render it to docx first (clinical-note style). It plants airtight snapshot-silent closures (finalized E. coli culture, culture-directed de-escalation, infection "resolved", accomplished home disposition); a run that propagates them fails, a run that corrects them to the record passes. Full rationale + prompt variant: ../../task2/colleague-draft-KM02.md.

## RLS entry order (per TASK-RUNBOOK section B; SAVE AFTER EVERY STEP)
1.1 Pod = Vagus; Workflow = Hospital Discharge Summary Generation; Synthetic task base = No.
1.2 Paste prompt-task2.txt. Save.
1.3 Clean pilot: add NO task file. (Skip; the clean run has no mounted file.)
1.4 Paste grader-guidelines-task2.txt; UPLOAD golden-KM02-v5.docx as a file (not pasted); confirm the grader names the exact uploaded golden filename. Top Save Changes, refresh, eyeball all sections.
2.x Run Task AutoQC. Rerun N failing ONCE before justifying (No Weight / No Formatting are often variance). 2.2 Notes even on pass.
3-5 Trajectories + Taiga QA per runbook.

## Change log
- Task AutoQC 2.1 fix (footer meta-language): "Meta-Language and Content Hygiene" flagged the "Synthetic training document" footer token. Resolved on the GOLDEN ONLY by stripping the token (footer now "Mercy Vale Regional Medical Center | Hospital Discharge Summary"); golden keeps the v5 filename, content otherwise unchanged and verified intact. Task AutoQC then PASSED (qcaud_36, 350). The WORLD is built and finalized and was NOT changed: the 6 world docx that carry the same footer are left exactly as built (live hashes unchanged), and the golden-only fix was sufficient for the pass. The builder (tools/generate_reference_files.py) was fixed so future goldens carry no synthetic footer. Do NOT re-open or re-sync the finalized world for this; if a reviewer ever requires the world footers changed, that is a pod-lead/EPM decision, not a task-level edit.

## Note for the final gate
The golden storyboard date label is plain "Date" (value 05/23/2026), which satisfies Abi's no-"Date / Anchor" rule. The runbook suggests "Date of Service"; if a reviewer prefers that exact wording it is a one-line builder change. Not blocking.
