# Identity Package v1

Date: 2026-05-31

Status: LOCKED.

Purpose: lock the synthetic patient identity and basic demographic/compliance details needed before Governance Package and World Spec drafting.

This document does not draft the World Spec, create milestones, create a file inventory, create tasks, write prompts, create golden responses, or create grader guidance.

## Locked Identity

| Field | Locked value |
| --- | --- |
| Name | Korvin Merrow |
| DOB | 1964-02-18 |
| Age | 62 |
| MRN | KM-6427819 |
| Height | 178 cm (5'10") |
| Weight | 97 kg (214 lb) |
| BMI | 30.6 |
| Allergy | Lisinopril (cough) |
| Code Status | Full Code |

## Identity Package Review

### VERIFIED

Finding: age is consistent with DOB for a 2026 encounter after February 18.

Evidence: DOB is 1964-02-18. Korvin Merrow is 62 from 2026-02-18 through 2027-02-17.

Impact: Age 62 is internally consistent for the current 2026 project timeline.

Action required: Later calendar date skeleton must keep the admission/world timeline within the age-62 window unless Alexander explicitly changes age or DOB.

### VERIFIED

Finding: BMI is consistent with height and weight.

Evidence: 97 kg / (1.78 m x 1.78 m) = 30.6 kg/m2 when rounded to one decimal place.

Impact: Height, weight, and BMI can be used consistently in later clinical profile work.

Action required: Preserve all three values together; do not independently round or alter one value later.

### VERIFIED

Finding: MRN is synthetic and appropriately non-realistic.

Evidence: `KM-6427819` uses patient initials plus a numeric sequence rather than a bare real-world identifier.

Impact: Supports World Spec AutoQC synthetic identity expectations.

Action required: Use this exact MRN consistently if MRN is needed in World Spec or future synthetic files.

### NO ISSUE

Finding: lisinopril cough allergy fits the clinical story.

Evidence: Patient has hypertension, CKD, HFrEF/CAD, and is currently on sacubitril/valsartan rather than lisinopril. ACE-inhibitor cough is common and does not conflict with the approved medication list.

Impact: Adds realistic medication history without changing the core case.

Action required: Later medication/allergy reconciliation should preserve this as an ACE-inhibitor intolerance/allergy and avoid accidental lisinopril restart.

### NO ISSUE

Finding: Full Code status does not conflict with the Brainstorm or ratified Clinical Story Skeleton.

Evidence: Approved story involves a 62-year-old medically complex but previously independent patient who lives with family and is undergoing discharge planning after improvement.

Impact: Full Code is plausible and does not alter the discharge-safety failure target.

Action required: Preserve as locked unless Alexander explicitly reopens code status.

### NO ISSUE

Finding: identity package is consistent with the approved Brainstorm and ratified Clinical Story Skeleton.

Evidence: Name, age, and demographic profile match the approved Korvin Merrow concept and do not add new diagnoses, tasks, traps, frictions, labs, dates, or file plans.

Impact: Identity Package v1 can safely support Governance Package and later World Spec profile fields.

Action required: Use as the identity source of truth going forward.

### PLAUSIBLE

Finding: BMI 30.6 is clinically compatible with the world but does not need to become a major complexity driver.

Evidence: BMI falls in class I obesity range, which is compatible with OSA, diabetes, hypertension, CAD/HFrEF, and functional reserve concerns.

Impact: This strengthens realism but should not distract from the approved core failure target.

Action required: Treat BMI as background context unless Alexander later chooses to make weight/OSA/functional reserve clinically salient.

### DISPUTED

Finding: none.

Evidence: No conflict found with approved Brainstorm, ratified Clinical Story Skeleton, or current World Spec preparation boundaries.

Impact: No redesign or narrative revision required.

Action required: None.

## Carry-Forward Guardrails

- The later calendar skeleton must keep Korvin Merrow age 62 unless DOB or age is explicitly reopened.
- Use MRN exactly as `KM-6427819`.
- Preserve lisinopril cough as the allergy/intolerance.
- Do not infer additional allergies.
- Do not infer new diagnoses from BMI.
- Do not draft World Spec or populate templates from this package until Alexander explicitly authorizes drafting.

## Review Addendum

Claude hostile-review implementation notes are recorded in `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.

These notes do not reopen Identity Package v1. They only carry forward future implementation requirements: treat lisinopril cough as an ACE-inhibitor intolerance, eventually provide coherent prior ACE-inhibitor-to-ARNI medication history, and explicitly place baseline anchors such as baseline function, baseline creatinine, dry weight, and similar comparison points during Patient Profile / Clinical History design.

## Final Status

Identity Package v1
Status: LOCKED
