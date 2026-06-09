# Medication Expansion Package v1

Date created: 2026-05-31

Status: LOCKED.

Purpose: define the baseline medication architecture for Korvin Merrow before admission labs, hospital-course medication changes, medication reconciliation tasks, discharge medications, file inventory, or World Spec drafting.

This package answers: what medications exist in the world at baseline, and why?

This package does not create medication doses, medication frequencies, medication schedules, medication timelines, medication reconciliation outputs, hospital medication changes, admission medication lists, discharge medication lists, tasks, task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

All medication names below are candidate baseline architecture items for physician review. They are not locked final medication reconciliation content.

## Source Constraints

Use only:

- Approved Brainstorm.
- Ratified Clinical Story Skeleton v1.
- Locked Identity Package v1.
- Ratified Governance Package v1.
- Locked Key Milestones Calendar Skeleton v1.
- Locked Baseline Anchor Package v1.
- Locked Clinical Story Timeline Package v1.
- Locked Task Architecture Package v1.
- Current Clinical Logic.

## Target

- Approximately 18-22 baseline medications.
- Clinically realistic polypharmacy burden.
- Strong support for medication-reconciliation reasoning.
- Strong support for HF/AKI restart reasoning.
- Strong support for steroid source-of-truth reconstruction.
- Strong support for discharge-safety reasoning.

## 1. Medication Architecture Expansion

Candidate baseline medication count: 20 medication items.

### Core Cardiovascular Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Aspirin | Secondary prevention for CAD. | Fits established CAD history. | Supports discharge medication reconciliation and copy-forward risk. |
| Atorvastatin | Lipid management and CAD risk reduction. | Fits CAD and hyperlipidemia. | Provides chronic protective therapy that should not be lost during transition. |
| Nitroglycerin rescue medication | Symptom-directed CAD/angina safety medication. | Plausible for a patient with CAD history without adding a new dominant disease arc. | Adds reconciliation complexity because rescue/supportive medications are easy to omit or copy forward without context. |

### Heart-Failure Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Sacubitril/valsartan | HFrEF guideline-directed therapy. | Fits established HFrEF and prior ACE-inhibitor intolerance history. | Central to Cardiology vs Nephrology friction and HF/AKI restart reasoning. |
| Carvedilol | HFrEF and CAD therapy. | Fits HFrEF/CAD and creates hemodynamic decision tension during acute illness. | Supports hypotension/restart reasoning and consultant disagreement. |
| Furosemide | Volume management in HFrEF. | Fits HFrEF and dry-weight/volume-status framework. | Supports dehydration vs congestion reasoning and discharge safety. |
| Spironolactone | HFrEF guideline-directed therapy. | Fits HFrEF but interacts with CKD and electrolyte risk. | Supports HF/AKI medication trap and renal-safety reasoning. |
| Empagliflozin | HFrEF and diabetes therapy. | Fits HFrEF, type 2 diabetes, and CKD context. | Supports acute-illness hold/restart reasoning and medication reconciliation complexity. |

### CKD-Related / Anemia-Related Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Ferrous sulfate | Chronic anemia support. | Fits anemia of CKD and chronic disease burden. | Adds polypharmacy and constipation/discharge-safety considerations without becoming central. |

### Diabetes Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Metformin ER | Type 2 diabetes therapy. | Fits long-standing diabetes and baseline A1c framework, with renal/acute illness relevance. | Supports AKI-related medication safety and discharge restart reasoning. |
| Insulin glargine | Basal diabetes control. | Fits long-standing diabetes with imperfect baseline control. | Supports discharge medication-management ability and family safety concerns. |

Carry-forward note: insulin lispro is removed from baseline medication architecture and reserved as a future inpatient-only candidate medication during hospital-course construction. This preserves inpatient glycemic-management reasoning without over-expanding baseline outpatient medications.

