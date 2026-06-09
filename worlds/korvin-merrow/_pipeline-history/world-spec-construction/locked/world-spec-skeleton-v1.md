# World Spec Skeleton v1

Date created: 2026-06-01

Status: LOCKED

Purpose: define the structure, section order, source-package mapping, and construction boundaries for the final Korvin Merrow World Spec before full World Spec prose is drafted.

This artifact answers: what sections will the World Spec contain, what belongs in each section, and which locked architecture package feeds each section?

This is not the full World Spec. It does not create final World Spec prose, synthetic files, file inventory rows, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, reference files, or templates.

## Governing Structure

Official template source: `reference/templates/World_Spec_Template_05_06.docx`

Local template map: `reference/world-spec-guidelines/06_world_spec_template_map.md`

Required canonical World Spec sections:

1. Clinical Scenario.
2. Task Specifications.
3. World File Plan.
4. World Summary.

Operational rule: the final World Spec must follow the official template. The subsections below are a construction skeleton for mapping locked architecture into the template, not a replacement template.

## Locked Inputs

- Approved Brainstorm.
- Ratified Clinical Story Skeleton v1.
- Locked Identity Package v1.
- Ratified Governance Package v1.
- Locked Key Milestones Calendar Skeleton v1.
- Locked Baseline Anchor Package v1.
- Locked Clinical Story Timeline Package v1.
- Locked Task Architecture Package v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Locked Provider Roster Package v1.
- Locked Surgical History Package v1.
- Locked Daily Hospital Course Framework v1.
- World Spec AutoQC v6.3 index.
- World Spec writer playbook.
- Official Task Selection Categories tracker.

## 1. Proposed World Spec Section Structure

### Section 1: Clinical Scenario

Official template anchor:

- 1.1 Big Picture Summary.
- 1.2 Patient Profile.
- 1.3 Clinical History and Context.
- 1.4 Key Milestones.
- 1.5 Clinical Complexity Overview.

Skeleton subsections to map into Section 1:

| Skeleton subsection | Final template location | Purpose | Source package |
| --- | --- | --- | --- |
| Big Picture Summary | 1.1 Big Picture Summary | Orient reviewer to patient, clinical domain, world type, task count, and core reasoning target. | Approved Brainstorm; Task Architecture Package; Daily Hospital Course Framework |
| Patient Profile | 1.2 Patient Profile | Provide synthetic identity, demographics, allergy, code status, anthropometrics, and baseline contextual anchors. | Identity Package; Baseline Anchor Package; Comorbidity Expansion Package |
| Baseline Clinical State | 1.2 Patient Profile or 1.3 Clinical History and Context | Define pre-decline functional, cognitive, medication-management, home-support, and baseline comparator state. | Baseline Anchor Package; Clinical Story Skeleton; Clinical Story Timeline Package |
| Comorbidity Profile | 1.2 Patient Profile or 1.5 Clinical Complexity Overview | State baseline disease burden and why it matters for the world. | Comorbidity Expansion Package; Governance Package; Clinical Logic |
| Medication Architecture | 1.2 Patient Profile or optional home medication list under Section 1 | Present baseline medication architecture and polypharmacy burden at the World Spec level. | Medication Expansion Package; Governance Package |
| Surgical / Procedural History | 1.3 Clinical History and Context or Patient Profile table | Record remote PCI/stent and sleep study as background procedural anchors. | Surgical History Package |
| Provider / Care Team Roster | 1.2 Patient Profile, 1.3 Clinical History, or care team subsection | Identify recurring services/providers and source/authority roles. | Provider Roster Package; Governance Package |
| Key Milestones | 1.4 Key Milestones | Provide canonical dates and anchors for decline, HD1-HD6, world close, discharge, +7, and +30. | Key Milestones Calendar Skeleton; Clinical Story Timeline Package |
| HD1-HD6 Hospital Course | 1.3 Clinical History and Context and/or optional hospital course timeline | Define daily clinical evolution without turning it into individual notes. | Daily Hospital Course Framework; Clinical Story Timeline Package |
| Friction Architecture | 1.5 Clinical Complexity Overview and optional Decision Friction Table | Preserve stakeholder disagreements and why both sides are defensible. | Governance Package; Task Architecture Package; Daily Hospital Course Framework |
| Trap / Failure Design Architecture | 1.5 Clinical Complexity Overview and later Section 2 Failure Design | Explain world-level traps and how they remain document/synthesis problems. | Approved Brainstorm; Daily Hospital Course Framework; Task Architecture Package |
| Source-of-Truth Hierarchies | 1.3 Clinical History, 1.5 Clinical Complexity Overview, or data hierarchy note | State factual hierarchy, prednisone hierarchy, and authority/source distinction. | Governance Package; Clinical Story Skeleton Ratification |

