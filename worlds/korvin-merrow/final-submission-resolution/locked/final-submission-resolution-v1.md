# Final Submission Resolution v1

Date: 2026-06-03

Status: CANDIDATE REVIEW

Purpose: resolve final submission dependencies and export architecture before execution and artifact generation.

Scope boundary: this artifact makes execution-ready decisions only. It does not populate DOCX files, generate PDF files, create a manifest, create a submission package, run AutoQC, upload anything, submit anything, modify locked artifacts, create scoring artifacts, or create AutoQC responses.

## 1. Authoritative Evidence Reviewed

### Official Template Evidence

- `reference/templates/World_Spec_Template_05_06.docx` is the controlling World Spec template.
- The template is organized as one Word document with four canonical sections:
  - 1. Clinical Scenario.
  - 2. Task Specifications.
  - 3. World File Plan.
  - 4. World Summary.
- The template contains separate World File Plan subsections for:
  - Essential Files (World-Level).
  - Essential Files (Task-Level).
  - Supplementary Files.
- The template, not example-world variation, governs final World Spec structure.

### Official Upload And Guidance Evidence

- `reference/source/New Writers Version - Instruction Guide (05_24).md` states that writers upload the World Spec document to RL Studio, upload template/reference files needed for the spec, run spec-stage AutoQC, address audit items, and re-upload as needed.
- The same source states that the World Spec is finalized as `.docx`.
- The same source describes template/reference files as world-level templates, public-domain references, custom-made templates, and writer-produced world-level files that support engineering conversion.
- The same source states that template/reference files are uploaded individually, not as a zip.
- The same source identifies task prompts, golden responses, and grader guidelines as later pipeline artifacts, not current World Spec submission uploads.
- Local transcript text-source evidence remains limited, but the current RL Studio UI evidence and locked Transcript Resolution resolve the transcript mechanism as file upload.

### AutoQC Evidence

- `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx` says the writer uploads the world spec `.docx`, the approved Brainstorm document, and templates/reference files for World Spec QC.
- `reference/world-spec-guidelines/08_autoqc_master_index.md` records the v6.3 file-plan expectation, including row completeness and Source / Tool / Template-Reference-Origin separation.
- The v6.3 8-column issue is resolved for Korvin by preserving the locked File Inventory v1 structure as the source mapping while using the official World Spec template as the final DOCX structure. Do not redesign the template during population.

### Example Evidence

- `reference/world-spec-examples/World_Spec_Document_Harold.docx`, `World_Spec_Document_Marcus.docx`, and `World_Spec_Document_Opus.docx` are Word documents.
- Example folders show separate areas for World Spec documents, synthetic file templates, world-level files, task-level folders, and QA.
- Example world-level files are delivered as document or original binary artifacts such as `.docx`, `.pdf`, `.png`, and `.jpg`; they are not Markdown submission files.
- Example task-level prompt, golden, and grader files are Word documents in task-level folders, supporting later pipeline organization rather than the current World Spec upload set.

### Current RL Studio Evidence

- Current RL Studio shows file-upload fields for:
  - 2.1 Spec Document.
  - 2.2 Template/Reference Files.
  - 2.3 Upload Claude Transcripts.
- Current RL Studio does not show a transcript text field; transcript mechanism is file upload.

### Locked Korvin Evidence

- World Spec v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- File Inventory v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`.
- FI-W01 through FI-W22 are locked under `worlds/korvin-merrow/synthetic-files/locked/batch-*/`.
- FI-T01 through FI-T07 are locked under `worlds/korvin-merrow/task-context-files/locked/`.
- FI-S01 through FI-S04 are locked under `worlds/korvin-merrow/supplementary-files/locked/`.
- Transcript Resolution is locked; `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact, and the Claude share URL is provenance.

## 2. Required Upload Set

### REQUIRED_UPLOAD

These are required for the current World Spec / pre-AutoQC upload sequence.

