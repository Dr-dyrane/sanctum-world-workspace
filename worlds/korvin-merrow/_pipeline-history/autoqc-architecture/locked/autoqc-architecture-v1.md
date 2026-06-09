# AutoQC Architecture v1

World: Korvin Merrow

Status: CANDIDATE REVIEW

Purpose: define how future AutoQC preparation, formal AutoQC runs, and AutoQC response handling should be organized after Grader Guidance Construction lock.

This is architecture only. It does not run AutoQC, create AutoQC responses, create scoring rubrics, create scoring thresholds, create pass/fail bands, create point allocations, create DOCX artifacts, create RL Studio materials, create submission artifacts, or fabricate missing official AutoQC prompts.

## Source Basis

This architecture was checked against:

- Locked World Spec v1 and World Spec Skeleton v1.
- Locked Governance Package v1.
- Locked File Inventory Architecture v1 and File Inventory v1.
- Locked FI-W01 through FI-W22.
- Locked FI-T01 through FI-T07.
- Locked FI-S01 through FI-S04.
- Locked Task Prompt Architecture v1 and TP-KM01 through TP-KM06.
- Locked Expected Output Architecture v1 and EO-KM01 through EO-KM06.
- Locked Golden Architecture v1 and Golden-KM01 through Golden-KM06.
- Locked Grader Guidance Architecture v1 and GG-KM01 through GG-KM06.
- Ratifications and validation reviews for the locked layers above.
- FI-W20, FI-T, and FI-S03 reconciliation records.
- `worlds/korvin-merrow/reviews/ecosystem-comparison-audit.md`.
- `reference/world-spec-guidelines/08_autoqc_master_index.md`.
- `reference/world-spec-guidelines/10_submission_package_requirements.md`.
- `reference/source/New Writers Version - Instruction Guide (05_24).md`.

## AutoQC Scope

AutoQC Architecture v1 governs organization only.

It may define:

- which future QC surfaces need preflight review;
- which official prompt or locked architecture source governs each future QC surface;
- how findings should be routed to response, reconciliation, revision, or packaging-prep work;
- what evidence must be checked before any future AutoQC response is drafted;
- what unresolved watch items must be carried forward.

It must not:

- run any platform or Claude AutoQC;
- draft an AutoQC response;
- invent a missing AutoQC checklist;
- create grader guidance, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX files, manifests, or submission materials;
- change locked clinical, file, prompt, expected-output, golden, or grader-guidance artifacts.

## AutoQC Artifact IDs

Future AutoQC work should use these architecture IDs. These IDs are organizational labels only, not completed AutoQC responses.

| AutoQC architecture ID | Future QC surface | Governing status | Primary source basis | Boundary |
| --- | --- | --- | --- | --- |
| AQC-KM01-WS | World Spec AutoQC v6.3 preflight and formal run | Official local prompt exists | `reference/world-spec-guidelines/08_autoqc_master_index.md`; `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx` | Do not populate DOCX or run AutoQC in this architecture phase. |
| AQC-KM02-FILE | File-layer QC | Architecture only; official downstream prompt not locally materialized | File Inventory v1; FI-W/FI-T/FI-S locked files; ecosystem audit | Do not create new files or revise locked files. |
| AQC-KM03-TP | Task-prompt QC | Architecture only; official downstream prompt not locally materialized | Task Prompt Architecture v1; TP-KM01 through TP-KM06 | Do not revise locked prompts. |
| AQC-KM04-EO | Expected-output QC | Architecture only; no official prompt locally materialized | Expected Output Architecture v1; EO-KM01 through EO-KM06 | Do not revise locked expected outputs or create scoring language. |
| AQC-KM05-GOLDEN | Golden-response QC | Architecture only; no official prompt locally materialized | Golden Architecture v1; Golden-KM01 through Golden-KM06 | Do not revise locked goldens or create grader guidance. |
| AQC-KM06-GG | Grader-guidance QC / future Section 6 Grader Guidelines AutoQC | Official Section 6 prompt is referenced but not locally available | Grader Guidance Architecture v1; GG-KM01 through GG-KM06; source guide Section 6 prompt reference | Do not fabricate Section 6 AutoQC content. |
| AQC-KM07-PKG | Packaging and submission-readiness QC | Architecture only; manifest pending | Ecosystem audit; submission package requirements; World Spec AutoQC v6.3 checks 2.67, 2.70, 2.71, 2.88, 2.103, 2.104 | Do not create DOCX, manifest, upload package, or submission artifact. |

