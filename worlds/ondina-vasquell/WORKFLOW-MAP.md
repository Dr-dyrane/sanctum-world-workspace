# Ondina Vasquell - workflow map

Updated 2026-06-16, reconciled to the LIVE Studio board (Alexander). Lane names from reference/approved-workflows-and-guidance-2026-06-13.md.

State: six tasks built or in flight (OV01-OV06). OV01/OV02/OV04 Ready for Delivery; OV05 in Taiga QA (v3 re-pilot pending); OV03 floored (FA/GA done, bank pending self-score); OV06 just built (awaiting pilot). OV06 opens the Referral lane, so THREE lanes are now in use and SEVEN are open. Target is eight tasks; OV07 and OV08 each take a distinct open lane for coverage.

## Held (live Studio state)

| Task | Studio ID | Workflow as selected in Studio | Status |
|---|---|---|---|
| OV01 | Task 1 | Medication Reconciliation at Care Transitions | Ready for Delivery |
| OV02 | rpfl3eac | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV04 | jqxv7246 | Medical Transcription and Clinical Documentation Completion | Ready for Delivery |
| OV05 | aoe3bfe1 | Medical Transcription and Clinical Documentation Completion (reconciliation deliverable; relabel candidate) | Taiga QA (v3 quiet-K-load) |
| OV03 | ckrz3598 | Documentation Completion (discharge med plan; confirm vs Medication Reconciliation) | Floored v2; FA/GA done; bank pending self-score |
| OV06 | new | Referral Intake, Triage, and Scheduling Coordination | BUILT; awaiting pilot |

Three lanes in use: Medication Reconciliation (OV01), Medical Transcription and Clinical Documentation Completion (OV02, OV04, OV05, and OV03 if filed there), and Referral Intake, Triage, and Scheduling Coordination (OV06, new). The Transcription lane carries three to four tasks. That is the real concentration. For coverage, OV07 and OV08 must each take a fresh open lane, and OV05 (a reconciliation) and OV03 (a med plan) should be confirmed or relabeled so the Transcription lane is not overloaded.

## Open (build the remaining tasks here, one distinct lane each)

| Workflow | Tier |
|---|---|
| Inpatient Medical Coding and DRG Assignment | P0 |
| Claims Denial Analysis and Appeal Preparation | P0 |
| Pharmacy Insurance Claim Rejection Resolution | P0 |
| HEDIS Medical Record Chart Abstraction and Review | P0 |
| CDI Query Response Review | P1 |
| Utilization Review Concurrent Stay Documentation | P1 |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 |

## Build rule

Four more tasks reach eight, each in a distinct open lane. Each pairs a completion deliverable with a high-stakes step it does not force, on a quiet axis, with the index data in a task-level artifact that does not state it cleanly: the off-text image handle (OV04 family) or the synthesis-suppression handle (OV02 family). Cold-bench before any pilot. See OV-APPROACH-MEMO.md and OV-FLOOR-MECHANISM-LIBRARY.md.

## Open reviewer item to clear before delivery
- OV01 (Larry, round 2): remove accidental templating language in the grader ("With include_input_files=true, verify any specific..."), and set the FA/GA to the 2nd-lowest scoring run with the run output visible. Confirm done.