### Neuropathy / Pain Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Gabapentin | Diabetic neuropathy symptom control. | Fits diabetic peripheral neuropathy and baseline mobility concerns. | Supports functional/cognitive safety reasoning because sedating medications may contribute to weakness or confusion. |
| Acetaminophen | Chronic pain or PMR-related symptom support. | Plausible supportive medication in chronic musculoskeletal disease. | Adds benign-looking medication burden and copy-forward risk. |

### Steroid-Related Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Prednisone | PMR management with uncertain taper status. | Fits ratified PMR/steroid timeline and prednisone source-of-truth hierarchy. | Central to steroid source-of-truth trap and Endocrinology vs Primary Team friction. |

### GI Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Pantoprazole | GI protection / reflux symptom support in a patient with aspirin and steroid exposure. | Clinically plausible in chronic aspirin/steroid context. | Adds reconciliation complexity and supports source-of-truth questions around what is chronic vs carried forward. |
| Polyethylene glycol | Constipation prevention or treatment. | Plausible with iron, reduced mobility, chronic disease, and hospitalization risk. | Adds discharge-safety complexity because supportive medications affect real-world medication burden. |
| Senna | Constipation regimen support. | Plausible adjunct in chronic constipation risk. | Adds duplicate/supportive-medication reconciliation challenge without changing the core disease arc. |

### Bone-Health Medications

| Medication | Purpose | Rationale | Architectural role |
| --- | --- | --- | --- |
| Alendronate | Osteoporosis/osteopenia treatment. | Fits chronic steroid exposure and reviewer-approved bone-health comorbidity. | Supports steroid-history realism and medication-list complexity. |
| Calcium carbonate / vitamin D combination | Bone-health support. | Fits steroid-related bone disease. | Supports chronic medication burden and reconciliation of supplements vs medications. |
| Cholecalciferol | Vitamin D repletion or maintenance. | Plausible in osteoporosis/osteopenia management. | Adds supplement/medication reconciliation complexity and source classification issues. |

### Other Clinically Justified Chronic Therapy

No additional unrelated chronic medication class is needed in v1. The candidate list already reaches the target complexity range without adding a new disease arc such as BPH, chronic lung disease, anticoagulation, opioid therapy, or psychiatric medication.

## 2. Polypharmacy Review

### VERIFIED

Finding: candidate medication burden meets the target range.

Evidence: the package identifies 20 baseline medication items, within the target of approximately 18-22.

Impact: supports reviewer expectations for complex inpatient medication reasoning without exceeding a plausible outpatient burden.

Action required: physician review should confirm whether any candidate medication feels artificial before lock.

### VERIFIED

Finding: medication burden is clinically realistic for the approved condition profile.

Evidence: the candidate list is driven by HFrEF, CAD, hypertension, CKD stage 3, type 2 diabetes, diabetic neuropathy, PMR with chronic prednisone exposure, anemia of CKD, osteoporosis/osteopenia, and supportive GI/bowel needs.

Impact: supports realism for a 62-year-old medically complex patient with chronic disease and acute hospitalization.

Action required: later construction must still avoid turning every medication into an active problem.

### VERIFIED

Finding: medication architecture supports medication-reconciliation complexity.

Evidence: the list includes chronic protective medications, acute-illness-sensitive medications, insulin, steroid therapy with uncertain taper status, supplements, rescue/supportive medications, and bowel/GI medications.

Impact: creates realistic opportunities for copy-forward errors, outdated medication holds, omitted supportive medications, and confusion about chronic vs temporary therapy.

Action required: do not create actual reconciliation outputs until the authorized task/file construction phase.

### PLAUSIBLE

Finding: candidate supportive medications are realistic but should remain secondary.

Evidence: pantoprazole, polyethylene glycol, senna, acetaminophen, and bone-health supplements are common in similar patients but are not central to the world.

Impact: strengthens medication burden and discharge safety without changing the core arc.

Action required: keep these as secondary complexity; avoid making them new major traps.

## 3. Trap Support Review

### Steroid Source-of-Truth Trap

Support:

- Prednisone remains the central medication for the steroid timeline/source-of-truth trap.
- Alendronate, calcium/vitamin D, cholecalciferol, and pantoprazole reinforce chronic steroid exposure without proving current adrenal suppression.

Risk:

- Steroid-related medications could accidentally make adrenal insufficiency look like the hidden answer.

Guardrail:

- Preserve the mixed-physiology model. Steroid risk is important but not dominant.

### HF/AKI Medication Trap

Support:

- Sacubitril/valsartan, carvedilol, furosemide, spironolactone, empagliflozin, metformin ER, and insulin therapies create realistic acute-illness medication reasoning.
- Cardiology and Nephrology can reasonably disagree about restart timing, renal recovery, hypotension risk, and long-term protection.

Risk:

- Overloading the medication trap could reduce task diversity.

Guardrail:

- Keep HF/AKI medication reasoning central to medication reconciliation and consultant synthesis, but secondary in summary/discharge-safety tasks when appropriate.

### Functional / Cognitive Decline Trap

Support:

- Gabapentin, insulin complexity, diuretics, HFrEF therapy, prednisone uncertainty, and supportive medications all plausibly contribute to medication-management vulnerability.
- Medication burden reinforces family concern that the patient may not safely manage the changed regimen.

Risk:

- Do not imply that one medication fully explains the near-fall or cognitive slowing.

Guardrail:

- Preserve the multi-factorial near-fall framework.

### Discharge-Safety Trap

Support:

- The number and diversity of medication classes make discharge instructions, home support, medication adherence, and follow-up planning realistically difficult.
- Supplements, rescue medications, bowel regimen medications, and insulin add real-world reconciliation burden beyond headline HF/diabetes drugs.

Risk:

- If the final discharge plan later appears too complete, the discharge-safety trap may weaken.

Guardrail:

- Later construction should keep discharge safety dependent on synthesis across medication plan, PT/OT, family concerns, consultant notes, and follow-up.

### Polypharmacy-Related Reasoning

Support:

- The medication architecture creates baseline polypharmacy without requiring a new diagnosis or rare medication interaction.
- Complexity comes from timing, source reliability, chronic vs temporary status, and patient ability to manage the regimen.

Risk:

- Adding too many marginal medications could feel like artificial complexity.

Guardrail:

- Candidate list should be physician-reviewed for plausibility and trimmed if any medication does not serve the world.

## 4. Friction Support Review

### Cardiology vs Nephrology

Support:

- Sacubitril/valsartan, carvedilol, furosemide, spironolactone, and empagliflozin directly support the medication restart friction.
- Metformin ER adds renal/acute illness medication safety reasoning without becoming a cardiology drug.

Assessment: strongly supported.

### Family vs Primary Team

Support:

- Insulin complexity, gabapentin, diuretics, supportive medications, bowel regimen medications, steroid uncertainty, and the total regimen burden support family concern about medication management and discharge safety.
- Primary Team can still reasonably view discharge as defensible if infection, renal function, mental status, and intake are improving.

Assessment: strongly supported.

### Endocrinology vs Primary Team

Support:

- Prednisone remains the direct friction substrate.
- Bone-health and GI medications corroborate chronic steroid exposure but do not prove current adrenal suppression.

Assessment: adequately supported with guardrail against reveal-drift.

## 5. Future Construction Compatibility

### VERIFIED

Finding: compatible with 12-15 comorbidity target.

Evidence: medications map to already approved conditions and leave room for later comorbidity refinement without requiring a new disease arc.

Impact: later comorbidity package can expand or refine without medication contradiction.

Action required: do not add new comorbidities inside this package.

### VERIFIED

Finding: compatible with named-provider roster package.

Evidence: medication architecture supports later outpatient PCP, rheumatology, cardiology, nephrology, endocrinology, pharmacy, and hospitalist documentation without naming providers now.

Impact: later provider roster can assign source responsibility without changing medication logic.

Action required: do not create provider names here.