| Artifact | Source | Target Format | Upload Field | Rationale |
| --- | --- | --- | --- | --- |
| Final World Spec document | `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md` plus locked supporting layers | DOCX | 2.1 Spec Document | Official template and examples require Word document delivery. Markdown is working source only. |
| World-level template/reference package for FI-W01 through FI-W22 | Locked File Inventory v1 plus FI-W source artifacts | DOCX or original binary if a row is writer-produced media | 2.2 Template/Reference Files | Official guidance requires world-level templates/reference files needed for engineering conversion. Korvin has no authorized final binary file generation yet, so execution must create uploadable template/reference artifacts from locked FI-W sources. |
| Supplementary world-level template/reference package for FI-S01 through FI-S04 | Locked File Inventory v1 plus FI-S source artifacts | DOCX or original binary if a row is writer-produced media | 2.2 Template/Reference Files | Supplementary rows are part of the locked file inventory and support the world-level reference package while remaining background/supporting sources. |
| Claude transcript upload artifact | `docs/claude-transcript-formatted.md` | DOCX preferred; PDF optional; Markdown not final unless RL Studio explicitly accepts it at upload time | 2.3 Upload Claude Transcripts | Current RL Studio requires file upload. Markdown is a working format; transcript is document-like and should be exported before submission. |

### OPTIONAL_UPLOAD

These are optional or conditional. They should not be uploaded unless RL Studio, reviewer, pod lead guidance, or the execution operator specifically requests them.

| Artifact | Source | Target Format | Rationale |
| --- | --- | --- | --- |
| Approved Brainstorm document | `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx` | DOCX | AutoQC guidance identifies the approved Brainstorm as supplemental QC input. It is available as a reference attachment if requested. |
| Transcript PDF companion | Export from `docs/claude-transcript-formatted.md` | PDF | Optional read-only companion if reviewer-access fidelity is desired. Not required by current evidence. |
| Claude share URL provenance | `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` | Link evidence or included note inside transcript DOCX | Provenance support only. Current UI does not show a URL-only transcript field. |
| Task-level context file export package FI-T01 through FI-T07 | Locked FI-T source artifacts | DOCX | Optional for local staging and later task-level pipeline readiness. Current World Spec upload guidance says task-level files are out of scope for the world-level template/reference package unless RL Studio explicitly requests them. |
| Task prompts TP-KM01 through TP-KM06 | Locked task prompts | DOCX or PDF later | Later pipeline artifact. Not current pre-AutoQC upload unless a later task-level upload surface asks for it. |
| Expected outputs EO-KM01 through EO-KM06 | Locked expected outputs | DOCX or PDF later | Later pipeline/internal benchmark artifact. Not current pre-AutoQC upload unless explicitly requested. |
| Golden responses Golden-KM01 through Golden-KM06 | Locked goldens | DOCX or PDF later | Later pipeline/internal benchmark artifact. Not current pre-AutoQC upload unless explicitly requested. |
| Grader guidance GG-KM01 through GG-KM06 | Locked grader guidance | DOCX or PDF later | Later Section 6 / grader-guidance artifact. Not current pre-AutoQC upload unless explicitly requested. |

### DO_NOT_UPLOAD

These should not be uploaded for the current World Spec / pre-AutoQC execution.

| Artifact Class | Rationale |
| --- | --- |
| Markdown source files as final submission artifacts | Markdown is the workspace authoring format. Submission-facing text artifacts should be exported to DOCX unless official evidence explicitly requires Markdown. |
| Locked architecture packages, ratifications, reconciliations, validation reviews, and decision logs | Governance evidence only. They are not upload deliverables. |
| AutoQC Architecture / AutoQC Construction artifacts | Preparation artifacts only. They are not AutoQC responses and are not upload deliverables. |
| Packaging, Submission Preparation, Execution Preparation, Transcript Resolution artifacts | Preparation or resolution records only. They are not submission deliverables. |
| Candidate-review artifacts from earlier phases | Superseded or inactive lifecycle artifacts. |
| Raw transcript `docs/claude-transcript.md` | Historical/provenance only. The formatted transcript is the current candidate artifact. |
| Scoring rubrics, thresholds, point allocations, pass/fail bands | Prohibited. None should be created or uploaded. |
| AutoQC responses, DOCX artifacts, PDF artifacts, manifest, final package | Not created in this phase. They require later authorization. |

## 3. Submission Folder Mapping

Do not create this structure yet. It is the expected local staging map for the later Execution and Artifact Generation phase.

