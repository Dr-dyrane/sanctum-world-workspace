# Claude Transcript Requirements

Source scope: `reference/New Writers Version - Instruction Guide (05_24).md`, local template/link indexes under `reference/templates/`, and existing source-derived World Spec guideline files.

This is the canonical local transcript note. It records only source-of-truth evidence. It separates:

- `VERIFIED`: directly stated by source text.
- `PLAUSIBLE`: supported by nearby workflow evidence but not explicitly stated as a requirement.
- `NOT FOUND`: searched for and not found in local source text.

## Search Method

Expanded source-only search terms included:

- `Claude Transcript`
- `transcript`, `transcripts`
- `Claude conversation`, `Claude chat`, `Project chat`, `fresh chat`, `new chat`
- `export`, `download`
- `Claude upload`, `upload Claude`, `RL Studio Claude`
- `prompt starter`, `COPY-PASTE`, `copy/paste`
- `attach`, `deliverable`, `supplemental documents`
- `AutoQC`, `Claude QC`

## VERIFIED

### A World Spec upload tutorial explicitly mentions a Claude Transcript.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:314` links a video titled "Uploading World Spec/Template Files/Claude Transcript + AutoQC".

Interpretation:

- The source verifies that "Claude Transcript" is part of the named World Spec upload tutorial topic.
- The local text does not define the transcript artifact itself.

### Claude Project is expected in the workflow before World Spec upload.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:241-243` frames how Claude and other LLMs fit into the workflow.
- `reference/New Writers Version - Instruction Guide (05_24).md:250-254` says Claude/LLMs are guides and accelerators, not the primary driver.
- `reference/New Writers Version - Instruction Guide (05_24).md:355-365` says Sanctum is Claude-collaborative and that the physician owns quality.

### The guide expects separate Claude Project chats for major workflow stages.

Evidence:

- Brainstorm: `reference/New Writers Version - Instruction Guide (05_24).md:1379-1381` says to open a new Claude Project chat for the Brainstorm prompt and attach the Brainstorm template.
- World Spec: `reference/New Writers Version - Instruction Guide (05_24).md:1718` recommends a fresh Claude Project chat so the World Spec session is self-contained.
- Template/reference files: `reference/New Writers Version - Instruction Guide (05_24).md:2410-2414` says to open a new Claude Project chat and paste the template/reference prompt starter.
- Claude QC: `reference/New Writers Version - Instruction Guide (05_24).md:2621-2629` says to start a new Claude Project chat and paste the QC prompt.

### World Spec creation has a specific Claude conversation structure.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:1714` says the World Spec prompt assumes Brainstorm signoff and walks through every World Spec Template section.
- `reference/New Writers Version - Instruction Guide (05_24).md:1718` says to have the approved Brainstorm ready, open a fresh chat, paste the block, and Claude will ask for the Brainstorm in Phase 1.
- `reference/New Writers Version - Instruction Guide (05_24).md:1914-1939` says Claude should run a systematic audit before drafting and wait for confirmation before Phase 7.
- `reference/New Writers Version - Instruction Guide (05_24).md:1941-1950` says drafting occurs only after confirmation and uses the World Spec Template structure.

### Template/reference file creation has a specific Claude conversation structure.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:2402` says to use Claude Project to package and produce template files and recommends OPUS for this step.
- `reference/New Writers Version - Instruction Guide (05_24).md:2410-2414` gives the exact first message prompt starter for the template/reference file chat.
- `reference/New Writers Version - Instruction Guide (05_24).md:2420-2424` says to attach the System Prompt for Template/Reference File generation and provides the system prompt text.
- `reference/New Writers Version - Instruction Guide (05_24).md:2427-2434` says to attach the finalized World Spec `.docx` and DataBank `.docx`; Claude gives individual template/reference files for RL Studio/engineering handoff.

### Claude QC has a specific conversation structure.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:2621` says this QA workflow occurs before world-level materials are uploaded to RL Studio.
- `reference/New Writers Version - Instruction Guide (05_24).md:2623-2629` says to start a new Claude Project chat and paste the QC prompt.
- `reference/New Writers Version - Instruction Guide (05_24).md:2644-2651` says to attach the deliverable plus the corresponding AutoQC prompt files and supplemental documents. For World Spec, those supplemental documents are the Brainstorm document and templates/reference files.

## PLAUSIBLE

### The transcript likely refers to the Claude Project conversation(s) used for World Spec and/or template/reference file generation.

Evidence:

- The only explicit phrase is the upload tutorial title: "Uploading World Spec/Template Files/Claude Transcript + AutoQC" at `reference/New Writers Version - Instruction Guide (05_24).md:314`.
- The World Spec Claude chat is expected to be fresh and self-contained at `reference/New Writers Version - Instruction Guide (05_24).md:1718`.
- The template/reference file Claude chat is also a new chat and produces upload-bound template/reference files at `reference/New Writers Version - Instruction Guide (05_24).md:2410-2434`.

Why only plausible:

- The local source text never states which Claude chat transcript is required or whether multiple transcripts are required.

### The safest future workflow is to preserve transcripts for every World Spec-stage Claude chat.

Candidate chats to preserve:

1. World Spec drafting/interview chat.
2. Template/reference file generation chat.
3. Claude QC chat, if used.

Why only plausible:

- The source verifies these chats are expected workflows, but does not explicitly say their transcripts must be uploaded.

### Brainstorm transcript may not be required for World Spec upload.

Evidence:

- The upload video title at `reference/New Writers Version - Instruction Guide (05_24).md:314` names World Spec, Template Files, Claude Transcript, and AutoQC, not Brainstorm transcript.
- The World Spec QC supplemental input list at `reference/New Writers Version - Instruction Guide (05_24).md:2651` includes the Brainstorm document, not a Brainstorm transcript.

Why only plausible:

- The source does not explicitly say "Brainstorm transcripts are not required."

## NOT FOUND

### Exact transcript requirement

Not found.

The local text source does not state:

- whether a Claude transcript upload is mandatory,
- whether it is required for onboarding or veteran writers only,
- whether one transcript or multiple transcripts are required,
- whether the transcript is for World Spec drafting, template/reference generation, Claude QC, or all of those chats.

### Transcript format

Not found.

No local source text states whether the transcript must be:

- `.docx`,
- `.pdf`,
- `.txt`,
- pasted text,
- Google Doc link,
- screenshot,
- Claude share link,
- exported conversation file,
- or another format.

### Transcript export method

Not found.

No local source text explains how to export, download, copy, or save a Claude transcript.

### Transcript examples

Not found.

No local source text provides an example Claude transcript or screenshot of a transcript export.

### RL Studio transcript field name

Not found.

No local source text gives the exact RL Studio field name for a Claude transcript upload.

### Brainstorm Claude transcript upload requirement

Not found.

No local source text states that a Brainstorm Claude transcript must be uploaded with the World Spec submission.

## Operational Rule For Korvin Merrow

Before World Spec upload:

1. Preserve the full Claude World Spec drafting/interview chat if export/copy is available.
2. Preserve the full Claude template/reference generation chat if used.
3. Preserve the Claude QC chat if used.
4. Do not assume upload format until the RL Studio field, upload tutorial, pod lead, or reviewer confirms it.
5. If RL Studio asks for a transcript and the format is unclear, stop and ask before submitting.

