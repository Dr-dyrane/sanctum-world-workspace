# Baseline Anchor Package v1

Date created: 2026-05-31

Status: CANDIDATE REVIEW.

Purpose: define candidate baseline comparator values and baseline function anchors needed for later World Spec construction.

This package is for physician review. It does not create admission labs, hospital-course lab trends, file inventory, task architecture, World Spec prose, prompts, golden responses, grader guidance, templates, reference files, or synthetic files.

## Source Constraints

Use only as candidate baseline anchors for future construction:

- Ratified Clinical Story Skeleton v1.
- Locked Identity Package v1.
- Ratified Governance Package v1.
- Locked Key Milestones Calendar Skeleton v1.
- Current clinical logic.

## Candidate Baseline Anchors

| Anchor | Candidate Baseline | Rationale For Review | Construction Use Later |
| --- | --- | --- | --- |
| Baseline functional status | Independent with ADLs; slower pace from chronic illness; lives with family; family provides intermittent support. | Matches ratified Clinical Story Skeleton. | Comparator for functional decline and discharge-readiness reasoning. |
| Baseline creatinine | 1.6-1.8 mg/dL. | Plausible CKD stage 3 baseline in a 62-year-old with diabetes, hypertension, HFrEF, and CAD. | Comparator for AKI and renal recovery. |
| Baseline eGFR | Approximately 40-50 mL/min/1.73 m2. | Consistent with CKD stage 3 and candidate creatinine range. | Comparator for renal medication safety and consultant recommendations. |
| Baseline hemoglobin | 10.5-11.5 g/dL. | Plausible anemia of CKD baseline. | Comparator for chronic anemia vs acute deterioration if needed later. |
| Baseline A1c | 7.6-8.2%. | Plausible long-standing type 2 diabetes with insulin plus metformin, avoiding an unrealistically perfect or extreme baseline. | Diabetes-control context for infection risk, steroid decisions, and discharge planning. |
| Dry weight | Approximately 96-98 kg; use 97 kg as working dry-weight candidate pending physician approval. | Aligns with locked weight 97 kg and HFrEF volume-status reasoning. | Comparator for dehydration/volume status and HF medication reasoning. |
| Baseline mobility | Ambulates without major assistance; occasional cane use for longer distances or bad days. | Matches locked story and allows later functional decline to be meaningful. | Comparator for PT/OT and discharge safety. |
| Baseline cognition | Mild age-related forgetfulness only; normally oriented and able to participate in daily routines. | Matches locked story and preserves altered mental status as deviation from baseline. | Comparator for confusion and family concern. |
| Baseline medication-management ability | Manages some medications himself with family oversight/support; complex regimen creates vulnerability. | Matches approved Brainstorm and supports medication-reconciliation trap. | Comparator for medication-management mistakes and discharge safety. |
| Baseline home support | Lives with family/caregiver support; family knows baseline function and cognition. | Matches approved family/team friction. | Comparator for transition planning and caregiver concern. |

## Candidate Review Questions For Alexander

- Confirm whether baseline creatinine range should be 1.6-1.8 mg/dL or adjusted.
- Confirm whether baseline eGFR range should be approximately 40-50 mL/min/1.73 m2.
- Confirm whether baseline hemoglobin range should be 10.5-11.5 g/dL.
- Confirm whether baseline A1c should be 7.6-8.2% or a single value later.
- Confirm whether 97 kg should serve as dry weight or whether locked weight and dry weight should differ.
- Confirm whether occasional cane use applies only outside the home / longer distances.

## Consistency Review

### VERIFIED

Finding: baseline functional status matches the ratified Clinical Story Skeleton.

Evidence: the skeleton states Korvin lives with family, is independent but slowed by chronic illness, uses an occasional cane, and has mild age-related forgetfulness only.

Impact: supports a clear comparator for functional decline.

Action required: Alexander should approve or refine the wording before it becomes World Spec content.

### VERIFIED

Finding: dry-weight candidate aligns with locked anthropometrics.

Evidence: locked Identity Package weight is 97 kg, and the candidate dry weight is approximately 96-98 kg with 97 kg as working candidate.

Impact: avoids conflict between identity package and future volume-status reasoning.

Action required: Alexander should decide whether dry weight equals locked weight or differs slightly.

### PLAUSIBLE

Finding: baseline creatinine and eGFR ranges fit CKD stage 3.

Evidence: creatinine 1.6-1.8 mg/dL and eGFR 40-50 mL/min/1.73 m2 are plausible for a 62-year-old male with diabetic/hypertensive CKD stage 3.

Impact: supports future AKI-on-CKD interpretation.

Action required: physician approval required before locking.

### PLAUSIBLE

Finding: baseline hemoglobin range fits anemia of CKD.

Evidence: hemoglobin 10.5-11.5 g/dL is plausible for chronic anemia of CKD without implying an acute anemia problem.

Impact: creates a baseline comparator without adding hospital-course trends.

Action required: physician approval required before locking.

### PLAUSIBLE

Finding: baseline A1c range fits long-standing type 2 diabetes on mixed therapy.

Evidence: A1c 7.6-8.2% is plausible for a medically complex patient on metformin plus basal insulin.

Impact: supports diabetes context without making glycemic control the central problem.

Action required: physician approval required before locking.

### NO ISSUE

Finding: this package does not create admission labs or hospital-course trends.

Evidence: all numeric values are labeled candidate baseline anchors only.

Impact: preserves phase boundary.

Action required: do not reuse these as admission values unless Alexander explicitly authorizes later.

### NO ISSUE

Finding: this package does not create file inventory, task architecture, prompts, goldens, grader guidance, templates, reference files, or synthetic files.

Evidence: package is limited to baseline comparator candidates and review questions.

Impact: World Spec construction boundaries remain intact.

Action required: stop before converting candidate anchors into final World Spec prose.

### DISPUTED

Finding: none.

Evidence: no candidate baseline anchor conflicts with ratified architecture, but numeric anchors remain unapproved.

Impact: no redesign required.

Action required: physician review before lock.

## Final Status

Baseline Anchor Package v1

Status: CANDIDATE REVIEW
