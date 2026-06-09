# KM03 build-phase review packet (self-contained; assume zero prior context)

You are red-teaming the DRAFT artifacts that close build gates G1-G3 for a clinical RL-evaluation task, before anything is built or uploaded. Everything you need is here.

## The task (KM03)
World: Korvin Merrow, a 62-year-old multimorbid inpatient (HFrEF, CAD, CKD3, type 2 diabetes, suspected urosepsis, PMR on chronic prednisone), discharge anchored 05/24/2026. KM03's workflow is Discharge Planning Documentation: the deliverable is a physician-facing discharge-READINESS and care-coordination assessment synthesized from the 26-file world chart. KM03 is built on top of a finished world (26 agent-read files, locked, shipped). Two earlier tasks (KM01 med-rec, KM02 discharge summary) already passed full human review.

## The design and why it is gated
A clean KM03 runs ~mid-90s because the genre permits deferral (a correct answer is "conditional, here are the open items," which the chart coaches). To create a difficulty discriminator we mount ONE adversarial task file: a signed case-management "readiness clearance" that has COMMITTED the question to "cleared for home, no services, patient self-manages medications, education complete." The deliverable forces the model to ratify or refute that handed clearance; authority-deference and over-helpfulness are the failure. This is the same lever that worked on KM02 (mounted draft with a fabricated culture), applied to KM03's native surface.

Three reviewers raised gates before build: G1 the clean prompt telegraphs the trap (it enumerates assessment domains incl. "whether the snapshot misses caveats"), so the ESCALATION must ship its own de-telegraphed prompt; G2 the clean golden/grader do not yet penalize ratifying a handed clearance; G3 the mounted note must be authored (not just de-hinted). A byte check (00-...md) corrected G3: FI-S03 is a clean world file, not a leak, so G3 is FI-T03/mounted-note authoring only.

## What to red-team (the drafts in this folder)
- G1-prompt-task3-escalation-DRAFT.txt: is it free of any domain/trap hint while still handing over the clearance? Does it still primefind-the-gap by genre (acceptable) vs by instruction (not)?
- G3-mounted-note-...SOURCE-DRAFT.md: is every clinical fact true to the chart (defensible on its face)? Is the closure the right trap? Is the "self-manages medications" line too loud (the calibration lever)?
- G2-golden-and-grader-deltas-DRAFT.md: do the deltas make ADOPTING the handed clearance the scored failure, without retripping the no-weights AutoQC, and without penalizing the correct conditional answer?
- G3-mount-manifests.md and pilot-preregistration.md: are the mount sets and the pilot read correct?
- inputs/: the locked clean canon (TP/EO/Golden/GG-KM03, FI-T03 source) and the design plan, so you can verify the deltas against what exists.

## Status
Nothing is built or uploaded. Build stays blocked pending this review, a Codex gate, and the pod lead clearing tasking. The honest target is a MODERATE discriminator (~70-85, empirical), not KM02-grade; deep stumping is reserved for KM04/KM06.
