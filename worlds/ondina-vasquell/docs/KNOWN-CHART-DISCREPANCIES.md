# OV (Ondina Vasquell) - known chart discrepancies and disclosures

The OV 34-file world chart is FROZEN (never edited during tasking; standing rule). This file discloses benign internal inconsistencies a reviewer or the task AutoQC may flag as "medication discrepancies not documented as intentional traps." They are NOT intentional traps; they are immaterial real-world or authoring artifacts, are not referenced by any task's trap or golden, and are not scored. For any task flagged on one of these, cite this disclosure in the Studio dispute field. Do not edit the frozen chart.

## D1. MAR omits two home supplements the H&P marks "Continued" (ferrous sulfate, cholecalciferol)

Facts (verified 2026-06-19):
- The MAR `mar_05162026_05212026.docx` (05/16 to 05/21) lists the active and held inpatient agents (metformin, empagliflozin, lisinopril held; vancomycin, piperacillin-tazobactam, cefepime, insulin, furosemide, etc.) but does NOT list ferrous sulfate or cholecalciferol.
- The admission H&P `admission_hp_05162026.docx` home-medication reconciliation table marks `Ferrous sulfate 325 mg PO daily - Continued` and `Cholecalciferol 2000 units PO daily - Continued`, and the assessment text says "Iron continued; monitor."
- The medication hold orders `medication_hold_orders_05162026.docx` address only metformin, empagliflozin, and lisinopril.

So both supplements are "continued" per the H&P but absent from the MAR, and they are not in the hold orders.

Paste-ready dispute (Studio dispute field):

> This discrepancy is a benign documentation artifact, not an undocumented trap, and is immaterial to the evaluation. (1) Realism: home oral supplements such as ferrous sulfate and cholecalciferol are routinely absent from the inpatient MAR when they are low-priority patient's-own-medications or are deferred during an acute admission, while the admission reconciliation still records them as continued at the home level. A MAR-versus-reconciliation gap on supplements is a common real-world record state, not a contradiction the task introduced. (2) Not a trap: the task's single intended discrepancy is documented in the preamble and grader (the first-level worksheet's false "transitioned to oral antibiotics" claim, contradicted by the MAR's ongoing IV vancomycin, piperacillin-tazobactam, and cefepime). Ferrous sulfate and cholecalciferol appear in neither the worksheet trap, the golden, nor any scored element. (3) Immaterial: both are supplements with no bearing on the utilization-review continued-stay determination, the antibiotic-route issue, or the renal and glycemic picture the determination turns on; a model is neither credited nor penalized for addressing or omitting them, and the finding's own severity is "minor." We request the finding be waived; the chart is frozen and the supplement records are immaterial to task validity.

This discrepancy is in the shared chart, so it can surface on any OV task that mounts the full chart. The dispute above is reusable across tasks.
