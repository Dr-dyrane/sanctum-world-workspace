# Comorbidity Expansion Package v1

Date created: 2026-05-31

Status: LOCKED.

Purpose: define the baseline chronic-condition architecture for Korvin Merrow before labs, hospital-course events, task drafting, file planning, or World Spec drafting.

This package answers: what chronic conditions exist in the world at baseline, and why?

This package does not create labs, vitals, medication doses, medication schedules, hospital-course events, provider names, surgical history, tasks, task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

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
- Locked Medication Expansion Package v1.
- Current Clinical Logic.

## Target

- Approximately 12-15 baseline comorbidities.
- Preserve all already-approved conditions.
- Do not create new dominant disease arcs.
- Do not create conditions that answer open clinical questions.
- Do not create conditions that collapse mixed physiology.
- Do not create conditions solely to increase count.

Ratified baseline comorbidity count: 14 conditions.

## 1. Comorbidity Architecture Expansion

| # | Condition | Why it exists | Relationship to current architecture | Architectural role | Supports frictions | Supports traps | Supports baseline realism | Supports disposition safety | Supports medication complexity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Heart failure with reduced ejection fraction | Already approved established cardiovascular disease. | Central to Cardiology vs Nephrology and the HF/AKI medication-restart problem. | Creates high-stakes long-term therapy that cannot simply be ignored during AKI. | Yes, strongly. | Yes, HF/AKI medication and outdated consultant recommendation traps. | Yes. | Yes, readmission and functional reserve risk. | Yes, GDMT burden. |
| 2 | Coronary artery disease | Already approved established cardiovascular disease. | Supports chronic protective therapy and cardiology involvement. | Adds realistic secondary-prevention stakes without becoming the main acute diagnosis. | Yes, with Cardiology vs Nephrology. | Yes, medication reconciliation and discharge safety. | Yes. | Yes, risk if protective therapy is omitted. | Yes, antiplatelet/statin/rescue medication logic. |
| 3 | Hypertension | Already approved chronic condition. | Fits CKD, CAD, HFrEF, and long-term medication complexity. | Supports hemodynamic tension when BP remains borderline after acute illness. | Yes, secondary support. | Yes, temporal clinical context and medication safety traps. | Yes. | Yes, because hypotension risk affects safe discharge. | Yes. |
| 4 | Hyperlipidemia | Reviewer-approved expansion and already incorporated after Brainstorm SEND BACK. | Fits CAD and statin therapy. | Provides routine chronic disease realism and secondary prevention. | Indirectly. | Yes, discharge medication reconciliation. | Yes. | Indirectly. | Yes, chronic protective medication preservation. |
| 5 | Chronic kidney disease stage 3 | Already approved baseline renal disease. | Central to AKI-on-CKD reasoning and nephrology involvement. | Makes renal recovery, medication holds, and restart timing clinically meaningful. | Yes, strongly with Nephrology vs Cardiology. | Yes, HF/AKI medication, temporal labs/context, outdated recommendations. | Yes. | Yes, renal recovery affects discharge safety. | Yes, renal-sensitive medications. |
| 6 | Type 2 diabetes mellitus | Already approved long-standing condition. | Supports A1c baseline anchor, SGLT2/metformin/basal insulin logic, infection vulnerability, and neuropathy. | Adds metabolic chronic disease burden and medication-management complexity. | Indirectly. | Yes, medication reconciliation and discharge safety. | Yes. | Yes, self-management and follow-up burden. | Yes, strongly. |
| 7 | Diabetic peripheral neuropathy | Already approved complication of diabetes. | Supports baseline mobility vulnerability and multi-factorial near-fall design. | Reinforces functional decline without making the near-fall single-cause. | Yes, through Family vs Primary Team. | Yes, buried functional/cognitive status and discharge safety traps. | Yes. | Yes, strongly. | Yes, gabapentin-related complexity. |
| 8 | Obstructive sleep apnea | Reviewer-approved expansion and ratified governance condition. | Fits BMI 30.6, cardiometabolic disease, fatigue, and baseline functional reserve. | Adds realistic chronic burden without explaining the acute presentation by itself. | Indirectly. | Indirectly, functional/cognitive and discharge safety traps. | Yes. | Yes, fatigue/safety context. | No major medication effect. |
| 9 | Polymyalgia rheumatica | Already approved inflammatory condition. | Central substrate for chronic prednisone exposure and taper uncertainty. | Supports steroid timeline/source-of-truth trap without making adrenal insufficiency the hidden answer. | Yes, Endocrinology vs Primary Team. | Yes, steroid source-of-truth and sepsis anchoring after partial improvement. | Yes. | Yes, weakness/fatigue ambiguity. | Yes, prednisone and bone/GI protection logic. |
| 10 | Anemia of CKD | Reviewer-approved expansion and ratified governance condition. | Fits CKD and baseline hemoglobin anchor. | Adds chronic disease burden and fatigue vulnerability without creating a new acute diagnosis. | Indirectly. | Yes, temporal clinical context and discharge safety traps. | Yes. | Yes, contributes to reduced reserve. | Yes, iron therapy and bowel regimen complexity. |
| 11 | Osteoporosis / osteopenia from chronic steroid exposure | Reviewer-approved expansion and ratified governance condition. | Confirms cumulative steroid exposure but does not prove current adrenal suppression. | Reinforces steroid-history realism and chronic medication burden. | Indirectly supports Endocrinology vs Primary Team. | Yes, steroid source-of-truth trap as corroborating context. | Yes. | Yes, fall-consequence risk without making fall etiology single-cause. | Yes, bone-health medications/supplements. |
| 12 | Class I obesity by BMI | Directly supported by locked Identity Package BMI 30.6. | Fits OSA, diabetes, hypertension, HFrEF, mobility reserve, and discharge planning. | Adds baseline realism from already-locked anthropometrics without creating a new disease arc. | Indirectly, Family vs Primary Team. | Indirectly, functional/discharge safety traps. | Yes, strongly. | Yes, mobility and rehab planning context. | Indirectly. |
| 13 | Chronic gastroesophageal reflux / chronic acid-suppression indication | Supported by medication architecture and chronic aspirin/steroid exposure context. | Fits pantoprazole as a secondary chronic medication without creating a dominant GI arc. | Adds realistic chronic supportive-medication burden and reconciliation complexity. | No major direct support. | Yes, medication reconciliation/source-of-truth traps. | Yes. | Indirectly. | Yes, supportive-medication classification. |
| 14 | Chronic constipation tendency | Supported by iron therapy, gabapentin, reduced mobility, and polypharmacy context. | Fits polyethylene glycol and senna as secondary chronic/supportive medications. | Adds real-world medication burden and discharge instruction complexity without changing the core story. | Indirectly, Family vs Primary Team. | Yes, discharge safety and medication reconciliation traps. | Yes. | Yes, home regimen complexity. | Yes, bowel regimen duplication/continuation logic. |