### Section 2: Task Specifications

Official template anchor:

- Task title.
- Workflow.
- Draft Prompt.
- Expected Output.
- Failure Design.
- Task-level files.

Skeleton subsections to map into Section 2:

| Skeleton subsection | Final template location | Purpose | Source package |
| --- | --- | --- | --- |
| Task Architecture Mapping | Section 2 task blocks | Preserve six task concepts across four approved workflows. | Task Architecture Package; Active task-map |
| Workflow Discipline | Workflow line in each task block | Ensure exact approved tracker wording and 3-5 workflow discipline. | Task Architecture Package; Task tracker |
| Temporal Anchors | Workflow context / prompt context | Ensure every task occurs after world close. | Key Milestones Calendar Skeleton; Task Architecture Package |
| Task Independence | Each task block | Keep each task independently solvable from world files and task-level files if any. | Task Architecture Package; AutoQC index |
| Failure Design Architecture | Failure Design tables later | Map world-level and task-level traps without writing final grader content now. | Daily Hospital Course Framework; Task Architecture Package |
| Administrative Deliverable Placement | Relevant task block(s) | Preserve Discharge Planning Documentation / Care Coordination as the administrative deliverable. | Task Architecture Package; Governance Package |

Boundary: this skeleton does not write final task prompts, expected outputs, failure design tables, remediation paths, task-level file lines, time estimates, or grader-facing content.

### Section 3: World File Plan

Official template anchor:

- 3.1 Essential Files (World-Level).
- 3.2 Essential Files (Task-Level).
- 3.3 Supplementary Files.
- Total file count.

Skeleton subsections to map into Section 3:

| Skeleton subsection | Final template location | Purpose | Source package |
| --- | --- | --- | --- |
| Future File Inventory Placement | Section 3 overview and file tables | Reserve the file plan for after task structure is stable. | World Spec Writer Playbook; AutoQC index |
| Essential World-Level Files | 3.1 Essential Files | Later document the chart ecosystem that supports all tasks. | Daily Hospital Course Framework; Governance Package; Task Architecture Package |
| Essential Task-Level Files | 3.2 Essential Files | Later identify files that exist only for specific task contexts. | Task Architecture Package; future task design |
| Supplementary Files | 3.3 Supplementary Files | Later add realistic noise that does not change correct answers. | Future file inventory phase |
| Traceability Discipline | Section 3 columns and descriptions | Ensure clinical facts, traps, and task outputs trace to source files. | AutoQC index; Governance Package |

Boundary: this skeleton does not create file rows, filenames, dates, file IDs, source/tool/origin entries, template/reference files, synthetic files, chart notes, labs, vitals, or hospital-course documentation.

### Section 4: World Summary

Official template anchor:

- 3-5 sentence final summary.

Skeleton subsections to map into Section 4:

| Skeleton subsection | Final template location | Purpose | Source package |
| --- | --- | --- | --- |
| Clinical reasoning target | Section 4 | Summarize what judgment the world tests. | Approved Brainstorm; Clinical Story Skeleton; Daily Hospital Course Framework |
| Trap architecture rationale | Section 4 | Explain why the world is difficult without rare-disease puzzle logic. | Approved Brainstorm; Governance Package; Daily Hospital Course Framework |
| AI difficulty statement | Section 4 | Explain why synthesis, temporal reasoning, and source hierarchy matter. | Approved Brainstorm; Task Architecture Package; AutoQC index |

