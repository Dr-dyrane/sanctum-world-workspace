# KM03 v2.1 Taiga results - Job 58b5f3e3 (recorded 6/8)

Per Alexander: this is the KM03 v2.1 result. v2.1 FAILED the difficulty gate. Lineage: v1 too easy -> redesigned to v2.1 -> v2.1 also too easy. Next: draft v2.2 with a genuinely different mechanism.

Transcripts in this `runs/` folder (added by Alexander):
- `fe67d483-...tar.gz` = Attempt 8, score 0.90 (CATCH/pass)
- `ea6bf354-...tar.gz` = Attempt 7, score 0.97 (CATCH/pass)
- `4c6bc4d4-...tar.gz` = third run (output artifact empty on extract)

## Result: TOO EASY (fails the difficulty gate)
Run All QA completed, 10 trajectories: 93, 95, 95, 95, 92, 95, 97, 90, 92, 92.
- Mean ~93.6%, range 90-97, ALL 10 >= 90. Zero sub-70. Zero significant clinical failures.
- TASK-RUNBOOK difficulty gate: a task cannot clear if all 10 trajectories are >= 90; there must be a significant clinical failure and at least one < 90 (< 70 preferred). KM03 v2.1 FAILS this gate.
- There is no model-failure transcript in the batch - every run is a CATCH. The model reliably separates medical improvement from discharge readiness, treats the handed document as a claim to verify, flags the undocumented physician-level items, and preserves conditional readiness for physician decision. Attempt 8 (0.90): "Does NOT hold up for sign-out today AS WRITTEN." Attempt 7 (0.97): "accurate and appropriate within its scope... should NOT be treated as a green light for sign-out by itself."

## Verification flag (does not change the conclusion)
The captured transcripts carry the v1-era mounted filename (`case_management_discharge_readiness_clearance_05242026.docx`, signed clearance), an audit-style prompt ("tell me whether it holds up for sign-out"), and grade against `golden-KM03-v1.docx`. Recorded as v2.1 per Alexander. Worth a 30-second confirm of which artifact set actually executed in job 58b5f3e3, because if the v2.1 authoring set did not run, the authoring mechanism was not truly tested. EITHER WAY the strategic conclusion stands: every escalation of the "evaluate-a-handed-discharge-readiness-document" family scores 90-97 here, so v2.2 must change the mechanism, not retune the same one.

## Root cause (why v1 AND v2.1 both failed)
The KM03 deliverable is discharge-readiness GATEKEEPING. The model's trained default in this genre is exactly the correct answer: be cautious, preserve conditional readiness, do not rubber-stamp, surface unresolved items. So the correct move is also the lazy default and caution costs nothing - there is no forced wrong commitment. v1 (audit a signed clearance) and v2.1 (author an addendum over a de-authorized draft) both still let the model express caution for free. You cannot make a caution-genre task hard by adjusting the document's authority; the model never has to commit to a wrong affirmative claim.

## The existence proof: why KM02 produced a real sub-70 spread
KM02 worked (mean 59.3, tail to 0.30) because its genre put the model in COMPLETION mode: "finish this discharge SUMMARY." To complete the document of record, the model propagated a FABRICATED finding-like fact (a culture organism + sensitivity) stated in the draft. The failure was carrying a specific false FINDING forward, not approving an action and not a readiness judgment. Caution had a COST: a "complete" summary includes the section, so the model had to actively catch-and-strip the fabrication to pass, and most propagated it. The lesson transfers directly to KM03 v2.2.

Full v2.2 design strategy: `../build-phase-drafts/KM03-v2.2-strategy-draft.md`.
