# AutoQC Construction v1

World: Korvin Merrow

Status: CANDIDATE REVIEW

Purpose: organize future AutoQC execution, dependency checking, response routing, reconciliation routing, and packaging routing after AutoQC Architecture v1 lock.

This is a preparation package only. It does not run AutoQC, create platform responses, draft AutoQC responses, fabricate missing official prompts, create scoring rubrics, create scoring thresholds, create pass/fail bands, create point allocations, create DOCX artifacts, create submission artifacts, or modify locked artifacts.

## Source Basis

This construction package is based on:

- `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-v1.md`
- `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-validation-review.md`
- `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`
- `worlds/korvin-merrow/reviews/ecosystem-comparison-audit.md`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/world-spec-guidelines/10_submission_package_requirements.md`
- `reference/source/New Writers Version - Instruction Guide (05_24).md`
- locked World Spec, Governance Package, File Inventory, FI-W, FI-T, FI-S, Task Prompt, Expected Output, Golden, and Grader Guidance layers.

## Core Rules

### No-Fabrication Rule

Missing official prompts must remain missing until imported or produced by the platform. In particular, the official Section 6 Grader Guidelines AutoQC prompt is not locally available and must not be recreated from memory, inferred from examples, or reverse-engineered from locked GG-KM files.

### Locked-Artifact Protection

AutoQC Construction may identify future inputs, dependencies, and routing paths. It must not edit locked artifacts. If a future AutoQC result appears to require locked-artifact modification, route it to reconciliation first.

### Import-Not-Inference Rule

Future AutoQC execution must use imported official prompts, local locked sources, or platform diagnostics. It must not infer missing checklist text or platform expectations from architecture summaries.

## Future AutoQC Execution Order

Execution order must remain dependency-aware:

1. AQC-KM01-WS: World Spec AutoQC v6.3 preflight and future formal run.
2. AQC-KM02-FILE: File-layer QC.
3. AQC-KM03-TP: Task-prompt QC.
4. AQC-KM04-EO: Expected-output QC.
5. AQC-KM05-GOLDEN: Golden-response QC.
6. AQC-KM06-GG: Grader-guidance QC / future Section 6 Grader Guidelines AutoQC.
7. AQC-KM07-PKG: Packaging and submission-readiness QC.

This order does not authorize running any AutoQC. It defines the future dependency sequence only.

## AQC Surface Map

| AQC ID | Surface | Required Inputs | Official Prompt Dependency | Current Blocked Dependencies | Future Output Type |
| --- | --- | --- | --- | --- | --- |
| AQC-KM01-WS | World Spec AutoQC v6.3 | Locked World Spec v1, File Inventory v1, task specs, source hierarchy, milestone architecture, local v6.3 index/prompt | Local World Spec AutoQC v6.3 exists | Formal run not authorized; DOCX population/submission state pending | Future diagnostic set or preflight finding list |
| AQC-KM02-FILE | File-layer QC | File Inventory v1, FI-W01 through FI-W22, FI-T01 through FI-T07, FI-S01 through FI-S04, reconciliation records | No separate official file-layer prompt locally available | No official prompt imported; locked files cannot be revised without authorization | Future file-layer finding list or reconciliation queue |
| AQC-KM03-TP | Task-prompt QC | Task Prompt Architecture v1, TP-KM01 through TP-KM06, FI-T07 addendum rule, physician-perspective rule | No separate official task-prompt prompt locally available | No official prompt imported; locked prompts cannot be revised without authorization | Future prompt-layer finding list or reconciliation queue |
| AQC-KM04-EO | Expected-output QC | Expected Output Architecture v1, EO-KM01 through EO-KM06, TP/EO mapping, file dependencies | No separate official expected-output prompt locally available | No official prompt imported; locked EOs cannot be revised without authorization | Future EO-layer finding list or reconciliation queue |
| AQC-KM05-GOLDEN | Golden-response QC | Golden Architecture v1, Golden-KM01 through Golden-KM06, EO dependencies, special golden watch items | No separate official golden prompt locally available | No official prompt imported; locked goldens cannot be revised without authorization | Future golden-layer finding list or reconciliation queue |
| AQC-KM06-GG | Grader-guidance QC / Section 6 | Grader Guidance Architecture v1, GG-KM01 through GG-KM06, anti-verbatim principle, no-scoring-leakage boundary | Official Section 6 prompt referenced but not locally available | Section 6 prompt missing; platform diagnostics absent; locked GG files cannot be revised without authorization | Future Section 6 diagnostics or reconciliation queue |
| AQC-KM07-PKG | Packaging and submission-readiness QC | Submission requirements, ecosystem audit watch items, transcript file note, final packaging scope, upload sequence | No complete packaging prompt locally available beyond source guide and v6.3 packaging checks | DOCX population pending; manifest pending; transcript requirement ambiguous; goldens/GG submission scope ambiguous | Future packaging checklist, manifest plan, or submission-prep queue |

No AQC-KM08 is authorized.

## Future Response Routing Paths

Future AutoQC findings must be classified before any response is drafted:

- Valid finding against unlocked preparation artifact: route to authorized correction if that phase is open.
- Valid finding against locked artifact: route to reconciliation review before any edit.
- False positive against locked canon: route to evidence-backed response only after official diagnostic text exists.
- Ambiguous finding due to missing prompt or missing platform context: route to dependency block, not response drafting.
- Packaging-only finding: route to packaging preparation, not clinical artifact revision.

This package does not draft any response language.

## Reconciliation Routing Paths

Use reconciliation when a future finding would:

- modify locked World Spec, FI-W, FI-T, FI-S, TP, EO, Golden, or GG files;
- broaden or narrow workflows, traps, frictions, hierarchy rules, source dependencies, or task responsibilities;
- reinterpret File Inventory rows;
- change FI-T07 addendum-only relationship;
- change FI-W22 visible-but-incomplete handling;
- change FI-S background/supporting role;
- change physician-perspective rule;
- change source-of-truth or prednisone hierarchy.

Reconciliation outputs must identify the authoritative source, rationale, and smallest canon-supported correction. This package does not create a reconciliation result.

## Packaging Routing Paths

Packaging issues must route to a future Submission / Packaging Preparation phase when they concern:

- final World Spec DOCX population;
- single-DOCX requirement;
- page numbering, landscape table handling, template placeholder removal, and file naming convention;
- submission manifest and upload order;
- per-file upload rather than zip;
- reference/template file curation;
- `docs/claude-transcript.md` handling, transcript scope, transcript format, and whether transcript submission is required;
- whether goldens and grader guidance are submitted with World Spec or later.

Packaging routing must not create DOCX artifacts, manifests, upload packages, submission files, or RL Studio actions in this phase.

## Blocked Dependencies

The following dependencies remain blocked:

1. Formal AutoQC run authorization.
2. Platform diagnostic output.
3. Official Section 6 Grader Guidelines AutoQC prompt.
4. Any separate official File, Task Prompt, Expected Output, Golden, or Packaging AutoQC prompts if they exist outside the local repository.
5. DOCX population authorization.
6. Submission manifest authorization.
7. Transcript-format clarification.
8. Goldens/grader guidance submission-scope clarification.
9. Any authorization to reopen or modify locked artifacts.

## Carry-Forward Watch Items

- World Spec AutoQC v6.3 exists locally and is the only local official AutoQC prompt.
- Official Section 6 Grader Guidelines AutoQC prompt is not yet locally available.
- Packaging-layer checks remain pending.
- Submission manifest remains pending.
- DOCX population remains pending.
- Transcript requirement remains ambiguous.
- `docs/claude-transcript.md` exists as a submission-phase carry-forward item and must not be formatted, converted, or submitted until authorized.
- Goldens/grader guidance submission scope remains ambiguous.
- Multi-layer AutoQC specification beyond v6.3 remains undefined unless official prompts are imported.

## Construction Boundary Confirmation

AutoQC Construction v1 created:

- an execution-order map;
- AQC-KM01 through AQC-KM07 dependency routing;
- response-routing paths;
- reconciliation-routing paths;
- packaging-routing paths;
- blocked-dependency tracking;
- carry-forward watch items.

AutoQC Construction v1 did not create:

- AutoQC runs;
- platform responses;
- AutoQC response text;
- scoring rubrics;
- scoring thresholds;
- pass/fail bands;
- point allocations;
- DOCX artifacts;
- submission artifacts;
- fabricated Section 6 prompt content.

## Final Status

AutoQC Construction

Status:
CANDIDATE REVIEW

Next Eligible Phase:

AutoQC Construction Review