Boundary: this skeleton does not write the final 3-5 sentence World Summary.

## 2. Section-To-Source Mapping

| Final World Spec component | Primary locked source | Secondary/supporting source | Construction note |
| --- | --- | --- | --- |
| World type | Approved Brainstorm | Reviewer feedback / remediation history | Use "Typical Clinical World." |
| Patient identity | Identity Package | Key Milestones Calendar Skeleton | Confirm age/DOB/date consistency. |
| Demographics and anthropometrics | Identity Package | Baseline Anchor Package | Do not reopen locked values. |
| Allergy / code status | Identity Package | Identity review addendum | Treat lisinopril cough as ACE-inhibitor intolerance later. |
| Baseline function | Baseline Anchor Package | Clinical Story Skeleton | Include home support, cognition, mobility, and medication-management ability. |
| Baseline disease burden | Comorbidity Expansion Package | Governance Package | Use 14 baseline conditions. |
| Medication burden | Medication Expansion Package | Governance Package | Use 20-medication baseline architecture; do not create new schedules here. |
| Surgical/procedural history | Surgical History Package | Comorbidity Expansion Package | Keep PCI and sleep study remote/background. |
| Care team/provider roster | Provider Roster Package | Governance Package | Use named high-authority roles and role-based minor contributors. |
| Authority hierarchy | Governance Package | Governance clarification | Authority hierarchy does not erase consultant disagreement. |
| Source-of-truth hierarchy | Governance Package | Clinical Story Skeleton Ratification | Include master clinical hierarchy and prednisone-specific hierarchy. |
| Key milestones | Key Milestones Calendar Skeleton | Clinical Story Timeline Package | Every future date used in tasks/files must appear here. |
| Pre-admission decline | Clinical Story Skeleton | Clinical Story Timeline Package | Approximately 3-week decline beginning 04/27/2026. |
| HD1-HD6 course | Daily Hospital Course Framework | Clinical Story Timeline Package | Use daily evolution spine, not note-level content. |
| Frictions | Governance Package | Daily Hospital Course Framework | Preserve human-to-human perspective conflicts. |
| Traps | Approved Brainstorm | Daily Hospital Course Framework; Task Architecture Package | Preserve information/synthesis traps and Trap #3/#5 distinction. |
| Task count and workflows | Task Architecture Package | Active task-map; task tracker | Six task concepts across four workflows. |
| Administrative deliverable | Task Architecture Package | Governance Package | Discharge Planning Documentation / Care Coordination. |
| Future file plan | Not yet started | Writer Playbook; AutoQC index | Must follow task design, not precede it. |
| World Summary | All locked packages | Approved Brainstorm | Draft only after Sections 1-3 stabilize. |

## 3. Boundary Classification

| Skeleton area | Belongs in World Spec | Belongs in future file inventory | Belongs in future synthetic files | Belongs in future tasks | Belongs in future prompts | Belongs in future goldens / grader guidance |
| --- | --- | --- | --- | --- | --- | --- |
| Big Picture Summary | Patient, domain, task count, reasoning target, high-level file composition | None | None | None | None | None |
| Patient Profile | Identity, baseline anchors, comorbidities, medication architecture, allergies, code status | Source documents that prove or carry these facts later | Chart-facing evidence later | None | None | None |
| Baseline Clinical State | Baseline comparator narrative/table | Baseline-supporting files later | Outpatient/primary care/rheumatology style artifacts later, if authorized | Used as task evidence later | None | Grading anchors later only after task design |
| Medication Architecture | Baseline medication architecture and rationale | Medication lists/MAR/reconciliation rows later | Actual med lists, MAR, pharmacy history later | Medication reconciliation task design later | Prompt wording later | Expected medication reasoning later |
| Surgical / Procedural History | Remote procedural anchors and exclusions if useful | Procedural provenance later if needed | Procedure/provenance files later only if authorized | None unless relevant to task evidence | None | None unless task requires |
| Provider / Care Team Roster | Services, named recurring high-authority providers, stakeholder roles | Authorship/provenance rows later | Provider-authored notes later | Requester/persona logic later | Prompt voice later | Role-specific grading later |
| Key Milestones | All dates used anywhere in spec/tasks/files | Filename/date rows later | File timestamps later | Task anchors later | Prompt dates later | Temporal grading later |
| HD1-HD6 Hospital Course | Daily course prose/table at architecture level | Daily note/file rows later | ED/admission/progress/consult/PT/nursing docs later | Task evidence later | None | Temporal trap grading later |
| Friction Architecture | Decision Friction Table and defensible positions | Friction-bearing files later | Consultant/family/team notes later | Task-specific conflict handling later | None | Friction-handling criteria later |
| Trap / Failure Design Architecture | World-level trap explanation | Trap-bearing files and dates later | Documents that carry traps later | Task-level trap selection later | None | Failure Design/remediation later |
| Source-of-Truth Hierarchies | Master and prednisone hierarchies | File provenance and authority rows later | Conflicting source documents later | Task source-reconciliation logic later | None | Source-weighting criteria later |
| Task Architecture Mapping | Task titles/concepts/workflows only when Section 2 is authorized | Task-level files later | Task-specific materials later | Full task specs later | Physician-authored prompts later | Expected outputs and grader logic later |
| Future File Inventory Placement | Section 3 structure and dependency rules only | Actual file rows later | Actual files later | None | None | None |

