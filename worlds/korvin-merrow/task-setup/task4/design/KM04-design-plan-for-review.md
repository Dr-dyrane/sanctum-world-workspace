# KM04 consultant synthesis design plan for review

Status: PREBUILD REVIEW PACKET. No DOCX build, no platform staging, no RLS upload, no AutoQC, and no agent run. This packet is for Alexander, Claude, Codex, or reviewer critique before any one-way build step.

Task: KM04 = Consultant Synthesis / Interdisciplinary Care Plan, discharge anchor 05/24/2026, hospitalist-led interdisciplinary team requester. Locked canon: TP-KM04, EO-KM04, Golden-KM04, GG-KM04, FI-T04.

This plan does not ask Alexander to re-choose the task. The task was already selected during world planning. The review question is narrower: how to execute KM04 so it is realistic, faithful to the locked world, and adversarial enough to measure the intended consultant-synthesis capability.

## Settled Task Identity

KM04 is the consultant-synthesis task. Its locked task prompt asks for a hospitalist-led interdisciplinary care plan that reconciles Cardiology, Nephrology, Endocrinology, family concerns, functional evidence, objective trends, MAR actions, and the discharge-facing snapshot. The locked expected output and golden both require hospitalist synthesis rather than consultant deference.

The correct answer is not "pick Cardiology," "pick Nephrology," "pick Endocrinology," "follow family," or "copy FI-W22." The correct answer is a staged, source-aware, owner-aware plan that preserves uncertainty where the chart leaves it unresolved.

## Verified Source Findings

Primary verification layer: agent-read DOCX files under `worlds/korvin-merrow/file-review/upload/filesystem/`, read with python-docx including table cells. The detailed source audit lives at `../build-phase-drafts/00-byte-verification-and-source-audit.md`.

Finding 1: Cardiology and Nephrology are both reasonable. Cardiology warns against silently losing chronic HFrEF/CAD protection. Nephrology warns against full simultaneous restart based on improving creatinine alone. The MAR shows partial inpatient action, not a final outpatient restart plan.

Finding 2: Endocrinology and the primary team are both reasonable in different lanes. Endocrinology treats chronic steroid exposure and unclear taper as a risk substrate. The primary team correctly avoids declaring adrenal insufficiency proven because the patient improved with infection, renal, volume, and supportive management. Rheumatology remains the source for intended PMR taper history.

Finding 3: Objective trends and MAR actions inform synthesis but do not settle it. The trend summary explicitly is not a medication restart authorization or disposition decision. The MAR is an inpatient action record, not the discharge medication list.

Finding 4: Functional, family, nursing, and care-management evidence remain clinically material. PT recommends rolling walker and supervised mobility. OT documents reproducible medication-management errors. Nursing documents persistent difficulty with multi-step medication questions. Family gives baseline evidence and supervision constraints. CM/SW says services, equipment, transport, pharmacy logistics, caregiver scope, and teach-back ownership remain under coordination.

Finding 5: FI-W22 is useful but seductive. It says anticipated discharge on 05/24/2026, home with services under coordination, but it also says final medication reconciliation, education, services, equipment, and transportation remain pending. It is not a completed answer file.

Finding 6: Raw FI-T04 is not platform-clean. It contains architecture labels, trap names, friction labels, source-of-truth safeguards, FI IDs, and answer-shaped synthesis bullets. The Step 10 packet already calls E1-T4 the worst offender. Do not mount FI-T04 raw.

## Discriminator

Clean KM04 is likely high-scoring because the chart gives a strong model the synthesis map. The deliverable asks for consultant reconciliation, and the chart repeatedly says "both sides are reasonable, preserve uncertainty." A clean run may still be useful as calibration, but it is not enough as the main difficulty mechanism.

The proposed KM04 forced slot is a consultant-consensus overclaim.

