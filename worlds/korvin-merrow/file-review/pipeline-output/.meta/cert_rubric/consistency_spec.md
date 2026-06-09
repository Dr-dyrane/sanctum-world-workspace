# Consistency and Provenance Specification

## Overview

This specification defines the consistency checks, provenance tracking, and canonical artifact requirements for every pipeline run. Builders may run internal pre-submit self-checks against their prompt/checklist before handoff, but all consistency checks at gates are performed by the **Gate Evaluator subagent** via the dedicated `run_gate_review.py` harness rather than self-approved by the main agent.

## Canonical Artifacts

The pipeline must maintain these objects for every run:

- Canonical backbone (3 layers)
- Document exposure map
- Metric authority table
- Planned inconsistency register
- Cross-kernel integration board
- Cross-kernel leakage matrix
- Open issues register
- Document manifest
- Provenance ledger
- Change log
- Release manifest

The **document manifest must always include**:

- In-world SOW
- Consolidated email archive containing the project kickoff thread
- Project kickoff deck

## Backbone Rules

- **Layer 1** (canonical truth) is immutable without explicit override. Any override must be logged as a backbone patch with justification.
- **Layer 2** (system distortions) must explain every planned inconsistency. Each distortion traces to a Layer 1 truth value and documents how and why the system distorts it.
- **Layer 3** (exposure) must explain how each document surfaces, buries, or omits the truth. Every document in the manifest has an exposure entry.

## Required Consistency Checks

These checks are performed by the Gate Evaluator subagent at each relevant gate:

1. **Metric consistency (evidence-bounded)**: Same metrics must have same values across all truth documents, unless the discrepancy is registered in the planned inconsistency register. **The evaluator must independently extract key numeric parameters from every document that references them and perform pairwise comparison.** A claim of "no unregistered mismatches" is only valid if the evaluator documents: (a) which parameters were compared, (b) which documents were checked for each parameter, and (c) the specific values found. Register-only verification (checking that registered items appear) is insufficient -- the evaluator must also search for conflicts NOT in the register.
2. **Chronology consistency**: All dates across documents respect the world timeline. No anachronisms.
3. **Stakeholder and entity naming consistency**: Names, titles, and entity references are consistent across all documents.
4. **Answer-contract traceability**: Every answer contract is supported by evidence present in the generated documents.
5. **Discrepancy completeness (bidirectional)**: Every planned inconsistency in the register appears in the generated content (register-to-content direction), AND no unplanned inconsistencies exist in the content (content-to-register direction). **The content-to-register direction requires the evaluator to independently discover potential conflicts, not merely verify that registered ones are present.** The evaluator must document the parameter-extraction methodology used for the content-to-register sweep.
6. **Cross-kernel leakage review**: No single document or pair of documents trivializes a task from any kernel.
7. **No accidental shortcut**: Context and distractor files do not inadvertently contain answers.
8. **Entity coverage completeness**: For every screening step in the backbone, verify that the supporting data file covers 100% of the entity set being screened. Report the entity count in the backbone vs. the entity count in the data file.
9. **Reference chain completeness**: For every screening parameter that defers to another document or standard, verify that the target document contains the specific threshold value. Document each reference chain traced and its terminal value.
10. **Ambiguity register confidence audit**: For every entry in the ambiguity register, verify that (a) a confidence level is recorded, (b) any outcome-affecting entry with confidence below "High" is flagged as blocking, (c) any `deferred` entry includes an `immateriality_rationale` showing that competing interpretations collapse to the same downstream answer and do not change authority choice, (d) no more than **2** total entries remain `deferred`, (e) **0** outcome-affecting entries remain `deferred`, and (f) entries citing solver convergence as evidence specify that solvers were uncontaminated by pre-guidance documents.

## Evidence-Bounded Consistency Checking Protocol

The following protocol replaces register-bounded checking at G3 and G4. The Gate Evaluator must follow these steps in order:

### Step 1: Parameter Extraction
For every workflow task brief, identify every numeric parameter referenced (dollar amounts, percentages, counts, thresholds, dates, rates). For each parameter, identify every document that could contain or reference that value.

### Step 2: Cross-Document Comparison
For each parameter, extract the actual value from every document identified in Step 1. Record the values in a comparison table:

| Parameter | Document | Location (section/cell) | Value |
|-----------|----------|------------------------|-------|
| Holding cost per SF | CFO valuation memo | Section IV, para 3 | $0.75/SF/mo |
| Holding cost per SF | Construction estimates | Tab "Assumptions", cell D12 | $1.25/SF/mo |

### Step 3: Conflict Classification
For each parameter with differing values across documents:
- Check whether the difference is registered in the planned inconsistency register
- If registered: verify the register entry includes a resolution path (which document governs)
- If NOT registered: this is an AB-3 (Unregistered Cross-Document Numeric Conflict) and is unconditionally blocking

### Step 4: Documentation
Include the comparison table in the gate report. The evaluator must be able to show their work -- not just assert "no unregistered mismatches" but demonstrate the comparisons that support that assertion.

## Silent Mutation is Prohibited

Every change after intake normalization must be logged as one of:

- `derived_content_correction` — fixing a value derived from backbone
- `rendering_correction` — fixing a formatting or rendering issue
- `trigger_preservation_correction` — adjusting content to preserve trigger mechanisms
- `backbone_patch` — modifying canonical truth (requires explicit justification)
- `human_override` — expert-directed change

Each log entry must include:

- Timestamp
- Phase in which the change occurred
- Artifact changed (file path or artifact ID)
- Reason for the change
- Validator or check that triggered the change

## Provenance Ledger Minimum Fields

Every document in the provenance ledger must have:

- `doc_id` — unique identifier
- `file_path` — path relative to world output directory
- `format` — file type (docx, pptx, xlsx, html, pdf)
- `role` — document role (truth, distractor, context, bootstrap)
- `visual_class` — declared visual class (see `validators/visual_signoff_spec.md`)
- `source_workflows` — which workflows this document serves
- `backbone_sources` — which backbone entries this document draws from
- `discrepancy_participation` — which planned inconsistencies this document participates in (if any)
- `authoring_agent` — which agent or generator produced this document
- `validating_agents` — which validators reviewed this document
- `generation_timestamp` — when the document was generated

Schema definitions for these fields are maintained in `contracts/` alongside `intermediate_artifact_contracts.md`.

## Release Rule

No world may release unless every rendered document is traceable back to:

1. Expert packet (input)
2. Backbone objects (Layer 1, 2, 3)
3. Generation agent output (which generator, which prompt)
4. Validation history (which gates passed, which checks ran)

The Gate Evaluator subagent verifies traceability at G3 (assembly) and G4 (release). Any document without complete provenance blocks release.
