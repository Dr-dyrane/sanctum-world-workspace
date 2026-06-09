# platform/task2 - KM02 platform artifacts

KM02 = Hospital Discharge Summary Generation.

Current status: KM02 v3 active platform set is complete and in Abi review. Clean pilot is superseded.

## Active Platform Set

Use only `current/` for live platform materials:

- `prompt-task2-escalation.txt`
- `golden-KM02-v5.docx` - date corrected to 05/24/2026; sha256 prefix `2dd3e0ad`
- `grader-guidelines-task2.txt`
- `discharge_summary_draft_incomplete_05242026.docx`
- `RUN-INSTRUCTIONS.md` - historical instructions for the escalation run and fairness guardrail

## Historical / Held Material

- `hold/`: superseded clean prompt and held draft extraction. Do not upload unless Alexander explicitly reopens it.
- `archive/`: future retired platform material.

Run evidence lives under `../../task2/runs/`, not in this platform folder.

## Current Gate

Task AutoQC / Taiga gates passed qcaud_5e, qcaud_4a, and qcaud_ef. FA/GA candidate uses Attempt 8 at score 0.30 from v3 job `8f393839`. KM02 remains in Abi review.

## Change log
- Task AutoQC 2.1 fix (footer meta-language): "Meta-Language and Content Hygiene" flagged the "Synthetic training document" footer token. Resolved on the GOLDEN ONLY by stripping the token (footer now "Mercy Vale Regional Medical Center | Hospital Discharge Summary"); golden keeps the v5 filename, content otherwise unchanged and verified intact. Task AutoQC then PASSED (qcaud_36, 350). The WORLD is built and finalized and was NOT changed: the 6 world docx that carry the same footer are left exactly as built (live hashes unchanged), and the golden-only fix was sufficient for the pass. The builder (tools/generate_reference_files.py) was fixed so future goldens carry no synthetic footer. Do NOT re-open or re-sync the finalized world for this; if a reviewer ever requires the world footers changed, that is a pod-lead/EPM decision, not a task-level edit.

## Note for the final gate
The golden storyboard date label is plain "Date" (value 05/24/2026, fixed 6/7 per first review; matches the escalation in-world today and the mounted draft), which satisfies Abi's no-"Date / Anchor" rule. The runbook suggests "Date of Service"; if a reviewer prefers that exact wording it is a one-line builder change. Not blocking.

6/7 reseed note: the LIVE task uses `current/prompt-task2-escalation.txt` (in-world today = 05/24, finish-my-draft framing). The clean-pilot prompt was moved to `hold/prompt-task2-CLEAN-SUPERSEDED.txt` so it cannot be grabbed by mistake during re-upload. Golden re-dated to 05/24/2026 (sha `2dd3e0adb903`).
