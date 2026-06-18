# Marva Lydell Brainstorm Draft

Status: draft from the approved planning canvas only. Not a submission artifact.

Date: 2026-06-18.

Approved patient-world name: Marva Lydell.

Demographic direction: Black older adult woman. Race is documented context only. It should not be used as a hidden clue or scoring shortcut.

## World Concept

This world tests discharge readiness in Marva Lydell, a Black older adult woman who is improving in the hospital but is not yet safe to leave unless the transition details are handled correctly.

The clinical setting is acute decompensated heart failure with chronic kidney disease, atrial fibrillation, COPD or OSA overlap, frailty, and home-access barriers. The patient looks stable at rest. The hard part is whether the discharge plan is safe under exertional oxygen needs, equipment delivery, anticoagulation, renal recovery, diuretic ownership, and post-acute coordination.

The world is not a heart-failure treatment quiz. It is a transition-readiness world.

## Why This World Is Useful

Strong models read standard clinical notes well. They usually find buried text, avoid obvious fabrication, and summarize common conditions correctly. The failure we want is narrower: a model accepts a routine handoff line, payer position, vendor status, or background closure that the chart contradicts.

The world should therefore make the wrong move quiet and realistic. A clinician can catch it by reconciling the chart. A cursory completion can miss it.

## Source Material Plan

The shared world files should give raw material, not answer-key synthesis.

Planned world-level file families:

- ED physician note.
- Admission H&P.
- Hospitalist progress notes across decongestion.
- Cardiology consult.
- Nephrology consult.
- Pulmonary or respiratory therapy assessment.
- Echocardiogram report.
- Chest imaging reports.
- BNP trend.
- BMP and renal trend.
- CBC trend.
- Medication administration record.
- Home medication list.
- Anticoagulation history.
- Telemetry or atrial fibrillation summary.
- PT evaluation with exertional tolerance.
- OT evaluation with stairs and ADL barriers.
- RT oxygen assessment note.
- Case management note.
- DME coordination note.
- Nursing notes.
- Discharge rights or Medicare notice.
- Family communication note.
- PCP baseline summary.
- Pharmacy fill history.
- Weight and intake-output flowsheet.

Target: at least 30 world-level files before spec submission.

Task-level files create the forced move. They may include payer denial letters, vendor delivery notes, scanned walk-test sheets, started discharge documents, SNF pharmacy sheets, UR worksheets, and safety-event intake summaries.

## Candidate Task Slate

| # | Task shape | User-facing task idea | Hidden work |
|---|---|---|---|
| 1 | External appeal | Draft an oxygen or DME denial appeal. | Resting saturation looks safe, but off-text exertional testing qualifies oxygen. |
| 2 | Completion | Finish a discharge summary or transition note. | A background line says no oxygen need or DME delivered, but the chart contradicts it. |
| 3 | Determination | Write a utilization review continued-stay note. | Clinical markers improved, but discharge is unsafe because equipment or exertional oxygen is unresolved. |
| 4 | Forced inventory | Reconcile discharge anticoagulation or medications. | External SNF or pharmacy sheet carries a wrong dose, duplicate, or hold timing. |
| 5 | Investigation | Write a safety-event RCA after a bounceback. | The tempting cause is patient nonadherence, but the source chain shows a handoff or equipment failure. |
| 6 | Synthesis | Build a cardiology-nephrology-pulmonary handoff. | A quiet unresolved owner remains for oxygen, diuresis, renal labs, or anticoagulation. |
| 7 | Abstraction | Complete a quality or risk abstraction. | A fixed field turns on a source-specific exclusion or denominator distinction. |
| 8 | External request | Prepare a post-acute or prior-authorization appeal. | Denial treats home health as enough, while functional data supports skilled or equipment need. |
| 9 | Follow-up | Complete an early post-discharge follow-up note. | Patient report sounds improved, but objective weight, oxygen, or DME data shows deterioration. |
| 10 | Physician review | Review a CDI, coding, or documentation query. | Only use if tied to a fresh source-geometry distinction, not a known CDI trope. |

The first three to prioritize are oxygen/DME denial, discharge-readiness completion, and utilization review. They are the least spent by Korvin or Ondina and best match this world.

## Fairness Rules

- The task must not tell the model to inspect the trap directly.
- The wrong move must sit in a background line, subordinate source, external document, or task-level sheet.
- The chart must contradict the wrong move. Silence is not enough.
- A clinician catcher must be able to reach the answer from the mounted files.
- No same-author false draft claim unless the prompt asks for correction or the draft uses true placeholders.
- No public post-July-2025 clinical knowledge dependency unless the exact source is attached.
- No task file belongs in shared world files.
- Race must not be used as a task mechanism. Every scored fact must come from the mounted chart.

## Expected Frictions

- Resting improvement versus exertional failure.
- Equipment ordered versus equipment actually delivered.
- Specialist note conflict without a single resolving summary.
- Renal recovery versus medication and diuretic safety.
- Anticoagulation risk across discharge destination.
- Payer pressure versus clinical readiness.
- Patient-reported readiness versus objective transition failure.

## First Red-Team Gate

Before this becomes a Brainstorm DOCX, each proposed task needs a one-line answer to four questions:

1. What decision does the deliverable force?
2. Where is the quiet wrong move?
3. What exact chart source contradicts it?
4. How does a catcher reach it without private knowledge?
