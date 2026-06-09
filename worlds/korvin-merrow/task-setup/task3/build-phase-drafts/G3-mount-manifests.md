# KM03 mount manifests (pin both sets before any build; G3 prerequisite)

## CLEAN mount set (calibration baseline)
- The 26 agent-read world files only. No task-level file.
- FI-W22 (discharge_facing_plan_snapshot) and FI-S03 (home_support_equipment_reference) are WORLD files, both agent-read, both verified clean. EO-KM03 expecting the model to mention FI-S03 is fine: it is a world file, present in every task.
- Clean deliverable: generate the readiness assessment from the world. Predicted mid-90s; run only to justify the mounted note.

## ESCALATION mount set (the discriminator)
- The same 26 world files, PLUS exactly ONE task-level file: the committed-clearance mounted note (case_management_discharge_readiness_clearance_05242026.docx), rendered through the world builder from G3-mounted-note source, mounted in 1.3.
- No other task-level files. FI-S03 stays a world file (no action; it is clean). FI-T03 holdback is NOT mounted as-is (it is neutral; the mounted note is new closure content authored for the slot).
- Filename must not collide with any of the 26 world files or the 7 holdback request files (collision = blank trajectories). "case_management_discharge_readiness_clearance_05242026.docx" is unique.
- Clean vs escalation differ only by that one mounted file. Both sets pinned here so the no-leak/date audits apply to exactly the right files.