## 2. Preservation Of Existing Architecture

### VERIFIED

Finding: all already-approved baseline conditions are preserved.

Evidence: the package retains HFrEF, CKD stage 3, type 2 diabetes, CAD, hypertension, hyperlipidemia, OSA, diabetic neuropathy, PMR, anemia of CKD, and osteoporosis/osteopenia.

Impact: no approved Brainstorm, Governance, or reviewer-remediation condition is removed.

Action required: locked; preserve the three retained secondary conditions unless Alexander explicitly reopens the package.

### VERIFIED

Finding: no added condition becomes a new dominant disease arc.

Evidence: class I obesity, chronic GERD/acid-suppression indication, and chronic constipation tendency are secondary baseline conditions that support existing medication, mobility, and discharge-safety architecture.

Impact: the world remains a mixed-physiology hospital medicine case rather than becoming a new obesity, GI, or bowel-regimen case.

Action required: later construction should keep these conditions as background complexity unless Alexander explicitly elevates one.

### VERIFIED

Finding: no added condition answers an open clinical question.

Evidence: none of the added conditions determines the infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, medication contribution, or discharge readiness.

Impact: presumed/active questions remain open and clinically uncertain.

Action required: do not use these additions to resolve the acute presentation.

## 3. Trap Support Review

### Steroid Timeline / Source-of-Truth Trap

