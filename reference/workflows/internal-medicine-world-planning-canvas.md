# Internal Medicine World Planning Canvas

Use this before any internal medicine brainstorm, world spec, file plan, task file, prompt, golden, or grader is drafted. It is a planning surface, not a build artifact. Do not create a new world folder from this canvas until Alexander explicitly authorizes the world build.

## What This Prevents

Korvin taught the expensive lesson: if the chart is built before the task surfaces and trap inventory are fixed, the later task slate collapses into draft-and-finalize repetition. The next world starts the other way around. First choose the task structures, then design the patient and source geometry to arm those tasks.

No-repeat receipt for this canvas:

- Tasks before files. Every essential source exists because a named task needs it.
- World files are raw material, not answer keys. Completed synthesis belongs out of the shared world layer unless every task truly needs it.
- A floor is bankable only when the failure is fair. Same-author drafts need true placeholders or an explicit correct-errors instruction.

## Use Order

1. Fill the structure slate.
2. Fill the trap inventory ledger.
3. Fill the source geometry board.
4. Stress-test fairness, reachability, and reviewer risk.
5. Only then write the Brainstorm in the official four-section format.

Stop immediately if a row needs a file, prompt, golden, grader, task DOCX, image, audio clip, or platform action. Those belong after approval.

## 1. World Thesis

Answer these before inventing documents.

| Question | Working answer |
|---|---|
| What real internal medicine workflow pain does this world model? | |
| What pressure makes the clinician move too fast? | |
| What clinical mistake would be serious in real care? | |
| Why would a strong model plausibly make that mistake? | |
| Which facts should be raw and scattered rather than summarized? | |
| Which single source would accidentally become an answer key if included? | |
| What is the world snapshot date? | |
| What is the latest allowed task anchor date? | |

Good internal medicine worlds usually come from ordinary complexity, not rare diagnoses. Prefer a common patient with interacting renal, cardiac, infectious, endocrine, pulmonary, geriatric, medication, functional, and documentation pressures.

## 2. Structure Slate First

Target 10 tasks. Use at least 5 distinct structures from `docs/task-structure-dossier.md`. Cap completion or draft-and-finalize at 1 or 2 tasks.

| Task | Structure | Approved workflow string | Deliverable | Native forced slot | Expected wrong move | Why it matters | Post-snapshot anchor | Grader mode | Reachability plan |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |

Grader mode choices:

- Chart-aware: needed when the model synthesizes from provided charts.
- Golden-only: only safe when the task is a planted-artifact catch and the golden contains the complete scoring target.
- Vision or audio aware: required when a photo, scan, handwritten note, or audio transcript is central.

Reachability choices:

- Actual catcher trajectory expected.
- Golden self-score check planned.
- Pod clarification needed because the clinical stance is contestable.

## 3. Trap Inventory Ledger

Every trap must be assigned to a task and a source route before any file is built.

| Trap | Task(s) | Warm or cold | Forced by what | Chart contradicts or mandates what | Fairness route | Expected model failure | Catch evidence needed | Grader hard-error status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

Fairness routes:

- True placeholder in a same-author draft.
- Prompt explicitly asks the model to correct unsupported draft content.
- External adversarial document that is wrong by genre, such as payer denial, CDI query, HIM worksheet, pharmacy handoff, or night-float signout.
- Forced inventory row, such as med rec, coding, DRG, quality abstraction, or charge capture.
- Off-text clinical evidence, such as a photo, scan, handwritten list, medication bottle, or preliminary image capture, with a minimal chart clue.

Reject a trap if it is only chart-silent, cosmetic, prompt-hinted, impossible to inspect, post-cutoff without an attached source, or carried by a same-author draft as a routine-looking assertion.

## 4. Source Geometry Board

No single file should answer a task alone. Shared world files should provide raw facts, conflicts, timestamps, orders, observations, and source provenance. Task-level files can provide the required form, external request, realistic noise, or off-text evidence.

