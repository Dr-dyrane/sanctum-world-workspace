# Marva Lydell Brainstorm

## Concept pitch

Build a cardiopulmonary transition world around Marva Lydell, a 72-year-old Black woman admitted with acute decompensated heart failure, cardiorenal acute kidney injury, COPD and obstructive sleep apnea overlap, atrial fibrillation on anticoagulation, diabetes, and limited home support. The world closes when she is medically improving but not yet transition-safe. Her resting oxygen saturation looks acceptable, the creatinine is improving, and the discharge plan reads clean at a glance. The real work is in the contradictions: exertional hypoxemia, incomplete oxygen equipment delivery, unresolved volume risk, renal-dose medication decisions, anticoagulation source hierarchy, and a home setting that cannot absorb a premature handoff.

The world should test whether a model can move from chart summarization to transition judgment. A strong answer must not merely list cardiology, nephrology, respiratory therapy, therapy, and case-management facts. It must decide what is safe to sign, what remains open, which owner must act, and which external document is wrong.

## 1. World setup

| Field | Plan |
| --- | --- |
| World type | Typical clinical world |
| Patient | Marva Lydell, 72-year-old Black woman in the United States |
| Core admission | Acute decompensated heart failure with hypoxemia, cardiorenal acute kidney injury, atrial fibrillation, COPD/OSA overlap, diabetes, and functional decline |
| Snapshot close | 06/10/2026 at 18:00, after improvement on inpatient diuresis but before safe post-acute execution is complete |
| Task window | 06/11/2026 through 06/17/2026. All tasks occur after the world snapshot and use task-level files for post-snapshot prompts, denials, drafts, reports, or follow-up notes |
| World file strategy | At least 30 world-level files. Hospital course, cardiology, nephrology, respiratory therapy, PT/OT, case management, pharmacy, labs, weights, oxygen testing, sleep equipment notes, medication lists, discharge planning notes, and family communication. No task answers in world files |
| Knowledge boundary | No task requires post-July 2025 medical knowledge. The clinical reasoning is standard transition-of-care reasoning, and every needed fact is in the mounted chart or task-level file |
| Product thesis | The patient is not a data visualization. The product is readiness. Each task asks whether the record supports a safe next move |

## 2. Major friction points

| Friction | Why it works |
| --- | --- |
| Hospital medicine and cardiology versus payer medical director | The patient appears clinically improved, but the payer sees only stable resting vitals and misses exertional oxygen need, unresolved equipment, and post-acute skilled needs |
| Cardiology versus nephrology | Diuresis, kidney recovery, potassium, ACE inhibitor or SGLT2 restart, and anticoagulation all require ownership and timing. A model that treats improvement as resolution will close too much |
| Respiratory therapy and pulmonary versus case management and DME vendor | Resting oxygen and exertional oxygen tell different stories. DME status can look complete in one note while a vendor log shows portable equipment was not delivered |
| Patient and family preference versus functional safety | Marva wants home. A daughter can help intermittently. Therapy notes, stairs, fatigue, oxygen equipment, and medication complexity may still make the first plan unsafe |
| Pharmacy and SNF intake versus the inpatient chart | External medication or intake documents can carry forward the wrong anticoagulation dose, duplicate therapy, or stale renal dosing. The task should require source hierarchy, not transcription |
| Quality reviewer versus clinician author | A reviewer may ask for a clean documentation conclusion, while the right clinical answer is to leave control, equipment, or follow-up open with the correct owner |

## 3. Major traps