Support:

- PMR remains the primary condition substrate.
- Osteoporosis/osteopenia supports cumulative chronic steroid exposure.
- GERD/acid-suppression medication can later corroborate chronic aspirin/steroid exposure context without proving current adrenal suppression.

Guardrail:

- Steroid-related bone disease and acid suppression do not prove adrenal insufficiency. Current steroid/adrenal contribution remains an active interpretive question.

### HF-AKI Medication Reconciliation Trap

Support:

- HFrEF, CAD, hypertension, CKD stage 3, diabetes, and hyperlipidemia support a realistic chronic cardiometabolic medication burden.
- The condition architecture preserves a clinical reason for both medication holds and later restart review.

Guardrail:

- Do not make renal or cardiac medication management the only meaningful trap; discharge safety and steroid source-of-truth must remain independent.

### Buried Functional / Cognitive Status Trap

Support:

- Diabetic neuropathy, OSA, anemia of CKD, class I obesity, PMR, and chronic disease burden all plausibly reduce functional reserve.
- These conditions support functional decline without creating a single-cause explanation for weakness, confusion, or near-fall.

Guardrail:

- Functional decline remains multi-factorial and must later be supported by nursing, PT/OT, family, and progress-note evidence.

### Sepsis Anchoring After Partial Improvement Trap

Support:

- Diabetes, CKD, HFrEF, PMR/steroid exposure, and anemia all make partial recovery more complex than "infection treated, patient fixed."
- Persistent weakness and discharge concern remain plausible after infection improvement.

Guardrail:

- Infection may be real or reasonable initially, but it should not explain the entire hospitalization.

### Discharge Safety / Source-Hierarchy Trap

Support:

- The total chronic condition burden makes discharge planning genuinely difficult.
- Functional reserve, medication self-management, family support, and follow-up planning remain clinically meaningful.

Guardrail:

- Later discharge artifacts must not be so complete that they erase the need for synthesis across functional evidence, medication changes, consultant notes, and family concerns.

## 4. Friction Support Review

### Cardiology vs Nephrology

Support:

- HFrEF, CAD, hypertension, CKD stage 3, diabetes, and hyperlipidemia make both cardiovascular protection and renal/hemodynamic caution clinically defensible.

Assessment: strongly supported.

### Family vs Primary Team

Support:

- Diabetic neuropathy, OSA, anemia of CKD, obesity, PMR, osteoporosis/osteopenia, chronic constipation tendency, and total medication burden reinforce why family may see a patient who is not safely back to baseline.
- Infection improvement, AKI improvement, improved intake, and follow-up can still make discharge clinically defensible from the primary team's perspective.

Assessment: strongly supported.

### Endocrinology vs Primary Team

Support:

- PMR remains the central condition.
- Osteoporosis/osteopenia and related supportive therapy corroborate chronic steroid exposure.
- These conditions do not convert adrenal insufficiency into a hidden reveal.

Assessment: adequately supported with guardrail against reveal-drift.

## 5. Future Construction Compatibility

### VERIFIED

Finding: compatible with locked Medication Expansion Package v1.

Evidence: the 14-condition architecture supports the 20-medication baseline architecture without requiring new medications, doses, schedules, or medication timelines.

Impact: medication reconciliation reasoning remains available without being pre-written.

Action required: later medication construction should preserve this condition-to-medication rationale.

### VERIFIED

Finding: compatible with locked Baseline Anchor Package v1.

