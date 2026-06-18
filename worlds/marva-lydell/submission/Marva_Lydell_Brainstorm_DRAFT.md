# Marva Lydell Brainstorm Draft

Status: bootstrap draft. Not a DOCX. Not upload-ready.

Date: 2026-06-18.

## World Concept

Marva Lydell is a Black older adult woman admitted with a cardiopulmonary decompensation that improves at rest but remains unsafe at transition unless discharge readiness is reconciled carefully.

The core is not heart-failure treatment. The core is transition readiness: oxygen qualification, DME delivery, exertional physiology, anticoagulation safety, renal recovery, diuretic handoff, conflicting specialty notes, and payer or post-acute pressure.

## Why This World Should Work

Korvin and Ondina showed that strong models are good at clean chart synthesis. They usually read standard notes, avoid obvious fabrication, and correct familiar medication issues.

This world moves the failure point to source geometry. The wrong move should sit in a routine background line, external denial, vendor handoff, SNF sheet, or started document. The chart must contradict it. The deliverable must force a decision. A catcher can find it, but a completion-mode model can miss it.

## Candidate Source Base

The world should carry at least 30 world-level files before spec submission.

Planned file families:

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

Task-level files create the forced move. Candidate task files include payer denial letters, vendor delivery notes, scanned walk-test sheets, started discharge documents, SNF pharmacy sheets, UR worksheets, and safety-event intake summaries.

## Task Slate

| # | Structure | Working task | Quiet failure axis |
|---|---|---|---|
| 1 | External appeal | Oxygen or DME denial appeal | Resting saturation looks safe, but off-text exertional testing qualifies oxygen. |
| 2 | Completion | Discharge summary or transition note | Background line says no oxygen need or DME delivered, but the chart contradicts it. |
| 3 | Determination | Utilization review continued-stay note | Clinical markers improve, but equipment or exertional oxygen remains unresolved. |
| 4 | Forced inventory | Discharge anticoagulation or medication reconciliation | External SNF or pharmacy sheet carries wrong dose, duplicate therapy, or hold timing. |
| 5 | Investigation | Safety-event RCA after bounceback | Tempting answer blames patient nonadherence, but source chain shows equipment or handoff failure. |
| 6 | Synthesis | Cardiology-nephrology-pulmonary handoff | Quiet unresolved owner remains for oxygen, diuresis, renal labs, or anticoagulation. |
| 7 | Abstraction | Quality or risk abstraction | Fixed field turns on a source-specific exclusion or denominator distinction. |
| 8 | External request | Post-acute or prior-authorization appeal | Denial treats home health as enough, while functional data supports skilled or equipment need. |
| 9 | Follow-up | Early post-discharge follow-up note | Patient report sounds improved, but objective weight, oxygen, or DME data shows deterioration. |
| 10 | Physician review | CDI, coding, or documentation query | Use only if tied to fresh source geometry, not a known CDI trope. |

## Guardrails

- Race is demographic context only. It is not a task mechanism or scoring cue.
- The chart must carry every scored fact.
- No answer-key synthesis in shared world files.
- No task file in world files.
- No prompt telegraph.
- No same-author false draft claim unless the prompt asks for correction or the draft uses true placeholders.
- No public post-July-2025 knowledge dependency unless the exact source is mounted.

## First Red-Team Gate

Before DOCX build, each proposed task must answer:

1. What decision does the deliverable force?
2. Where is the quiet wrong move?
3. What exact chart source contradicts it?
4. How does a catcher reach it without private knowledge?
