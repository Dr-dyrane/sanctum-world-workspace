# QC error-class register (how we stop repeating send-backs)

Purpose: record each recurring AutoQC / reviewer failure CLASS, its root cause, and the GUARD that now catches it, so the class does not recur. The governing lesson is below.

## Governing lesson: verify against the LIVE AutoQC, not a stale house convention

The boilerplate failure (2026-06-19) happened because our local gates encoded a stale house "five-block" convention and REQUIRED the phrase "These are patterns to reason about, not items to tick off." as the Section C opener (`verify_ondina.SECC_OPENER`, `presubmit_task_gate` line 107). The live AutoQC fail-criteria later named that exact phrase as banned boilerplate filler. The gate was checking our own convention, not the current AutoQC rules, so it passed every grader straight into a send-back. When AutoQC rejects what used to pass, flip the gate the same day and sweep the artifacts. Keep `BANNED_BOILERPLATE` (in both gates) synced to the live AutoQC named-boilerplate list.

## Error-class register

| Class | Example that bit us | Root cause | Guard now in place |
|---|---|---|---|
| Banned boilerplate filler in the grader | "patterns to reason about, not items to tick off" (OV08, OV11) | gate REQUIRED a phrase AutoQC later banned | `BANNED_BOILERPLATE` list checked in `presubmit_task_gate.py` and `verify_ondina.py`; flags any listed filler. Extend the list from the AutoQC criteria. |
| Task-file referenced but not uploaded | OV08 `continued_stay_determination_worksheet_05252026.docx` present in the repo but omitted from the Studio upload | manual upload omission; no machine checklist | `presubmit_task_gate.py` emits an explicit per-task UPLOAD MANIFEST and flags any RUN-INSTRUCTIONS mount-list file missing from the repo. Cross-check the manifest against the Studio upload before submitting. |
| Undocumented chart discrepancy read as a trap | MAR omits ferrous sulfate / cholecalciferol while the H&P marks them "Continued" | frozen-chart authoring artifact, immaterial, not disclosed | `worlds/ondina-vasquell/docs/KNOWN-CHART-DISCREPANCIES.md` discloses it with a paste-ready dispute; the chart stays frozen. |

## AutoQC named-boilerplate list (seed - extend me)

Mirror the full set of banned filler phrases the live AutoQC fail-criteria name into `BANNED_BOILERPLATE` in both gates. Confirmed so far:
- "These are patterns to reason about, not items to tick off."

Add the rest from the criteria as they are confirmed; one entry per phrase, lowercase substring.

## Submit checklist (per task)

1. `python3 tools/verify/presubmit_task_gate.py taskN` -> PASS, and read the printed UPLOAD MANIFEST.
2. Confirm every manifest file is attached in the Studio task upload (the OV08 miss).
3. `python3 tools/verify/verify_ondina.py` -> PASS.
4. Have any applicable KNOWN-CHART-DISCREPANCIES dispute ready to paste.
