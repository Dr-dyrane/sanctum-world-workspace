# Claude Workflow Audit

Source scope: `reference/New Writers Version - Instruction Guide (05_24).md`, local template/link indexes under `reference/templates/`, and source-derived World Spec guideline files. This audit does not use clinical authored content as source-of-truth evidence for expected workflow.

## Executive Finding

The guide describes Project Sanctum as Claude-collaborative, with the physician retaining ownership and judgment. It provides explicit Claude setup instructions, a Brainstorm prompt starter, a World Spec prompt starter, a template/reference file prompt starter, and a Claude QC prompt. It mentions "Claude Transcript" only in a video title; no local text source defines transcript export format or exact transcript upload requirements.

## VERIFIED

### Claude is expected as a guide and accelerator, not the clinical authority.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:241-243` introduces how Claude and other LLMs fit into the workflow.
- `reference/New Writers Version - Instruction Guide (05_24).md:250-254` says AI is a tool, not the driver, and the physician is the ultimate expert.
- `reference/New Writers Version - Instruction Guide (05_24).md:355-365` says Sanctum is Claude-collaborative, but the writer owns quality and professional judgment overrides AI.

### The guide expects a Claude Project with persistent project instructions.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:1213-1219` introduces Claude Project setup for brainstorming and World Spec drafts.
- `reference/New Writers Version - Instruction Guide (05_24).md:1228-1234` says the project instructions anchor Claude behavior across every conversation and should be pasted once into the Claude Project Instructions.
- `reference/New Writers Version - Instruction Guide (05_24).md:1239-1265` begins the copy-paste project instruction block and defines collaboration style, World, world types, world snapshot, and task independence.

### Brainstorm creation has an official Claude prompt starter.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:1377` says the Brainstorm starter prompt is for the first Claude Project chat when ready to brainstorm and that Claude will conduct a structured interview, run an audit, and then draft the brainstorm DOCX.
- `reference/New Writers Version - Instruction Guide (05_24).md:1379-1381` says to open a new Claude Project chat, paste the copy-paste block, attach the Brainstorm template as a PDF, and push back if Claude skips phases.
- `reference/New Writers Version - Instruction Guide (05_24).md:1386-1509` provides the Brainstorm prompt block and phase sequence.

Expected Brainstorm Claude interaction:

1. Save Project Instructions.
2. Open a new chat in Claude Project.
3. Paste the Brainstorm Interview prompt.
4. Attach the Brainstorm template as a PDF.
5. Claude interviews through:
   - Phase 1: Get to know the physician.
   - Phase 2: World setup.
   - Phase 3: Major friction points.
   - Phase 4: Major traps.
   - Phase 5: Rough task ideas.
   - Phase 6: Systematic audit.
   - Final drafting only after audit passes.

### World Spec creation has an official Claude prompt starter.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:1714` says the World Spec starter prompt assumes Brainstorm signoff and walks through every World Spec Template section before drafting.
- `reference/New Writers Version - Instruction Guide (05_24).md:1718` says to have the approved Brainstorm ready, open a fresh Claude Project chat, paste the copy-paste block, and Claude will ask for the Brainstorm in Phase 1.
- `reference/New Writers Version - Instruction Guide (05_24).md:1905-1912` says Claude should ask for the World Summary.
- `reference/New Writers Version - Instruction Guide (05_24).md:1914-1939` says Claude must run a systematic audit before drafting and wait for confirmation before Phase 7.
- `reference/New Writers Version - Instruction Guide (05_24).md:1941-1950` says Claude drafts the spec in DOCX format using the World Spec Template structure after confirmation.

Expected World Spec Claude interaction:

1. Use a fresh Claude Project chat.
2. Paste the official World Spec starter prompt.
3. Provide the approved Brainstorm as DOCX or pasted text.
4. Claude walks section-by-section:
   - Phase 1: Load approved Brainstorm.
   - Clinical Scenario.
   - Task Specifications.
   - World File Plan.
   - World Summary.
   - Systematic audit before drafting.
   - Draft World Spec only after writer confirmation.

### Template/reference file creation has an official Claude workflow and prompt.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:2402` says to use Claude Project to package and produce template files and notes OPUS is recommended for this step.
- `reference/New Writers Version - Instruction Guide (05_24).md:2410-2417` says to open a new Claude Project chat, paste the exact prompt starter, and not modify wording.
- `reference/New Writers Version - Instruction Guide (05_24).md:2420-2424` says to attach the System Prompt for Template/Reference File generation and provides the system prompt text.
- `reference/New Writers Version - Instruction Guide (05_24).md:2427-2434` says to attach the finalized World Spec `.docx` and DataBank `.docx`; Claude returns individual template/reference files.

Expected template/reference Claude interaction:

1. Use Claude Project, preferably OPUS per guide.
2. Open a new chat for template/reference packaging.
3. Paste the exact prompt starter.
4. Attach:
   - finalized World Spec `.docx`,
   - DataBank of Templates `.docx`,
   - System Prompt for Template/Reference File generation `.docx`.
5. Claude works in installments of 3-5 rows.
6. Claude flags ambiguity, missing DataBank templates, public domain rows, writer-produced media, and task-level rows.
7. Claude returns individual `.docx` template/reference files where appropriate.

### AutoQC review can be run through Claude as an informal self-check.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:361` says platform AutoQC is required and formalized.
- `reference/New Writers Version - Instruction Guide (05_24).md:363` says self-check with Claude is encouraged but not required before upload.
- `reference/New Writers Version - Instruction Guide (05_24).md:2621-2629` gives a Claude QC workflow and prompt: ask Claude to use the QC checklist to review the World Spec document, walk through every check, and flag Blockers, Majors, then Minors.
- `reference/New Writers Version - Instruction Guide (05_24).md:2644-2651` says to attach the deliverable and corresponding AutoQC files; for World Spec, the supplemental documents are the World Spec AutoQC file, the Brainstorm document, and templates/reference files.

Expected AutoQC Claude interaction:

1. Start a new Claude Project chat.
2. Paste the QC prompt.
3. Attach the deliverable and corresponding AutoQC prompt/checklist files.
4. For World Spec QC, include the Brainstorm document and templates/reference files.
5. Use Claude QC as preflight; RL Studio AutoQC remains required.

### Example Claude prompts are provided.

Evidence:

- Brainstorm prompt block: `reference/New Writers Version - Instruction Guide (05_24).md:1386-1509`.
- World Spec prompt block: `reference/New Writers Version - Instruction Guide (05_24).md:1714-1950`.
- Template/reference prompt starter and system prompt: `reference/New Writers Version - Instruction Guide (05_24).md:2410-2424`.
- Claude QC prompt: `reference/New Writers Version - Instruction Guide (05_24).md:2627-2629`.

### AI tools other than Claude are discussed.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:241-243` frames Claude and other LLMs.
- `reference/New Writers Version - Instruction Guide (05_24).md:2424` mentions Nano Banana Pro, ElevenLabs, GarageBand, Photoshop, clinical data generators, and similar tools for writer-produced media.
- `reference/New Writers Version - Instruction Guide (05_24).md:2504` says Nano Banana Pro or ChatGPT may be used to generate photos.

## PLAUSIBLE

### The preferred Claude conversation structure is separate chats by workflow stage.

Evidence:

- Brainstorm instructions say "Open a new chat in your Claude Project" for Brainstorm at `reference/New Writers Version - Instruction Guide (05_24).md:1379-1381`.
- World Spec instructions say a fresh chat is recommended so the World Spec session is self-contained at `reference/New Writers Version - Instruction Guide (05_24).md:1718`.
- Template/reference instructions say to open a new Claude Project chat at `reference/New Writers Version - Instruction Guide (05_24).md:2410-2414`.
- QC instructions say to start a new chat at `reference/New Writers Version - Instruction Guide (05_24).md:2621-2629`.

Impact:

- It is likely best practice to preserve separate chats for Brainstorm, World Spec drafting, template/reference curation, and QC.

Action:

- Before World Spec drafting, start a fresh Claude Project chat and preserve the resulting output/transcript if later upload fields require it.

### The World Spec upload may require a Claude transcript, but details are unavailable in local text source.

Evidence:

- `reference/New Writers Version - Instruction Guide (05_24).md:314` links a video titled "Uploading World Spec/Template Files/Claude Transcript + AutoQC".

Impact:

- RL Studio may have a transcript field or reviewer may expect a transcript, but local text does not define scope or format.

Action:

- Confirm in RL Studio or from the upload video/pod guidance before final World Spec upload.

## NOT FOUND

### Example Claude responses are provided in local text source.

Not found.

The guide provides prompt starters and process instructions, but no complete example Claude response was found in the local text source.

### Transcript examples are provided in local text source.

Not found.

The term "Claude Transcript" appears in a video title at `reference/New Writers Version - Instruction Guide (05_24).md:314`, but no transcript example appears in the local text source.

### Transcript exports are shown in local text source.

Not found.

No local text source shows how to export a Claude transcript, what file type to use, or where exactly to upload it.

### Brainstorm Claude transcript upload requirement.

Not found.

No local text source says Brainstorm Claude transcripts must be uploaded with the World Spec submission or any other submission.

### Claude.ai URL or direct Claude.ai workflow.

Not found.

The source refers to Claude Project and video/resources, but no local text source instruction was found requiring a specific `claude.ai` URL workflow.

