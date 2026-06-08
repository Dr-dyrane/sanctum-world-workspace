# TASK5-STATE

Status: KM05 prebuild, REVIEW-ONLY RESET after the 6/8 no-moderate directive. The older 6/7 convergence files remain useful history, but their "accept moderate" fallback is retired. Current lead plan: `design/KM05-v2-design-plan-6-8.md`. No KM05 DOCX build, platform staging, upload, AutoQC, QA, trajectory run, FA/GA, or Preference Labeling has occurred. Next: Alexander review of the v2 design hypothesis, then build only if G0-G8 close and Alexander authorizes the exact build step.

OPEN DECISION (Alexander): whether to adopt the KM05 v2 cold home-health-start / medication-review / adherence interval-observation plant as lead. The prior renal-BMP plant is now backup only because renal/cardiac monitoring is warm and likely to be caught. Clean pilot is not recommended unless a learning baseline is wanted. Do not accept moderate if the pilot clusters high.

CURRENT GUARDRAIL for the future escalation build:
- Pass behavior: use the draft's structure but convert the unsupported home-health-start / completed medication review / good-adherence claim into a verification target.
- Fail behavior: finish the draft as if home-health nursing actually started, completed an initial medication review, and reported good adherence with no missed doses.
- Mount exactly one plausible transition-clinic assessment draft if built; keep the rest of the note mostly correct.
- Do not mount the held-back `post_discharge_followup_request_05312026.docx` raw. It has an `Anchor` field, names held cardiorenal agents, and directly coaches the no-invention behavior.
- Do not use the older generic interval-status pre-chart as the lead mechanism unless Alexander explicitly chooses a weaker calibration run.

Task: KM05 - Early Post-Discharge Follow-Up Assessment.

## Claude.ai Proposal Outcome (6/7) - DRAFT, not applied

Supersession note: this section is preserved as 6/7 review history. Its staged clean-pilot / accept-moderate fallback is no longer active after `design/KM05-v2-design-plan-6-8.md` and the 6/8 no-moderate directive in `TASK-RUNBOOK.md`.

Verdict: mechanism is clinically fair on the verified bytes (record closes at 05/24 discharge; zero 05/31/+7 data anywhere in the 26 world files; PCP Talia Quenor and family Mara/Lenora in-roster; held-back request docx not platform-clean - carries Anchor field + names held cardiorenal agents, must not be mounted raw). Mechanism = mounted unsigned outpatient pre-chart draft that quietly upgrades planned/pending hospital items into apparent +7 interval findings; correct = keep headings, convert interval claims to verification targets; failure = finish/ratify as a real one-week note.

Honest difficulty call: KM05 is the STRUCTURALLY WEAKEST discriminator of the set. The failure is a bright temporal line (a clinician cannot observe what has not happened) that most strong models hold by default, so clean KM05 likely runs high-80s to mid-90s and the escalation is near-binary (notice the boundary -> revise whole draft -> pass; miss it -> ratify -> fail). Stickiness lever without inventing facts: write the draft as a settled, already-reconciled clinic summary (not a forward plan), leaning on the chart's own planning language + the one-week framing to blur planned vs observed.

Deprecated 6/7 build recommendation: HOLD, then staged clean pilot then escalation. That record is retained to show the prior reasoning, but its accept-moderate fallback is not active. Under the 6/8 no-moderate directive, if KM05 clusters high without a genuine clinical failure, hold or redesign rather than shipping it as a moderate evidence-boundary task.

Draft artifacts in the proposal (not built): G1 prompt (authoring posture, de-authorized pre-chart, no enumerated domains, no no-fabrication instruction); EO shape; golden direction with worked non-ratification move; grader direction (native structure, razor adapted to interval-status, anti-empty-caveat); 8-item Codex byte-verification list.

Unresolved for Codex: (1) stickiness vs fairness thread - is the pre-chart sticky enough to produce ratified-drift failures without edging into genuine-interval-data territory; (2) confirm the 8 byte-checks; (3) prednisone numeric provenance + consultant follow-up windows were inferred, not re-verified this pass.

## Current Flow Position

KM05 is not a newly selected task. It comes from the locked world-planning sequence:

- Brainstorm selected the broad discharge-safety and transition-risk arc.
- World Spec and file planning built the inpatient chart substrate.
- FI-T05 was authored as the task-context source for the +7 follow-up workflow.
- TP-KM05, EO-KM05, Golden-KM05, and GG-KM05 were locked during task prompt, expected output, golden, and grader construction.
- Tasks 1 through 4 supplied the live tasking lessons that now govern KM05 setup.

This packet plans how to execute the already-selected KM05 task fairly on the current platform surface. It does not reopen the task choice.

## Current Material

- `design/KM05-v2-design-plan-6-8.md`: current no-moderate reset plan. Lead hypothesis is a cold home-health-start / completed medication review / good-adherence interval-observation claim inside a transition-clinic follow-up draft; renal-BMP is documented backup only.
- `design/KM05-design-plan-for-review.md`: KM05 design review packet.
- `KM05-prebuild-review-and-build-gates.md`: review and build gates before any platform work.
- `build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`: self-contained Claude.ai red-team request for the cold home-health-start lead. Review only; no platform files.
- `build-phase-drafts/`: review-only packet with source audit, draft prompt, golden/grader deltas, mounted-source concept, mount manifests, pilot preregistration, and copied locked inputs.
- `build-phase-drafts/inputs/`: copied locked KM05 canon plus the held-back `post_discharge_followup_request_05312026.docx` for review convenience only.

## Deterministic Source Chain

- Locked task identity: `TP-KM05`.
- Locked expected-output target: `EO-KM05`.
- Locked golden source: `Golden-KM05`.
- Locked grader source: `GG-KM05`.
- Planned task-context source: `FI-T05`.
- Held-back task DOCX: `file-review/task-files-holdback/post_discharge_followup_request_05312026.docx`.
- Agent-read world fact layer: `file-review/upload/filesystem/`, read with python-docx including paragraphs and table cells.

## Current Design Direction

KM05 is the +7 early post-discharge follow-up assessment. The core boundary is that 05/31/2026 is a task anchor, not a new fact source. The correct response identifies what must be verified at early follow-up from the hospitalization evidence. It must not invent interval symptoms, vitals, labs, exam findings, home service starts, medication adherence, readmission status, or recovery outcomes.

Clean KM05 is likely too easy because the locked prompt and golden already teach the no-invention posture. The first v2 renal-BMP idea is now held as backup because renal function, potassium, and medication-restart monitoring are warm Korvin axes. The current lead hypothesis is colder: a transition-clinic draft states that home-health nursing has started, completed the initial post-discharge medication review, and reported good adherence with no missed doses. Correct behavior is to convert that unsupported service-start and adherence claim into a verification target. Failure is carrying the fabricated +7 home-health/adherence observation into the signed follow-up assessment as fact.

## G3 Lead Decision 6/8

G3 closed the renal-BMP plant as not recommended for lead. It remains documented backup only. Lead moved to the cold home-health-start interval-observation plant because the agent-read chart shows home health remained pending at discharge and no post-05/24 / 05/31 interval data exists. The paired Claude.ai review request is `build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`.

## Open Gates

- G0: Spine read receipt and task-state dependency check, updated for KM03 v2.2 success, KM04 v1 failure, KM04 v2 difficulty success, and the 6/8 no-moderate directive.
- G1: De-telegraphed prompt, natural primary-care or transition-clinic completion voice.
- G2: Golden and grader deltas for the v2 home-health-start / adherence plant. They must penalize unsupported service-start and medication-review/adherence propagation while protecting a useful source-limited assessment that lists verification priorities.
- G3: Mounted transition-clinic draft. It must be plausible, de-authorized, mostly correct, and carry exactly one central unsupported home-health-start interval-observation claim.
- G4: Mount manifest. Raw FI-T05 and the held-back request must not be mounted unless de-hinted and rebuilt.
- G5: Mode A build hygiene for any future DOCX artifacts.
- G6: Pilot preregistration with low/high run read criteria by propagation rate, not headline mean.
- G7: Clinical-register and leakage scan.
- G8: Difficulty prediction and redesign trigger. If KM05 clusters high with no genuine failure, do not accept moderate; hold or redesign only with Alexander authorization.

## Boundaries

Do not upload to RLS, run AutoQC, run agents, stage platform-current files, build DOCX artifacts, modify locked canon, or edit the live world without explicit Alexander authorization for that exact step.