| Trap | Intended model miss | Fair catcher |
| --- | --- | --- |
| Resting oxygen hides exertional hypoxemia | Model writes that oxygen is stable because resting saturation is acceptable | Reads the walk-test or therapy signal and recognizes that exertional desaturation still needs oxygen planning |
| Equipment delivery over-closure | Model accepts "DME arranged" from discharge planning prose | Checks the vendor or delivery note showing the portable oxygen piece is not delivered or not functional |
| Volume status over-closure | Model treats improving creatinine or lower BNP as readiness | Reconciles weight, intake/output, edema, orthopnea, and renal trend before signing readiness |
| Renal-med restart drift | Model restarts ACE inhibitor, SGLT2 inhibitor, or metformin because discharge is near | Keeps restart deferred until renal and volume parameters are met, with a clear owner |
| Anticoagulation source hierarchy | Model follows an external intake or SNF list with a wrong dose or duplicate antiplatelet | Uses the chart, renal function, indication, bleeding history, and active orders to choose the safer reconciliation |
| Home support inflation | Model converts "daughter can check in" into a safe daily-care plan | Preserves the actual support limits and connects them to oxygen, stairs, medication complexity, and follow-up reliability |
| Sleep and respiratory control over-closure | Model writes COPD or OSA is controlled because the chart says home devices exist | Looks for actual device use, oxygen need, symptoms, or follow-up gaps before closing control |
| Denial-letter authority bias | Model softens the appeal because the payer denial is structured and official | Refutes the denial using the chart facts that make skilled or equipment-level care necessary |
| Readmission attribution shortcut | Model blames nonadherence after a bounceback | Finds the system failure, such as incomplete equipment delivery, unsafe medication handoff, or missing monitoring plan |

## 4. Rough task ideas

| ID | Working title | Workflow fit | Task-level file shape | Central catch |
| --- | --- | --- | --- | --- |
| ML01 | Oxygen and SNF denial appeal | Claims Denial Analysis and Appeal Preparation | Payer denial plus quiet transfer-day oxygen or therapy addendum | Resting saturation does not answer exertional oxygen need or skilled transition risk |
| ML02 | Discharge medication reconciliation | Discharge Medication Reconciliation at Care Transitions | External discharge medication list or SNF intake list | Stop or correct a stale renal or anticoagulation item while keeping open renal restarts open |
| ML03 | Continued-stay review | Utilization Review Concurrent Stay Documentation | Utilization review worksheet with tempting "medically stable" language | Medical improvement is not transition readiness when oxygen equipment and exertional function remain unresolved |
| ML04 | Transition note completion | Medical Transcription and Clinical Documentation Completion | Started transition note with true blanks and one weak external claim | Complete the note without closing oxygen, volume, or follow-up items that are still open |
| ML05 | Post-acute coordination plan | Post-Acute Care Coordination Documentation | Case-management handoff draft and DME vendor status | Identify the missing equipment and owner before signing the transfer plan |
| ML06 | Cardiorenal follow-up letter | Specialist Referral Letter and Documentation Preparation | Started cardiology-nephrology follow-up note | Route diuretic, kidney-function, potassium, anticoagulation, and restart decisions to the right follow-up owner |
| ML07 | Home health versus SNF appeal | Claims Denial Analysis and Appeal Preparation | Home-health denial response packet | Show why home health does not meet oxygen, monitoring, and functional needs without overstating the chart |
| ML08 | Safety event review after bounceback | Patient Safety Event Investigation and Root Cause Analysis | Readmission event note and equipment delivery record | Attribute the event to the unsafe transition gap, not patient nonadherence |
| ML09 | Quality abstraction review | HEDIS Medical Record Chart Abstraction and Review | Abstractor worksheet with source conflicts | Abstract the documented measure only, and do not award a clean transition when key evidence is missing |
| ML10 | Documentation query response | Clinical Documentation Improvement Query Response Review | CDI query about acute hypoxic respiratory failure or cardiorenal AKI | Answer with supported specificity while rejecting unsupported over-claims |

## 5. Why this should be harder than a generic cardiology world

The model will be strong at reading heart-failure notes, pulling labs, naming the medication classes, and writing a polished discharge plan. That is not enough here. The failure axis is readiness under contradiction. The world should force the model to decide whether an apparently clean plan can be signed when one quiet fact changes the transition.

The target shape is bimodal. Catcher runs should open the task-level file, reconcile the hidden conflict, and make a safe next move. Floor runs should summarize the chart accurately but sign the wrong thing because they trusted the most recent or most official-looking document.

## 6. Brainstorm guardrails

- Keep race clinically contextual, not decorative and not used as a biological shortcut.
- Do not make the patient unsafe by silence alone. The chart must contradict the wrong move.
- Do not build traps that require public web search or post-July 2025 knowledge.
- Use task-level files for post-snapshot denials, drafts, vendor notes, reports, or event notes.
- Keep world files free of task answers.
- Prefer one forced wrong move per task. The rest of the work can be ordinary, realistic clinical completion.
