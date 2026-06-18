# Ondina Vasquell - workflow map

Updated 2026-06-17, reconciled to the live Studio board screenshot from Alexander. Lane names from reference/approved-workflows-and-guidance-2026-06-13.md.

State (2026-06-18): eight confirmed floors. OV01, OV02, OV04 Ready for Delivery; OV03 floored (FA/GA done); OV06 floored (FA/GA final, banking); OV07 floored (off-text image on Claims Denial, FA/GA done); OV08 floored (bimodal, mean 0.63, Utilization Review Concurrent Stay, FA/GA done, 5th lane); OV09 floored (bimodal, mean ~0.62, Post-Acute Care Coordination, FA/GA done, 6th lane). OV05 revived (bottle-photo retired; slot rebuilt 2026-06-18 as a skilled-wound-care downgrade on the Referral lane, the OV06 conflicting-authority engine, 2nd task on that lane, pilot-ready). TARGET RAISED (Dyrane 2026-06-17) to 8 to 10 shippable tasks across 6 to 7 distinct workflows: a workflow may carry 2 or more tasks, so reusing a strong lane to hit the count is acceptable, and Coding/DRG and CDI Query are back in play as candidate lanes. Six lanes in use; OV09 = Post-Acute Care Coordination Documentation (6th lane). v3 (embedded-wrong on the disposition headline) CEILINGED 0.84, range 0.72-0.92, no floor (job e9c38261), because disposition is the handoff headline and the model corrected it every run. v4 re-cut moved the embedded wrong to a background axis (three held oral agents resumed at discharge) and FLOORED bimodal, mean ~0.62 (four floors 0.25-0.35, five catchers 0.78-0.92; job cc337773); FA/GA done. Contrast v1 and osteo-image v2 retired. Headline-vs-background confirmed: v3 on the disposition headline ceilinged 0.84, v4 on the background med line floored. OV10 built (Dyrane 2026-06-18) = Discharge Summary (bone-health / CKD-MBD over-closure via a subordinate chronic-disease review, the OV06 external-input fair form, pilot-ready, 7th lane), toward 10+ diversified tasks.

## Held (live Studio state)

| Task | Studio ID | Workflow as selected in Studio | Status |
|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation at Care Transitions | Ready for Delivery |
| OV02 | rpfl3eac | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV03 | ckrz3598 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV04 | jqxv7246 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV05 | none live | Medical Transcription and Clinical Documentation Completion (retired packet) | Retired 2026-06-16 after repeated ceilings |
| OV06 | Task 1rqn2959 | Referral Intake, Triage, and Scheduling Coordination | FLOORED v2 (de-telegraphed; mean 0.39, bimodal, 7/10 sub-0.70, job 577effae); FA/GA final per Ahmad; banking |
| OV07 | (pending Studio upload) | Claims Denial Analysis and Appeal Preparation | FLOORED v1 (off-text image; bimodal mean 0.51, 6 floors 0.20-0.30 + 4 catchers 0.85-0.95, job a33db3d0); FA/GA pending a floor-run transcript |

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
