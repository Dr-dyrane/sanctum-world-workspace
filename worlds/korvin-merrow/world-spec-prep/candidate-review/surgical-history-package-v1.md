# Surgical History Package v1

Date created: 2026-06-01

Status: CANDIDATE REVIEW.

Purpose: define the pre-world surgical and procedural history architecture for Korvin Merrow before Daily Hospital Course Framework construction, World Spec drafting, file inventory planning, synthetic documents, task prompts, expected outputs, golden responses, or grader guidance.

This package answers: what surgical and procedural history exists before the world begins, and what role does it play in the case?

This package does not create operative reports, procedure notes, hospital-course events, labs, vitals, file inventory, task prompts, expected outputs, golden responses, grader guidance, synthetic files, World Spec prose, templates, or reference files.

## Source Constraints

Use only:

- Approved Brainstorm.
- Locked Identity Package v1.
- Ratified Governance Package v1.
- Locked Baseline Anchor Package v1.
- Locked Clinical Story Timeline Package v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Locked Provider Roster Package v1.
- Current Clinical Logic.

## Design Standard

Surgical and procedural history should be clinically realistic but quiet.

It should:

- support existing comorbidity and medication architecture;
- provide plausible provenance for CAD and OSA;
- avoid creating a new dominant disease arc;
- avoid explaining the current presentation by itself;
- avoid weakening the mixed-physiology model;
- avoid becoming a hidden answer to functional decline, steroid interpretation, AKI/HF medication tension, or discharge safety.

## 1. Surgical History Inventory

| Item | Procedure | Approximate timeframe | Clinical rationale | Current relevance | Source-of-truth implications | Future document relevance | Classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Percutaneous coronary intervention with coronary stent placement | Remote pre-world history, several years before admission | Fits established CAD and supports chronic secondary-prevention therapy. | Supports aspirin, statin, nitroglycerin rescue medication, cardiology involvement, and the importance of not losing protective therapy during discharge medication reconciliation. | Most authoritative source would be cardiology history, prior procedure summary, or outpatient problem list; patient/family recollection may be less precise. | May later appear as prior cardiac procedure history in admission history, cardiology consult background, PCP records, or discharge summary history section. | Confirmed |
| 2 | Diagnostic sleep study confirming obstructive sleep apnea | Remote pre-world history, before current hospitalization | Fits locked OSA diagnosis and baseline fatigue/functional-reserve context without creating an acute procedural issue. | Supports OSA as a chronic comorbidity and background contributor to reduced reserve, but does not explain the acute decline alone. | Most authoritative source would be outpatient sleep medicine or PCP documentation; family/patient may report CPAP use or nonuse imprecisely. | May later appear in baseline medical history, PCP records, or functional/disposition context if sleep quality or home routine is relevant. | Confirmed |
| 3 | Coronary artery bypass grafting | Not included | Would be plausible for some CAD/HFrEF patients but is not required by the current architecture. | Would add unnecessary cardiac-surgical complexity and could over-intensify the cardiac history beyond what is needed. | Not applicable. | Not planned. | Unnecessary |
| 4 | Dialysis access creation or kidney procedure | Not included | CKD stage 3 does not justify dialysis-access history. | Would contradict the intended CKD3 baseline and create a renal arc that is too advanced for this world. | Not applicable. | Not planned. | Unnecessary |
| 5 | Major orthopedic fracture repair or joint replacement | Not included | Osteoporosis/osteopenia increases fall-consequence risk, but no fracture-repair history is needed. | Could distract from the intentionally multi-factorial near-fall model and create a competing mobility explanation. | Not applicable. | Not planned. | Unnecessary |
| 6 | Limb amputation or major diabetic foot surgery | Not included | Diabetic neuropathy supports mobility vulnerability, but no major diabetic foot procedural history is needed. | Would create a dominant functional-disability arc and weaken the current baseline of independent but slowed function. | Not applicable. | Not planned. | Unnecessary |
| 7 | Temporal artery biopsy or rheumatologic diagnostic procedure | Not included | PMR does not require a procedural history for this world. | Could introduce giant-cell arteritis or a separate rheumatologic diagnostic arc not approved in the Brainstorm. | Not applicable. | Not planned. | Unnecessary |
| 8 | Screening colonoscopy | Background-only if needed later | Common for age-appropriate preventive care, but not required by the current architecture. | Does not support the active frictions, traps, medication reasoning, or discharge-safety failure target. | Not needed for source-of-truth hierarchy. | Do not include unless later source material requires routine preventive-history texture. | Unnecessary for v1 |

## 2. Surgical History Classification

### Confirmed

- Remote percutaneous coronary intervention with coronary stent placement.
- Remote diagnostic sleep study confirming obstructive sleep apnea.

### Presumed

None.

Rationale: no procedure should be presumed merely to add realism. If a procedure matters architecturally, it should be explicit. If it does not matter, it should remain out of the package.

