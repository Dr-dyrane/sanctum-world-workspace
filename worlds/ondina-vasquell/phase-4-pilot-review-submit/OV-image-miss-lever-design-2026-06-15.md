# OV image-miss lever - design + Codex image spec (2026-06-15)

The sixth mechanism class, untested here and the only one that does not fight the model's prose strength. From "Raising Task Difficulty: Worked Example #1" (reference/source/Raising_Task_Difficulty_Worked_Example.pdf), Change 3 ("did most of the work"): a critical finding lives ONLY in a task-level image, prose silent, and the model fails because it reads images poorly. Their Before was all 95-98 percent (our exact ceiling); After was 15-40 percent bimodal. In-house precedent: KM08 banked as an all-floor photo-miss.

## Why this is frozen-world-safe
The worked example's Change 1 (remove the leaking discharge summary from the WORLD files) is the only world-file edit, and we SKIP it. We do not need it: our finding is novel and image-only, so no world file leaks it. Everything we add is TASK-LEVEL (image + a noise/intake note + a template). No world file is opened.

## Substrate gate - PASSED
- No frozen world file describes the IV/PICC line site (the chart is foot-only). So an infected-line finding is prose-silent: nothing in text states OR contradicts it. That is what avoids the prose wall that ceilinged the other five levers.
- IV antibiotics are documented (vancomycin/cefepime/pip-tazo "in use"), so a line exists - the finding is clinically grounded, not invented.
- Design rule the freeze imposes: the image finding MUST be prose-silent. A wound-deterioration photo would FAIL (world prose loudly says the wound is granulating/improving -> contradiction -> model catches it in text). The infected LINE passes; a worsening-wound image does not.

## Mechanism
Critical finding = an infected peripheral IV / PICC line site (the line delivering her IV antibiotics). It appears NOWHERE in prose. The only signals are (1) the task-level photo and (2) one buried low-grade temperature in a task-level intake note plus a one-line "line-site photo taken, see image" with no description. The physician finalizing the deliverable must catch the line infection and act (hold the transfer, remove/culture the line, the IV-antibiotic route is compromised). Missing an infected line that is delivering IV vancomycin is indefensible. Floor = the finalized deliverable does not catch the infected line. Catcher = it catches it from the image + temp and acts.

## Task design (genre = SNF transfer / admission note, the worked-example genre)
Task-level files (all new, frozen-safe):
1. `iv_line_site_photo_<date>.jpg` - the infected-line photo (Codex; spec below).
2. A nursing/transfer intake note - noise plus the two buried hints: a low-grade temp (about 38.0 C / 100.4 F) in the vitals, and a line "photo taken, see image" line with NO description of what it shows.
3. A SNF transfer/admission note template the response must follow (format requirement + reconciliation load).
Prompt: harried finish-the-transfer register, NO audit cue. E.g., "We're transferring Mrs. Vasquell to the SNF today. Finish her transfer note on the template so I can sign it." Do NOT say "check the line" or "review for issues."
Golden (physician-produced): completes the transfer note AND flags the infected line as a new active problem - hold or qualify the transfer, remove and culture the line, do not continue IV antibiotics through an infected line, escalate. Cites the photo and the low-grade temp. Signs.
Grader (KM five-block; CAP, don't deduct): missing the infected line is a HARD FAIL (cap low) regardless of how complete the rest of the transfer note is (worked-example rule). Also credit only if the response acts on it (line removal/culture + route change), not merely "noted." Standard untrusted-verification clause. Noise-sieve and template-format expectations in Section B.

## Vision gate (KM08 precedent) - REQUIRED before any pilot
Confirm the infection is AGENT-VISIBLE (the model under test can open and see the image) AND GRADER-VISIBLE (the grader can see it to score the miss). A task whose floor rides on an image that does not render to one side is broken. Verify both before spending a pilot.

## Bench rule (decisive)
Cold screen: does a fresh strong model, finishing the transfer note, CATCH the infected line or MISS it? Because models read images poorly, a reviewer MISS is the FLOOR signal here - the inverse of the prose levers, where the reviewer caught everything. Proceed to pilot ONLY on a floor (reviewer-miss) verdict. If the cold reviewer reliably catches it, this lever ceilinged; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).

## Codex image spec (hand to Codex imagegen; decision-10 delegation)
- Subject: a close, clinical photograph of a peripheral intravenous or PICC catheter insertion site on an older adult's forearm or upper arm, showing clear early infection: erythema (redness) spreading around the insertion site, purulent or cloudy exudate at the site, mild swelling; optionally faint proximal streaking. The catheter/dressing is visible. Realistic ward-photo look.
- Severity: the infection must be clearly VISIBLE to a careful human reader (fair - a catcher can see it), but it is the kind of finding the model under-reads. Not subtle to the point of ambiguity; not captioned.
- Hard constraints (OV image doctrine + KM08): fully synthetic; NO identifying features (no face, no tattoos/marks, no name bands with real data); NO text in the image that resolves the finding (no "infected", no arrows/labels); temporally anchored (consistent with the encounter dates, after the 05/21 snapshot); EXIF length 0; no prior-world identifiers; renders cleanly to PNG/JPG and is verifiable agent- and grader-visible.
- Filename: task-level, e.g., `iv_line_site_photo_05242026.jpg`. Deliver into the OV image pipeline like EW30/EW31, but mounted as a TASK-LEVEL file for this task only (not a world file).

## Slot
Proposed: OV08 (Referral Intake, Triage, and Scheduling Coordination) - the SNF transfer/admission genre is the worked example's exact context, and OV08's prior mechanism (perfusion-closure) was warm/disproven, so re-centering it is clean. Alternative: OV10 (Documentation Completion). Confirm before wiring. Approved-workflow string verified live at Step 10.

## Status
Substrate gate PASSED. Awaiting: (1) decision to proceed, (2) Codex image generation from the spec above, (3) build of the task package, (4) vision gate, (5) cold bench screen. No world-file edits at any step.