## 4. Studio Alignment Review

### VERIFIED

Finding: skeleton preserves the official four-section World Spec structure.

Evidence: it maps all construction content into Clinical Scenario, Task Specifications, World File Plan, and World Summary.

Impact: the final DOCX can follow the official template without structural drift.

Action required: use the official DOCX template when building the final submission artifact.

### VERIFIED

Finding: the skeleton supports a world that can anchor multiple tasks.

Evidence: Task Architecture Package v1 preserves six task concepts across four workflows, and the skeleton reserves Section 2 for those task specifications.

Impact: the spec can define the world in a way that supports all planned task concepts.

Action required: do not reduce the task architecture or add unapproved workflows during later drafting.

### VERIFIED

Finding: reference/template files remain separate from the World Spec skeleton.

Evidence: Section 3 is explicitly deferred to later file inventory architecture and no reference files are created here.

Impact: Studio upload package requirements can be handled later without contaminating the skeleton with file rows.

Action required: preserve separate upload handling for reference files if later required.

### PLAUSIBLE

Finding: Claude transcript requirements remain later submission work.

Evidence: transcript guidance has been audited separately, and this skeleton does not create transcript artifacts.

Impact: transcript readiness is not blocked by this skeleton but remains a submission-package concern.

Action required: revisit `reference/world-spec-guidelines/11_transcript_requirements.md` and `13_claude_workflow_audit.md` before upload packaging.

### VERIFIED

Finding: Spec AutoQC remains later validation work.

Evidence: this artifact performs structural readiness only and does not run or simulate official AutoQC.

Impact: no AutoQC pass is claimed prematurely.

Action required: run local preflight and official v6.3 checks only after a completed draft exists.

## 5. AutoQC Readiness Review

| Readiness area | Status | Evidence | Prevention strategy |
| --- | --- | --- | --- |
| Temporal consistency | VERIFIED | Calendar Skeleton and Daily Hospital Course Framework are locked. | Reuse canonical dates and prohibit orphan dates. |
| Source-of-truth consistency | VERIFIED | Governance Package locks master and prednisone hierarchies. | State hierarchy in Section 1 and enforce provenance in Section 3 later. |
| Task solvability | PLAUSIBLE | Six task concepts are architecturally supported but task specs and files are not built yet. | Build Section 2 before Section 3 and trace every task to files later. |
| Workflow-count discipline | VERIFIED | Task Architecture Package locks four workflows. | Do not add TCM/risk as standalone workflows. |
| Administrative deliverable | VERIFIED | Discharge Planning Documentation / Care Coordination is locked as the administrative deliverable. | Make it explicit in Section 2 when task specs are authorized. |
| File traceability | PLAUSIBLE | Traceability doctrine exists, but file rows do not yet exist. | Use Section 3 file rows only after tasks stabilize. |
| No orphan dates | PLAUSIBLE | Canonical dates are locked, but future task/file dates are not yet populated. | Every later task/file date must enter Key Milestones. |
| No post-world world files | PLAUSIBLE | World close and post-world anchors are locked. | Separate world-level files through 05/23/2026 18:00 from task/post-discharge materials later. |
| No section drift | VERIFIED | Skeleton follows template sections 1-4. | Do not add Section D/E or extra top-level sections. |
| No premature downstream artifacts | VERIFIED | No file rows, prompts, expected outputs, goldens, grader guidance, labs, vitals, notes, or synthetic files are created. | Preserve phase gate. |

