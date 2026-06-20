# World 3 chat-reference copy (paste into Sanctum Coach)

This is the chat-reference copy of the World 3 inputs. The canonical work is governed in this workspace; this file exists to drop into a Sanctum Coach session so the platform transcript matches what was built here. Refresh it from the committed state before each Coach session. Run the Coach in its veteran path (open with the activation phrase from the Coach instructions; do not print it in workspace files). State the phase when you start: World Spec next, Template Curation after the file plan exists.

Hold rule for the Coach: the substance below is settled here. Let the Coach assemble it into World_Spec_Template.docx and run its audit. Accept format and audit fixes. Do not let it re-open the clinical design or introduce new substance.

## World essentials

Patient: Marva Lydell, 72F. Inpatient hospital medicine world: a 7-day admission for acute decompensated heart failure with hypoxemia and cardiorenal acute kidney injury. Comorbidities: HFpEF, atrial fibrillation on anticoagulation, CAD with prior PCI, CKD stage 3b to 4, COPD, OSA, type 2 diabetes with peripheral neuropathy, hypertension, obesity, anemia of CKD, vitamin D deficiency, hypothyroidism, GERD, chronic constipation, limited mobility at baseline. Home oxygen and CPAP. Baseline meds: empagliflozin, spironolactone, torsemide, metoprolol succinate, losartan, apixaban, aspirin, metformin, insulin glargine, atorvastatin, cholecalciferol, ferrous sulfate, tiotropium with albuterol, gabapentin, levothyroxine, pantoprazole, senna.

Snapshot: clinically improved at rest, transition safety unresolved. Open issues: exertional oxygen need, portable oxygen delivery, diuretic and renal-medication follow-up, anticoagulation source hierarchy, functional tolerance, limits of home support.

DATE POLICY (note, not binding): the Coach curriculum says the whole timeline must precede a July 2025 knowledge cutoff, but the Coach is behind and the OV world shipped on 2026 dates, so this rule is treated as Coach-stale. Keep Marva's July 2025 timeline as in the brainstorm unless Larry or the canonical doc says otherwise.

Self-containment: every task is an independent post-snapshot encounter, solved from the world chart plus that task's own task-level files. Tasks never stack; no task uses another task's output. The shared chart stays raw, with no single summary that states the final readiness conclusion.

## Task table (workflow strings locked to Larry, 2026-06-20)

Each workflow string below is locked to Larry's latest cut, corroborated by the canonical 06/19 doc where the lane already appears. See the working log and reconciliation section 1 for the per-row evidence.

| # | Requester | Deliverable | Workflow (locked) | Tier | Forced decision | Clinical trap | Anchor |
|---|---|---|---|---|---|---|---|
| 1 | Hospitalist attending for case management | Oxygen and SNF denial appeal | Claims Denial Analysis and Appeal Preparation | P0 | Appeal, accept, or narrow the denial | Denial leans on resting oxygen, ignores exertional oxygen need and transition risk | July 11 2025 09:00 |
| 2 | Hospitalist attending | Discharge medication reconciliation | Discharge Medication Reconciliation | P0 | Continue, hold, change, stop, or defer per medication row | Outside list carries stale renal or anticoagulation logic despite updated kidney function and active orders | July 11 2025 10:00 |
| 3 | Physician advisor | Continued-stay review | Utilization Review Concurrent Stay Documentation | P1 | Approve continued stay, narrow, or deny | Review worksheet treats improvement after diuresis as readiness despite unresolved oxygen equipment and tolerance | July 11 2025 14:00 |
| 4 | Discharging attending | Transition note completion | Medical Transcription and Clinical Documentation Completion | P0 | Finish open sections without falsely closing readiness | TRUE PLACEHOLDER: started note leaves oxygen, volume, and follow-up ownership genuinely open under a reassuring tone | July 12 2025 08:30 |
| 5 | Case manager | Post-acute coordination plan | Post-Acute Care Coordination Documentation | P0 | Assign owner, status, and next action per transition item | Case-management prose says DME arranged while vendor status leaves portable oxygen unresolved | July 12 2025 13:00 |
| 6 | Hospitalist attending | Cardiorenal follow-up handoff | Specialist Referral Letter and Documentation Preparation | P0 | Route diuretic, renal labs, potassium, anticoagulation, and restart decisions to the correct owner | TRUE PLACEHOLDER: started letter is an open handoff, not a draft that falsely states the plan is settled | July 13 2025 11:00 |
| 7 | Hospitalist attending for utilization management | Home health vs SNF appeal | Claims Denial Analysis and Appeal Preparation | P0 | Support skilled need or accept home-health pathway | Denial treats home health as sufficient despite stairs, oxygen burden, functional limits, medication complexity | July 15 2025 10:00 |
| 8 | Patient safety officer | Safety review after bounceback | Corrective Action Plan (CAP) Development and Tracking | P1 | Identify likely cause and prevention steps | Initial event note blames nonadherence while the record supports equipment or handoff failure | July 16 2025 09:00 |
| 9 | Quality abstraction nurse | Heart-failure transition quality abstraction | HEDIS Medical Record Chart Abstraction and Review | P0 | Record documented value, exclusion, or unable-to-determine per field | Abstractor worksheet rewards a clean transition although oxygen or follow-up evidence is incomplete | July 17 2025 09:00 |
| 10 | CDI specialist | Documentation query response | Clinical Documentation Improvement (CDI) Query Response Review | P0 | Agree, decline, or clarify supported specificity | Query asks for over-specific acute respiratory failure or cardiorenal language beyond the treating record | July 17 2025 12:00 |

