# Handoff to claude.ai - Task 1 close-out (two items)

Task 1 (Korvin Merrow discharge medication reconciliation) has cleared first human review, preference labeling, the PL AutoQC, and reached Ready for Delivery; it was briefly reopened only to attach a difficulty-warning response, which is done. Two small items remain to close, both record-consistency, neither blocking. Please read against the attached artifacts and confirm or flag.

## Item 1: FA / GA consistency with the 0.78 run
The concern: do the FA and GA in RLS read in the same plain-prose, no-header form as the rest of the record, and do they describe the 0.78 run's prednisone exactly the way the PL and the Paolo reply do, a hedged 5 mg bridge that still commits to a number, rather than a bald "manufactured dose"?

To check: read the attached current FA/GA text (FA-GA-current.md) against the attached run-5 model output and grading transcript. Confirm three things: (1) two-paragraph plain prose, no bullets, no headers; (2) the GA describes the grader scoring output vs golden + guidelines, not "going into the chart"; (3) the prednisone is described as a hedged 5 mg bridge that commits to a number, with no language calling it a bald manufactured dose. If any line overstates it to a flat manufactured dose, flag the exact sentence.

Expected: it is consistent. The current text says the model "wrote prednisone 5 mg PO daily as a bridging dose anchored to that same 5 mg fill" and that "deferring the taper makes the bridge reasonable, but committing to a number off the most recent dispense is the dispensing-equals-dose inference." That is the hedged framing, matching everything else.

## Item 2: the "Date / Anchor" artifact in the world files
The "Date / Anchor" project-artifact label appears in several finalized world files (count uncertain across reads: roughly 13 to 19 of 26; the held-back task files already had it removed). AutoQC never flagged it and the human reviewers have not opened those headers, so it is effectively only known to us.

The standing decision (TASK-RUNBOOK A0): do NOT re-open the finalized, trajectory-synced, delivered world to strip a cosmetic header label. Re-opening a live world invalidates the synced trajectories and destabilizes a passing, delivered task for no reviewer-required reason. The fix belongs at BUILD time in World 2 (use real clinical date fields, never "Date / Anchor"). So for Task 1 / this world, the artifact is logged and deliberately left; it is not an open cleanup that blocks delivery.

To weigh in: given Task 1 is already delivered and the world is trajectory-synced, do you agree the correct call is to leave it and fix at World 2 build time, or do you see a reason it must be corrected now despite the re-open cost? If the latter, name the concrete risk that outweighs invalidating the delivered trajectories.

## Attach to claude.ai for this handoff
1. FA-GA-current.md (the current submitted FA/GA text).
2. The run-5 (0.78) model output: Merrow_discharge_medication_reconciliation_05242026.docx (download from RLS trajectory 5 / run 274914b8).
3. The run-5 grading transcript (the grader's reasoning for the 0.78, from the Grading Transcript tab).
4. golden-response-task1-v6.docx (the reference golden).
Optional for Item 2: the live world snapshot (the 26-file zip) if it wants to verify the Date/Anchor count itself.
