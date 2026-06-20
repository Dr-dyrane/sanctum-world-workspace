# Coach brainstorm pass: review and reconciliation, 2026-06-20

Transcript (platform record): https://claude.ai/share/5ed6be5f-6c9f-4293-b8e8-e83aac16e621
Assembled brainstorm (Coach output): worlds/marva-lydell/reviews/Brainstorm_Marva_Lydell.docx
Governed brainstorm (submitted record): worlds/marva-lydell/submission/Marva_Lydell_Brainstorm.md
Governed spec: worlds/marva-lydell/submission/Marva_Lydell_World_Spec.md

## What the Coach did

Ran the brainstorm in the veteran path, assembled it into the four-element template, and walked its GO/SEND-BACK list plus the full pre-submission AutoQC checklist, cross-checking every task against its live workflow list. The assembly is faithful to our submitted brainstorm: same world setup, the same six frictions, the same nine traps, the same ten tasks. It added a synthetic MRN (MB-6820374), the real submission date (06/20/2026), an in-world document date (07/18/2025), and a world-file-kinds preview paragraph. It kept the submitted brainstorm's original workflow strings and tiers and validated all ten against its live list as on-list, available, and tier-correct.

## Convergence with our own spec verification

The Coach audit and our independent spec verification agree, and most of what the Coach flagged we had already handled when building the spec:

- Task 9 physician-voice: the Coach says reframe the HEDIS abstraction to the physician reviewer's overread and attestation. ALREADY DONE in the spec (physician-completed and attested, signed by the attending as the abstracting reviewer).
- Tasks 5 and 8 physician-voice: the Coach says confirm physician authorship. ALREADY SO in the spec: Task 5 is the hospitalist attending coordinating with case management, Task 8 is the patient safety officer (Dr. Naismith, a physician).
- Tasks 1 and 7 overlap: the Coach soft-flags it; our verification subagent judged them genuinely distinct; the spec differentiates them (Task 1 leads on exertional oxygen and equipment, Task 7 on stairs, medication complexity, and home support).
- Task 8 bounceback supplied as a task-level input, not a carryover: ALREADY SO in the spec (E1-T8 safety-event and readmission intake).

Net: the Coach pass confirms the spec is sound. No new spec fix arises from the voice or overlap items.

## Brainstorm versus spec divergences (expected, recorded)

- Workflow strings and tiers: the brainstorm transcript keeps the original strings (six P0, four P1: Task 2 Medication Reconciliation P0, Task 6 Specialty Consultation Note P1, Task 10 CDI Query Response Review P1). The spec applies Larry's locks (Task 2 Discharge Medication Reconciliation P0, Task 6 Specialist Referral Letter and Documentation Preparation P0, Task 10 CDI Query Response Review P0), giving eight P0 and two P1. Spec-to-brainstorm divergence is legitimate; the submitted brainstorm record is preserved and the corrections land in the spec. The Coach used the originals because its stale endpoint lacks Larry's lanes, which is the expected behavior we documented.
- MRN: the Coach placeholder is MB-6820374; the spec uses ML-7782304, which follows our world-prefix convention (matching OV's OV-3358104). The spec's MRN governs.

## The one open decision: the timeline (the Coach's hard blocker)

The Coach flags the mid-2025 timeline as a hard date-check failure. Its reasoning: the agent's medical-knowledge freeze is about July 2025, the AutoQC gate fails any date on or after 07/01/2025, and the binding point is the latest task anchor (Task 9 on 07/17/2025). It proposes shifting the whole timeline back about three weeks (snapshot about 06/19, anchors 06/20 to 06/26, document date about 06/27). June is still mid-2025, so the design intent holds and not one clinical detail changes, only the calendar.

Assessment: the Coach is right, and this updates our earlier "keep July, the Coach is stale" lean. The cutoff is a structural project rule (it appears in the World Spec curriculum and as a pre-submission AutoQC dimension), not a Coach quirk. The OV-2026 precedent does not protect W3: OV's later dates are an unverified risk, not a blessing, and several OV tasks are still in review. And the fix is genuinely costless: a uniform 21-day-earlier shift moves every date and every filename datestamp back, changes no clinical content, and clears the gate with margin (latest anchor 06/26, before 06/30). Recommendation: shift the spec timeline back 21 days, re-verify, re-commit. Hold the July dates only if Larry or the project confirms the model under test has a later knowledge cutoff.

### Proposed 21-day shift map (if approved)
- Pre-admission: 06/20/2025 to 05/30/2025; 06/22/2025 to 06/01/2025
- Admission and stay: 07/04 to 06/13 (HD1) through 07/10 to 06/19 (HD7, snapshot)
- Snapshot: 07/10/2025 18:00 to 06/19/2025 18:00
- Task anchors: 07/11 to 06/20, 07/12 to 06/21, 07/13 to 06/22, 07/15 to 06/24, 07/16 to 06/25, 07/17 to 06/26
- In-world document date: 07/18/2025 to 06/27/2025

RESOLVED 2026-06-20: Dyrane approved the shift. Applied to the spec as a uniform 21-day move and re-verified clean (47 rows, all dates in Key Milestones, no world file after the 06/19 snapshot, all anchors after it, latest anchor 06/26 before the cutoff, no dashes). The spec now runs snapshot 06/19/2025 with anchors 06/20 to 06/26. The submitted brainstorm and this transcript keep the original July dates as the record; the corrected calendar lives in the spec.