### VERIFIED

Finding: compatible with surgical-history package.

Evidence: no medication requires a surgical history to make sense.

Impact: future surgical-history documentation can remain independent.

Action required: do not create surgical history here.

### VERIFIED

Finding: compatible with daily hospital-course framework.

Evidence: medication classes can be held, reviewed, reconciled, or continued later without this package specifying timing or orders.

Impact: daily hospital-course construction remains flexible.

Action required: defer hospital medication changes until explicitly authorized.

### VERIFIED

Finding: compatible with future medication reconciliation construction.

Evidence: this package establishes baseline medication existence and rationale only; it does not create admission, inpatient, or discharge med lists.

Impact: later med-rec work can build from this architecture without being pre-written.

Action required: preserve source-of-truth hierarchy when med-rec construction is authorized.

### VERIFIED

Finding: compatible with future file inventory architecture.

Evidence: no file names, document dates, or source files are created.

Impact: Section 3 file planning remains unstarted.

Action required: do not convert this package into a file plan.

## Medication Expansion Consistency Review

### VERIFIED

Finding: medication architecture is consistent with Governance Package v1.

Evidence: medication categories map to confirmed conditions and support the ratified frictions.

Impact: no governance redesign required.

Action required: ratification review before lock.

### VERIFIED

Finding: medication architecture is consistent with the locked Clinical Story Timeline Package.

Evidence: the package preserves mixed physiology, medication-management mistakes, HF/AKI medication tension, steroid uncertainty, and discharge safety without creating hospital-course medication events.

Impact: timeline remains intact.

Action required: none before ratification review.

### VERIFIED

Finding: medication architecture is consistent with the locked Baseline Anchor Package.

Evidence: medication logic uses baseline creatinine/eGFR, A1c, dry weight, mobility, cognition, medication-management ability, and home support as comparator concepts only.

Impact: baseline anchors remain useful without becoming admission values.

Action required: none before ratification review.

### VERIFIED

Finding: medication architecture supports approved frictions and traps.

Evidence: HF medications support Cardiology vs Nephrology; prednisone supports Endocrinology vs Primary Team; total regimen burden supports Family vs Primary Team and discharge safety.

Impact: strengthens current architecture without adding new frictions or traps.

Action required: none before ratification review.

### PLAUSIBLE

Finding: medication burden is realistic after physician decision resolution.

Evidence: 20 medications remains plausible for this comorbidity profile after removing insulin lispro from baseline architecture and reserving it as a future inpatient-only candidate.

Impact: the package remains within the 18-22 target range while preserving baseline diabetes architecture as metformin plus basal insulin.

Action required: carry forward into later authorized medication reconciliation and hospital-course construction.

### NO ISSUE

Finding: discharge-safety and source-of-truth design are preserved.

Evidence: the package creates no discharge list, no reconciliation output, and no medication timeline. It only defines baseline medication architecture.

Impact: downstream traps remain available.

Action required: stop before medication reconciliation construction.

### DISPUTED

Finding: none.

Evidence: no candidate medication contradicts the approved Brainstorm, ratified Governance Package, locked Timeline Package, or locked Baseline Anchor Package.

Impact: no redesign required.

Action required: none before physician review.

## Physician Decision Resolution

Accepted decisions:

- Remove insulin lispro from baseline medication architecture.
- Reserve insulin lispro as a future inpatient-only candidate medication during hospital-course construction.
- Preserve all other medications unchanged.
- Preserve all medication categories unchanged.
- Preserve all trap and friction rationale unchanged.

Result:

- Baseline medication architecture contains 20 medications.
- Medication Expansion Package v1 remains within the approved 18-22 target range.
- Baseline diabetes architecture remains aligned with the locked Baseline Anchor Package rationale: metformin plus basal insulin.
- Future inpatient glycemic-management reasoning remains available for discharge and medication-reconciliation construction.

## Final Status

Medication Expansion Package v1

Status: LOCKED
