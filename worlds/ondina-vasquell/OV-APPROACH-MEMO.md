# OV approach memo - what works, what fails, how we build (2026-06-16)

One page. The clean chart is the ideal substrate, not a cap. Floors are manufactured at the task layer.

## The engine that works
One mechanism, three expressions. A completion frame ("finish this") plus a high-stakes step the deliverable does not force. The model completes the surface and skips the step.
- OV01: finish the med rec. The model copies the inpatient list forward and does not re-evaluate enoxaparin at discharge.
- OV02: finish the note. The model fills the sections and does not assemble the prose-silent line infection.
- OV04: finish the transition note. The model writes it and never opens the peripheral CPAP image.
The catch sits on an axis the model has no reflex to police, in a deliverable that lets it skip the step.

## What fails, and why
Every ceiling pointed the trap at a model strength. Four patterns to avoid.
- Catch on a LOUD axis the chart already states (anemia, offloading, the HR 50 vital). The model reads it and catches.
- Deliverable FORCES the read (the med rec and the AKI RCA both compel checking the meds). The model cannot skip what the task compels.
- DECLINE an external premise (coding query, OV07, the UR determination). The model pushes back cleanly and commits.
- Finding BURIED IN TEXT (the prelim-imaging incidental). The model reads all text and recognizes it at or above a physician.

## The real limitations (not the chart)
- Model strength. It reads every file it opens, recognizes findings well, declines bad premises, commits to verdicts.
- Our craft. The pairing is the work: a completion deliverable matched to a step it genuinely does not force, on a quiet axis, fair, in an approved workflow.
- The fairness bar. No planted falsehood, no telegraphing, no grader tuned for depth. OV04 v1 and the anemia bench died here.
- The one reliable handle. The model skips OPENING some image files. That is the cleanest place it fails to gather (OV04, about 40 percent did not open the image).

## Constraints
World files frozen; build at the task layer only. Workflow selected from the approved P0/P1 list; we do not invent lanes. One re-roll then retire. FA/GA from the 2nd-lowest distinct run. Bench cold before spending a pilot. Alexander voice on all output text (verify_voice).

## The pivot, task 1 to here
Task 1 (OV01) banked first on cold knowledge. The rest of the deck was built as the spec's workflow tasks; most ceilinged. We stopped shipping the workflow as written and started manufacturing the trap at the task layer: pull the answer out of the world files, leave it off-text, frame the ask as "finish this." That produced OV02 and OV04.

## How we build the next floor
Not a new world. A new pair. Pick an approved workflow whose face-value completion lets the model skip a high-stakes step. Put the index data in a task-level artifact that does not state it cleanly: an image the model may not open, or a problem that must be assembled. Keep the axis quiet and the prompt plain. Cold-bench first. Two open handles: off-text image (OV04 family) and synthesis suppression (OV02 family).

## Status
Three floors confirmed: OV01, OV02, OV04. OV05 is a fair catcher, kept. Drive to eight in this world by manufacturing more task-layer pairs.
