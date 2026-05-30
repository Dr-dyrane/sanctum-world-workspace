# Post-GO World Spec Interview Plan

Status: preparation only.

Trigger: use this plan only after Brainstorm Human Review returns GO and Alexander authorizes World Spec decision work.

Boundary: this is an interview sequence, not a World Spec draft. Do not populate the World Spec template, create a World File Plan inventory, write task prompts, write golden responses, or invent clinical details from this document.

Source inputs:

- `worlds/james-carter/world-spec-prep/claude-review-triage.md`
- `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/templates/World_Spec_Template_05_06.docx`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`

## Phase 1: Identity And Compliance Decisions

Goal: establish a single synthetic identity block before any World Spec section is populated.

### Decision 1.1: Synthetic Patient Name

Why AutoQC requires it:

- World Spec AutoQC treats patient identity as a hard rule.
- The name must be clearly invented and not generically plausible.

Relevant AutoQC checks:

- 2.1 Header Table Complete
- 2.2 Patient Name Synthetic
- 2.8 Patient Profile Identity Fields
- 2.55 Cross-Cutting Identity Across Sections

Reviewer risks:

- A common first-name plus surname combination can fail the World Spec even if the Brainstorm passed fictional identity.
- Changing the name inconsistently across header, patient profile, tasks, filenames, and summaries creates cross-section identity failures.

Physician decision required:

- Choose the final synthetic patient name to use in the World Spec.
- Decide whether the working title "James Carter World" remains an internal/project title while the patient identity changes for submission.

### Decision 1.2: Synthetic MRN

Why AutoQC requires it:

- MRN must not resemble a real institutional numbering pattern.

Relevant AutoQC checks:

- 2.3 MRN Synthetic Format
- 2.8 Patient Profile Identity Fields
- 2.55 Cross-Cutting Identity Across Sections

Reviewer risks:

- A bare numeric MRN or familiar hospital-style format may look real.
- MRN inconsistency across sections or future files undermines the synthetic identity rule.

Physician decision required:

- Approve a clearly synthetic MRN format.
- Decide whether the MRN should be visible in every simulated chart artifact or only in selected file types later.

### Decision 1.3: Demographics And Anthropometrics Consistency

Why AutoQC requires it:

- Age, DOB, sex, height, weight, BMI, allergies, code status, and relevant demographics must be populated and internally consistent.

Relevant AutoQC checks:

- 2.8 Patient Profile Identity Fields
- 2.9 Patient Profile Anthropometrics Self-Consistent
- 2.10 Patient Profile Allergies Populated
- 2.15 Code Status Populated
- 2.55 Cross-Cutting Identity Across Sections
- 2.56 Cross-Cutting Anthropometrics Consistent
- 2.100 Patient DOB Matches Stated Age

Reviewer risks:

- DOB and age do not match the snapshot date.
- Height/weight/BMI arithmetic is wrong.
- Demographics are added as filler rather than because they matter clinically or socially.

Physician decision required:

- Confirm final age, DOB relative to the snapshot date, sex, allergies, code status, height, weight, BMI, and any clinically relevant social/demographic details.

## Phase 2: Clinical Scenario Decisions

Goal: convert the approved Brainstorm concept into a coherent, source-backed clinical scenario plan before drafting.

### Decision 2.1: Calendar Timeline And World Snapshot

Why AutoQC requires it:

- The World Spec needs exact MM/DD/YYYY dates, a definite world snapshot, and task anchors after the snapshot.

Relevant AutoQC checks:

- 2.20 Key Milestones Date/Event Table Format
- 2.21 Key Milestones MM/DD/YYYY Format
- 2.22 Every Spec Date Listed in Milestones
- 2.23 No Orphan Milestones
- 2.41 Temporal Architecture Verified
- 2.61 Display Date Format MM/DD/YYYY

Reviewer risks:

- Keeping Brainstorm-style "Hospital Day 6" language without calendar dates.
- Creating a task anchored before or during the world snapshot.
- Creating a world document dated after a task anchor.

Physician decision required:

- Choose an index ED arrival date.
- Confirm the world snapshot date/time equivalent to the approved concept: Hospital Day 6 at 18:00 during discharge planning.
- Choose post-snapshot task anchor dates only after the snapshot.

### Decision 2.2: Key Milestones

Why AutoQC requires it:

- Every date used in tasks, traps, filenames, narrative, and file descriptions must appear in the Key Milestones table.

Relevant AutoQC checks:

- 2.17 Clinical History Coverage
- 2.20 Key Milestones Date/Event Table Format
- 2.22 Every Spec Date Listed in Milestones
- 2.23 No Orphan Milestones
- 2.44 File Dates Match Milestones
- 2.90 Trap Locked to Specific Date or Document

Reviewer risks:

- Milestones become a full timeline draft rather than a compressed date/event anchor table.
- Dates appear in task anchors or file rows but not milestones.
- Milestones include unused dates that create orphan-date failures.

Physician decision required:

- Identify the minimum necessary milestone events: ED presentation, admission, key clinical turning points, consultant inputs, medication decision points, functional/cognitive observations, discharge-planning snapshot, and post-snapshot task anchors.

### Decision 2.3: Source-Of-Truth / Authority Hierarchy

Why AutoQC requires it:

- This world depends on authority ambiguity: steroid timeline, medication lists, consultant recommendations, nursing/PT/family observations, and discharge-planning documents can conflict.

Relevant AutoQC checks:

- 2.13 Multiple Med Lists Labeled
- 2.14 Decision Friction Table Present
- 2.18 Clinical History Fact Provenance
- 2.37 Frictions vs Traps Distinguished
- 2.57 Cross-Cutting Medication Doses Consistent
- 2.65 Source-of-Truth Hierarchy Documented

Reviewer risks:

- Treating the newest note as automatically correct.
- Treating family report, EMR med list, active orders, discharge med list, or consultant note as interchangeable.
- Making intentional contradictions look like drafting errors.

Physician decision required:

- Approve a hierarchy for this world, including how to weigh attending/team decisions, consultant notes, active orders/MAR, medication reconciliation, outpatient/rheumatology records, nursing/PT notes, and family report.
- Decide where the hierarchy will be documented in the spec.

## Phase 3: Task Architecture Decisions

Goal: finalize task architecture decisions before any task prompts or Expected Output blocks are written.

### Decision 3.1: Workflow Consolidation

Why AutoQC requires it:

- World Spec v6.3 requires 3-5 distinct approved catalog workflows across the task suite.

Relevant AutoQC checks:

- 2.28 Task Required Components Present
- 2.39 Single Deliverable Per Task
- 2.40 Task Independence
- 2.98 Workflow Names Match Approved Tracker
- 2.107 Three to Five Distinct Catalog Workflows Per World

Reviewer risks:

- Carrying six distinct Brainstorm workflow mappings directly into the World Spec.
- Changing the clinical foundation instead of only consolidating workflow labels or task architecture with physician approval.
- Creating near-duplicate tasks while trying to reduce workflow count.

Physician decision required:

- Decide which approved task concepts share workflow categories.
- Confirm the final distinct workflow count is 3-5.
- Preserve the approved clinical intent while adjusting only what is needed for World Spec compliance.

### Decision 3.2: Administrative Deliverable Determination

Why AutoQC requires it:

- Typical clinical and medical director worlds should include both clinical and healthcare administration work products where appropriate.

Relevant AutoQC checks:

- 2.98 Workflow Names Match Approved Tracker
- 2.108 World Includes Both Clinical and Administrative Work
- 2.110 Task Output Type Diversity
- 2.111 Task Audience Diversity

Reviewer risks:

- The task suite reads as discharge documentation only.
- Adding an administrative task that feels bolted on or inconsistent with the hospital medicine world.
- Replacing the case's clinical strength with an admin-only detour.

Physician decision required:

- Decide whether one existing rough task can become or map to a clinically grounded administrative deliverable, such as quality/safety, utilization review, readmission-risk review, or another approved tracker workflow.
- If no fit is clinically appropriate, decide whether to seek team clarification rather than force an admin deliverable.

### Decision 3.3: Task Independence And Temporal Anchors

Why AutoQC requires it:

- Each task must be standalone, have one deliverable, and occur after the world snapshot.

Relevant AutoQC checks:

- 2.28 Task Required Components Present
- 2.30 Task Natural Anchor
- 2.38 Task-Level Files Line Populated
- 2.39 Single Deliverable Per Task
- 2.40 Task Independence
- 2.41 Temporal Architecture Verified
- 2.112 Temporal Reasoning Task Present

Reviewer risks:

- Follow-up/readmission-style tasks depend on a discharge summary generated by another task.
- Task prompt combines multiple deliverables.
- Task anchor is inside the hospitalization rather than after the snapshot.

Physician decision required:

- For each task, approve a single requester, single deliverable, task anchor date, and independence statement.
- Confirm no task uses another task's output as input.

## Phase 4: Traceability And File Strategy

Goal: design the evidence discipline before writing Section 3 or Expected Output content.

### Decision 4.1: Evidence Provenance Workflow

Why AutoQC requires it:

- Every clinical fact used outside Section 1 must trace to the Clinical History narrative or a World File Plan row.

Relevant AutoQC checks:

- 2.18 Clinical History Fact Provenance
- 2.35 Trap Remediation Grounded
- 2.48 Fact-to-File Traceability
- 2.49 Trap Substrate in File Plan
- 2.58 Cross-Cutting Lab Values Consistent
- 2.60 Cross-Cutting No Fabricated Content

Reviewer risks:

- Lab values, medication doses, consultant recommendations, or functional findings appear in Expected Output or Failure Design without a file home.
- Correct reasoning relies on outside medical knowledge instead of chart evidence.
- Uncertainty is converted into an unsupported assertion.

Physician decision required:

- Approve a traceability-map workflow before drafting: every key fact gets a source location or is explicitly left uncertain.
- Decide which facts belong in Clinical History versus simulated chart files later.

### Decision 4.2: File Modalities

Why AutoQC requires it:

- The World File Plan must have enough files, complete rows, and at least four modalities.

Relevant AutoQC checks:

- 2.42 File Plan Row Completeness
- 2.45 Total File Count Statement
- 2.46 No File ID Collisions
- 2.50 Supplementary Litmus Test
- 2.51 Modality Diversity
- 2.52 Essential vs Supplementary Mix

Reviewer risks:

- File plan is mostly physician progress notes.
- Supplementary files contain answer-changing evidence.
- File count or modality diversity is too thin for a realistic hospital world.

Physician decision required:

- Approve modality categories to consider later: ED/admission notes, progress notes, consultant notes, nursing notes, PT/case-management notes, labs/vitals trends, MAR/orders/med lists, outpatient records, and discharge-planning documentation.
- Confirm that no final file inventory is created until task architecture is approved.

### Decision 4.3: Trap Substrate Planning

Why AutoQC requires it:

- Every trap must be anchored to a date and document, and task Failure Design tables must avoid unsupported or duplicated trap rows.

Relevant AutoQC checks:

- 2.34 Failure Design Trap Count Minimum 5
- 2.35 Trap Remediation Grounded
- 2.36 Plausible Wrong Answer
- 2.49 Trap Substrate in File Plan
- 2.90 Trap Locked to Specific Date or Document
- 2.91 No Duplicate Traps Across Tasks

Reviewer risks:

- World-level traps are copied into every task's Failure Design table.
- Trap remediation cites a document that does not exist in the file plan.
- Steroid or medication contradictions look accidental rather than intentional.

Physician decision required:

- Decide the primary trap for each task and which shared world traps are referenced but not re-entered.
- Approve which planned document types will eventually carry each trap.
- Confirm that every wrong answer is something a careful but imperfect clinician could plausibly produce.

## First Interview Sequence After GO

1. Confirm Brainstorm Human Review result and whether any reviewer conditions apply.
2. Resolve Phase 1 identity/compliance decisions.
3. Resolve Phase 2 calendar timeline, milestones, and authority hierarchy.
4. Resolve Phase 3 task architecture decisions before prompts or expected outputs.
5. Resolve Phase 4 traceability/file-strategy decisions before any Section 3 file plan rows.
6. Only after the above, ask Alexander for explicit approval to begin World Spec drafting in the official template.

## Stop Conditions

- Brainstorm has not returned GO.
- Reviewer returns SEND BACK instead of GO.
- A decision would require changing the approved Brainstorm foundation without Alexander's explicit approval.
- A proposed task prompt, golden response, grader guideline, file inventory, synthetic file, or final World Spec text starts to emerge before authorization.
