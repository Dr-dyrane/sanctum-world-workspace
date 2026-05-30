# World Spec Rubric Checklist

## Source-Of-Truth Rule

Use the official World Spec template and the self-review checklist from the source guide. Every item below should pass before upload.

## Section 1: Clinical Scenario

- [ ] Big Picture Summary captures patient, clinical picture, task count, why the case is hard, and task architecture in 1-2 paragraphs.
- [ ] Patient Profile includes relevant fields only: fictional name, DOB, age/sex, allergies, MRN, problem list, and any clinically relevant optional rows.
- [ ] Clinical History is a continuous narrative detailed enough for a file builder to generate documents from it.
- [ ] Every clinical fact elsewhere traces back to the Clinical History or to a file in Section 3.
- [ ] Key Milestones table contains every date referenced in tasks, traps, or file descriptions.
- [ ] Clinical Complexity Overview explains why the case is difficult, not just what diseases exist.
- [ ] Patient has multiple active comorbidities with interacting treatments.
- [ ] All patients, providers, institutions, and identifiers are fictional.
- [ ] Named specialists appear in at least one file and at least one task if used.

## Section 2: Task Specifications

- [ ] 5-10 tasks are planned.
- [ ] At least one task uses a P0 workflow.
- [ ] Every task maps to an approved workflow.
- [ ] Every task produces one concrete, evaluable output.
- [ ] Every task has Workflow, Draft Prompt, Expected Output, Failure Design, and Task-level files completed.
- [ ] Every task has an anchor point after the world snapshot.
- [ ] Each Draft Prompt is in persona voice and sounds like a naturalistic real request.
- [ ] The prompt does not hint that something is wrong.
- [ ] Failure Design includes 5-6 highest-yield traps with remediation paths.
- [ ] Tasks span varied workflows, documents, and trap structures.
- [ ] Frictions and traps remain distinct.
- [ ] Task-level files use E#-T# convention and reuse is noted.

## Section 3: World File Plan

- [ ] Files are designed after tasks.
- [ ] Every essential file exists because a task requires it.
- [ ] Every supplementary file adds noise only and carries no answer-changing trap content.
- [ ] Essential world-level files include all required columns: #, ID, Filename_MMDDYYYY.type, Source, Tool, Template/Reference File Origin, Description, Pearls/Traps/Friction.
- [ ] Essential task-level files use E#-T# convention and same column completeness.
- [ ] Supplementary files use D# for world-level or S# / S#-T# for task-level.
- [ ] Dates appear in filenames for temporal anchoring.
- [ ] Approximate mix is 90% essential and 10% supplementary.
- [ ] No single file resolves any task without cross-reference.
- [ ] At least 3-4 distinct file modalities are represented.
- [ ] Total file count summary is stated.

## Section 4: World Summary

- [ ] 3-5 sentence summary is present.
- [ ] Summary covers clinical reasoning tested.
- [ ] Summary explains why trap architecture is effective.
- [ ] Summary explains why the world is hard for an AI agent.

## Cross-Cutting

- [ ] Every correct-answer claim is traceable to prompt + task-level files + world-level files.
- [ ] Anything not traceable is acknowledged as uncertain.
- [ ] Dates, medication dosages, lab values, names, and identifiers are consistent everywhere.
- [ ] Expected Outputs are precise enough for two graders to score consistently.

