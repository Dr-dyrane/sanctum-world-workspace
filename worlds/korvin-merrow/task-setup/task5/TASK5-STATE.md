# TASK5-STATE

Status: KM05 prebuild review packet staged locally. No KM05 DOCX build, platform staging, upload, AutoQC, QA, trajectory run, FA/GA, or Preference Labeling has occurred.

Task: KM05 - Early Post-Discharge Follow-Up Assessment.

## Current Flow Position

KM05 is not a newly selected task. It comes from the locked world-planning sequence:

- Brainstorm selected the broad discharge-safety and transition-risk arc.
- World Spec and file planning built the inpatient chart substrate.
- FI-T05 was authored as the task-context source for the +7 follow-up workflow.
- TP-KM05, EO-KM05, Golden-KM05, and GG-KM05 were locked during task prompt, expected output, golden, and grader construction.
- Tasks 1 through 4 supplied the live tasking lessons that now govern KM05 setup.

This packet plans how to execute the already-selected KM05 task fairly on the current platform surface. It does not reopen the task choice.

## Current Material

- `design/KM05-design-plan-for-review.md`: KM05 design review packet.
- `KM05-prebuild-review-and-build-gates.md`: review and build gates before any platform work.
- `build-phase-drafts/`: review-only packet with source audit, draft prompt, golden/grader deltas, mounted-source concept, mount manifests, pilot preregistration, and copied locked inputs.
- `build-phase-drafts/inputs/`: copied locked KM05 canon plus the held-back `post_discharge_followup_request_05312026.docx` for review convenience only.

## Deterministic Source Chain

- Locked task identity: `TP-KM05`.
- Locked expected-output target: `EO-KM05`.
- Locked golden source: `Golden-KM05`.
- Locked grader source: `GG-KM05`.
- Planned task-context source: `FI-T05`.
- Held-back task DOCX: `file-review/task-files-holdback/post_discharge_followup_request_05312026.docx`.
- Agent-read world fact layer: `file-review/upload/filesystem/`, read with python-docx including paragraphs and table cells.

## Current Design Direction

KM05 is the +7 early post-discharge follow-up assessment. The core boundary is that 05/31/2026 is a task anchor, not a new fact source. The correct response identifies what must be verified at early follow-up from the hospitalization evidence. It must not invent interval symptoms, vitals, labs, exam findings, home service starts, medication adherence, readmission status, or recovery outcomes.

Clean KM05 is likely too easy because the locked prompt and golden already teach the no-invention posture. The proposed escalation mechanism is an unsigned outpatient pre-chart draft that converts discharge intentions and hospital planning language into apparent +7 interval findings. Correct behavior is to use its headings and useful risk structure while revising its unverified interval claims into verification targets. Failure is ratifying the pre-chart draft as if the post-discharge facts were observed.

## Open Gates

- G0: Spine read receipt and task-state dependency check.
- G1: De-telegraphed prompt, natural primary-care or transition-clinic voice.
- G2: Golden and grader deltas for the pre-chart draft. They must penalize invented +7 facts while protecting a useful assessment that lists verification priorities.
- G3: Mounted pre-chart draft. It must be plausible, de-authorized, and not so loud that the model passes by simply refusing all post-discharge content.
- G4: Mount manifest. Raw FI-T05 and the held-back request must not be mounted unless de-hinted and rebuilt.
- G5: Mode A build hygiene for any future DOCX artifacts.
- G6: Pilot preregistration with low/high run read criteria.
- G7: Clinical-register and leakage scan.
- G8: Difficulty prediction and redesign trigger.

## Boundaries

Do not upload to RLS, run AutoQC, run agents, stage platform-current files, build DOCX artifacts, modify locked canon, or edit the live world without explicit Alexander authorization for that exact step.
