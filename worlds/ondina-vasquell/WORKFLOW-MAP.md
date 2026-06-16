# Ondina Vasquell - workflow map

Updated 2026-06-16, reconciled to the LIVE Studio board (Alexander). Lane names from reference/approved-workflows-and-guidance-2026-06-13.md.

State: four tasks built. Three are Ready for Delivery (OV01, OV02, OV04). One is in Taiga QA (OV05). Two approved lanes are in use; eight are open. Target is eight tasks; the remaining four each take a distinct open lane for coverage.

## Held (live Studio state)

| Task | Studio ID | Workflow as selected in Studio | Status |
|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation at Care Transitions | Ready for Delivery |
| OV02 | rpfl3eac | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV04 | jqxv7246 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV05 | aoe3bfe1 | Medical Transcription and Clinical Documentation Completion | Taiga Trajectories & QA |

Two lanes in use: Medication Reconciliation (OV01) and Medical Transcription and Clinical Documentation Completion (OV02, OV04, OV05). The Transcription lane carries three tasks. That is the real concentration. For coverage, no new task should reuse Transcription or Medication Reconciliation.

## Open (build the remaining tasks here, one distinct lane each)

| Workflow | Tier |
|---|---|
| Inpatient Medical Coding and DRG Assignment | P0 |
| Claims Denial Analysis and Appeal Preparation | P0 |
| Pharmacy Insurance Claim Rejection Resolution | P0 |
| HEDIS Medical Record Chart Abstraction and Review | P0 |
| CDI Query Response Review | P1 |
| Utilization Review Concurrent Stay Documentation | P1 |
| Referral Intake, Triage, and Scheduling Coordination | P1 |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 |

## Build rule

Four more tasks reach eight, each in a distinct open lane. Each pairs a completion deliverable with a high-stakes step it does not force, on a quiet axis, with the index data in a task-level artifact that does not state it cleanly: the off-text image handle (OV04 family) or the synthesis-suppression handle (OV02 family). Cold-bench before any pilot. See OV-APPROACH-MEMO.md and OV-FLOOR-MECHANISM-LIBRARY.md.

## Open reviewer item to clear before delivery
- OV01 (Larry, round 2): remove accidental templating language in the grader ("With include_input_files=true, verify any specific..."), and set the FA/GA to the 2nd-lowest scoring run with the run output visible. Confirm done.