| Planned file | World or task level | Modality | Raw facts it carries | What it must not summarize | Conflicts created | Tasks requiring it | Leakage risk |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Leakage checks:

- No shared discharge summary, consultant synthesis, or problem list should state the final answer unless the whole world legitimately needs it.
- No task file name may say clean, fixed, corrected, reviewer, final-answer, or similar.
- No duplicate mounted copy should exist under `.apps_data` or any extra volume.
- No stale v-file should survive beside the current task file.
- No file should contain golden, grader, FA, GA, PL, reviewer, or workspace metadata.

## 5. Internal Medicine Idea Bank

Use these as seed categories, not as facts. The physician owns the final clinical stance.

Physiology and trajectory:

- AKI on CKD after diuresis, sepsis physiology, contrast exposure, obstruction, or cardiorenal shifts.
- Heart failure versus dehydration, oxygen need versus atelectasis, COPD versus pneumonia, steroid response versus infection.
- Delirium, encephalopathy, sleep deprivation, OSA, sedating meds, falls, and family-reported baseline.
- Diabetes transitions, inpatient insulin needs versus outpatient regimen, steroid hyperglycemia, hypoglycemia risk.

Medication and safety:

- Renally cleared drugs, anticoagulation, antiplatelets, NSAIDs, RAAS inhibitors, diuretics, SGLT2 inhibitors, antibiotics, opioids, gabapentinoids, benzodiazepines, and OTC sedatives.
- Held medications that are not automatically discontinued.
- Home med bottles, pharmacy fills, MAR holds, and specialist recommendations that disagree.
- Dose timing errors, pill organizer mismatch, family teach-back, and discharge-day escalation.

Documentation integrity:

- CDI query overreach, coder severity pressure, POA status, sepsis sequencing, malnutrition, pressure injury staging, encephalopathy versus symptoms, and unable-to-determine paths.
- Treating physician assessment versus ancillary observation.
- External query or payer document that cites real indicators but draws the wrong conclusion.

Transitions and teams:

- SNF, home health, PCP, nephrology, cardiology, endocrinology, wound care, sleep medicine, pharmacy, HIM, payer, and family perspectives.
- Consultant recommendations that are reasonable in isolation but unsafe at the transition point.
- Pending cultures, preliminary imaging, discharge equipment, oxygen, CPAP, wound supplies, mobility supervision, and follow-up timing.

Off-text or low-salience evidence:

- Foot or line photo, medication bottle image, handwritten home BP log, downtime note, scanned outside medication list, preliminary imaging screenshot, or bundled lab sheet.
- Use only when Studio and the grader can actually inspect the modality.

## 6. Pre-Build Stop Sign

Do not build until every answer below is yes.

- The slate has at least 5 structures and no more than 2 completion tasks.
- Every task has a forced slot, not just a broad synthesis request.
- The source geometry can support at least 30 world-level files, with every essential file present because a task needs it.
- No world file acts as an answer key for the task slate.
- Every same-author draft trap is a true placeholder or has a correct-errors instruction.
- Every external adversarial file is realistic by genre.
- Every off-text signal has a visibility plan for the agent and the grader.
- Every task is anchored after the world snapshot and not in the future.
- Every task names a grader access mode, including input-file access when needed.
- At least one realistic catcher path exists for any all-floor risk.
- The failure is clinical, safety, coding, documentation integrity, quality, coverage, or material deliverable harm. It is not cosmetic.

## 7. Brainstorm Export

After this canvas is complete, export only the appropriate high-level content into the official Brainstorm:

- World setup: the patient, setting, timeline shape, and internal medicine complexity.
- Major friction points: stakeholder conflicts, not traps.
- Major traps: only the highest-yield trap classes and source locations.
- Rough task ideas: one line per task with structure, workflow, deliverable, forcing function, and post-snapshot anchor.

Keep the canvas local as the design cockpit. Do not paste the full ledger into the Brainstorm unless the official template asks for it.
