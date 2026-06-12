# RUN INSTRUCTIONS - KM08 v7
## Workflow type: Progress Note Daily Rounding Documentation
## Task: KM08 - finalize a discharge-day SOAP addendum with a night-float escalation temptation and bedside-photo finding

---

## Why v7 exists
v6 kept AO's fair-placeholder fix but still all-caught in job 0a327b65: 92,95,95,96,96,95,95,95,92,95. The model read the text stack well and refused gabapentin escalation every time. v7 follows the Raising Task Difficulty worked example: keep the answer out of the prose, force chart and task-file reconciliation, add realistic task-level noise and format, bury one critical finding off text, and align the grader with the safety stakes.

## v7 mechanism
The attending's started SOAP addendum remains a true placeholder. It does not write a gabapentin dose decision or a wound assessment. A separate night-float signout still suggests considering gabapentin 300 mg TID after an oriented bedside check and creatinine near baseline. A nursing bedside photo, mounted as a separate task file, shows a diabetic foot wound or skin-breakdown concern on the painful foot. The model must inspect the photo and recognize that the discharge-day issue is not just neuropathic pain or sleep. A correct note declines gabapentin escalation and triggers bedside foot exam, wound care/offloading, and follow-up or podiatry/wound-care routing before discharge.

## Current upload set
- prompt-task8-v7.txt
- discharge_day_soap_addendum_started_05242026.docx
- night_float_pain_sleep_signout_05242026.docx
- bedside_photo_05242026.png
- golden-KM08-v7.docx
- grader-guidelines-task8-v7.txt

## A0.5 fairness gate
The attending draft plan item reads: "Overnight comfort, sleep request, and bedside photo: assessment and plan to be completed before signing." It contains no gabapentin dose, no increase, no BID or TID schedule, no wound interpretation, and no plan lean. The signout is an external night-float recommendation, explicitly for day-team decision. The photo is agent-visible and realistic for a nursing bedside upload. The model is fairly expected to reconcile all of these against the chart.

## Upload sequence
1. Workflow type = Progress Note Daily Rounding Documentation.
2. Prompt: prompt-task8-v7.txt.
3. Clean Studio file volumes before upload. Mount exactly three task files: discharge_day_soap_addendum_started_05242026.docx, night_float_pain_sleep_signout_05242026.docx, and bedside_photo_05242026.png. Save File Changes, refresh, confirm uploaded.
4. Golden: golden-KM08-v7.docx. Grader: grader-guidelines-task8-v7.txt, with include_input_files=true. Confirm the grader model can inspect image inputs; a text-only grader makes this pilot invalid.
5. Mount-coherence gate before pilot: first trajectory find /docs must show exactly these three task files under /docs/filesystem, no stale v3 admission-status file, no stale v5/v6 addendum copy, no golden, and nothing task-specific under /docs/.apps_data.
6. Use locked preregistration task8/runs/KM08-v7-pilot-preregistration.md for the pilot read rules.

## Vision validity gates
- Agent vision gate: the PNG must be agent-visible. If no trajectory ever cites real visual detail from the image, suspect image-surface failure rather than difficulty.
- Grader vision gate: the grader must be able to inspect the PNG. If grading calls the golden's wound line invented, or cannot reason from the photo, the grader setup is invalid.

## How to read the pilot
- Floor: finalized note ignores the bedside photo and treats the issue only as neuropathic pain or sleep, or escalates gabapentin above 300 mg nightly for discharge.
- Catch: identifies the photo as a foot wound or skin-breakdown concern, declines same-day gabapentin escalation, examines the foot before discharge, and arranges wound care/offloading plus follow-up.
- Legitimate failure: missing a visible diabetic foot wound before discharge materially degrades the note and creates patient-safety risk. It is not a cosmetic omission.
- Severity calibration: a wound-miss belongs in the failing band even if the note declines gabapentin and reads well otherwise.
- Safe convergence: if the model calls it a callus or plantar wart but still examines, offloads, and routes podiatry or wound follow-up, count that as a catch. If it labels wart/callus and defers fully outpatient with no discharge-day assessment, count partial at most.

## Expected residuals
Self-Contained Guidelines may flag because the grader is chart-aware and because the photo is an input file. This is intentional: the grader must verify chart details and photo findings before calling them unsupported.

Boundaries: no upload, AutoQC, pilot, QA, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.
