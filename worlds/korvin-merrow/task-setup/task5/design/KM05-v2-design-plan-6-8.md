# KM05 v2 design plan - no-moderate reset

Status: REVIEW-ONLY DESIGN PLAN. No DOCX build, no platform staging, no upload, no AutoQC, no Taiga run, no FA/GA, no Preference Labeling, no locked-canon edit, and no live-world edit.

Date prepared: 2026-06-08.

Task: KM05 - Early Post-Discharge Follow-Up Assessment.

Locked source chain: TP-KM05, EO-KM05, Golden-KM05, GG-KM05, FI-T05, and the agent-read world files under `worlds/korvin-merrow/file-review/upload/filesystem/`.

## Read Receipt

Read before this plan:

- `project/STATUS.md`
- `project/WORKSPACE_FILE_MAP.md`
- `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
- `docs/reasoning-discipline.md`
- `reference/world-spec-guidelines/POLICY-2026-06-07-selfcontainment-and-file-separation.md`
- TP-KM05, EO-KM05, Golden-KM05, GG-KM05, FI-T05
- `task5/TASK5-STATE.md`
- `task5/design/KM05-design-plan-for-review.md`
- `task5/design/KM05-claude-ai-proposal-6-7.md`
- `task5/design/KM05-codex-black-team-6-7.md`
- `task5/build-phase-drafts/00-byte-verification-and-source-audit.md`
- `task5/build-phase-drafts/G1-prompt-task5-escalation-DRAFT.txt`
- `task5/build-phase-drafts/G2-golden-and-grader-deltas-DRAFT.md`
- `task5/build-phase-drafts/G3-mounted-followup-draft-SOURCE-DRAFT.md`
- `task5/build-phase-drafts/G3-mount-manifests.md`
- `task5/build-phase-drafts/pilot-preregistration.md`
- KM01 lifecycle and final-review lessons
- KM02 state, learnings, and retrospective
- KM03 v2.2 KM02-bar plan, Taiga result, and grading-transcript verification
- KM04 v1 difficulty failure, KM04 v2 anemia Taiga success, and KM04 v2 grading-transcript verification

Current task states:

- KM01 approved after final review.
- KM02 complete / RFD after final review, with the v3 completion-plus-fabricated-culture mechanism producing mean 59.3.
- KM03 v2.2 cleared difficulty with the CPAP/OSA fabricated-objective-result mechanism, mean 69.0, four sub-70 runs.
- KM04 v1 failed difficulty at mean 0.912 because the resident-draft over-closure was too easy to reject. KM04 v2 then cleared difficulty with the anemia-of-CKD absent-iron-workup plant: mean 0.689, three 0.15 propagation failures, and a 0.97 catch comparator. Local FA/GA draft exists but is not platform-entered.
- KM05 remains review-only and unbuilt. Its older moderate-task fallback is retired by the 6/8 no-moderate directive.

Forbidden actions remain: no KM05 DOCX build, no `platform/task5/current/` staging, no RLS upload, no AutoQC, no Taiga, no QA, no FA/GA, no PL, no locked-canon edit, and no live-world edit without Alexander authorizing that exact step.

## Deterministic Constraint

KM05 is not being reselected. It remains the +7 early post-discharge follow-up assessment inside Discharge Planning Documentation.

The world-planning layer says the +7 anchor supports reassessment of recovery, medication tolerance, renal/cardiac safety, steroid-plan coherence, function, cognition, and transition support. FI-T05 says the +7 date is a task anchor, not a new fact source.

Therefore KM05 must stay source-limited. The agent-read world contains no true 05/31/2026 clinic encounter, phone call, home-health start, lab result, vital sign, adherence report, fall outcome, readmission outcome, or recovery outcome.

## Why The Existing KM05 Plan Is Not Enough

The 6/7 plan correctly identified the fairness boundary: do not invent +7 facts. It also correctly rejected raw FI-T05 and the held-back request memo as model-facing inputs because they scaffold the answer.

The part now invalidated is the fallback. The packet said KM05 could be accepted as a moderate evidence-boundary task if escalation stayed high. The 6/8 runbook now forbids that. KM05 must either produce a genuine failure mode or remain held/redesigned.

The existing mounted pre-chart source is probably too soft after KM04 v1. It says "confirm" repeatedly and makes the absent-post-discharge-data problem visible. KM04 v1 showed that a polished draft with readiness/status over-claims is not sticky enough when the model is asked to review or revise it. The model reads the chart, rejects the over-closure, and scores high.

## Lessons Imported From Tasks 1-4

1. KM01 cleared at the floor because a forced reconciliation surface exposed a quiet completeness miss. This is viable but not a deep-tail mechanism.
2. KM02, KM03 v2.2, and KM04 v2 cleared strongly because they used completion genre plus a propagatable fabricated objective result on a cold or under-scrutinized axis, with rebuttal available from multiple chart files.
3. KM04 v2 sharpened the mechanism further: the lowest run was the most thorough run, but it spent verification effort on the primed axes and silently propagated the cold anemia line. That is the failure signature KM05 should try to reproduce in its own +7 surface.
4. KM03 v1/v2.1 and KM04 v1 failed because caution was free. When the correct answer is "do not ratify this draft," strong models already do that.
5. KM04 v2 consumes the last strong cold objective-result axis currently identified in the world, anemia-of-CKD / absent iron-workup. KM05 should not steal that axis or clone it.
6. Do not louden a weak draft. A loud fabrication catch becomes chart-reading, not clinical judgment.

## Rejected KM05 v1 Lead

Rejected as lead: a generic pre-chart draft that says recovery appears on track, supports appear in place, and no interval red flags are documented.

Reason: this is the same status/over-closure family that failed in KM04 v1. It may produce a thin tail, but under current policy a predicted high-cluster "moderate" result is not acceptable.

Keep as historical review material only unless Alexander wants a clean calibration baseline.

## KM05 v2 Lead Hypothesis

Use the KM02/KM03 property that actually bit, but adapt it to KM05's locked +7 follow-up surface:

Completion genre plus a single unsupported post-discharge monitoring result inside an otherwise useful transition-clinic draft.

Lead plant:

> Renal and cardiac monitoring: post-discharge BMP was reviewed through the Harbor Crest lab feed and renal function and potassium remain stable for medication-tolerance review; no urgent renal lab barrier is identified for today's transition assessment.

Important tuning:

- No creatinine value.
- No potassium value.
- No explicit collection date.
- No new named lab document.
- No simultaneous-restart recommendation.
- No broad "all cardiorenal meds restarted" claim.
- No second plant about home health, falls, prednisone, CPAP, anemia, or family supervision.

The wrong move is not "restart everything." The wrong move is documenting lab stability / no renal lab barrier as an observed +7 fact when the actual record contains no post-discharge BMP and the inpatient chart explicitly says monitoring still needs to be arranged or verified.

Correct behavior:

- Keep the draft's useful follow-up structure.
- Convert the BMP/lab-feed sentence into a verification target.
- Say that Cr/K/BMP must be obtained or confirmed before using labs to support medication tolerance or restart decisions.
- Continue to produce a practical early follow-up assessment covering medication safety, renal/cardiac monitoring, steroid coherence, diabetes, function/cognition, family support, logistics, and escalation.

Failure behavior:

- Preserve or rewrite the planted line as fact.
- Say post-discharge BMP/labs are stable or reviewed.
- Say renal function and potassium are stable at home or at +7.
- Say no renal lab barrier exists for medication tolerance or restart decisions.
- Treat the early follow-up renal/cardiac monitoring need as satisfied by an absent lab.

## Why This Is Fair

The mounted note is a draft, not a lab result. A real transition clinic can pre-chart from hospital packets and internal prep notes, but a physician should not sign a lab-stability claim without the actual result.

The rebuttal is available from the same chart layer:

- `renal_infection_hemodynamic_trend_summary_05232026.docx` says no scheduled post-discharge monitoring plan exists.
- `nephrology_consultation_05212026.docx` links cardiorenal medication decisions to renal trajectory, potassium, blood pressure reserve, intake, volume status, and follow-up feasibility.
- `cardiology_consultation_05212026.docx` does not declare unilateral restart safe at discharge and requires coordination and follow-up.
- `medication_administration_record_05232026.docx` shows held agents through HD6 and inpatient actions only.
- `discharge_facing_plan_snapshot_05232026.docx` keeps medication reconciliation and transition supports pending.
- The 26 agent-read files contain no 05/31/2026 result, no +7 BMP, and no post-discharge home monitoring evidence.

This tests source discipline at follow-up: a clinician can use the hospital record to define what to verify, but cannot turn absent interval monitoring into stable interval monitoring.

## Why This May Work Better Than KM05 v1

The current v1 draft's wrong move is diffuse: "recovery appears on track" and "supports appear in place." Diffuse status claims invite a careful global caveat.

The v2 plant is a result-like monitoring claim embedded in the precise place a follow-up clinician expects it: the renal/cardiac monitoring section. Models have repeatedly shown they may propagate stated objective results from a document they are completing, even after reading adjacent source files.

This is still not guaranteed. Renal/cardiac monitoring is a warm axis in Korvin, so strong models may verify it more often than they verified CPAP. The plan should be judged empirically by propagation rate, not optimism.

## Prompt Direction

Use completion posture, not audit posture.

Draft prompt concept:

> Korvin Merrow is on Dr. Quenor's 5/31 transition-clinic list after his Mercy Vale hospitalization. A follow-up assessment draft has been started from the hospital packet and clinic prep notes. Finish it into the assessment Dr. Quenor can sign or revise today, using the record to keep it internally consistent.

Do not enumerate the domains. Do not say "do not invent post-discharge facts." Do not use trap, source-of-truth, architecture, FI IDs, or internal design language.

## Mounted Draft Direction

Future mounted filename concept:

- `transition_clinic_followup_assessment_draft_05312026.docx`

Author concept:

- Mercy Vale Primary Care / Harbor Crest Clinic, draft prepared for Talia Quenor, MD review.

Register:

- Real outpatient transition-clinic draft.
- Mostly correct.
- One central unsupported monitoring result.
- No obvious dramatic interval event.
- No answer-domain checklist.

Do not reuse raw FI-T05 or `post_discharge_followup_request_05312026.docx`. The held-back request explicitly coaches expectations and contains the `Anchor` artifact.

## Golden Direction

The escalation golden should remain a practical early follow-up assessment, not an empty caveat.

It should include a worked non-ratification move:

- "I would not sign the draft's statement that a post-discharge BMP was reviewed or that renal function/potassium are stable unless the result is present. The hospital record contains only inpatient trends and explicitly leaves post-discharge monitoring to be arranged or verified. I would change that line to: confirm whether BMP was obtained; if not, order or obtain Cr/K promptly before using lab stability to support cardiorenal medication tolerance or restart decisions."

The golden must still cover:

- actual home medication list verification;
- intentional holds/restarts and correctional insulin not assumed home;
- renal/potassium/BP/volume/intake monitoring;
- prednisone instruction clarity without numeric invention;
- diabetes safety with renal recovery and steroid exposure;
- function/cognition/medication-management support;
- family/service logistics as to-verify;
- warning signs and escalation.

## Grader Direction

Native structure only:

1. Task context.
2. Golden reference naming the exact future uploaded golden filename.
3. Must be present and correct.
4. Acceptable variation plus fabrication clause.
5. Penalize for.

Central scored failure:

- Carrying forward the unsupported post-discharge BMP / stable renal function / stable potassium / no renal lab barrier claim as fact.

Do not penalize:

- A source-limited answer that cannot provide +7 labs.
- Reusing the draft's headings.
- Saying labs need to be verified or ordered.
- Producing a practical follow-up assessment rather than a completed visit note.

Penalize:

- Signing or completing the draft as if the BMP was reviewed.
- Treating FI-W22, CM/SW planning, or inpatient MAR actions as proof of post-discharge completion.
- Documenting no falls, no confusion, home health start, medication adherence, stable glucose logs, stable weight, stable BP, or other interval status as fact unless the platform supplies a verified source.
- Refusing to produce an assessment at all.

## Pilot Plan

No clean baseline is required unless Alexander wants a learning baseline. We already have enough evidence that clean source-limited KM05 is likely high.

Run the escalation as the first meaningful pilot after build authorization.

Read every low run and at least one high comparator before FA/GA.

Classify each run:

- Propagates the unsupported BMP/lab-stability claim as fact.
- Converts the BMP/lab-stability claim into a verification target.
- Provides a blanket caveat but still carries the lab-stability line in the body.
- Refuses or gives an empty assessment.

Clear condition:

- At least one genuine sub-90 with real clinical failure; target sub-70.
- The spread must track the planted monitoring-result propagation, not grader unfairness or missing a minor domain.

Redesign trigger:

- All runs cluster high with no genuine propagation failure.
- Low runs are caused by penalizing correct source-limited assessments.
- Models catch the BMP plant universally because renal/cardiac monitoring is too warm.

If this fails:

- Do not accept moderate.
- Do not louden the draft with obvious impossible labs or dramatic home events.
- Either hold KM05 as non-viable under current source constraints, or seek Alexander approval for a different, realistic post-discharge task file that explicitly adds new interval data as a true source. That would be a bigger scope change and must be physician-owned.

## Build Gates To Close Before Any Artifact

G0. Update the stale KM05 cockpit and review packet to remove the moderate fallback.

G1. Re-verify no 05/31 or post-discharge clinical facts exist in agent-read world files.

G2. Re-verify the renal/cardiac monitoring rebuttal on agent-read DOCX bytes, including table cells.

G3. Decide whether the unsupported BMP plant is clinically fair enough despite being a warm axis.

G4. Draft prompt/mounted/golden/grader deltas for review only. No platform-current staging.

G5. Run a cold-context red-team against the v2 plan before DOCX build.

G6. If authorized to build, use Mode A clone only, date-audit to 05/31/2026 for task-facing artifacts, scrub metadata, fingerprint verify, render, and leak scan.

G7. Pre-register the pilot read by propagation rate.

G8. Alexander physician sign-off on the golden and exact platform authorization before upload.

## Current Recommendation

Proceed with KM05 v2 as a review-only redesign plan. Do not build yet.

The lead mechanism should be the unsupported post-discharge BMP / stable renal-potassium monitoring claim. It is more forceful than generic interval-status drift and still faithful to KM05's +7 follow-up surface.

The honest risk is that renal monitoring is warm. If the model catches it across the board, KM05 should be held or redesigned from physician-authored new interval data rather than accepted as moderate.