### Unnecessary

- Coronary artery bypass grafting.
- Dialysis access creation or kidney procedure.
- Major orthopedic fracture repair or joint replacement.
- Limb amputation or major diabetic foot surgery.
- Temporal artery biopsy or rheumatologic diagnostic procedure.
- Screening colonoscopy for v1 purposes.

Rationale: these procedures either create unnecessary complexity, imply a more advanced disease course than approved, or distract from the existing functional/disposition and mixed-physiology design.

## 3. Comorbidity Compatibility Review

### CAD

Support:

- Remote PCI with stent placement directly supports established CAD.
- It strengthens aspirin/statin/nitroglycerin and cardiology-background logic.

Guardrail:

- Do not convert the current admission into an acute coronary syndrome or post-procedural complication story.

### HFrEF

Support:

- PCI is compatible with ischemic cardiomyopathy or CAD-associated HFrEF history without requiring a new cardiac arc.

Guardrail:

- HFrEF remains a chronic contributor to medication restart tension, not the single explanation for weakness, hypotension, or discharge risk.

### CKD Stage 3

Support:

- No kidney procedure is added.

Guardrail:

- Avoid dialysis-access or transplant history because those would contradict the intended CKD3 baseline and alter nephrology stakes.

### Type 2 Diabetes Mellitus

Support:

- No diabetic foot surgery or amputation is added.
- This preserves diabetic peripheral neuropathy as a functional-reserve contributor rather than a dominant disability.

Guardrail:

- Diabetes remains part of chronic disease and medication complexity, not a limb-loss or wound-care world.

### PMR

Support:

- No PMR procedure is needed.
- Steroid history remains document-driven rather than procedure-driven.

Guardrail:

- Avoid temporal artery biopsy or giant-cell arteritis implications unless Alexander explicitly creates that arc later.

### Osteoporosis / Osteopenia

Support:

- No fracture-repair history is added.
- Osteoporosis remains a fall-consequence and steroid-exposure context, not evidence that a major fall/fracture already occurred.

Guardrail:

- The near-fall remains multi-factorial and not explained by prior orthopedic disease.

### Obstructive Sleep Apnea

Support:

- Diagnostic sleep study confirms the diagnosis without adding an acute procedural burden.

Guardrail:

- OSA remains background functional reserve context, not the main cause of altered mental status or hospitalization.

### Functional Decline Story

Support:

- The surgical history is deliberately limited so functional decline continues to arise from mixed physiology, polypharmacy, deconditioning, neuropathy, infection physiology, poor intake, and steroid-related physiology.

Guardrail:

- Do not add procedures that would make functional limitation obvious or single-cause.

## 4. Medication Compatibility Review

### 20-Medication Baseline Architecture

Compatibility:

- PCI supports aspirin, atorvastatin, and nitroglycerin rescue medication.
- OSA sleep-study history does not require new medications.

Assessment: compatible.

### Prednisone Architecture

Compatibility:

- No rheumatologic procedure is added.
- Prednisone source-of-truth remains based on rheumatology recommendation, verified medication reconciliation, pharmacy/refill history, family report, and patient recollection.

Assessment: compatible.

### HF/AKI Medication Trap

Compatibility:

- PCI strengthens why cardiology cares about chronic protective therapy.
- It does not alter renal recovery, hypotension risk, or acute medication-hold logic.

Assessment: compatible.

## 5. Friction Compatibility Review

### Cardiology vs Nephrology

Compatibility:

- Remote PCI supports cardiology's long-term protective-therapy perspective.
- It does not make cardiology automatically correct, and it does not erase nephrology's AKI/hypotension safety concerns.

Assessment: preserved.

### Family vs Primary Team

Compatibility:

- Surgical history does not create a new obvious functional baseline explanation.
- Family concerns remain rooted in deviation from baseline, cognition, mobility, medication management, and home safety.

Assessment: preserved.

### Endocrinology vs Primary Team

Compatibility:

- No procedure is added that reframes the steroid issue.
- The steroid conflict remains a risk-interpretation disagreement, with documentation discrepancy as a trap.

Assessment: preserved.

## 6. Trap Compatibility Review

### Trap #1: Steroid Timeline / Source-of-Truth Trap

Compatibility:

- No surgical/procedural history reveals the steroid answer.
- No rheumatologic procedure is added that would shift the steroid story toward a different disease.

Assessment: preserved.

### Trap #2: HF/AKI Medication Reconciliation Trap

Compatibility:

- PCI increases the credibility of chronic cardiovascular medication stakes.
- It does not determine when medications should be restarted after AKI/hypotension.

Assessment: strengthened without collapse.

### Trap #3: Buried Functional / Cognitive Status Trap

Compatibility:

