# World Spec Writer Playbook

Source materials:

- `reference/New Writers Version - Instruction Guide (05_24).md`
- `reference/templates/World_Spec_Template_05_06.docx`
- `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- Approved Korvin Merrow Brainstorm
- Task Selection Categories tracker

Current boundary: this is authoring workflow preparation only. Do not draft the World Spec before Brainstorm Human Review returns GO.

## Section 1 Clinical Scenario

### Required Inputs

- Synthetic patient identity: name, DOB, MRN, age, sex, relevant demographics.
- Patient-first Big Picture Summary with total task count, integration anchor, and working file-plan composition.
- Patient profile details: allergies, code status, PMH, active problems, anthropometrics, relevant home medication lists.
- Decision Friction Table if the world depends on multiple specialty conflicts or diagnostic conflicts.
- Continuous Clinical History narrative with arrival context, condition progression, key workups, surgical history or explicit none, transitions of care, and current world snapshot status.
- Key Milestones table with every date used anywhere in the spec.
- Clinical Complexity Overview explaining why the case is hard for AI.
- Care team roster if providers or services are named.

### Common Reviewer Failures

- Big Picture starts with institution/workflow instead of patient and clinical problem.
- Patient identity or MRN is too realistic.
- Home medications omit dose, route, frequency, or indication.
- Multiple medication lists are not temporally labeled.
- Clinical History is an outline rather than continuous prose.
- Clinical facts elsewhere do not trace back to Clinical History or file plan.
- Key Milestones omit dates used elsewhere.
- Clinical Complexity restates the problem list rather than explaining evaluation difficulty.

### AutoQC Risks

- 2.1 through 2.27 cover header, patient identity, Big Picture Summary, Patient Profile, Clinical History, Key Milestones, Clinical Complexity, and Care Team.
- Blocker risks include non-synthetic patient identity/MRN and untraceable clinical facts.
- Major risks include medication completeness, PMH certainty, missing coverage areas, orphan dates, weak complexity explanation, and care-team inconsistencies.

### Validation Checklist

- [ ] Header table has one chosen value per field.
- [ ] Patient name and MRN are synthetic.
- [ ] DOB, age, and snapshot date are arithmetically consistent.
- [ ] Big Picture Summary names task count, integration anchor, and file composition.
- [ ] Every medication list is complete and temporally labeled.
- [ ] Clinical History is continuous prose and supports file generation.
- [ ] Every date appears in Key Milestones in MM/DD/YYYY format.
- [ ] Clinical Complexity covers at least two interacting dimensions.
- [ ] Care team roster, if used, includes all named services/providers consistently.

## Section 2 Task Specifications

### Required Inputs

- Final task list with 5-8 or more tasks as supported by the world.
- Exact approved workflow names from the Task Selection Categories tracker.
- For each task: title, workflow line, anchor line, capability line, physician-authored Draft Prompt, Expected Output, Failure Design table, Task Level Files line, and time estimate.
- Task prompt dictated or drafted by Alexander in natural requester voice.
- At least five traps per Failure Design table, with grounded remediation.
- Specific expected output format, register, length range, and clinical anchors.

### Common Reviewer Failures

- Claude/Codex writes final task prompts from scratch.
- Prompt reads like an exam question or telegraphs the trap.
- Workflow does not match tracker wording.
- Expected Output is generic or duplicated across tasks.
- Failure Design has fewer than five traps.
- Plausible wrong answers are contrived.
- Task fuses multiple deliverables.
- Task references another task's output.
- Task anchor occurs at or before the world snapshot.

### AutoQC Risks

- 2.28 through 2.41 focus on required task components, persona voice, natural anchors, no trap hints, specific/differentiated expected outputs, Failure Design quality, task-level file line, single deliverable, task independence, and temporal architecture.
- 2.77 through 2.83 add task architecture checks: requester persona, consistent failure-design columns, title format, sequential numbering, tracker workflow names, difficulty distribution, task count, capabilities, workflow spread, audience spread, and temporal reasoning.

### Validation Checklist

- [ ] Every task has exactly one deliverable.
- [ ] Every task prompt is physician-authored and naturalistic.
- [ ] Every task anchor is after the world snapshot.
- [ ] Every workflow name matches the tracker exactly.
- [ ] Expected Output names format, voice, length, and specific grading anchors.
- [ ] Failure Design has at least five traps and remediation grounded in chart evidence.
- [ ] Task Level Files line is populated or explicitly says world-level files only.
- [ ] Tasks are independent and do not share outputs.
- [ ] Task set spans distinct capabilities, workflows, timepoints, output types, and audiences where appropriate.

## Section 3 World File Plan

### Required Inputs

- Task-supported file needs after Section 2 is stable.
- Essential world-level file rows.
- Essential task-level file rows, if any.
- Supplementary file rows, if any.
- ID scheme that clearly separates file categories.
- Filename_MMDDYYYY.type for every file.
- Source, Tool, Template/Reference File Origin, Description, and Pearls/Traps/Friction for each row.
- Reference template source classification: Public Domain, internal DataBank, Custom Built by Writer, or writer-produced media where applicable.

### Common Reviewer Failures

- Files designed before tasks.
- File rows lack complete columns.
- Filename dates do not match milestones.
- Source/tool/template origin is blank.
- Descriptions are too vague for a non-domain expert builder.
- Supplementary files carry answer-changing information.
- Essential/supplementary mix is poorly justified.
- File IDs collide, have gaps, or do not signal scope.
- Writer-produced media rows use placeholder filenames instead of final upload filenames.

### AutoQC Risks

- 2.42 through 2.58 focus on file-plan row completeness, filenames, date matching, source/tool/template origin, descriptions, Pearls/Traps/Friction, essential versus supplementary mix, file modalities, no single-file answer, and file count summary.
- 2.81 through 2.96 add ID, filename, source, scope, task-level reference, and writer-produced media checks.

### Validation Checklist

- [ ] Section 3 is built only after tasks are clear.
- [ ] Every essential file supports at least one task.
- [ ] Every supplementary file passes the removal test.
- [ ] Every filename includes date and extension.
- [ ] Every date in filenames appears in Key Milestones.
- [ ] Every file row has source/tool/template origin.
- [ ] Every trap is locked to a specific date and document.
- [ ] No single file answers a task alone.
- [ ] Total file count and essential/supplementary mix are stated.

## Section 4 World Summary

### Required Inputs

- Final clinical reasoning target.
- Final trap architecture rationale.
- Final explanation of why the world is hard for an AI agent.

### Common Reviewer Failures

- Summary is too generic.
- Summary restates the patient story without saying what the world tests.
- Summary does not connect task architecture to trap architecture.
- Summary introduces new facts not present elsewhere.

### AutoQC Risks

- Section 4 checks are fewer than earlier sections but cross-cutting checks still apply.
- Additional formatting/submission checks verify canonical sections, page numbers, filename suffix, DOCX format, no placeholders, no irrelevant optional sections, and no extra top-level sections.

### Validation Checklist

- [ ] 3-5 sentence summary is complete.
- [ ] It states what clinical reasoning the world tests.
- [ ] It explains why trap architecture is effective.
- [ ] It explains why the world is difficult for AI.
- [ ] It introduces no new unsupported facts.

## Final Preflight

- [ ] Run local check against `08_autoqc_master_index.md`.
- [ ] Run official v6.3 Writer Edition in Claude with the completed spec before RL Studio upload.
- [ ] Resolve or document every failure.
- [ ] Upload to RL Studio only after Alexander approves.
- [ ] Run RL Studio AutoQC and save full output.
- [ ] Do not move beyond Step 6 during onboarding.