## 6. Recommended Construction Plan After Skeleton Lock

1. World Spec Skeleton review and lock.
2. World Spec v1 prose construction using the official template structure.
3. World Spec v1 review.
4. World Spec lock.
5. File Inventory Architecture.
6. Synthetic world-level files.
7. Task-level files.
8. Task prompts.
9. Expected outputs.
10. Goldens.
11. Grader guidance.
12. AutoQC preparation and submission packaging.

Construction guardrail: the order above is a recommendation for phase discipline only. It does not authorize downstream artifacts before Alexander explicitly starts each step.

## World Spec Skeleton Consistency Review

### VERIFIED

Finding: skeleton is consistent with all locked preparation artifacts.

Evidence: each proposed section maps to a locked source package and no section introduces new clinical facts.

Impact: final World Spec construction can proceed from ratified architecture.

Action required: use locked source packages during drafting.

### VERIFIED

Finding: no premature file creation occurred.

Evidence: Section 3 is mapped structurally but contains no file inventory rows, filenames, source/tool rows, IDs, or synthetic documents.

Impact: file planning remains correctly downstream of task design.

Action required: stop before file inventory architecture.

### VERIFIED

Finding: no premature task drafting occurred.

Evidence: Section 2 maps task architecture only and does not create prompts, expected outputs, failure design tables, task-level file lines, or grader guidance.

Impact: physician-authored prompt requirement remains protected.

Action required: preserve task prompt boundary.

### VERIFIED

Finding: skeleton does not conflict with Studio requirements.

Evidence: it preserves the official four-section template, future separate reference file handling, later transcript work, and later AutoQC validation.

Impact: submission workflow remains intact.

Action required: use official DOCX template for final artifact.

### VERIFIED

Finding: traps and frictions do not collapse.

Evidence: frictions map to Governance Package and traps map to Brainstorm/Daily Framework/Task Architecture with separate boundary rules.

Impact: people conflicts and information traps remain distinct.

Action required: preserve Decision Friction Table and source-trap distinction in drafting.

### VERIFIED

Finding: source-of-truth hierarchy is preserved.

Evidence: master hierarchy and prednisone-specific hierarchy are assigned to Section 1 and later Section 3 provenance.

Impact: conflicting information can be resolved without erasing consultant disagreement.

Action required: state hierarchy explicitly in final World Spec.

### VERIFIED

Finding: no timeline drift is introduced.

Evidence: skeleton relies on the locked calendar and daily hospital course framework rather than creating new dates.

Impact: HD6 world close, discharge anchor, +7, and +30 doctrine remain intact.

Action required: no new dates without Key Milestones update.

### PLAUSIBLE

Finding: the skeleton can support all six task concepts.

Evidence: task architecture is locked, but full task specs, expected outputs, and file dependencies remain future work.

Impact: structure is ready, but task solvability cannot be fully verified until Section 2 and Section 3 are built.

Action required: build tasks before file inventory.

### DISPUTED

Finding: file inventory should begin now.

Evidence: official playbook says file planning comes after task design; this skeleton explicitly stops before file rows.

Impact: starting file rows now would risk reverse-engineering files before task requirements are stable.

Action required: do not start file inventory from this artifact.

### NO ISSUE

Finding: this artifact creates no prohibited downstream content.

Evidence: it contains no final prose, synthetic files, file inventory rows, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, reference files, or templates.

Impact: phase boundary remains intact.

Action required: proceed only when Alexander authorizes the next construction step.

## Final Status

World Spec Skeleton v1

Status: LOCKED
