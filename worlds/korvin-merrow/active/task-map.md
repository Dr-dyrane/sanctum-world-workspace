# Korvin Merrow Task Map

This map uses only the six approved rough task concepts. It does not add task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec sections, or synthetic files.

Source: `reference/source/_Task Selection Categories For Team.xlsx`

## Current Authoritative Architecture

Source: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`

Status: LOCKED.

Task Architecture Package v1 supersedes the Brainstorm-level original workflow mapping for World Spec construction.

Final architecture:

- Target task count: 6.
- Target workflow count: 4 distinct workflows.
- Administrative deliverable: Discharge Planning Documentation / Care Coordination.

Authoritative workflows:

1. Discharge Medication Reconciliation.
2. Hospital Discharge Summary Generation.
3. Discharge Planning Documentation.
4. Interdisciplinary Care Plan Development and Documentation.

Current task-family mapping:

| Rough task concept | Authoritative workflow | Architecture note |
| --- | --- | --- |
| Discharge medication reconciliation / medication safety review | Discharge Medication Reconciliation | Distinct medication-safety workflow preserving HF-AKI medication timing and steroid med-reconciliation complexity. |
| Hospital discharge summary generation | Hospital Discharge Summary Generation | Distinct narrative synthesis workflow preserving temporal course and copy-forward avoidance. |
| Transition-of-care / discharge readiness plan | Discharge Planning Documentation | Primary administrative/discharge-safety workflow. |
| Post-hospital follow-up assessment note | Discharge Planning Documentation | TCM reasoning and +7 anchor remain valid, but TCM is not a standalone workflow category in the locked architecture. |
| Consultant recommendation synthesis / care coordination note | Interdisciplinary Care Plan Development and Documentation | Distinct consultant synthesis and care-plan reasoning workflow. |
| Readmission risk / patient safety review | Discharge Planning Documentation | Readmission-risk reasoning remains valid, but Patient Risk Stratification Assessment is not a standalone workflow category in the locked architecture. |

Discharge Planning Documentation carries three task concepts and must be differentiated later by:

- requester;
- time anchor;
- reasoning emphasis;
- deliverable surface.

AutoQC 2.108 note:

- Primary administrative deliverable is Discharge Planning Documentation / Care Coordination.
- Utilization Review is a contingency only if later challenged by reviewer or source guidance.
- Do not add Utilization Review now.

## Historical Brainstorm-Level Mapping

The following mapping was used for Brainstorm approval and task-tracker validation. It is preserved for history only and is superseded by Task Architecture Package v1 for World Spec construction.

| Rough task | Recommended exact tracker workflow | Priority | Rationale |
| --- | --- | --- | --- |
| Discharge medication reconciliation / medication safety review | Discharge Medication Reconciliation | P0 | Exact discharge-focused match for reconciling continue/stop/modify/new medications with rationale. |
| Hospital discharge summary generation | Hospital Discharge Summary Generation | P0 | Exact match for signed discharge summary covering diagnoses, course, medications, and follow-up. |
| Transition-of-care / discharge readiness plan | Discharge Planning Documentation | P0 | Strongest match for disposition, post-acute referrals, medication reconciliation, follow-up appointments, patient/caregiver education, and payer authorization. |
| Post-hospital follow-up assessment note | Transitional Care Management Documentation (TCM) | P0 | Strongest post-discharge match because it includes hospital discharge review, medication reconciliation, follow-up coordination, care plan updates, and face-to-face visit documentation. |
| Consultant recommendation synthesis / care coordination note | Interdisciplinary Care Plan Development and Documentation | P1 | Strongest fit for reconciling recommendations across physicians, nurses, pharmacists, social workers, case managers, patient, and caregivers into one coordinated plan. |
| Readmission risk / patient safety review | Patient Risk Stratification Assessment | P0 | Strongest fit for synthesizing readmissions/utilization risk, polypharmacy, lab trends, functional status, and care-management recommendations. |

## Alternate Mappings Considered

| Rough task | Alternative tracker workflow | Priority | Reason not selected |
| --- | --- | --- | --- |
| Discharge medication reconciliation / medication safety review | Medication Reconciliation at Care Transitions | P0 | Also appropriate, but less specific than discharge medication reconciliation. |
| Discharge medication reconciliation / medication safety review | Medication Reconciliation Documentation | P0 | Broad med-rec workflow; discharge-specific tracker label is stronger. |
| Transition-of-care / discharge readiness plan | Acute Care Discharge Planning | P1 | Good conceptual fit, but P0 Discharge Planning Documentation is more complete and higher priority. |
| Post-hospital follow-up assessment note | Ambulatory Visit Note Generation (SOAP Notes) | P0 | Plausible if framed as a generic clinic SOAP note, but TCM better captures immediate post-discharge review. |
| Consultant recommendation synthesis / care coordination note | Progress Note Daily Rounding Documentation | P0 | Would require reframing as a daily progress note; current task concept is care coordination/synthesis. |
| Consultant recommendation synthesis / care coordination note | Care Coordination Referral Tracking and Closure | P1 | More referral-tracking oriented than consultant recommendation synthesis. |
| Readmission risk / patient safety review | Medications Associated With Hospital Readmissions | P2 | Too medication-specific for the broader safety/readiness concept. |
| Readmission risk / patient safety review | Patient Safety Event Investigation and Root Cause Analysis | P0 | Strong safety workflow, but would imply an actual adverse event/RCA rather than prospective readmission-risk review. |

## QC Notes

- Historical Brainstorm labels were assigned for all six rough task concepts.
- At least one P0 was present.
- Brainstorm-level mapping spanned five distinct selected workflow categories:
  - Medication reconciliation
  - Discharge documentation/planning
  - Transitional care management
  - Interdisciplinary care planning
  - Patient risk stratification
- Current locked World Spec construction architecture supersedes this with four workflows:
  - Discharge Medication Reconciliation
  - Hospital Discharge Summary Generation
  - Discharge Planning Documentation
  - Interdisciplinary Care Plan Development and Documentation
- No new clinical task concepts added.