```text
korvin-merrow-final-submission-staging/
  01_spec-document/
    Korvin_Merrow_World_Spec.docx
  02_template-reference-files/
    world-level/
      FI-W01 through FI-W22 exported template/reference files
    supplementary/
      FI-S01 through FI-S04 exported template/reference files
    optional-task-level-hold/
      FI-T01 through FI-T07 exported files, only if RL Studio requests task-level context uploads
  03_claude-transcript/
    Korvin_Merrow_Claude_Transcript.docx
    optional: Korvin_Merrow_Claude_Transcript.pdf
  04_optional-qc-inputs/
    Korvin_Merrow_Brainstorm.docx
  05_hold-not-upload/
    prompt-golden-grader-guidance-exports, only if a later phase explicitly requests them
```

Expected RL Studio field mapping:

| RL Studio Field | Local Staging Folder | Upload Rule |
| --- | --- | --- |
| 2.1 Spec Document | `01_spec-document/` | Upload one DOCX. |
| 2.2 Template/Reference Files | `02_template-reference-files/world-level/` and `02_template-reference-files/supplementary/` | Upload each required file individually; do not zip. |
| 2.3 Upload Claude Transcripts | `03_claude-transcript/` | Upload transcript DOCX. PDF companion only if desired or requested. |
| AutoQC | none yet | Run only after explicit authorization. |
| AutoQC Notes | none yet | Create only after AutoQC results exist. |

## 4. Execution Inventory

### READY_NOW

These sources are complete and available for transformation.

| Artifact | Source | Status |
| --- | --- | --- |
| Locked World Spec v1 | `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md` | Ready as source for DOCX population. |
| Locked File Inventory v1 | `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md` | Ready as source for file-plan mapping and export inventory. |
| FI-W01 through FI-W22 | `worlds/korvin-merrow/synthetic-files/locked/batch-*/FI-W*.md` | Ready as source for world-level template/reference exports. |
| FI-S01 through FI-S04 | `worlds/korvin-merrow/supplementary-files/locked/FI-S*.md` | Ready as source for supplementary template/reference exports. |
| FI-T01 through FI-T07 | `worlds/korvin-merrow/task-context-files/locked/FI-T*.md` | Ready as optional/later task-level export sources. |
| Formatted transcript | `docs/claude-transcript-formatted.md` | Ready as source for transcript DOCX export. |
| Claude share URL | `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` | Ready as provenance evidence. |
| Approved Brainstorm | `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx` | Ready as optional QC supplemental input. |

### NEEDS_TRANSFORMATION

| Artifact | Required Transformation | Notes |
| --- | --- | --- |
| World Spec | Populate official DOCX template from locked Markdown and locked support packages | Must preserve official template structure and 7-column decision closure while carrying v6.3 source/tool/origin completeness where the template permits. |
| FI-W01 through FI-W22 template/reference exports | Convert or package as DOCX template/reference artifacts, unless a row is determined to require original binary media | Do not create final synthetic chart files beyond locked content. Use these as engineering-facing template/reference artifacts. |
| FI-S01 through FI-S04 template/reference exports | Convert or package as DOCX template/reference artifacts | Preserve their background/supporting role. |
| Claude transcript | Export formatted Markdown transcript to DOCX | Do not rewrite transcript content. Retain share URL provenance. |
| Optional transcript PDF | Export from the same transcript source after DOCX, only if authorized/requested | Not required by current evidence. |
| Optional FI-T task-level exports | Convert to DOCX only if RL Studio requests task-level context uploads or later task-level staging begins | Not required for current pre-AutoQC World Spec upload. |

### MISSING

| Missing Item | Impact | Resolution |
| --- | --- | --- |
| Final populated World Spec DOCX | Blocks Spec Document upload and AutoQC. | Create during Execution and Artifact Generation. |
| Exported world-level template/reference files for FI-W and FI-S | Blocks complete Template/Reference Files upload if current RL Studio field remains required. | Create during Execution and Artifact Generation. |
| Transcript DOCX | Blocks transcript file upload if Markdown is not accepted or if DOCX-first policy is followed. | Create during Execution and Artifact Generation. |
| Official Section 6 Grader Guidelines AutoQC prompt | Blocks later formal Section 6 AutoQC, not current World Spec pre-AutoQC upload. | Import only when authorized and available. |
| Manifest | Not needed before AutoQC; prohibited in this phase. | Create only after explicit manifest authorization. |

## 5. DOCX Population Blueprint

Use the official World Spec template as the structural base. Do not redesign it, modernize it, add unrelated columns, or remove template sections.

