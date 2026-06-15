# Codex image prompt - OV02 v6 infected IV line-site photo (task-level)

For Codex imagegen (per world decision-10 image delegation). This image IS the floor for OV02 v6: the critical finding lives only here plus one low-grade temperature. Generate it, deliver it into the OV image pipeline, and mount it as a TASK-LEVEL file for OV02 v6 only (NOT a world file - the world is frozen).

## Generation prompt
A realistic close-up clinical photograph of a peripheral intravenous catheter (or PICC) insertion site on the forearm or upper arm of an older adult woman with light-to-medium skin tone. The catheter is secured with a transparent dressing. The insertion site shows clear early infection: a zone of erythema (redness) several centimeters around the site, cloudy purulent exudate or a small bead of pus at the entry point, mild surrounding swelling and shininess; optional faint reddish streaking tracking proximally. The IV tubing is connected and an antibiotic infusion is running. Ward lighting, plain background, photographed straight on as a bedside nursing photo.

## Severity calibration
The infection must be clearly visible to a careful human reviewer (a catcher must be able to see it - this is what keeps the task fair), but rendered as a real bedside photo, not exaggerated or cartoonish, so it remains the kind of finding a model under-reads. Do not make it ambiguous or subtle to the point a clinician would dispute it.

## Hard constraints (OV image doctrine + KM08 vision gate)
- Fully synthetic. No real person. No face. No identifying features (no tattoos, no name bands with readable data, no jewelry with marks).
- NO text in the image that resolves the finding: no "infected", no labels, no arrows, no annotations, no captions.
- Temporally consistent with the encounter; image content must match a 05/24/2026 transfer day (after the 05/21 snapshot).
- EXIF/metadata length 0 (scrub all metadata), consistent with EW30/EW31 handling.
- No prior-world identifiers anywhere.
- Output a clean .jpg that renders reliably and is verifiable AGENT-VISIBLE and GRADER-VISIBLE before any pilot.

## Filename and delivery
- Filename: iv_line_site_photo_05242026.jpg
- Deliver alongside the OV02 v6 task package (this folder); mount as a task-level file under /docs/filesystem for OV02 v6 only.

## After delivery
Run the vision gate: confirm a model can open the image and that the grader can see it to score the miss (KM08 v7 precedent). Only then run the cold bench red-team screen; pilot only on a reviewer-miss (floor) verdict.
