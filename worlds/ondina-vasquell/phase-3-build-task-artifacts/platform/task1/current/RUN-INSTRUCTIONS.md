# platform/task1/current - OV01 v1 pilot template (Discharge Medication Reconciliation)

This is the FIRST Ondina task and the pilot template for OV02 to OV10. Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot leans on them.

## Workflow type: Medication Reconciliation at Care Transitions (P0)
REMAPPED 2026-06-13: original workflow Discharge Medication Reconciliation (hca-discharge-med-recon) was retired from the platform menu; this is the nearest open analogue. Deliverable framing may need a light adjustment to fit it. VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
Source-of-truth reconciliation under renal constraint. The unreconciled order set (E1-T1) carries the admission antibiotic dose forward and leaves the three held oral agents ambiguous. A correct reconciliation doses to the current renal function, treats metformin, empagliflozin, and lisinopril as explicit deferred restarts, keeps acetaminophen and not an NSAID, continues home insulin, and surfaces a renally correct, deep-culture-directed antibiotic plan. Central failure = carrying admission dosing forward or silently resuming or discontinuing a held agent.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/), which the model reads to reconcile.
- Task-level file: preliminary_discharge_order_set_05212026.docx (E1-T1). Upload and confirm it shows UPLOADED, not staged, before AutoQC. Confirm no filename collision with a world file (verified: none).
- Grader is chart-aware (include_input_files true): the deliverable is built from the chart, so true chart specifics are credited, not flagged as invented.

## Fairness (hard line)
Every discrepancy in the order set is contradicted by the chart: the renal trend shows the improved GFR, the admission hold orders state the holds as decisions, and the deep-tissue culture outranks the swab. Correcting them is the right move and is rewarded; propagating them is a real clinical error. The held agents are NOT pre-resolved in any file (A0.4 confirmed), so deferring their restart is a genuine judgment, not a coached catch.

## RLS entry (1.1 to 1.4) - save after every step
Workflow type = Medication Reconciliation at Care Transitions (verify on the live Task Selection Categories sheet).
1.2 Prompt: prompt-OV01.txt.
1.3 Add Files: upload the order set, click Save File Changes, refresh, confirm UPLOADED.
1.4 Golden golden-OV01-v1.docx and grader grader-guidelines-OV01.txt; confirm the grader names the golden by filename and the golden shows UPLOADED.
Top Save Changes, refresh, run Task AutoQC (rerun N failing once before disputing), 2.2 note, run Taiga Trajectories.

## Expectation
See OV01-v1-pilot-preregistration.md for the locked forecast and read rules. Read the low trajectories against the chart to confirm any failure is a propagated dosing or restart error, not grader noise.
