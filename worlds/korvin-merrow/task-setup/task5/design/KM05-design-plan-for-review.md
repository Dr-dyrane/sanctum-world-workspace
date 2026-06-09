# KM05 early post-discharge follow-up design plan for review

Status: PREBUILD REVIEW PACKET. No DOCX build, no platform staging, no RLS upload, no AutoQC, no QA, and no agent run. This is for Alexander, Claude, Codex, or reviewer critique before any one-way task step.

Task: KM05 = Early Post-Discharge Follow-Up Assessment, +7 anchor 05/31/2026, primary-care or transition-team requester. Locked canon: TP-KM05, EO-KM05, Golden-KM05, GG-KM05, FI-T05.

This plan follows the full workspace flow. KM05 originated in brainstorm and world planning, was represented in the World Spec and file ecosystem, received FI-T05 as its task-context source, and now inherits the lived tasking lessons from KM01 through KM04. The review question is not "which task should Task 5 be?" The review question is how to execute the locked +7 follow-up task so it is realistic, self-contained, fair, and adversarial enough.

## Settled Task Identity

KM05 asks for an early post-discharge follow-up assessment based on the locked hospitalization evidence. The +7 date is a follow-up anchor, not evidence that a clinic visit, phone call, labs, home services, medication adherence, or recovery outcome happened.

The correct answer is a transition-risk surveillance assessment. It should identify what the outpatient clinician must verify early: medication list accuracy, renal and potassium monitoring, HFrEF/CAD and diabetes medication status, prednisone instruction clarity, functional recovery, cognition, family supervision, service logistics, warning signs, and escalation path.

The correct answer is not a completed clinic note with new findings. It must not invent interval symptoms, exam findings, vitals, labs, service starts, adherence, readmission status, or successful recovery.

## Verified Source Findings

Primary verification layer: agent-read DOCX files under `worlds/korvin-merrow/file-review/upload/filesystem/`, extracted with python-docx including table cells. The detailed source audit lives at `../build-phase-drafts/00-byte-verification-and-source-audit.md`.

Finding 1: No agent-read world file contains true post-discharge +7 clinical facts. The world closes at HD6 05/23/2026 18:00, with anticipated discharge on 05/24/2026. KM05's 05/31/2026 anchor is a task date only.

Finding 2: The hospitalization creates a strong follow-up substrate. Baseline function/cognition, three-week decline, near-fall, infection physiology, AKI on CKD, HFrEF/CAD holds, diabetes complexity, steroid uncertainty, functional/cognitive deficits, and family/care-management concerns all support early follow-up.

Finding 3: Medication follow-up is necessary but unresolved by the inpatient record. The MAR shows many held agents through HD6, consultants support staged reassessment, and FI-W22 says medication reconciliation remains pending. The follow-up should verify the actual home list rather than assume a final list exists in the chart.

Finding 4: Steroid follow-up is about source coherence, not a hidden diagnosis. Rheumatology anchors taper intent without a numeric dose; refill history and family/patient report are insufficient alone; Endocrinology flags risk but does not prove adrenal insufficiency.

Finding 5: Function, cognition, family supervision, and services remain live transition issues. PT recommends a rolling walker and early supervision; OT documents reproducible medication-management errors; nursing notes slower multi-step medication reasoning; family asks for clear supervision expectations; CM/SW and FI-W22 show services and logistics under coordination rather than complete.

Finding 6: The held-back `post_discharge_followup_request_05312026.docx` is not platform-clean as-is. It contains an `Anchor` field, lists held cardiorenal agents by name, and directly instructs the steroid no-invention behavior. It is useful provenance, but it should not be mounted raw.

## Discriminator

Clean KM05 is likely high-scoring. A strong model can read the prompt and the locked chart and say, correctly, that no +7 facts exist and that the note should identify follow-up priorities. That is clinically correct but may not create a strong failure mode.

The proposed KM05 forced slot is a pre-chart / transition-clinic draft that over-converts hospital discharge intentions into apparent +7 interval findings.

