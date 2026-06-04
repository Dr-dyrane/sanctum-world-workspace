# Transcript Resolution v1

World: Korvin Merrow

Status: CANDIDATE REVIEW

Date: 2026-06-03

## Purpose

Resolve the Claude transcript requirement, format, and scope using authorized evidence before any upload, submission, DOCX population, manifest creation, or AutoQC execution.

This artifact does not format, clean, rewrite, convert, package, upload, or submit transcript material.

## Evidence Reviewed

- Current Studio screenshot provided by Alexander: `C:\Users\Dyrane\Pictures\Screenshots\Screenshot 2026-06-03 181618.png`
- Alexander's current-platform observation: current Studio has no transcript text field and instead has upload-only transcript handling
- `reference/source/How to Upload Your Clod Transcript.mp4`
- `docs/claude-transcript.md`
- `reference/world-spec-guidelines/10_submission_package_requirements.md`
- `reference/world-spec-guidelines/11_transcript_requirements.md`
- `reference/world-spec-guidelines/12_required_upload_inventory.md`
- `reference/world-spec-guidelines/13_claude_workflow_audit.md`
- `reference/source/New Writers Version - Instruction Guide (05_24).md`
- `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-v1.md`
- `worlds/korvin-merrow/execution-preparation/locked/execution-preparation-validation-review.md`
- `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`
- `worlds/korvin-merrow/submission-preparation/locked/submission-preparation-v1.md`
- `worlds/korvin-merrow/packaging/locked/packaging-construction-v1.md`
- `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-v1.md`

## Evidence Hierarchy For Transcript Mechanics

Current Studio evidence supersedes the older upload tutorial video for present platform mechanics.

The older video remains historical evidence that a Claude transcript surface existed and previously used a Claude share URL. It must not be treated as current Korvin upload mechanics after Alexander's current Studio screenshot shows an upload-file control instead.

## Transcript Evidence Register

| Question | Resolution | Evidence | Notes |
| --- | --- | --- | --- |
| Does current Studio require Claude transcript handling? | RESOLVED: yes. | Current screenshot shows section `2.3) UPLOAD CLAUDE TRANSCRIPTS`. | The field is marked required with an asterisk. |
| Does current Studio use a transcript URL text field? | RESOLVED: no, not in the current screenshot. | Current screenshot shows `Upload Claude Transcripts*` with an `Upload File` button and no visible text field. | The stale video showed a URL workflow, but current Studio evidence supersedes that. |
| Is the current transcript mechanism file upload? | RESOLVED: yes. | Current screenshot shows an `Upload File` control under `Upload Claude Transcripts*`. | This resolves mechanism, not final file type or file content. |
| What transcript file format is required? | UNRESOLVED. | Current screenshot does not show accepted file extensions or formatting rules. Local text sources do not define transcript file type. | Do not convert the transcript until a later authorized formatting/packaging decision. |
| What transcript scope is required? | PARTIALLY RESOLVED. | Current screenshot labels the field in plural as `Upload Claude Transcripts*`. Local text/video suggest Claude transcript relates to the spec-generation conversation, but current screenshot does not define which chats. | Multiple transcript files may be expected, but exact scope remains unresolved. |
| Is a Brainstorm transcript required by the reviewed evidence? | UNRESOLVED. | Current Studio plural field could include more than one transcript, but does not specify Brainstorm. Local text sources do not show a separate Brainstorm transcript rule. | Do not include or exclude Brainstorm transcript silently. |
| Does `docs/claude-transcript.md` contain a Korvin Claude share URL? | NOT FOUND. | Search of `docs/claude-transcript.md` found transcript discussion and auditor notes but no Korvin `claude.ai/share` URL evidence. | This matters less for current upload mechanics, but share URL evidence remains absent locally. |
| Is `docs/claude-transcript.md` itself ready to upload? | UNRESOLVED. | It exists as raw markdown transcript/provenance evidence, but current Studio only shows a file-upload control, not accepted format or readiness criteria. | Do not upload raw markdown without packaging/upload authorization and format confirmation. |

