# Ondina Vasquell - workflow map

Updated 2026-06-17, reconciled to the live Studio board screenshot from Alexander. Lane names from reference/approved-workflows-and-guidance-2026-06-13.md.

State: six OV slots are accounted for. OV01, OV02, OV03, and OV04 are Ready for Delivery. OV05 is retired. OV06 v2 FLOORED (de-telegraphed re-pilot job 577effae: mean 0.39, bimodal, 7/10 sub-0.70); it is the world's fifth confirmed floor (OV01, OV02, OV03, OV04, OV06) and banks pending golden self-score plus FA/GA. Three lanes are in use: Medication Reconciliation, Medical Transcription and Clinical Documentation Completion, and Referral Intake, Triage, and Scheduling Coordination. Target is eight shippable tasks; the next live task after OV06 should use a distinct open lane if possible.

## Held (live Studio state)

| Task | Studio ID | Workflow as selected in Studio | Status |
|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation at Care Transitions | Ready for Delivery |
| OV02 | rpfl3eac | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV03 | ckrz3598 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV04 | jqxv7246 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV05 | none live | Medical Transcription and Clinical Documentation Completion (retired packet) | Retired 2026-06-16 after repeated ceilings |
| OV06 | Task 1rqn2959 | Referral Intake, Triage, and Scheduling Coordination | FLOORED v2 (de-telegraphed; mean 0.39, bimodal, 7/10 sub-0.70, job 577effae); FA/GA final per Ahmad; banking |
| OV07 | (pending Studio upload) | Claims Denial Analysis and Appeal Preparation | BUILT v1 (off-text image, 2.0 cm wound undermining); Codex image rendered + QA-passed; awaiting pilot |

Four lanes in use: Medication Reconciliation (OV01), Medical Transcription and Clinical Documentation Completion (OV02, OV03, OV04, retired OV05 history), Referral Intake, Triage, and Scheduling Coordination (OV06), and Claims Denial Analysis and Appeal Preparation (OV07). The Transcription lane carries the concentration. For coverage, OV08 should take another distinct fresh open lane.

## Open (build the remaining tasks here, one distinct lane each)

| Workflow | Tier |
|---|---|
| Inpatient Medical Coding and DRG Assignment | P0 |
| Pharmacy Insurance Claim Rejection Resolution | P0 |
| HEDIS Medical Record Chart Abstraction and Review | P0 |
| CDI Query Response Review | P1 |
| Utilization Review Concurrent Stay Documentation | P1 |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 |

## Build rule

Four Ready for Delivery tasks are banked. OV06 v2 floored and is now in the banking lane. Future tasks should pair the chosen workflow with a high-stakes step it does not force, on a quiet axis, with the index data in a task-level artifact that does not state it cleanly: the off-text image handle (OV04 family), the synthesis-suppression handle (OV02 family), or a KM-proven embedded wrong element placed away from the obvious error cluster. Cold-bench lightly, then pilot in Studio. See `OV-APPROACH-MEMO.md` and `OV-FLOOR-MECHANISM-LIBRARY.md`.

## Open reviewer item to clear before delivery
- OV01 Larry round 2 cleared on 2026-06-15. Board now shows Ready for Delivery.
