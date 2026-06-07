# KM03 platform/task3/current - staged for upload (escalation)

Workflow: Discharge Planning Documentation. Pod Vagus. Synthetic task base: No.

## Files (RLS upload map)
- 1.2 Prompt: prompt-task3-escalation.txt (de-telegraphed; writer-owned - confirm wording before paste)
- 1.3 Task file: case_management_discharge_readiness_clearance_05242026.docx (Mode A clone of KM02 draft chrome; verified)
- 1.4 Golden: golden-KM03-v1.docx (Mode A clone of golden-KM02-v5; NEEDS PHYSICIAN SIGN-OFF)
- 1.4 Grader: grader-guidelines-task3.txt (native structure; penalizes ADOPTING the clearance; golden ref = golden-KM03-v1.docx; no weights/bands)

## Build compliance (verified 6/7)
- Both docx: styles.xml byte-identical to base, fills/borders identical, em/en-dash 0, NO synthetic footer token, 3-row Epic band, date 05/24 header + Date cell.
- Grader: 5 native sections, names golden-KM03-v1.docx, 0 weight/band language, em-dash 0, G2 delta + fairness guard.
- Prompt: de-telegraphed (0 enumerated domains), em-dash 0.

## HOLD before upload (do not skip)
1. Codex gate: COMPLETE 2026-06-07 (frame = COMPLETION; byte-findings, no-leak, fingerprints, dates, and render sample checked).
2. Alexander: finalize/confirm the prompt wording, and SIGN OFF the golden clinical content.
3. Abi: greenlight tasking before upload.
After all three: upload 1.2/1.3/1.4, run Task AutoQC, then trajectories. Mount only this one task file in 1.3 (no world-file upload). Clean TP-KM03 stays locked; this escalation ships its own prompt.

## Pilot (pre-registered)
Run clean baseline first (expect mid-90s, calibration only), then escalation. Per-line read: which completion claims do failing runs adopt vs passing runs flag as pending. Don't force below 70; moderate discriminator by design.
