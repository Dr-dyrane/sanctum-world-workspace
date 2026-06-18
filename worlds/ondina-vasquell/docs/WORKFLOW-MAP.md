# Ondina Vasquell - workflow map

For live task status and lifecycle, docs/WORLD-STATUS.md governs. This file maps each task to its approved workflow label (lane) and tracks which lanes are used versus open. Lane names from reference/approved-workflows-and-guidance-2026-06-13.md. Updated 2026-06-18.

## Lanes in use (7 distinct)

| Task | Studio ID | Workflow label (lane) | Pilot | State |
|---|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation at Care Transitions | FLOOR | Delivered |
| OV02 | rpfl3eac | Medical Transcription and Clinical Documentation Completion | FLOOR ~0.10 | Delivered |
| OV03 | ckrz3598 | Medical Transcription and Clinical Documentation Completion | FLOOR 0.05-0.20 | Delivered |
| OV04 | jqxv7246 | Medical Transcription and Clinical Documentation Completion | FLOOR bimodal | Delivered |
| OV05 | retired | Referral Intake, Triage, and Scheduling Coordination | CEILING all-catch 0.88-0.92 | Retired 2026-06-18 (cannot floor; headline axis + frozen consult) |
| OV06 | 1rqn2959 | Referral Intake, Triage, and Scheduling Coordination | FLOOR 0.39 | Delivered |
| OV07 | ah6e821b | Claims Denial Analysis and Appeal Preparation | FLOOR 0.51 | In first human review (Larry) |
| OV08 | l6jo01e4 | Utilization Review Concurrent Stay Documentation | FLOOR 0.63 | Awaiting first human review |
| OV09 | ebv61af9 | Post-Acute Care Coordination Documentation | FLOOR ~0.62 | Awaiting first human review |
| OV10 | ilsjf671 | Discharge Summary | FLOOR ~0.15 uniform | Awaiting first human review; FA/GA submitted |

Seven distinct lanes. Medical Transcription carries three (OV02, OV03, OV04); the other six lanes carry one each. OV05 (Referral) retired 2026-06-18 after an all-catch ceiling; the Referral lane keeps OV06. A workflow may carry 2 or more tasks (Dyrane 2026-06-17 target of 8 to 10 tasks across 6 to 7 lanes, met).

## Open lanes (candidates if more tasks are wanted)

| Workflow | Tier |
|---|---|
| Inpatient Medical Coding and DRG Assignment | P0 |
| Pharmacy Insurance Claim Rejection Resolution | P0 |
| HEDIS Medical Record Chart Abstraction and Review | P0 |
| CDI Query Response Review | P1 |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 |

Utilization Review Concurrent Stay Documentation is now used by OV08, so it has moved off the open list.

## Build rule

Future tasks pair the chosen workflow with a high-stakes step it does not force, on a quiet axis, with the index datum in a task-level artifact that does not state it cleanly: the off-text image handle (OV04/OV07 family), the off-text text-synthesis handle (OV02 family), the conflicting-subordinate-input handle (OV06/OV05/OV08/OV10 family), or a background embedded-wrong placed away from the obvious error cluster (OV09). Cold-bench lightly, then pilot in Studio. See docs/FLOOR-MECHANISM-LIBRARY.md and docs/APPROACH-MEMO.md.

## Open reviewer item
- OV07 in first human review with Larry (ah6e821b). OV01 cleared Larry round 2 on 2026-06-15.