| Template Section | Source Artifact | Population Method |
| --- | --- | --- |
| Title/header | Locked World Spec v1; project status | Populate with Korvin Merrow world title and task/workflow summary. |
| 1. Clinical Scenario | `world-spec-v1.md`; locked identity, timeline, governance, medication, comorbidity, provider, and daily course packages | Populate narrative and tables from locked sources only. |
| 1.4 Key Milestones | `key-milestones-calendar-skeleton-v1.md`; `clinical-story-timeline-package-v1.md`; `world-spec-v1.md` | Populate compressed timeline without adding new dates. |
| 1.5 Clinical Complexity Overview | Governance Package v1, File Inventory v1, locked frictions/traps, World Spec v1 | Preserve three frictions, five information-problem domains, source hierarchy, prednisone hierarchy, and physician-perspective rule. |
| 2. Task Specifications | TP-KM01 through TP-KM06 plus locked task architecture | Populate six task descriptions and prompt-level architecture without creating new tasks or TP-KM07. |
| 3. World File Plan | File Inventory v1 | Populate World-Level, Task-Level, and Supplementary file plan sections from the locked 8-column inventory source while preserving the official template layout. |
| 4. World Summary | World Spec v1 and locked architecture decisions | Populate concise summary only; do not add new deliverables or conclusions. |

Population guardrails:

- Do not create final synthetic chart facts beyond locked source content.
- Do not import grading rubrics, scoring thresholds, or point language.
- Do not embed full golden responses or grader-guidance files into the World Spec unless the official template explicitly requires their summarized architecture.
- Do not upload or include locked governance artifacts as appendices unless requested.
- Do not change the resolved 7-column structure decision or reopen it.

## 6. Export Architecture Review

Permitted export targets for future execution: DOCX, PDF, or original binary format when required.

| Source | Target Format | Rationale |
| --- | --- | --- |
| `world-spec-v1.md` | DOCX | Official template and examples are DOCX. |
| FI-W text-based locked Markdown files | DOCX | Template/reference files are document-like and should not remain Markdown for submission. |
| FI-W writer-produced media rows, if any are identified during execution | Original binary format | Official guidance says writer-produced media bypass engineering and use original/final binary artifacts. |
| FI-S text-based locked Markdown files | DOCX | Supplementary reference files are document-like and should not remain Markdown for submission. |
| FI-T locked Markdown files | DOCX only if requested later | Task-level files are later pipeline or optional hold material, not current world-level template/reference upload. |
| `docs/claude-transcript-formatted.md` | DOCX | Current UI requires file upload; transcript is a document artifact. |
| `docs/claude-transcript-formatted.md` | PDF optional | Optional read-only companion. Current evidence does not require both DOCX and PDF. |
| `Korvin_Merrow_Brainstorm.docx` | Original DOCX | Already in Word format and optional as QC supplemental input. |
| TP/EO/Golden/GG locked Markdown files | DOCX or PDF later only if a later phase requests them | Not current pre-AutoQC upload materials. |

## 7. Export Matrix

| Source | DOCX | PDF | REQUIRED | OPTIONAL | NOT_REQUIRED | Status |
| --- | --- | --- | --- | --- | --- | --- |
| World Spec v1 | Yes | No | Yes | No | No | NEEDS_TRANSFORMATION |
| FI-W01 through FI-W22 | Yes, unless original binary needed | Optional only if fixed-layout copy is requested | Yes for current Template/Reference Files upload | No | No | NEEDS_TRANSFORMATION |
| FI-S01 through FI-S04 | Yes | Optional only if fixed-layout copy is requested | Yes for current Template/Reference Files upload | No | No | NEEDS_TRANSFORMATION |
| FI-T01 through FI-T07 | Yes if later requested | Optional if later requested | No for current World Spec upload | Yes as later/task-level hold | No | READY_SOURCE_ONLY |
| Formatted Claude transcript | Yes | Optional | Yes | PDF optional | No | NEEDS_TRANSFORMATION |
| Claude share URL provenance | No | No | No | Yes | No | READY_PROVENANCE_ONLY |
| Approved Brainstorm DOCX | Already DOCX | No | No | Yes as QC supplemental input | No | READY_OPTIONAL |
| Task prompts TP-KM01 through TP-KM06 | Later only | Later only | No | Yes for later task pipeline | No for current upload | HOLD |
| Expected outputs EO-KM01 through EO-KM06 | Later only | Later only | No | Yes for later benchmark pipeline | No for current upload | HOLD |
| Golden responses Golden-KM01 through Golden-KM06 | Later only | Later only | No | Yes for later benchmark pipeline | No for current upload | HOLD |
| Grader guidance GG-KM01 through GG-KM06 | Later only | Later only | No | Yes for later Section 6 pipeline | No for current upload | HOLD |
| Governance/ratification/reconciliation files | No | No | No | No | Yes | DO_NOT_UPLOAD |
| AutoQC/Packaging/Submission/Execution prep files | No | No | No | No | Yes | DO_NOT_UPLOAD |

