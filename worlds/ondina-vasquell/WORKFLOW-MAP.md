# Ondina Vasquell - workflow map

Updated 2026-06-16. Lane names from reference/approved-workflows-and-guidance-2026-06-13.md (Abi 06/13 tracker, Vagus pod). Confirm the exact workflow string live at Step 10.

State: four tasks are built and kept (OV01, OV02, OV04, OV05). Seven approved lanes are open. Floors are manufactured at the task layer. Each open lane gets built with the proven engine. Target is eight tasks in this world.

## Held (built, kept)

| Task | Workflow | Tier | What it is |
|---|---|---|---|
| OV01 | Medication Reconciliation at Care Transitions | P0 | Floor, banked. Discharge med rec; the model carries inpatient enoxaparin forward to home. |
| OV02 | Inpatient Medical Coding and DRG Assignment | P0 | Floor. Off-text synthesis; the model does not assemble the unaddressed line infection. |
| OV04 | Medical Transcription and Clinical Documentation Completion | P0 | Floor, banked. Off-text CPAP compliance image the model does not open. |
| OV05 | Medication Reconciliation at Care Transitions | P0 | Catcher, kept. Home-medication-bottle image (unlisted ibuprofen). Shares OV01's lane. |

## OV05 lane settlement

OV01 and OV05 are both medication reconciliation. OV01 is the floor in this lane. OV05 is the catcher and the home for its ibuprofen image. One lane can carry one floor plus one catcher. The rule that matters is one FLOOR per lane, and OV01 is the only floor here, so OV05 stays as the catcher. No future floor task reuses the Medication Reconciliation lane. If a distinct lane is required at delivery, reframe the ibuprofen image into an open lane at that point.

## Open (build these right, one distinct lane each)

| Workflow | Tier |
|---|---|
| Claims Denial Analysis and Appeal Preparation | P0 |
| Pharmacy Insurance Claim Rejection Resolution | P0 |
| HEDIS Medical Record Chart Abstraction and Review | P0 |
| CDI Query Response Review (or DRG Reconciliation Review) | P1 |
| Utilization Review Concurrent Stay Documentation | P1 |
| Referral Intake, Triage, and Scheduling Coordination | P1 |
| Patient Safety Indicator (PSI) Analysis and Reporting | P2 |

## Build rule

Four more floor tasks reach eight, each in a distinct open lane. Each pairs a completion deliverable with a high-stakes step it does not force, on a quiet axis, with the index data in a task-level artifact that does not state it cleanly: the off-text image handle (OV04 family) or the synthesis-suppression handle (OV02 family). Cold-bench before any pilot. See OV-APPROACH-MEMO.md and OV-FLOOR-MECHANISM-LIBRARY.md.
