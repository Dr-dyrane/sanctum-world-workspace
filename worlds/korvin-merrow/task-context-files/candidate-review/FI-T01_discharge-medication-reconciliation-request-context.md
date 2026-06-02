# FI-T01 - Discharge Medication Reconciliation Request Context

File ID: FI-T01

File Type: Discharge medication reconciliation request context

Level: Task-Level

Status: CANDIDATE REVIEW

Approximate Date / Anchor: 05/24/2026 / discharge anchor

Requester / Source: Hospitalist, pharmacist, or discharge clinician requester

Workflow Category: Discharge Medication Reconciliation

Priority Family: P0 tracker provenance

Purpose: Frame a medication-safety review using locked world files without creating the final medication list, final restart plan, prednisone answer, discharge prescriptions, or task prompt.

Supported Workflow(s) / Trap(s) / Friction(s): Discharge Medication Reconciliation; Traps #1, #2, #5; Cardiology vs Nephrology; Endocrinology vs Primary Team

## Context Framing

This task-context file frames a future medication-safety request after the world-level chart closes. It does not answer the request.

The requester is preparing for a discharge-anchor medication reconciliation review and wants the future clinician-reviewer to reconcile chronic home medications, inpatient holds, inpatient-only actions, consultant recommendations, objective trends, prednisone-source uncertainty, functional medication-management safety, and the visible discharge-facing snapshot.

The context is intentionally incomplete unless the reviewer returns to the locked world files.

## Required World-File Synthesis

The future review must synthesize, at minimum:

| Source family | Locked file IDs | Why review is required |
| --- | --- | --- |
| Admission and baseline medication context | FI-W03, FI-W04 | Establish admission problem list, initial home-medication uncertainty, verified medication reconciliation, and early hold logic. |
| Pharmacy and prednisone provenance | FI-W05, FI-W06 | Separate pharmacy/refill evidence from outpatient rheumatology prednisone intent and actual home-use uncertainty. |
| Late hospitalist discharge-planning context | FI-W11 | Identify medical improvement, unresolved discharge concerns, and hospitalist synthesis burden. |
| Objective trend evidence | FI-W12 | Reassess renal, hemodynamic, infection, potassium, glucose, and intake trends without treating trends as self-interpreting. |
| Inpatient medication actions | FI-W13 | Understand what was held, administered, or reassessed in hospital without converting MAR actions into discharge orders. |
| Consultant reasoning | FI-W14, FI-W15, FI-W16 | Reconcile nephrology renal-safety timing, cardiology GDMT/CAD protection, and endocrinology steroid-risk interpretation. |
| Functional medication-management evidence | FI-W19 | Consider ADL/cognitive-functional medication-management safety as part of discharge medication risk. |
| Discharge-facing snapshot | FI-W22 | Use the visible plan as a source to reconcile, not as a final medication list or answer file. |

Other locked world files may be relevant when they clarify baseline function, family report, or hospital-course chronology.

## Review Focus

The future reviewer should be oriented to these medication-safety domains:

- medications held during AKI, hypotension risk, poor intake, or acute illness;
- medications that may need continuation because of HFrEF, CAD, diabetes, or chronic disease protection;
- timing and sequencing uncertainty around HFrEF/CAD medication reintroduction;
- prednisone exposure, taper history, and steroid-risk interpretation;
- inpatient-only actions that must not be converted into outpatient medications without evidence;
- medication-management safety in the home setting;
- follow-up and monitoring needs implied by the world evidence.

This context does not specify which medications to restart, hold, stop, taper, or prescribe.

## Trap Preservation

Trap #1 is active because prednisone history requires source reconstruction. Outpatient rheumatology remains the highest prednisone-history authority, followed by verified medication reconciliation, pharmacy/refill history, family report, and patient recollection.

Trap #2 is active because early medication holds may be appropriate when written but incomplete later. Cardiology and Nephrology remain simultaneously defensible, and neither service becomes the final restart authority.

Trap #5 is active because FI-W22 may look organized and reassuring but remains incomplete. It must be reconciled against consultants, trends, MAR/action evidence, functional medication-management evidence, and hospitalist context.

## Friction Preservation

Cardiology vs Nephrology remains a timing and sequencing friction. The future reviewer must integrate renal recovery, potassium and blood pressure risk, long-term GDMT/CAD benefit, MAR actions, objective trends, and discharge safety.

Endocrinology vs Primary Team remains an interpretation friction. The future reviewer may consider steroid exposure and diabetes/steroid interaction, but this file does not prove adrenal insufficiency, finalize prednisone adherence, or make Endocrinology the hidden diagnosis authority.

## Source-Of-Truth Safeguards

- This file may point to evidence channels but may not reorder them.
- This file does not replace FI-W04, FI-W05, FI-W06, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, or FI-W22.
- MAR action evidence shows inpatient administration and holds only.
- FI-W22 is not a final medication reconciliation.
- Family report is collateral evidence and does not override rheumatology prednisone authority.

## Prohibited Content

This file does not contain:

- a final medication list;
- a discharge prescription set;
- a restart algorithm;
- a steroid taper answer;
- a consultant winner;
- a final home regimen;
- a task prompt;
- an expected output;
- a golden response;
- grader guidance;
- post-world clinical events.

## Candidate Review Note

Candidate reviewers should verify that this file frames the medication reconciliation context while requiring use of the locked world files. It should not be usable as a standalone medication answer.