Evidence: baseline creatinine/eGFR, hemoglobin, A1c, dry weight, mobility, cognition, medication-management ability, and home support all have condition-level anchors in this package.

Impact: baseline anchors become clinically motivated without creating admission values.

Action required: do not create numeric admission or hospital-course values here.

### VERIFIED

Finding: compatible with locked Clinical Story Timeline Package v1.

Evidence: the condition architecture supports the three-week decline, mixed physiology, partial improvement, and discharge-safety tension without adding new hospital-course events.

Impact: timeline remains intact.

Action required: defer event-level details until the authorized construction step.

### VERIFIED

Finding: compatible with locked Task Architecture Package v1.

Evidence: the comorbidity burden supports discharge medication reconciliation, discharge summary generation, discharge planning documentation, and interdisciplinary care planning without creating final task prompts or deliverables.

Impact: task architecture remains intact.

Action required: do not create task prompts, expected outputs, or grader logic here.

### PLAUSIBLE

Finding: surgical-history documentation can remain independent.

Evidence: none of the 14 conditions requires a surgical history to be invented now.

Impact: future surgical-history package can be developed without contradiction.

Action required: do not create surgical history in this package.

### PLAUSIBLE

Finding: named-provider roster can later assign ownership without changing condition logic.

Evidence: the condition architecture naturally supports hospitalist, cardiology, nephrology, endocrinology, PCP, PT/OT, case management, and social work perspectives.

Impact: provider roster construction remains flexible.

Action required: do not create provider names here.

## Comorbidity Expansion Consistency Review

### VERIFIED

Finding: the package reaches the target comorbidity range.

Evidence: 14 ratified baseline conditions are listed, within the target range of approximately 12-15.

Impact: satisfies the reviewer-driven complexity target without padding the case with unrelated diagnoses.

Action required: preserve during later authorized construction.

### VERIFIED

Finding: the package is consistent with governance.

Evidence: it preserves the ratified confirmed conditions and keeps presumed/active questions unresolved.

Impact: Governance Package v1 remains authoritative.

Action required: none.

### VERIFIED

Finding: mixed physiology is preserved.

Evidence: chronic conditions support infection vulnerability, steroid complexity, CKD/HF physiology, polypharmacy, baseline functional vulnerability, and discharge safety without reducing the story to one diagnosis.

Impact: core world design remains intact.

Action required: later construction must continue to avoid reveal-drift.

### VERIFIED

Finding: discharge-safety reasoning is strengthened.

Evidence: neuropathy, anemia, OSA, obesity, PMR, osteoporosis/osteopenia, CKD, HFrEF, and medication-burden-linked supportive conditions all make functional reserve and home safety realistic concerns.

Impact: supports the primary failure target: disposition safety, functional decline recognition, and discharge-readiness reasoning.

Action required: later document construction must make the evidence discoverable across multiple files.

### PLAUSIBLE

Finding: GERD/acid-suppression indication and chronic constipation tendency are useful secondary additions.

Evidence: both fit the locked medication package and polypharmacy logic, but they are intentionally not major disease arcs.

Impact: they strengthen medication complexity and real-world discharge burden.

Action required: preserve as secondary complexity during later construction; do not elevate into dominant arcs.

### NO ISSUE

Finding: the package does not create labs, vitals, hospital events, provider names, surgical history, tasks, file inventory, World Spec prose, templates, reference files, or synthetic documents.

Evidence: the document is limited to condition-level baseline architecture and consistency review.

Impact: phase boundary remains intact.

Action required: stop before downstream construction.

### DISPUTED

Finding: none.

Evidence: no ratified condition contradicts the approved Brainstorm, ratified Clinical Story Skeleton, locked Identity Package, ratified Governance Package, locked Timeline Package, locked Baseline Anchor Package, locked Task Architecture Package, or locked Medication Expansion Package.

Impact: no redesign required.

Action required: none.

## Final Status

Comorbidity Expansion Package v1

Status: LOCKED
