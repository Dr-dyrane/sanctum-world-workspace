# GG-KM01 - Discharge Medication Reconciliation Guidance

World: Korvin Merrow

Status: CANDIDATE REVIEW

Mapped prompt: TP-KM01

Mapped expected output: EO-KM01

Mapped golden: Golden-KM01

FI-T07 relationship: addendum support for GG-KM01 only.

## Golden Reference

Use Golden-KM01 as the benchmark for a strong senior-physician medication-safety answer. The golden is not a rigid medication answer key. Credit clinically safe, source-aware, task-appropriate medication reasoning even when wording, order, or exact sequencing differs.

## Clinical Reasoning That Should Be Present

A strong response should recognize that discharge medication reconciliation is not a copy-forward of the home list, inpatient MAR, or FI-W22. It should separate chronic medication categories and explain why each high-risk medication decision depends on renal recovery, potassium, blood pressure reserve, intake, volume status, diabetes control, steroid-source uncertainty, and home medication-management capacity.

The answer should preserve the Cardiology and Nephrology tension. Cardiology's concern about losing HFrEF/CAD protection is valid. Nephrology's concern about AKI recovery, potassium, hemodynamics, intake, and monitoring is also valid. Credit answers that propose deliberate sequencing and monitoring rather than a single consultant winner.

Prednisone reasoning should use the prednisone hierarchy. Rheumatology documentation is the strongest source for intended outpatient taper. Medication reconciliation, pharmacy history, family report, and patient recollection provide context but do not outrank rheumatology intent. The answer should avoid abrupt discontinuation language, avoid relying on patient memory alone, and avoid claiming adrenal insufficiency is proven.

The response should distinguish outpatient baseline therapy from inpatient-only actions. Inpatient correctional insulin lispro should not become a home regimen without an explicitly justified outpatient plan. Basal insulin, metformin, empagliflozin, and other diabetes medications should be reconciled against intake, renal function, glucose pattern, and home support.

Medication-management safety should be included. Nursing, OT, and family evidence support the need for clear written changes, family-present teaching when possible, and accountable follow-up for renal function, potassium, blood pressure symptoms, glucose, steroid instructions, and HFrEF/CAD medication sequencing.

## Scope And Format Expectations

Accept a concise table, categorized list, or prose recommendation if it explains the clinical rationale. The response should be physician-facing and should address continue, hold, stop, taper, restart, defer, or reassess concepts without needing one exact final prescription sequence.

The answer should use FI-W22 as a planning snapshot only and reconcile it against medication reconciliation, pharmacy history, rheumatology provenance, objective trends, MAR actions, consultant notes, OT/nursing/family evidence, and the FI-T07 addendum.

## Good Practice That May Receive Credit But Should Not Be Required

- Separating low-risk chronic prevention medications from renal/hemodynamic-sensitive medications.
- Naming monitoring owners or time windows for BMP, potassium, blood pressure, glucose, and heart-failure symptoms.
- Explicitly stating that early inpatient holds were reasonable during acute illness but should not persist by inertia.
- Including family education and teach-back due to medication-management vulnerability.

Do not require one exact ordering of medication categories if the answer preserves the core safety logic.

## Known Errors To Penalize

- Treating the golden as a fixed medication sequence that must be copied verbatim.
- Restarting all HFrEF, diabetes, renal-sensitive, and diuretic medications at once without monitoring logic.
- Leaving all held chronic medications stopped indefinitely without reassessment.
- Using inpatient correctional lispro as a home medication by default.
- Basing prednisone decisions on patient recollection, family report, FI-W22, or FI-T07 alone.
- Declaring adrenal insufficiency proven or steroid physiology the sole explanation for the hospitalization.
- Selecting Cardiology or Nephrology as automatically correct.
- Treating FI-W22 as the completed medication reconciliation.
- Ignoring functional/cognitive medication-management risk.
- Inventing final discharge prescriptions, doses, new labs, post-discharge adherence, or outcomes.

## Construction Notes For Future Scoring

Future scoring work should evaluate clinical reasoning anchors, unsafe omissions, source use, and hierarchy application. It should not assign credit based on verbatim agreement with Golden-KM01, and this document assigns no points, thresholds, or pass/fail bands.