## 8. Reference File Review

### FI-W01 Through FI-W22

Determination: REQUIRED_UPLOAD for current Template/Reference Files upload, after transformation.

Rationale:

- FI-W files are the world-level file substrate.
- Official guidance requires world-level template/reference files needed by engineering.
- Current Korvin locked files are Markdown working artifacts, not final upload format.
- Execution should export text-based FI-W material to DOCX template/reference artifacts or original binary only if a specific row is determined to require writer-produced media.

### FI-T01 Through FI-T07

Determination: OPTIONAL_UPLOAD / later hold for current pre-AutoQC World Spec execution.

Rationale:

- FI-T files are task-level request-context files.
- Official template includes a task-level file plan subsection, but source guidance for template/reference upload says the world-level generation package is the current handoff and that task-level files are out of scope for that step.
- If RL Studio explicitly asks for task-level context files during current upload, stop and treat FI-T DOCX export as an execution subtask.

### FI-S01 Through FI-S04

Determination: REQUIRED_UPLOAD as supplementary world-level template/reference support, after transformation.

Rationale:

- FI-S files are part of the locked File Inventory v1.
- They are background/supporting sources and must not carry sole critical evidence.
- Their upload role is template/reference support, not answer leakage.

## 9. Transcript Requirements

Authoritative current decision:

- Transcript mechanism: file upload.
- Authoritative upload source: `docs/claude-transcript-formatted.md`.
- Provenance: `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040`.

Export determination:

- DOCX: required target for final transcript upload under the Markdown-is-working-format rule.
- PDF: optional companion only.
- Markdown: preserved as source, not preferred as final upload unless RL Studio explicitly rejects DOCX or explicitly requests Markdown.
- Share URL: preserve inside the transcript document or upload notes if a notes field exists; do not rely on the URL as a substitute for the file upload.

Content rule:

- Do not regenerate transcript content.
- Do not rewrite transcript content.
- Do not restore removed front-matter claims.
- Retain transcript content, phase chronology, decisions, ratifications, evidence trail, and Claude share URL provenance.

## 10. Final Execution Order Before AutoQC

1. Populate the official World Spec DOCX from locked sources.
2. Export FI-W01 through FI-W22 into DOCX template/reference artifacts or original binary where a row requires it.
3. Export FI-S01 through FI-S04 into DOCX supplementary template/reference artifacts.
4. Export the formatted Claude transcript to DOCX and preserve the Claude share URL inside the artifact.
5. Optionally stage the approved Brainstorm DOCX as QC supplemental input.
6. Do not create a manifest yet.
7. Do not create a final submission package yet.
8. Stop for Alexander authorization before RL Studio upload or AutoQC.

## 11. Stop Points

Stop if:

- RL Studio rejects DOCX transcript upload and requests another format.
- RL Studio requires task-level files during the current World Spec upload.
- RL Studio asks for task prompts, expected outputs, goldens, or grader guidance before the current World Spec AutoQC.
- Any FI-W or FI-S row cannot be exported without adding new clinical facts.
- Any file would need a new source not present in locked materials.
- Official template structure appears to conflict with locked File Inventory v1 in a way that cannot be represented without redesign.
- A manifest, package, upload, submission, AutoQC run, or AutoQC response would be needed.

## 12. Final Determination

Final Submission Resolution v1 determines that Korvin's current pre-AutoQC execution requires:

1. A final World Spec DOCX.
2. A world-level and supplementary template/reference export set for FI-W01 through FI-W22 and FI-S01 through FI-S04.
3. A transcript DOCX derived from `docs/claude-transcript-formatted.md`.
4. Optional retention of the approved Brainstorm DOCX as QC supplemental input.

Markdown remains workspace source format. It should not be treated as final submission format unless future RL Studio evidence explicitly requires it.

Final Submission Resolution

Status:
CANDIDATE REVIEW

Next Eligible Phase:
Execution and Artifact Generation
