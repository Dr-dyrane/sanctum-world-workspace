# Claude Review Triage - World Spec Preparation

Date: 2026-05-29

Status note: historical pre-GO World Spec preparation artifact. Some findings mention waiting for Brainstorm GO; those are superseded by reviewer approval and the ratified Clinical Story Skeleton. For live state, use `project/STATUS.md` and `WORLD_SPEC_KICKOFF.md`.

Scope: Preparation only. Brainstorm remained submitted and unchanged at the time of this artifact. World Spec drafting is still not authorized until Alexander explicitly authorizes drafting.

Reviewed artifact: `C:\Users\Dyrane\Downloads\Pasted markdown(17).md`

Primary source materials checked:

- `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/templates/World_Spec_Template_05_06.docx`
- `reference/templates/brainstorm.docx`
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md`
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-02.md`
- `reference/New Writers Version - Instruction Guide (05_24).md`

## Executive Triage

Claude's review is useful but mixes three different things:

- Verified World Spec requirements from AutoQC v6.3.
- Plausible reviewer risks that should shape the physician interview after GO.
- Unsupported or overextended claims, especially where Claude treats a World Spec requirement as a current Brainstorm failure.

The biggest true World Spec risks are:

- Patient name must be unmistakably synthetic in the World Spec.
- The final World Spec task suite must contain 3-5 distinct approved workflows.
- The task set must include clinical and healthcare administration work products where appropriate.
- The World Spec needs a Decision Friction Table if it depends on 2 or more specialty conflicts or embedded diagnostic conflicts.
- A source-of-truth hierarchy is required because this world has authority/source ambiguity traps.
- Every expected-output and failure-design fact must trace to the Clinical History narrative or a World File Plan row.

Reviewer SEND BACK subsequently required a synthetic-name remediation at the Brainstorm stage. The active remediation name is Korvin Merrow.

## Patient Name Audit

### Does the synthetic patient-name requirement apply to World Spec?

VERIFIED. AutoQC v6.3 Check 2.2 is titled "Patient Name Synthetic." The underlying DOCX states:

- Source: `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`, paragraph 37 and table 11.
- Severity: Blocker.
- Description: "Patient name is clearly invented and not generically plausible."
- Pass criteria: "Patient name is unmistakably synthetic. Generic combinations (common first name + common surname) are avoided; playful or clearly invented names are preferred."
- Fail criteria: "Patient name is generically plausible and could belong to a real person."

The local index records the same rule at `reference/world-spec-guidelines/08_autoqc_master_index.md:14`.

### Does the synthetic patient-name requirement apply to Brainstorm?

DISPUTED as stated. The local Brainstorm template requires patient/world setup but does not contain the World Spec v6.3 synthetic-name blocker. The Brainstorm AutoQC standard captured locally is "Fictional Patient Identity," not "Patient Name Synthetic."

Evidence:

- `reference/templates/brainstorm.docx`, table 0: Brainstorm asks for demographics, comorbidities, environment, encounter type, and timeline shape.
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md:113`: "Fictional Patient Identity."
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md:115`: "The name is clearly invented and no real identifiers are used... This meets the pass criteria at the brainstorm stage."
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-02.md`: final Brainstorm AutoQC passed with no failures or neutral items.

Conclusion: Brainstorm passed its identity check. The stricter synthetic-name blocker should be treated as a World Spec preparation decision, not a retroactive Brainstorm defect.

### What did this imply for the reviewer name fix?

VERIFIED as a risk for the prior submitted patient name because reviewer feedback specifically flagged that name as common and requested a more unmistakably fictional replacement. The current remediation name, Korvin Merrow, was supplied in the reviewer remediation instruction and should still be checked in the next Brainstorm AutoQC pass.

Action required now: use Korvin Merrow consistently in the Brainstorm remediation package and verify no active references to the prior name remain outside historical archives.

### Are there examples of acceptable synthetic names?

DISPUTED if Claude implies the sources provide exact acceptable patient names. The local AutoQC gives a category, not a list: "playful or clearly invented names are preferred." The local World Spec template uses placeholders only: `[Patient Name (fictional)]` and `[Full name (fictional)]`.

Important caution: the AutoQC filename examples `Joseph_World_Marcus_latest_4_14` and `Joseph_World_Marcus_latest_5_12` are filename convention examples, not validated examples of acceptable synthetic patient names.

## High-Priority Findings

| Classification | Finding | Evidence | Impact | Action required |
| --- | --- | --- | --- | --- |
| VERIFIED | World Spec patient name must be synthetic. | AutoQC v6.3 2.2; `08_autoqc_master_index.md:14`; World Spec template requires fictional name in header/profile. | Blocker if the World Spec uses a generically plausible name. | Carry Korvin Merrow consistently into any later World Spec if Brainstorm remediation is accepted. |
| VERIFIED | World Spec task suite must use 3-5 distinct approved catalog workflows. | AutoQC v6.3 2.107; `08_autoqc_master_index.md:119`. | Major fail if the spec keeps 6 distinct workflows. | After GO, decide how to consolidate existing task concepts into 3-5 distinct workflows without changing the approved clinical foundation until authorized. |
| VERIFIED | World Spec should include clinical and healthcare administration work products where appropriate. | AutoQC v6.3 2.108; `08_autoqc_master_index.md:120`. | Major fail if this typical clinical world remains entirely clinical when an admin-clinical task is expected. | After GO, ask physician whether one approved task can map to an admin-clinical deliverable already consistent with the world, or whether team clarification is needed. |
| VERIFIED | Decision Friction Table is required when the world depends on 2 or more specialty conflicts or embedded diagnostic conflicts. | AutoQC v6.3 2.14; `08_autoqc_master_index.md:26`; World Spec template table 2 describes the table format. | Major fail if frictions remain prose only in the World Spec. | After GO, populate a Decision Friction Table from the locked frictions: Nephrology vs Cardiology, Family vs Inpatient Medicine, Hospital Medicine vs Endocrinology. |
| VERIFIED | Source-of-truth hierarchy must be documented when authority traps are present. | AutoQC v6.3 2.65; `08_autoqc_master_index.md:77`; World Spec template table 2 includes a Data Hierarchy Note. | Major fail because steroid timeline, medication reconciliation, and outdated recommendations depend on authority/source hierarchy. | After GO, create a hierarchy decision with Alexander before drafting the spec. |
| VERIFIED | Traceability is required from task Expected Output and Failure Design facts to World File Plan rows. | AutoQC v6.3 2.18, 2.48, 2.49, 2.60; `08_autoqc_master_index.md:30`, `:60`, `:61`, `:72`. | Blocker risk if any lab, dose, date, diagnosis, or remediation fact lacks a file/narrative source. | After GO, build a traceability matrix before filling task specs or file plan rows. |

## Top 20 Reviewer Risks From Claude

| ID | Classification | Finding | Evidence | Impact | Action required |
| --- | --- | --- | --- | --- | --- |
| R1 | VERIFIED | Prior submitted name was not synthetic enough for reviewer expectations. | Reviewer SEND BACK explicitly required replacement with Korvin Merrow; AutoQC 2.2 supports the synthetic-name principle. | High rejection risk if any active reference remains. | Use Korvin Merrow consistently and audit active files. |
| R2 | PLAUSIBLE | Task suite may look clinically monolithic. | AutoQC 2.108 supports clinical plus admin mix where appropriate. | Major World Spec risk if no admin-clinical deliverable is included. | Ask physician/team after GO before restructuring. |
| R3 | VERIFIED | Six distinct workflows exceed World Spec workflow-count ceiling. | AutoQC 2.107 requires 3-5 distinct workflows. | Major fail if unchanged in the World Spec. | Consolidate workflow mappings only after GO and approval. |
| R4 | VERIFIED | Frictions cannot remain prose only. | AutoQC 2.14 requires Decision Friction Table when 2+ conflicts exist. | Major fail if absent. | Build table after GO. |
| R5 | PLAUSIBLE | Endocrinology friction needs an advocacy artifact. | AutoQC 2.37 requires frictions separated from traps; Section 3 requires file substrate for traps and facts. | Human reviewer may see the Endocrinology issue as a trap unless an actual consult carries a position. | During physician interview, decide what document carries Endocrinology's position. |
| R6 | PLAUSIBLE | Steroid thread could drift into a reveal. | Brainstorm intent explicitly rejects "missed adrenal insufficiency"; AutoQC 2.31 prohibits trap hints. | Reviewer risk if adrenal insufficiency becomes the hidden answer. | Preserve steroid issue as one competing concern. |
| R7 | VERIFIED | Trap tables can fail if thin or duplicative. | AutoQC 2.34 requires at least 5 traps per Failure Design table; 2.91 prevents duplicate traps across tasks without acknowledgment. | Major/minor risk depending on table construction. | Use distinct task-level traps and reference shared world traps without re-entering them. |
| R8 | VERIFIED | Plausible wrong answers must be clinically tempting. | AutoQC 2.36. | Major fail if traps are contrived. | Alexander should vet each failure mode during task-spec interview. |
| R9 | VERIFIED | Expected Output cannot be generic. | AutoQC 2.32 and 2.33. | Major fail and grader weakness. | Define format, register, length range, and checked anchors later without writing goldens. |
| R10 | VERIFIED | Prompts must not telegraph traps. | AutoQC 2.31. | Major fail if prompts mention adrenal/steroid trap too directly. | Keep prompts natural and clinician-voiced. |
| R11 | VERIFIED | Source-of-truth hierarchy must be documented. | AutoQC 2.65. | Major fail if authority ambiguity is unresolved. | Decide hierarchy before World Spec drafting. |
| R12 | VERIFIED | Self-containment and provenance are hard rules. | AutoQC 2.18, 2.48, 2.60. | Blocker risk. | Use traceability matrix before finalizing expected outputs/failure design. |
| R13 | PLAUSIBLE | A single over-authoritative discharge synthesis could make tasks too easy. | Supported indirectly by the world purpose and AutoQC emphasis on complexity and traceability; no exact single-source prohibition found. | Human reviewer difficulty risk. | Avoid one file that solves all tasks, but verify against file-plan requirements after GO. |
| R14 | VERIFIED | Difficulty must be engineered, not asserted. | AutoQC 2.24 requires explaining why the world is hard for AI beyond a problem list. | Major risk if clinical complexity is just a list. | Write complexity as synthesis failure modes after physician interview. |
| R15 | PLAUSIBLE | Snapshot/discharge timing could become muddled. | AutoQC 2.41 requires definite snapshot and all task anchors after it; Brainstorm final AutoQC already passed HD6 18:00 concept-level anchor. | Blocker if any World Spec file or task date violates temporal gate. | Convert HD anchors to calendar dates after GO. |
| R16 | VERIFIED | File plan needs modality diversity. | AutoQC 2.51 requires at least 4 modalities. | Major risk if file plan is mostly notes. | Plan documents across notes, consults, labs, MAR, nursing/PT, outpatient records. |
| R17 | PLAUSIBLE | Functional/cognitive evidence must be discoverable but not telegraphed. | Supported by Brainstorm trap design and AutoQC 2.31/2.36; not a separate named check. | Human reviewer fairness/difficulty risk. | Calibrate during file-plan interview after GO. |
| R18 | VERIFIED | Medication/steroid conflicts must not read as writing errors. | AutoQC 2.13, 2.57, 2.90 require labeled med lists, dose consistency, and trap anchoring. | Major risk if intentional conflicts are unlabeled. | Label temporal/source scope for medication lists and trap substrates. |
| R19 | VERIFIED | Tasks must be independent. | AutoQC 2.40. | Blocker if one task depends on another task output. | Keep each task as standalone against the frozen world. |
| R20 | PLAUSIBLE | Correct vs plausible-wrong paths need separable evidence. | AutoQC 2.32, 2.35, 2.36, 2.48 support this. | Reviewer/grading risk if near-misses cannot be judged. | Ensure remediations cite chart evidence; do not write goldens yet. |

## Top 20 AutoQC Risks From Claude

| ID | Classification | Finding | Evidence | Impact | Action required |
| --- | --- | --- | --- | --- | --- |
| Q1 | PLAUSIBLE | Current remediated patient name still needs confirmation on rerun. | AutoQC 2.2 verified; Korvin Merrow has not yet been rerun through RL Studio Brainstorm AutoQC after remediation. | Low-to-moderate residual risk until rerun confirms pass. | Verify on next Brainstorm AutoQC after approved clinical edits are incorporated. |
| Q2 | VERIFIED | More than 5 distinct workflows fails 2.107. | AutoQC 2.107. | Major fail. | Consolidate later with approval. |
| Q3 | VERIFIED | Missing admin deliverable can fail 2.108. | AutoQC 2.108. | Major fail where appropriate. | Confirm task-suite strategy after GO. |
| Q4 | VERIFIED | Decision Friction Table required. | AutoQC 2.14. | Major fail. | Add in World Spec only after GO. |
| Q5 | VERIFIED | Frictions and traps must be separated. | AutoQC 2.37. | Major fail if conflated. | Keep frictions in Decision Friction Table or task sub-blocks; traps in Failure Design. |
| Q6 | VERIFIED | Source-of-truth hierarchy required for authority traps. | AutoQC 2.65. | Major fail. | Decide hierarchy before drafting. |
| Q7 | VERIFIED | Trap count and duplicate trap handling are risks. | AutoQC 2.34 and 2.91. | Failure if undercounted or duplicated. | Build task-specific trap architecture later. |
| Q8 | VERIFIED | Each trap needs date/document substrate. | AutoQC 2.90 and 2.49. | Major/file-plan risk. | Lock traps to milestone dates and file rows after GO. |
| Q9 | VERIFIED | Expected-output and failure-design facts need file traceability. | AutoQC 2.48. | Blocker. | Build traceability map before final spec. |
| Q10 | VERIFIED | Clinical fact provenance and no fabrication are hard rules. | AutoQC 2.18 and 2.60. | Blocker. | Do not invent unsupported labs, doses, dates, or entities. |
| Q11 | VERIFIED | Medication dose/list consistency needs temporal labels. | AutoQC 2.13 and 2.57. | Major risk in steroid/HF-AKI design. | Label med-list origin and date in World Spec. |
| Q12 | VERIFIED | Task components and MM/DD/YYYY anchors required. | AutoQC 2.28 and 2.21. | Major/minor risk. | Convert all anchors after GO. |
| Q13 | VERIFIED | Temporal architecture is a blocker gate. | AutoQC 2.41. | Automatic fail if any task/file date violates snapshot logic. | Build timeline first after GO. |
| Q14 | VERIFIED | Trap hints in prompts fail. | AutoQC 2.31. | Major fail. | Keep draft prompts neutral and natural later. |
| Q15 | VERIFIED | Expected outputs must be specific and differentiated. | AutoQC 2.32 and 2.33. | Major fail. | Define output shape per task, not golden responses. |
| Q16 | VERIFIED | World File Plan must include at least 20 files and proper supplementary logic. | AutoQC 2.45 and 2.50. | Minor/major risk. | Plan file count and essential/supplementary split after GO. |
| Q17 | VERIFIED | At least 4 file modalities required. | AutoQC 2.51. | Major fail. | Use multi-modal chart plan after GO. |
| Q18 | VERIFIED | DOB, age, anthropometrics must reconcile. | AutoQC 2.9, 2.56, 2.100. | Major risk. | Create a single identity/demographics source after GO. |
| Q19 | VERIFIED | MRN must be synthetic. | AutoQC 2.3. | Blocker. | Choose synthetic MRN format after GO. |
| Q20 | VERIFIED | Single deliverable and task independence required. | AutoQC 2.39 and 2.40. | Major/blocker risk. | Keep one deliverable per task and no cross-task dependencies. |

## Common Accidental Violations

| Classification | Finding | Evidence | Impact | Action required |
| --- | --- | --- | --- | --- |
| VERIFIED | Self-containment violations are a real World Spec risk. | AutoQC 2.18, 2.48, 2.60. | Blocker if the correct answer needs facts outside the world. | Use a source-backed traceability matrix. |
| VERIFIED | Trap design must be document/date anchored and clinically plausible. | AutoQC 2.35, 2.36, 2.49, 2.90. | Major risk if traps become quizzes or unsupported claims. | Anchor each trap after GO. |
| VERIFIED | Frictions must be people/perspective conflicts, not information gaps. | AutoQC 2.14, 2.37; Brainstorm template distinguishes traps vs frictions. | Major risk if Endocrinology or outpatient history collapses into a trap. | Keep advocacy positions in the Decision Friction Table. |
| VERIFIED | Task independence must be preserved. | AutoQC 2.40. | Blocker if tasks chain outputs. | Each task reads the frozen world only. |
| VERIFIED | File-plan consistency is a major World Spec burden. | AutoQC 2.42-2.52, 2.113. | Multiple failure paths. | Build file plan only after GO and after task architecture decisions. |

## Readiness Assessment Triage

| Classification | Finding | Evidence | Impact | Action required |
| --- | --- | --- | --- | --- |
| VERIFIED | Brainstorm has a strong approved substrate but is still awaiting human GO. | RL Studio status recorded in `project/STATUS.md`; final AutoQC recorded in `brainstorm-autoqc-02.md`. | We can prepare but not draft World Spec. | Wait for GO before World Spec drafting. |
| PLAUSIBLE | Concrete clinical details, calendar dates, labs, doses, provider names, file rows, and hierarchy decisions remain physician decisions. | World Spec AutoQC requires these details, but current authorization forbids inventing them. | Expected preparation gap, not failure. | Interview Alexander after GO. |
| PLAUSIBLE | Patient name, workflow count, and admin-deliverable issues may require changes after GO. | Supported by AutoQC 2.2, 2.107, 2.108. | These are the most likely early World Spec structural blockers. | Queue as first post-GO decisions. |
| DISPUTED | "Two Blocker/Major failures are already live in the approved brainstorm." | Brainstorm AutoQC passed 51/51 and identity passed at Brainstorm stage. World Spec checks are stricter and apply to a not-yet-drafted artifact. | Treating this as a Brainstorm defect could cause unnecessary churn. | Do not edit Brainstorm. Reassess after Human Review GO. |

## Decision Queue For After Brainstorm GO

These are decisions, not drafts:

1. Choose a World Spec patient name that is unmistakably synthetic.
2. Choose a synthetic MRN format.
3. Decide whether/how to consolidate six rough task ideas into 3-5 distinct approved workflows.
4. Decide whether one task should become or map to a healthcare administration deliverable consistent with the existing clinical foundation.
5. Approve the source-of-truth hierarchy for conflicting steroid, medication, consultant, nursing/PT, family, and discharge-planning evidence.
6. Approve the Decision Friction Table structure.
7. Approve a traceability-map workflow before any Expected Output or Failure Design content is finalized.

## Boundaries Preserved

- Brainstorm was not modified.
- Task concepts were not modified.
- World Spec was not drafted.
- World Spec template was not populated.
- No file inventory was created.
- No clinical values, dates, labs, medications, providers, MRNs, or patient names were invented.
- No task prompts, golden responses, grader guidelines, or failure-analysis content were created.
