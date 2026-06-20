# OV12 v1 pilot preregistration (locked before pilot)

Date: 2026-06-20. Author: Claude (cowork), for Dr. Alexander. New locked prereg per pilot (DO-NOT-REPEAT #22).

## Task

- Studio task: OV12 (new, tenth task; not a revival of any retired packet).
- Workflow lane (Step 10): Acute Care Discharge Planning (P1). Exact approved string from the 06/18 catalog (Project_Sanctum_Task_Categories_with_Difficulty_Suggestions). Work product: "Documented discharge plan including post-acute services, follow-up appointments, and patient education." FRESH eighth lane, distinct from the seven in use. Physician-produced (the attending completes and signs the plan), so it passes the all-tasks-physician-produced gate.
- Mechanism: OFF-TEXT IMAGE (the OV04 engine) on a fresh cardiac-rhythm axis. A pre-discharge 12-lead ECG mounted in the chart shows new-onset atrial fibrillation with a rapid ventricular response and no prior on file. The plan's headline is discharge logistics (post-acute services, follow-ups, education); the chart is silent on rhythm and carries no AV-nodal agent.
- Deliverable: complete the started discharge plan from the chart so it is ready for attending signature.

## Mount set (exactly these task files plus the frozen world chart)

- discharge_plan_draft_05232026.docx (the started deliverable; logistics filled, follow-ups to complete, silent on rhythm)
- pre_discharge_nursing_note_05232026.docx (quiet prose breadcrumb: ECG obtained and added to the chart, no finding stated)
- pre_discharge_ecg_05232026.png (the off-text finding; raw fields, no printed diagnosis)
- Grader reference (not mounted): grader-guidelines-OV12.txt. Golden reference (not mounted): golden-OV12-v1.docx.

## The catch (scored against the golden)

Surface the new-onset atrial fibrillation from the ECG; add cardiology follow-up with renally appropriate rate control and an anticoagulation evaluation appropriate to chronic kidney disease stage 3b (weighing stroke and bleeding and her dual antiplatelet therapy); route to a rhythm-monitoring-capable facility; and do not clear routine skilled-nursing transfer until the new afib is addressed. The services, follow-ups, and education are the reachable backdrop.

## Floor mechanism and prediction

- Floor: the model completes the plan's services, follow-ups, and education from chart prose and never opens the ECG, clearing routine transfer and omitting cardiology. This is the OV04 skip-rate floor.
- Catcher: the model reviews the mounted ECG, recognizes new-onset afib, and adds cardiology with rate control and a CKD-appropriate anticoagulation evaluation, holding routine-transfer clearance.
- Cold-bench (2026-06-20, isolated chart, no golden or grader): 3 of 3 capable agents opened the ECG, recognized new-onset afib, and managed it correctly (renally dosed rate control, a CKD-appropriate anticoagulation decision weighed against her dual antiplatelet therapy, cardiology, held transfer). The bench was run twice, on the consult-note predecessor and again on the shipped discharge-plan deliverable under a plain de-primed prompt, both 3 of 3, confirming catcher-reachability, fairness, a correct golden, and that de-priming did not change the catch (the catcher mode is robust). A capable-agent bench cannot sample the satisficer/skip mode, so the floor is a Studio-population measurement (OV04 floored about 40 percent skip with this engine). The draft scope (logistics, follow-ups to complete) and the breadcrumb are de-nudged to widen the skip mode.
- Forecast: BIMODAL like OV04 (off-text image), target floor about 0.30 to 0.55 with at least one catcher above 0.85. Judge by failure materiality (clearing a patient for transfer with a new, anticoagulation-changing arrhythmia unaddressed is a critical signability failure), not the number.
- Risk and decision rule: discharge readiness is cardiac-adjacent, so a thorough completion may catch the rhythm (ceiling risk). If it ceilings (no run below about 0.70), the off-text-image engine is intact, so re-center by tightening the logistics headline to be more absorbing before retiring; one re-roll only. If it floors uniformly with no catcher, confirm reachability with a Studio golden self-score before banking.
- Catalog alignment: the 06/18 catalog's own difficulty guidance for the discharge/coordination family ("embed a clinically significant but easy-to-miss error... require the agent to flag it unprompted rather than in response to a direct question") is exactly this off-text-ECG design.

## Fairness (see OV12-v1-A0.5-fairness-check.md)

Off-text-image fair form (the finding is in a mounted study the planner must proactively read, not pre-written false in the model's own draft); un-primed logistics headline; additive and non-contradictory (chart silent on rhythm, vitals end 05/21, the 05/23 ECG is after the snapshot); anti-paralysis grader; self-contained pre-July-2025.

## FA/GA

From the 2nd-LOWEST distinct run (DO-NOT-REPEAT #20). Writer Overall Failure Score entered against the agentic grader per the canonical standard.