No AQC-KM08 is authorized by this architecture.

## Relationship To World Spec AutoQC v6.3

World Spec AutoQC v6.3 is the only official AutoQC prompt currently available locally.

AutoQC Architecture v1 treats v6.3 as:

- the governing future formal QC source for World Spec / Section 2-style checks;
- a local preflight map before any official platform run;
- a source for packaging-related constraints that already appear inside v6.3, including single DOCX, required section headings, formatting, placeholder removal, task specifications, file-plan completeness, traceability, task independence, date consistency, workflow naming, and filename conventions.

AutoQC Architecture v1 does not treat v6.3 as:

- a substitute for missing Section 3, Section 4, Section 5, or Section 6 official prompt text;
- a completed AutoQC run;
- permission to draft AutoQC responses;
- permission to create a final DOCX artifact.

## Relationship To Future Section 6 Grader Guidelines AutoQC

The official guide references an AutoQC Prompt: Section 6 Grader Guidelines document, but that prompt is not locally available in this repository.

Therefore:

- AQC-KM06-GG may reserve a future grader-guidance QC surface.
- The locked GG-KM01 through GG-KM06 files may serve as the artifact set to be checked when a proper Section 6 prompt is obtained or platform AutoQC is run.
- The locked Grader Guidance Architecture v1 and Grader Guidance Construction validation review may supply local boundary context.
- The missing Section 6 prompt content must not be recreated from memory, inferred from examples, or reverse-engineered from locked grader guidance.
- Future Section 6 AutoQC findings must be answered only after the actual official prompt or platform diagnostics are available.

## Task-Layer QC Boundaries

Task-layer QC includes:

- task count and ID consistency;
- TP-KM01 through TP-KM06 mapping to the six locked workflows;
- FI-T07 preserved as medication-safety addendum support for TP-KM01 / EO-KM01 / Golden-KM01 / GG-KM01 only;
- task independence;
- task anchor dates after the world snapshot;
- physician-perspective rule;
- prompt realism and non-exam-question voice;
- no trap telegraphing.

Task-layer QC must not:

- revise locked TP-KM files;
- create new TP-KM07 or AQC-derived task responsibilities;
- change workflow names;
- create expected outputs, goldens, grader guidance, scoring rubrics, AutoQC responses, or submission artifacts.

## File-Layer QC Boundaries

File-layer QC includes:

- FI-W01 through FI-W22 locked world-level file completeness;
- FI-T01 through FI-T07 locked task-context file completeness;
- FI-S01 through FI-S04 locked supplementary file completeness;
- file ID and filename consistency;
- source/tool/origin/description/trap-friction fields from File Inventory v1;
- FI-W22 visible-but-incomplete preservation;
- FI-S background/supporting role preservation;
- no single file becoming an answer file;
- world snapshot boundary preservation.

File-layer QC must not:

- edit locked FI-W/FI-T/FI-S files;
- reinterpret inventory rows;
- create new source files;
- convert supplementary files into critical answer files;
- create AutoQC responses or packaging artifacts.

## Prompt QC Boundaries

Prompt QC includes:

- TP-KM01 through TP-KM06 match locked Task Prompt Architecture v1;
- each prompt maps one-to-one to EO, Golden, and GG artifacts;
- task prompt voice remains physician-centered and clinically realistic;
- prompts do not expose trap labels, hidden grader logic, or answer cues;
- prompts preserve task independence and appropriate task anchor framing.

