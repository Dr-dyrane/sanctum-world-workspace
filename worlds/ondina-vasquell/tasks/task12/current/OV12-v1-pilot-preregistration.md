# OV12 v1 pilot preregistration (locked before pilot)

Date: 2026-06-20. Author: Claude (cowork), for Dr. Alexander. New locked prereg per pilot (DO-NOT-REPEAT #22).

## Task

- Studio task: OV12 (new, tenth floor; not a revival of any retired packet).
- Workflow lane (Step 10): Specialty Consultation Note (P1). FRESH eighth lane, distinct from the seven in use. Exact approved string from the 06/19 catalog; its named core challenge is "delivering a specialist's focused assessment ... integrating the targeted history, exam, and diagnostics", so integrating the off-text ECG diagnostic is squarely the work product. Physician-produced deliverable (passes the all-tasks-physician-produced gate): the attending completes and signs a pre-transfer nephrology consultation note.
- Mechanism: OFF-TEXT IMAGE (the OV04 engine) on a fresh cardiac-rhythm axis. A pre-discharge 12-lead ECG mounted in the chart shows new-onset atrial fibrillation with a rapid ventricular response and no prior on file. The consult's headline is renal (acute kidney injury on chronic kidney disease, dosing, held-agent restart); the chart is silent on rhythm.
- Deliverable: complete the started nephrology consult from the chart so it is ready for attending signature.

## Mount set (exactly these task files plus the frozen world chart)

- nephrology_consult_note_draft_05232026.docx (the started deliverable; silent on rhythm)
- pre_discharge_nursing_note_05232026.docx (quiet prose breadcrumb: ECG obtained and added to the chart, no finding stated)
- pre_discharge_ecg_05232026.png (the off-text finding; raw fields, no printed diagnosis)
- Grader reference (not mounted): grader-guidelines-OV12.txt. Golden reference (not mounted): golden-OV12-v1.docx.

## The catch (scored against the golden)

Surface the new-onset atrial fibrillation from the ECG; recommend renally appropriate rate control; recommend an anticoagulation evaluation given an elevated stroke risk, dosed and selected for chronic kidney disease stage 3b and weighing bleeding; obtain cardiology with telemetry; and do not clear the patient as renally optimized for transfer until the new afib is addressed. The renal recommendations (recovery, dosing, held metformin/empagliflozin/lisinopril) are the reachable backdrop.

## Floor mechanism and prediction

- Floor: the model completes the renal consult from chart prose and never opens the ECG, carrying the chart's quiet on rhythm forward and missing the new afib. This is the OV04 skip-rate floor.
- Catcher: the model reviews the mounted ECG, recognizes new-onset afib, and acts.
- Cold-bench (2026-06-20, isolated chart, no golden or grader): 3 of 3 capable agents opened the ECG, recognized new-onset afib, and managed it correctly (renally dosed rate control, a CKD-appropriate anticoagulation decision weighed against her dual antiplatelet therapy, cardiology, held transfer clearance). This confirms the catcher mode is reachable, the golden is correct, the ECG is legible, and the task is fair. A capable-agent bench cannot sample the satisficer/skip mode, so the floor is a Studio-population measurement (OV04 floored about 40 percent skip with this engine). The started draft scope and the nursing breadcrumb were de-nudged after the bench (renal-only completion instruction, neutral breadcrumb) to widen the skip mode.
- Forecast: BIMODAL like OV04 (off-text image), target floor about 0.30 to 0.55 with at least one catcher above 0.85. Judge by failure materiality (missing a new, anticoagulation-changing arrhythmia before transfer is a critical signability failure), not the number.
- Risk and decision rule: a consult note may pull more chart review than a transition note (thinner floor) or the rhythm axis may stay un-primed enough to skip (good floor). If it ceilings (no run below about 0.70), the off-text-image image is intact, so re-center by tightening the renal headline to be more absorbing before retiring; one re-roll only. If it floors uniformly with no catcher, confirm reachability with a Studio golden self-score before banking.

## Fairness (see OV12-v1-A0.5-fairness-check.md)

Off-text-image fair form (the finding is in a mounted study the consultant must proactively read, not pre-written false in the model's own draft); un-primed axis; additive and non-contradictory (chart silent on rhythm, vitals end 05/21, the 05/23 ECG is after the snapshot); anti-paralysis grader; self-contained pre-July-2025 (afib rate control and anticoagulation in CKD are long-established).

## FA/GA

From the 2nd-LOWEST distinct run (DO-NOT-REPEAT #20). Writer Overall Failure Score entered against the agentic grader per the canonical standard.
