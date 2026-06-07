# KM03 platform/task3/current - active platform set (escalation)

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

## Platform state (6/7 late pm)
1. Codex gate: COMPLETE 2026-06-07 (frame = COMPLETION; byte-findings, no-leak, fingerprints, dates, and render sample checked).
2. Upload: COMPLETE under Alexander operation.
3. Task AutoQC: PASS 36/36 (`qcaud_6b`) after DOCX core metadata scrub.
4. Current shas after scrub: task file `95f6affb`; golden `5feb3227`.
5. Current run state: Taiga Trajectories & QA running.
6. Open: Alexander physician sign-off on the golden clinical content.

Mount only this one task file in 1.3 (no world-file upload). Clean TP-KM03 stays locked; this escalation ships its own prompt. Do not rerun AutoQC, rerun agents, rerun QA, upload additional files, or mutate RL Studio without exact Alexander authorization.

## Pilot (pre-registered)
Run clean baseline first (expect mid-90s, calibration only), then escalation. Per-line read: which completion claims do failing runs adopt vs passing runs flag as pending. Don't force below 70; moderate discriminator by design.