Prompt QC must not:

- rewrite locked prompts;
- add a seventh prompt;
- add prompt text to AutoQC architecture;
- create rubrics, scoring criteria, or responses.

## Expected-Output QC Boundaries

Expected-output QC includes:

- EO-KM01 through EO-KM06 count and mapping;
- deliverable type per task;
- source-synthesis requirements;
- hierarchy and prednisone-rule fidelity;
- friction preservation;
- uncertainty handling;
- prohibited invention checks.

Expected-output QC must not:

- create final expected-output revisions;
- convert EO files into goldens;
- create grading logic or scoring criteria;
- create AutoQC response text.

## Golden QC Boundaries

Golden QC includes:

- Golden-KM01 through Golden-KM06 count and mapping;
- strong physician answer principle;
- multiple defensible reasoning paths;
- uncertainty preservation;
- evidence reconciliation;
- source hierarchy application;
- special watch items for medication algorithm drift, discharge-authorization drift, invented follow-up facts, RCA drift, and invented outcomes.

Golden QC must not:

- revise locked goldens;
- create Golden-KM07;
- turn goldens into rigid answer keys;
- create grader guidance or scoring rubrics;
- create AutoQC responses.

## Grader-Guidance QC Boundaries

Grader-guidance QC includes:

- GG-KM01 through GG-KM06 count and mapping;
- anti-verbatim-matching principle;
- multi-path defensibility;
- hierarchy fidelity;
- friction fidelity;
- source fidelity;
- FI-W22 visible-but-incomplete rule;
- FI-S background/supporting role;
- no scoring leakage.

Grader-guidance QC must not:

- revise locked GG files;
- create GG-KM07;
- create scoring rubrics, scoring thresholds, pass/fail bands, or point allocations;
- fabricate Section 6 AutoQC prompt content;
- create AutoQC responses.

## Packaging QC Boundaries

Packaging QC includes future checks for:

- final single World Spec DOCX requirement;
- required section headings;
- no template placeholders;
- correct filename convention;
- final document formatting;
- reference/template file handling;
- per-file individual upload rather than zipped package;
- submission manifest and upload order;
- transcript requirement clarification;
- whether goldens and grader guidance submit with the World Spec or in a later pipeline stage.

Packaging QC must not:

- create a DOCX artifact;
- populate the World Spec template;
- create a submission manifest;
- create upload materials;
- access RL Studio;
- run AutoQC.

## Carry-Forward Watch Items

The following watch items are mandatory carry-forward items:

1. Official Section 6 Grader Guidelines AutoQC prompt is not yet locally available.
2. World Spec AutoQC v6.3 exists locally and is the only local official AutoQC prompt.
3. Packaging-layer checks remain pending.
4. Submission manifest remains pending.
5. DOCX population remains pending.
6. Transcript requirement remains ambiguous.
7. Goldens/grader guidance submission scope remains ambiguous.
8. Ecosystem audit identifies multi-layer AutoQC specification as undefined beyond the local World Spec v6.3 source.
9. No future AutoQC response may be drafted until the relevant official prompt output or platform diagnostic exists.
10. Any future correction that would alter locked artifacts requires explicit authorization and a reconciliation record before modification.

## Cross-Artifact Consistency Conclusions

AutoQC Architecture v1 preserves:

- six TP -> EO -> Golden -> GG chains;
- FI-T07 addendum-only relationship;
- FI-W22 visible-but-incomplete rule;
- FI-S background/supporting role;
- source-of-truth hierarchy and prednisone hierarchy;
- physician-perspective rule;
- no-GG-KM07 / no-Golden-KM07 / no-EO-KM07 boundaries;
- no scoring leakage;
- no AutoQC response creation;
- no DOCX or submission artifact creation.

## Final Status

AutoQC Architecture v1

Status:
CANDIDATE REVIEW

Next Eligible Phase:

AutoQC Architecture Review