Mounted input: one plausible hospitalist synthesis draft, dated to 05/24/2026, written in attending-review or resident-draft register. It claims the consultant tensions have been reconciled and the interdisciplinary plan is ready to proceed. It should sound balanced and use true improvement facts, but it should over-close the actual uncertainty.

Primary planted error: the draft converts "can be sequenced and coordinated" into "consultants are aligned and the plan is ready." It treats improving creatinine, potassium, blood pressure, intake, MAR status, and FI-W22 as enough to finalize cardiorenal sequencing, steroid instructions, functional support, and transition logistics.

Correct behavior: revise the draft, decline to ratify the consensus claim, preserve staged cardiorenal sequencing, preserve steroid-source uncertainty, integrate PT/OT/nursing/family/CM evidence, and name owners or follow-up for unresolved items.

Failure behavior: adopt the handed synthesis as if consultant alignment is complete and discharge-facing logistics are settled.

## Why This Is Fair

The mounted draft should not invent new facts. It should over-interpret true facts:

- Creatinine returned near baseline and potassium improved.
- Carvedilol was cautiously resumed.
- Patient is eating better and ambulating more.
- FI-W22 says anticipated discharge on 05/24/2026.
- Consultants each provide a plausible lane.

The rebuttal is reachable in the same chart:

- Nephrology does not clear full simultaneous restart.
- Cardiology does not declare unilateral restart safe.
- Endocrinology does not prove adrenal insufficiency or write a final outpatient taper.
- Rheumatology anchors taper intent but not actual recent adherence.
- PT/OT/nursing/family/CM all preserve functional and transition conditions.
- FI-W22 itself leaves multiple elements pending.

The task therefore measures consultant-synthesis judgment and authority-deference, not obscure recall or a fabricated contradiction.

## Loud vs Quiet Claims

The quiet, load-bearing plant should be the consensus-wash: "the consultants have effectively aligned, so the plan can be signed." That is the KM04-native failure.

The loud claims should be kept limited. A full home-dose restart of every held medication, a numeric prednisone dose from a refill, or a "no services needed" declaration may become too obvious and collapse the task into simple chart-reading. Those can be secondary edges, but the primary discriminator should remain over-ratification of a polished synthesis draft.

## Honest Prediction

Clean KM04 likely scores high. It may still discriminate on completeness, but not enough for the deepest synthesis target.

Escalated KM04 should be stronger than KM03 because the deliverable is reconciliation itself. The model cannot pass by saying "conditional readiness" alone. It must decide whether to use, revise, or reject a handed synthesis. The number remains empirical: run, read transcripts, then decide whether the planted closure is fair and clinically significant.

## Build Sequence When Authorized

1. Confirm KM03 run state and any new pod guidance before starting KM04 build.
2. Finalize the escalation frame from this packet after Alexander/reviewer input.
3. Write the escalation prompt in short clinician voice, with no domain checklist.
4. Author the mounted synthesis draft source and pass it through fairness/no-leak review.
5. Extend golden and grader for the mounted draft. Do not alter locked clean canon.
6. Build DOCX artifacts only by Mode A clone. Task DOCX base: approved KM02 task draft or genre-appropriate held-back base. Golden base: golden-KM02-v5.
7. Date audit all artifacts to 05/24/2026 after any framing change.
8. Verify styles.xml byte-identical, fills/borders identical, palette subset, 3-row identity band, no synthetic footer, no python-docx metadata leak, no em/en dash, no Date-slash-Anchor artifact, no trap/meta words.
9. Run clean baseline only if still useful for calibration. Run escalation as the actual difficulty test. Read low and high transcripts before FA/GA.

## Attach For Review

- This file.
- `../KM04-prebuild-review-and-build-gates.md`.
- `../build-phase-drafts/README-context-for-claude.md`.
- `../build-phase-drafts/00-byte-verification-and-source-audit.md`.
- Drafts G1-G3 and pilot preregistration under `../build-phase-drafts/`.
- Locked inputs copied under `../build-phase-drafts/inputs/`.
