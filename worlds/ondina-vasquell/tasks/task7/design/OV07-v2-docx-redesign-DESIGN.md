# OV07 v2 redesign - docx embedded-wrong closure (no image)

Date: 2026-06-18. Status: BUILT 2026-06-18, awaiting re-pilot. The v2 artifacts are rendered through build_ov07.py (started appeal placeholder, home_health_suitability_screen, transfer-day wound note documenting the undermining, golden-OV07-v2), the grader and prompt are off "photograph," and the v1 image, its spec, and golden-v1 are archived. Gates green (verify_ondina, presubmit task7, verify_voice). Re-pilot, upload, and AutoQC remain gated on Alexander. Reason for redesign: Larry's 2026-06-18 send-back disallows the AI-generated wound photo. This pivots OV07 off the image entirely, onto a docx mechanism, per Alexander's direction (use a docx, a nursing-documented report, no image, no license back-and-forth).

## Why a documented-finding docx would ceiling (the constraint this design respects)

The original OV07 floor worked because the undermining lived in an IMAGE the model may not open. The floor-mechanism library is explicit that a finding buried in TEXT is read and recognized at or above physician level, so it ceilings. If we simply move the undermining into a nursing note the model reads, the model surfaces it and the task ceilings. So the docx cannot be a hidden finding to discover. It has to carry the trap as a wrong CLOSURE the appeal adopts under a completion frame, which is the engine that floored OV08 (false oral-antibiotics line, ~0.10) and OV10 and OV11 (fabricated closures, ~0.10 to 0.18).

## Mechanism (v2)

Lane unchanged: Claims Denial Analysis and Appeal Preparation. The skilled nursing facility level-of-care denial stands; the deliverable is the completed physician appeal.

The trap moves from off-text-image-miss to embedded-wrong-closure:

- A subordinate transfer-day screening document (a case-management or nursing home-health suitability screen) wrongly CLOSES the wound question. It records the wound as stable, routine dressing changes, suitable for intermittent home-health wound care, no skilled need. This is the wrong closure.
- The started appeal draft is a TRUE PLACEHOLDER for the clinical-justification section. It sets up the appeal letter and the administrative frame, and leaves the skilled-need basis to be completed. It asserts nothing about the wound's acuity.
- The chart supports skilled placement: the wound-care consult and the transfer-day nursing wound note document undermining or tracking that requires skilled packing and serial CWOCN assessment, intravenous antibiotics requiring skilled administration, continuous offloading with failed teach-back, and insufficient home caregiver support.
- The model finalizing the appeal must REJECT the screening's closure and build the appeal on the documented skilled need. Under the completion frame with no reconcile clause, the model is pulled to adopt the screening's routine-dressing framing and submit a rebuttable appeal.

FLOOR: the appeal adopts the screening's home-health-adequate closure, argues from routine dressing changes, and is rebuttable on its own terms. CATCHER: the appeal rejects the closure, builds the skilled-need case from the documented wound status, intravenous antibiotics, offloading failure, and caregiver gap, and requests reversal.

## Why this is fair

The wrong closure lives in a SUBORDINATE document the physician reviews and finalizes against, not in the model's own same-author draft as a planted false line. The started appeal draft is a true placeholder for the scored section. There is no reconcile clause and no telegraph. This is the OV08 fairness posture (a subordinate worksheet wrong by genre, finalized under a completion frame), which banked. The screening conclusion is wrong for an understandable reason (it reads the wound as improving and low-acuity), not a self-incriminating mischaracterization, so it is the floorable embedded-wrong, not the swatted-away suggested-wrong.

## What changes from v1

- REMOVE the image asset (`wound_photo_05242026.jpg`) and retire `wound-photo-image-spec.md` (the Codex generative spec). The non-AI compositor `build/composite_ov07_wound_annotation.py` is no longer needed for this path; keep it for history.
- ADD the subordinate screening docx (case-management or nursing home-health suitability screen) carrying the wrong closure, authored through build_one in the Epic house style.
- CHANGE the started appeal draft to a true placeholder for the clinical-justification section.
- KEEP the lane, the denial, and the skilled-need substance of the golden. The golden now rejects the screening closure and builds skilled need from the documented chart findings, rather than from the photograph.
- UPDATE the grader Preamble and Section A: the central requirement is rejecting the home-health-adequate closure and building the skilled-need basis on the documented wound status, intravenous antibiotics, offloading failure, and caregiver gap. The off-text-image language is removed.
- UPDATE the prompt only if it names a photograph; otherwise the plain finish-the-appeal prompt stands, no reconcile clause.

## Floor and catcher (design targets)

Bimodal, design floor 0.30 to 0.55 with at least one catcher above 0.85. Read by whether the floors adopt the screening's routine-dressing closure and the catchers reject it and build skilled need, not by the mean.

## Build, pilot, FA plan (all gated on Alexander)

1. Build the subordinate screening docx and the placeholder appeal draft through build_one; update the golden and grader; keep dates on the OV spine (05/24/2026), which is grandfathered for OV.
2. Run verify_ondina, presubmit_task_gate task7, verify_voice. Golden self-score under the new grader.
3. Bench cold to screen telegraph, then re-pilot (mandatory after any golden or grader change, DO-NOT-REPEAT #22). Confirm the mount tree: one screening docx and one placeholder appeal draft under /docs/filesystem, nothing stale.
4. Redo the FA and GA from the new run set, second-lowest distinct run, to the latest fa-ga-canonical guidance: failure-only FA ending with `Overall Failure Score: X.XX / 1.0` plus the writer score, and a GA with both mandatory moves (what the grader got right, and what it missed or could improve).

## One tradeoff to weigh

The OV suite already leans on the embedded-wrong family (OV01, OV03, OV06, OV08, OV09). Converting OV07 from the off-text image to another embedded-wrong closure removes the suite's clearest image task and adds a fifth-plus embedded-wrong, which raises monotony. It is still the right call here because the alternative, a documented finding in a readable docx, ceilings. If suite variety matters more than keeping OV07 on the appeal lane, the other option is to retire OV07 and replace the slot with a distinct structure, but that is a larger change than this redesign.