## Current Studio Review Summary

Alexander provided a current Studio screenshot for task `cyau8803` under Spec Drafting.

Observed current Studio layout:

1. Section `2.1) SPEC DOCUMENT` has `Spec Document*` and an `Upload File` control.
2. Section `2.2) REFERENCE FILES` has `Template/Reference Files*` and an `Upload File` control.
3. Section `2.3) UPLOAD CLAUDE TRANSCRIPTS` has `Upload Claude Transcripts*` and an `Upload File` control.
4. No transcript URL or pasted-text field is visible in the current screenshot.

Current interpretation:

- Current Studio requires uploaded Claude transcript file(s).
- Current Studio does not support using the stale video's URL-field workflow as the current requirement.
- The exact file type, naming convention, transcript scope, and whether `docs/claude-transcript.md` must be transformed remain unresolved.

## Stale Video Review Summary

The authorized local video is a 77.6-second screen recording of an older Studio layout and Claude sharing workflow.

Historical video findings:

1. The older layout showed an `Upload Claude Transcript` surface.
2. The older layout used a text field and demonstrated pasting a `claude.ai/share` URL.
3. The video does not determine current Studio mechanics after Alexander supplied a newer screenshot showing file upload.

Use of video evidence:

- It confirms historical transcript handling existed.
- It does not govern the current Korvin upload mechanism.
- It should be retained as stale historical reference only.

## Resolved Decisions

1. Current Studio transcript handling is required.
2. Current Studio transcript handling is file-upload based, not URL-field based.
3. The stale video must not be used to justify a Claude share URL as the current submission mechanism.
4. `docs/claude-transcript.md` remains preserved as raw provenance evidence and should not be formatted, cleaned, converted, uploaded, or treated as submission-ready in this phase.

## Unresolved Decisions

1. Accepted transcript file type or types.
2. Required transcript file naming convention.
3. Whether raw `.md` transcript is accepted or must be converted to `.docx`, `.pdf`, `.txt`, or another file type.
4. Whether the plural field requires multiple transcript files.
5. Which conversations are in scope: Brainstorm, World Spec, template/reference, Claude QC, or other Claude/Codex collaboration records.
6. Whether a Claude share URL remains useful as provenance even though current Studio uses file upload.
7. Whether current Studio upload validation imposes file size or extension constraints.

## Current Korvin Transcript State

`docs/claude-transcript.md` exists and remains the local raw transcript/provenance file.

A Korvin-specific Claude share URL was not found in the local transcript file during this resolution pass.

The current unresolved dependency is no longer "find a share URL." It is: determine the accepted uploaded transcript file format and scope for the current Studio `Upload Claude Transcripts*` field.

## Future Action Register

| Action | Status | Required before action |
| --- | --- | --- |
| Confirm accepted file type(s) for current Studio transcript upload. | PENDING | Current Studio field validation, pod/reviewer guidance, or official upload guidance. |
| Determine transcript scope for plural `Upload Claude Transcripts*` field. | PENDING | Current Studio instructions, pod/reviewer guidance, or explicit Alexander decision grounded in available evidence. |
| Decide whether `docs/claude-transcript.md` can be uploaded raw. | BLOCKED | Format/scope confirmation and packaging/upload authorization. |
| Convert or format transcript if required. | BLOCKED | Explicit formatting/conversion authorization after format decision. |
| Upload transcript file(s). | BLOCKED | Later upload authorization. |

## Boundary Verification

This phase did not:

- format the transcript
- clean the transcript
- rewrite the transcript
- convert the transcript
- package the transcript
- upload the transcript
- submit the transcript
- populate DOCX
- create a manifest
- run AutoQC
- create AutoQC responses
- modify locked artifacts
- create scoring artifacts

## Status

Transcript Resolution v1 is in CANDIDATE REVIEW.

Next eligible phase: Transcript Resolution Review.