Mounted input concept: one unsigned outpatient pre-chart draft for Dr. Talia Quenor's review, dated 05/31/2026. It uses true hospital-risk domains and plausible clinic headings, but it treats unverified post-discharge status as if it were known. It might say the patient appears to be following expected trajectory, home supports appear in place, medication reconciliation is ready to finalize, no interval red flags are documented, and the visit can be closed as routine if no new issues arise.

Correct behavior: revise the draft into a source-limited early follow-up assessment. Keep useful headings and risk domains, but convert unverified claims into questions or verification targets.

Failure behavior: ratify or finish the pre-chart draft as an actual +7 clinic note, documenting unobserved stability, no falls, no worsening confusion, medication adherence, home health start, lab stability, service completion, or prednisone clarity as if observed.

## Why This Is Fair

The mounted draft should not create a secret fact the model is expected to know. It should over-interpret true planning facts:

- FI-W22 anticipates home discharge with services under coordination.
- CM/SW has referrals and logistics in process.
- PT/OT/nursing/family show improvement plus residual risks.
- Consultants outline follow-up needs.
- The PCP or transition clinic could plausibly pre-chart from a hospital packet.

The rebuttal is reachable from the same record:

- No agent-read file after 05/23 18:00 gives post-discharge interval findings.
- FI-W22 explicitly says key items are pending.
- CM/SW is not a service authorization or final disposition order.
- The MAR and consultant notes do not create a final outpatient medication list.
- The prednisone dose and taper remain source-sensitive.

This tests evidence-boundary discipline and outpatient transition reasoning, not hidden medical knowledge or a secret external guideline.

## Loud vs Quiet Claims

The quiet load-bearing plant should be the "interval status drift": planned or pending hospital items are written as if they are known +7 facts.

Avoid making the draft too loud with obviously impossible new labs, a named readmission, or a fully normal exam. Those would turn the task into a simple fabrication catch. The strongest draft should look like a real outpatient pre-chart: plausible, helpful, and wrong only because it silently upgrades unverified planning assumptions into findings.

## Honest Prediction

Clean KM05 likely scores high, roughly high-80s to mid-90s, because the correct uncertainty posture is strongly signaled.

Escalated KM05 should be viable but probably less powerful than KM02 and KM04 unless the pre-chart draft is sticky. Expected escalation target after review: mean roughly 62 to 72 with a real low tail if some runs ratify unverified interval facts. If most runs simply refuse all post-discharge content and produce useful verification priorities, the task will run high and need a subtler draft. If lows come only from docking correct source-limited assessments, the grader is unfair and must be revised.

## Build Sequence When Authorized

1. Confirm KM03/KM04 current state and any pod guidance before building.
2. Finalize the escalation frame after Alexander/reviewer input.
3. Write a short clinician-owned prompt with no answer-domain checklist.
4. Author the mounted pre-chart draft source and pass it through fairness/no-leak review.
5. Extend golden and grader for the mounted draft. Do not alter locked clean canon.
6. Build DOCX artifacts only by Mode A clone.
7. Date audit all artifacts to 05/31/2026 where task-facing, while preserving chart dates such as DOB and hospitalization dates.
8. Verify styles.xml byte-identical, fills/borders identical, palette subset, 3-row identity band, no synthetic footer, no python-docx metadata leak, no em/en dash, no Date-slash-Anchor artifact, no trap/meta words.
9. Run clean baseline only if useful for calibration. Run escalation as the actual difficulty test. Read low and high transcripts before FA/GA.

## Attach For Review

- This file.
- `../KM05-prebuild-review-and-build-gates.md`.
- `../build-phase-drafts/README-context-for-claude.md`.
- `../build-phase-drafts/00-byte-verification-and-source-audit.md`.
- Drafts G1-G3 and pilot preregistration under `../build-phase-drafts/`.
- Locked inputs copied under `../build-phase-drafts/inputs/`.
