# Sanctum Coach merge: how the Coach fits our deterministic workflow

Date opened: 2026-06-20. Scope: cross-world. The Coach package was added to the repo at `tools/Sanctum_Coach/` (extracted from Sanctum_Coach_2026-06-15.zip; curriculum v1.5, QC specs brainstorm v18 / world spec v19).

## Thesis

The new instructions push every writer through Sanctum Coach. We are past the level the Coach teaches: we already author brainstorms, specs, builds, gates, FA/GA, and pilots deterministically here. So we do not hand the work to the Coach. We keep producing everything in this workspace, we adopt exactly ONE step the Coach genuinely resolves for us (template-file sourcing), and we run the Coach in its veteran path so the platform transcript matches the process they expect. The workspace governs; the Coach is a sourcing tool and a transcript surface.

Plain version: same flow we already run. The only thing the Coach settles that we did not already have nailed is where each world-level template file comes from. Everything else of ours stays.

## Division of labor

| Phase | Who governs and produces | The Coach's role |
|---|---|---|
| Brainstorm | Workspace (authored, reconciled to Larry, committed) | Transcript only. Paste the chat-reference copy, run the veteran path, let it tighten to the template and run its audit. No new substance. |
| World Spec | Workspace (substance: world setup, frictions, traps, task table, file plan, golden/grader design) | Transcript + format. The Coach assembles into World_Spec_Template.docx and runs its AutoQC-style audit. We keep authorship; it formats and checks. |
| Template Curation | Coach (this is the adopted step) | Real work: classify each world-level file row by origin, extract DataBank templates with formatting preserved, draft custom templates in house style, name public-domain sources. We supply the file plan; it returns the Reference Templates folder. |
| Writer-produced artifacts | Workspace (our renderers) | Out of scope for the Coach by design. The Coach lists them and stops; we produce them here. See "Writer-produced" below. |
| Build / gates / FA / GA / pilots | Workspace only | None. The Coach never touches task prompts, goldens, graders, FA, GA, or preference labels. The compliance boundary forbids it, and so do we. |

## The one thing the Coach resolves: template-file source

The Coach's Template Curation phase is the genuinely useful step. Per its curriculum, every world-level file row in the spec's Section 3 file plan gets exactly one of four origins, decided DataBank-first:

1. DataBank template: a premade clinical document in Template_DataBank.docx. The Coach opens the DataBank with its code tool and extracts the matching template as a formatted .docx, original fonts and spacing intact. Check here first.
2. Public-domain form: an official blank form (FMLA, USCIS, OSHA). The Coach names the source agency and link; the writer downloads and scrubs metadata.
3. Custom-made template: the Coach drafts it in the Clinical Template House Style (modest 12pt bold name line, Courier New 10 body, ALL-CAPS section labels, one blank line between sections, dash bullets, bracket placeholders, output as .docx). Co-equal fallback with public-domain.
4. Writer-produced file (not a template): a bespoke artifact made with specialty tools. OUT of the Coach's production scope; produced separately. This is our lane (next section).

Filename discipline (Module 4), which our file plan must follow:
- Template or reference file: generic descriptive name, NO datestamp (for example `DB_Progress_Note_Inpatient.docx`). This string IS the row's Reference File Origin value, and IS the actual file in the Reference Templates folder.
- Spec Filename.type column: the final synthetic name WITH datestamp (engineering's output, for example `ProgressNote_05112023.docx`). Never name a template this.
- Writer-produced file: keep the final datestamped name in BOTH Filename.type and Reference File Origin (engineering does not rename it).

House-style and content constraints we inherit for any template: realistic terse EHR voice, generic bracket placeholders only, never any synthetic / fictional / training / educational marker anywhere, .docx for documents, native format for media, American English, no em or en dashes.

## Workflow source of truth: the canonical doc and Larry, NOT the Coach endpoint

The Coach fetches an approved-workflow list from a live endpoint and treats it as authoritative. We do not. That endpoint is BEHIND: the EPMs have not pushed the current cut to it, so its lane set, tiers, and delivered counts lag. Our source of truth is the 06/19 Combined doc in `reference/source/task-selection-categories/` plus Larry, who holds the latest cut. When the endpoint and the canonical cut disagree, the canonical cut governs. The W3 workflow locks were corrected on 2026-06-20 after an earlier pass leaned on the stale endpoint (see `worlds/marva-lydell/docs/LARRY-2026-06-20-RECONCILIATION.md`, section 1).

Two real rules still apply, but judged against the canonical cut, not the endpoint:
- Saturation: an over-delivered lane (more than 20) should not be reused. Read the count off the canonical or Larry cut; the endpoint's counts are stale.
- Closed list: use only real lanes from the canonical cut; never invent. A lane that is in Larry's latest but not yet in the local doc (for example W3 Task 6's Specialist Referral lane) is still valid on Larry's authority; confirm spelling and tier with him or the next doc cut.