- No orthopedic, amputation, or major mobility-limiting procedure is added.
- Functional/cognitive risk must still be found in nursing, PT/OT, family, and functional documentation later.

Assessment: preserved.

### Trap #5: Discharge Source-Hierarchy Trap

Compatibility:

- Surgical history does not create a discharge artifact or source-hierarchy shortcut.
- Visible discharge artifacts must still be tested against functional evidence, medication changes, consultant notes, and family concerns later.

Assessment: preserved.

### Mixed-Physiology / Reveal-Drift Risk

Compatibility:

- Surgical history remains background architecture.
- It does not reveal the hidden cause of near-fall, weakness, hypotension, altered mental status, or discharge risk.

Assessment: preserved.

## 7. Future Construction Compatibility

### Daily Hospital Course Framework

Compatibility:

- Surgical history can appear as background past history without creating hospital-day events.
- No admission procedures or inpatient procedural decisions are created.

### File Inventory Architecture

Compatibility:

- Surgical history establishes possible provenance types but creates no file names, file counts, document dates, or Section 3 rows.
- Later file inventory may decide whether PCI history and sleep-study history appear in admission history, consultant history, PCP documentation, or problem-list summaries.

### World Spec Construction

Compatibility:

- The package can later support Patient Profile / Clinical History and comorbidity realism.
- It is not World Spec prose and should not be pasted as a final section.

### Task Construction

Compatibility:

- Surgical history may support medication reconciliation and discharge summary accuracy.
- It does not create a new task concept.

### Goldens And Grader Guidance

Compatibility:

- Future goldens/grader guidance may account for surgical history only if the authorized task requires accurate past-history synthesis.
- This package does not create expected outputs, goldens, or grader criteria.

## Surgical History Consistency Review

### VERIFIED

Finding: the package includes only procedures justified by existing architecture.

Evidence: PCI supports established CAD and cardiovascular medication reasoning; diagnostic sleep study supports locked OSA. Other plausible procedures are explicitly excluded or deferred.

Impact: surgical/procedural history strengthens realism without adding unrelated complexity.

Action required: physician review should confirm whether PCI and sleep study should remain the only confirmed procedures.

### VERIFIED

Finding: no unnecessary surgical complexity is introduced.

Evidence: CABG, dialysis access, orthopedic repair, amputation/diabetic foot surgery, rheumatologic biopsy, and screening colonoscopy are not included as active architecture.

Impact: the world remains focused on mixed physiology, medication reasoning, functional decline, and discharge safety.

Action required: do not add procedures solely to make the history look fuller.

### VERIFIED

Finding: surgical history is compatible with the 14-condition comorbidity package.

Evidence: confirmed procedures map to CAD and OSA only and do not contradict CKD3, diabetes, PMR, osteoporosis/osteopenia, or functional baseline.

Impact: no comorbidity redesign required.

Action required: none before physician review.

### VERIFIED

Finding: surgical history is compatible with the 20-medication baseline architecture.

Evidence: PCI supports existing CAD medications; diagnostic sleep study does not require medication changes or new medications.

Impact: no medication architecture change required.

Action required: none before physician review.

### VERIFIED

Finding: no source-of-truth conflict is created.

Evidence: the package identifies likely future provenance sources but creates no documents, dates, file names, or contradictory accounts.

Impact: source hierarchy remains available for later construction.

Action required: later file construction should decide where the procedural history is evidenced.

### VERIFIED

Finding: reveal-drift risk is controlled.

Evidence: no procedure explains the admission, near-fall, steroid concern, AKI, or discharge readiness by itself.

Impact: mixed physiology and uncertainty remain intact.

Action required: preserve this restraint during Daily Hospital Course Framework and file planning.

### PLAUSIBLE

Finding: screening colonoscopy is reasonable real-world background but unnecessary for v1.

Evidence: it is common for a 62-year-old but does not support the current frictions, traps, medication architecture, or discharge-safety target.

Impact: excluding it avoids low-yield chart noise.

Action required: include only if later source/reference requirements or Alexander's clinical design calls for routine preventive-history texture.

### NO ISSUE

Finding: no operative reports, procedure notes, hospital-course events, labs, vitals, file inventory, task prompts, expected outputs, golden responses, grader guidance, synthetic files, World Spec prose, templates, or reference files are created.

Evidence: the package is limited to surgical/procedural history architecture and compatibility review.

Impact: phase boundary remains intact.

Action required: stop before downstream construction.

### DISPUTED

Finding: none.

Evidence: no proposed included procedure contradicts the approved Brainstorm, locked Identity Package, ratified Governance Package, locked Baseline Anchor Package, locked Clinical Story Timeline Package, locked Medication Expansion Package, locked Comorbidity Expansion Package, locked Provider Roster Package, or current Clinical Logic.

Impact: no redesign required before physician review.

Action required: none.

## Final Status

Surgical History Package v1

Status: CANDIDATE REVIEW