Tier spread: eight P0 (1, 2, 4, 5, 6, 7, 9, 10), two P1 (3, 8). Structure spread: external position review twice, forced inventory, determination, completion once, coordination synthesis, specialist handoff, investigation, extraction to schema, query response.

Workflow source note: these strings are locked to Larry's latest cut, the canonical authority, corroborated by the 06/19 Combined doc in the source folder. The Sanctum Coach's own workflow endpoint is BEHIND Larry's cut (the EPMs have not updated it). If a Coach session pushes back on Task 2, 6, or 10 (it may still show the old P1 tiers, or lack the Specialist Referral lane), that is the stale endpoint, not an error here; Larry's cut governs. One item to confirm at spec time: the exact spelling and tier of Task 6's Specialist Referral lane, which is Larry's newest addition and not yet in the 06/19 doc.

## Fairness rules for the spec (Larry 06/20)

A fair trap is true buried information the model must synthesize, or a wrong element in a document the requester's job is to review and rebut. An unfair trap plants a false statement in the patient's own authoritative record and dings the model for trusting it.

- The world chart (the authoritative inpatient record) stays accurate. Every wrong, conflict, or over-closure lives in a TASK-LEVEL input the requester reviews: a payer denial, a continued-stay worksheet, an abstractor worksheet, a CDI query, an outside medication list, a started-draft placeholder. Never plant a falsehood in the world chart.
- Tasks 4 and 6 are completion tasks. Build them as TRUE PLACEHOLDERS: the started document leaves the contested items genuinely open under an optimistic but not-false tone. The model completes the open sections correctly; it is never asked to distrust a false closure.
- The synthesis traps (resting vs exertional oxygen, improving kidney vs medication readiness, volume vs transition readiness, home support overestimated, respiratory control over-closed) are true and buried; the model fails by not synthesizing, not by trusting a falsehood.

## File plan and template curation (when the spec's file plan exists)

Each world-level file row gets one origin, DataBank-first: DataBank extract, public-domain form, custom template, or writer-produced artifact. Filenames: templates generic with no datestamp (the Reference File Origin value equals the actual file); writer-produced files keep the final datestamped name in both columns. No synthetic or training markers in any file. At least 30 world-level file rows; reuse one template across many rows (one progress-note template for all daily notes, one consult template for cardiology and nephrology).

Writer-produced artifacts are produced in the workspace, not in the Coach chat. Likely W3 candidate, to confirm at file-plan time: an atrial-fibrillation rhythm or telemetry strip rendered in-repo (clean of any printed interpretation), consistent with the authored-image doctrine. Any such artifact is rendered here, named with its final datestamp, and uploaded alongside the templates.
