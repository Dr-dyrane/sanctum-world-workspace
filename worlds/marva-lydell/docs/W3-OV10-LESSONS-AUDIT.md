# World 3 (Marva Lydell) audit against the OV10 reviewer correction

Source of the corrections: worlds/ondina-vasquell/tasks/task10/LARRY-2026-06-20-OV10-CORRECTION.md (Larry E, 2026-06-20).
Purpose: make sure W3 does not repeat the OV10 problems BEFORE task creation. This is an audit and a set of recommendations only; nothing is being rebuilt here, and OV10 is not being solved yet.

## Verdict in one line
W3 has one real exposure: two of the ten tasks (Task 4 and Task 6) are note-completion / "finish a started draft" tasks, which is exactly the workflow Larry now deprecates. Everything else about W3 already aligns with the correction. Recommendation: redesign Tasks 4 and 6 off the completion format before they are built.

## P1 - No "finish the note" / completion workflows  (PRIMARY EXPOSURE)
Larry: finishing a note is not a realistic workflow; the discharge-summary / completion workflow is deprecated.

- Task 4, Transition Note Completion (workflow: Medical Transcription and Clinical Documentation Completion). Deliverable: "a finalized transition-of-care note completed from a started draft." Prompt: "I started Mrs. Lydell's transition-of-care note ... Please finish it from her chart ... so I can sign it." This is the deprecated pattern almost exactly, a transition-of-care (discharge-adjacent) note finished from a placeholder draft. HIGHEST RISK.
- Task 6, Cardiorenal Follow-up Referral Handoff (workflow: Specialist Referral Letter and Documentation Preparation). Deliverable: "a cardiorenal follow-up referral letter completed from a started draft." Same finish-the-draft completion shape. HIGH RISK on format; the underlying Specialist Referral workflow is likely acceptable if reframed as full authorship.
- Note: W3 built both as "true placeholders" (not planted-false closures) specifically to be fair. That was the right instinct under the OLD rule, but it does not save these tasks, because Larry now deprecates the completion FORMAT itself, fair or not.

Recommendation (hold for Alexander):
- Task 4: move off completion. Either (a) full authorship of an approved deliverable that is not a note (the chart already supports a payer, coordination, or determination task), or (b) Larry's own suggestion, a complete signed note that contains a common, realistic error, with the task being to review and correct it (a review task, not a completion). The exertional-oxygen miss or a silently-resumed held agent are natural "common mistakes" to plant in a COMPLETE note.
- Task 6: reframe to full authorship, write the whole cardiorenal referral/handoff letter from the chart, keeping the route-open-decisions-to-owners design. Drop the started-draft/placeholder framing.

## P2 - No planted false information; failure from realistic catchable errors  (ALREADY ALIGNED, one item to scrub)
Larry: do not punish the model for carrying over something stated in the chart; disagreements, accidental non-adjusted meds, and accidental omissions are fine.

W3 is already built this way. Per the spec, "every scored judgment has a documented contradiction or a documented restraint behind it," and "the two completion tasks carry true placeholders rather than planted-false closures, so the model is tested on finishing open work correctly, never on distrusting a falsehood in the patient's own record." The trap inventory is realistic:
- resting oxygen acceptable while the formal walk test shows exertional desaturation = an omission / synthesis trap, both facts true;
- case-management prose says equipment arranged while the vendor record shows portable oxygen undelivered = a documented discrepancy;
- a stale outside / SNF intake list carries an old renal dose or duplicate anticoagulant = an accidental non-adjusted med on an OUTSIDE list, with a stated source-of-truth order (active record governs);
- held agents tempt an auto-resume while nephrology frames restart as a careful judgment = a consultant judgment.
All of these are explicitly the kinds Larry calls fair.

One item to scrub during any Task 4 redesign: the started draft's "reassuring background discharge-medication line that would silently resume the held agents." Make sure that line reads as a realistic accidental carry-forward (a common mistake), and that the score does not hinge on the model merely having trusted a chart line. The cleanest resolution is the Task 4 redesign above (a complete note with a common error to catch), which removes the placeholder-trust dynamic entirely.

## P3 - No universal floor  (DESIGN OK; must be verified at pilot)
Larry: a task that fails ~15% across all ten runs is flagged unfair.

W3 intends a spread, "roughly three harder synthesis or determination tasks, five mid-range forced-judgment tasks, and two lighter but still discriminating tasks," and every trap is tied to a reachable carrying document. That is the right shape. But intent is not proof: at pilot, each task's score distribution must show that a capable model CAN pass (the catch is reachable, not a guaranteed floor). Any task that floors every run gets redesigned, not shipped. Carry the OV floor-mechanism discipline: the catch must be reachable and fair, never a gotcha that no run survives.

## P4 - New-format compliance  (ON TRACK)
W3 task creation must use the current project instructions, the new grader guidelines and the FA/GA and PL formats, which is already the working standard here. Confirm each task's grader and FA/GA are built on the current format at task time.

## Bottom line
- Redesign Task 4 and Task 6 off the note-completion format before building them (the one direct OV10 echo).
- Keep the rest of the trap architecture as is, it already satisfies the "realistic catchable error, no planted falsehood" rule.
- Treat the difficulty spread as a hypothesis to confirm at pilot, kill any universal floor.
- Build all task graders and FA/GA on the current format.
APPROVED 2026-06-20 by Alexander: the recommendation stands, Tasks 4 and 6 to be redesigned off the completion format before they are built (at task creation, after the spec + templates clear World Spec AutoQC). APPLIED 2026-06-20: Tasks 4 and 6 redesigned in the spec. Task 4 -> attending peer review of a COMPLETE signed resident transition note carrying two common errors (oxygen cleared despite the documented exertional desaturation; held agents silently resumed), Peer Review and Patient Safety category (verbatim lane string pending lead confirmation). Task 6 -> full authorship from the chart, started-draft dropped, E1-T6 reframed to a referral request. Subagent-verified SHIP; both stay P0.