Operationally: lock workflow strings from the canonical 06/19 doc or Larry's latest. Treat the Coach endpoint as a convenience the Coach uses in-session, not as a gate. If a Coach session balks at a lane because its endpoint is stale, that is not our error; the canonical cut governs and the workspace record holds the citation.

## Writer-produced artifacts: our simulative response is the sanctioned path

The instruction document's file-source table has a row "Writer-produced file, customized (not a template)": a finalized artifact that needs specialty tools or clinical expertise, that engineering cannot generate from a template, marked "No (already done)" for engineering conversion. Its own examples are "Custom EKG tracing (clinical data simulator)", a pill-bottle photo, ambient scribe audio. The Coach's origin 4 is the same category and explicitly routes it OUT of the chat: produced separately with the instruction-doc tools, owned by the writer, engineering does not touch it.

That is exactly what we already do. Our in-repo rendered artifacts (the ECG tracing produced by our renderer, and any telemetry, rhythm strip, or device printout we render) ARE writer-produced customized files. We maintain this approach unchanged. It is licensing-clean (rendered from synthesized data, not sourced, no PHI, metadata scrubbed) and it is the category the instruction document names. The instruction document recommends new writers avoid writer-produced files and lean on DataBank or custom templates; it permits them for a veteran or someone with strong project understanding, which is our standing.

How a writer-produced artifact enters the file plan: it is a row whose origin is 4, whose Reference File Origin and Filename.type both carry the final datestamped name (for example the discharge ECG image's dated filename), and which the Coach lists as "writer will produce" and does not generate. We render it here, name it per Module 4, and upload it alongside the templates.

What stays sourced vs rendered is governed by `docs/authored-image-artifact-menu.md`: waveforms, printouts, and forms are authorable license-clean; true diagnostic images (X-ray, CT, MRI, ultrasound, pathology, clinical photos) are not, and we mount the report instead.

## Veteran path

The Coach has a non-teaching mode for experienced writers, activated by a specific exact phrase the Coach never advertises. In that mode it stops calibrating and testing, takes our inputs directly, assembles and tightens the deliverable into the required template, and critiques it against its audit checklist instead of running pedagogy. Every hard rule still holds in that mode: live workflow fetch, the saturated-over-20 silent ban, the closed list, the temporal rule (the whole clinical timeline before July 2025), physician-voice framing, and the compliance boundary (it still must NOT author task prompts, goldens, graders, FA, GA, or preference labels; it elicits and critiques those). This is internal operational knowledge. It is not platform-facing and is never surfaced in any deliverable, disclosure, or writer comment.

Caution on the Coach's temporal rule: the curriculum says the whole clinical timeline must precede a July-2025 knowledge cutoff, but the Coach is behind, and the delivered OV world used 2026 dates, so this rule is likely Coach-stale. Do not move Marva's July 2025 timeline on the Coach's say-so; confirm the date policy against the canonical doc or Larry first.

## Governance: workspace is source of truth

- The workspace holds the canonical artifacts: specs, builds, goldens, graders, gates, FA/GA, pilots, and this doc set. If the Coach's output and our governed artifacts disagree, the workspace governs.
- Workflow names, tiers, and saturation come from the canonical 06/19 doc and Larry's latest cut, NOT the Coach's stale endpoint. We conform our strings to the canonical cut.
- Every Coach session is reconcilable to the workspace through two artifacts: the chat-reference copy we paste in (the inputs), and the working log we keep here (the trace). Nothing the Coach produces becomes canonical until it is checked into the workspace and passes our gates.

## Transcript-matching protocol (per world, per phase)

1. Finish and commit the substance here (brainstorm, then spec, then file plan).
2. Refresh the chat-reference copy for the world (`worlds/<world>/coach/` bundle) so it reflects the committed state and the workflow locks (from the canonical doc and Larry's cut).
3. Open the Coach as a Claude Project (its custom-instructions file pasted into the project prompt, the Upload_to_Claude curricula and the two templates added as project knowledge), activate the veteran path, and state the phase.
4. Paste the chat-reference copy. Let the Coach assemble to the template and run its audit. Accept formatting and audit fixes; reject any new substance that did not come from here.
5. At Template Curation, attach Template_DataBank.docx to the chat, walk the file plan, download each extracted or drafted template, and list the writer-produced rows. Produce those rows here with our renderers.
6. Record each step in the working log. Upload the spec plus the Reference Templates folder to Studio as separate files, not zipped.

## Pointers

- Working log (the trace): `docs/W3-WORKING-LOG.md`.
- Chat-reference copy (the inputs to paste): `worlds/marva-lydell/coach/W3-Coach-ChatRef.md`.
- Reconciliation (workflow locks + fairness): `worlds/marva-lydell/docs/LARRY-2026-06-20-RECONCILIATION.md`.
- Coach package: `tools/Sanctum_Coach/` (curricula, templates, DataBank).
- Authored-image doctrine: `docs/authored-image-artifact-menu.md`.
