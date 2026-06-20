# OV12 run instructions (Studio upload + pilot)

## Workflow (Step 10)
Consultation Note (Specialty Consultation Note). Fresh eighth lane.

## Prompt
Use prompt-OV12.txt verbatim:
"Dr. Solis started Mrs. Vasquell's pre-transfer nephrology consult note and got pulled away before finishing it. Finish it from her chart so I can sign it."

## Task Files card (mount exactly these under /docs/filesystem, nothing else)
1. nephrology_consult_note_draft_05232026.docx
2. pre_discharge_nursing_note_05232026.docx
3. pre_discharge_ecg_05232026.png
Plus the standard frozen world chart. Do NOT mount the golden or the grader.

## Grader
grader-guidelines-OV12.txt (paste into the grader field). Golden reference: golden-OV12-v1.docx (for the golden self-score, not mounted to the agent).

## Mount-hygiene gate (every upload or rerun; OV standing rule)
Inspect the first trajectory's `find /docs` tree before using any scores. Require exactly the three task files above under `/docs/filesystem`, no `/docs/.apps_data`, and no stale filename. If the gate fails, delete every file from the Studio Task Files card and re-add only the current three.

## Off-text-image note
The scored finding (new-onset atrial fibrillation, rapid ventricular response, no prior on file) lives only in pre_discharge_ecg_05232026.png. The grader scores the model's text against the golden; it does not read the image. Confirm the mounted PNG opens and the header and tracing are legible.

## Pilot
Ten runs. Expect a bimodal split (OV04 off-text-image pattern). Save the run set verbatim to tasks/task12/pilot/runs/. FA/GA from the 2nd-lowest distinct run (DO-NOT-REPEAT #20). Confirm a Studio golden self-score if the split has no catcher above 0.85.

## Nothing uploads, runs, or submits without Dr. Alexander's authorization for that exact step.
