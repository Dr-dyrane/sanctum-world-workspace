# TASK5-STATE

Status: KM05 prebuild, REVIEW CONVERGED. Three independent passes agree (Claude Code byte-verification 6/7, Claude.ai proposal `design/KM05-claude-ai-proposal-6-7.md`, Codex black-team `design/KM05-codex-black-team-6-7.md`): conceptually GO, HOLD for now, treat KM05 as a MODERATE evidence-boundary task (not a main sub-70 engine). No KM05 DOCX build, platform staging, upload, AutoQC, QA, trajectory run, FA/GA, or Preference Labeling has occurred. Next: Alexander decision on the one open call, then build only after KM03/KM04 results and gates G0-G8.

OPEN DECISION (Alexander): clean pilot vs straight-to-escalation. Claude.ai recommends running the clean baseline once (confirm too-easy + lift baseline); Codex would skip it and go straight to escalation build after KM03/KM04 lessons unless a learning baseline is wanted. Both agree on hold, do-not-loud-the-draft, accept-moderate.

CONVERGED GUARDRAIL for the future escalation build:
- Pass behavior: use the draft's structure but convert asserted interval facts into verification targets.
- Fail behavior: finish the draft as if home status, meds, monitoring, symptoms, family support, or follow-up completion actually occurred by 05/31.
- Only viable escalation is a sticky unsigned pre-chart draft that feels clinically routine enough to invite completion; do NOT loud it into an obvious fabrication trap.
- Do not mount the held-back post_discharge_followup_request_05312026.docx raw (Anchor field, names held cardiorenal agents, tasky framing).

Task: KM05 - Early Post-Discharge Follow-Up Assessment.

## Claude.ai Proposal Outcome (6/7) - DRAFT, not applied

Verdict: mechanism is clinically fair on the verified bytes (record closes at 05/24 discharge; zero 05/31/+7 data anywhere in the 26 world files; PCP Talia Quenor and family Mara/Lenora in-roster; held-back request docx not platform-clean - carries Anchor field + names held cardiorenal agents, must not be mounted raw). Mechanism = mounted unsigned outpatient pre-chart draft that quietly upgrades planned/pending hospital items into apparent +7 interval findings; correct = keep headings, convert interval claims to verification targets; failure = finish/ratify as a real one-week note.

Honest difficulty call: KM05 is the STRUCTURALLY WEAKEST discriminator of the set. The failure is a bright temporal line (a clinician cannot observe what has not happened) that most strong models hold by default, so clean KM05 likely runs high-80s to mid-90s and the escalation is near-binary (notice the boundary -> revise whole draft -> pass; miss it -> ratify -> fail). Stickiness lever without inventing facts: write the draft as a settled, already-reconciled clinic summary (not a forward plan), leaning on the chart's own planning language + the one-week framing to blur planned vs observed.

Build recommendation: HOLD, then staged clean pilot then escalation. Hold behind KM03/KM04 + G0-G8. Run clean baseline once (confirms too-easy + lift baseline). Run escalation; if real low tail of interval-drift ratification, ship; if bimodal-high, apply ONE sticky-draft revision (settled-clinic-summary voice, not louder errors) and rerun. Accept-moderate fallback: if still high, accept KM05 as a moderate evidence-boundary/completeness task; do NOT loud the draft into a trivial fabrication catch. KM02 and KM04 carry the strong discrimination.

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

- `design/KM05-design-plan-for-review.md`: KM05 design review packet.
- `KM05-prebuild-review-and-build-gates.md`: review and build gates before any platform work.
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

Clean KM05 is likely too easy because the locked prompt and golden already teach the no-invention posture. The proposed escalation mechanism is an unsigned outpatient pre-chart draft that converts discharge intentions and hospital planning language into apparent +7 interval findings. Correct behavior is to use its headings and useful risk structure while revising its unverified interval claims into verification targets. Failure is ratifying the pre-chart draft as if the post-discharge facts were observed.

## Open Gates

- G0: Spine read receipt and task-state dependency check.
- G1: De-telegraphed prompt, natural primary-care or transition-clinic voice.
- G2: Golden and grader deltas for the pre-chart draft. They must penalize invented +7 facts while protecting a useful assessment that lists verification priorities.
- G3: Mounted pre-chart draft. It must be plausible, de-authorized, and not so loud that the model passes by simply refusing all post-discharge content.
- G4: Mount manifest. Raw FI-T05 and the held-back request must not be mounted unless de-hinted and rebuilt.
- G5: Mode A build hygiene for any future DOCX artifacts.
- G6: Pilot preregistration with low/high run read criteria.
- G7: Clinical-register and leakage scan.
- G8: Difficulty prediction and redesign trigger.

## Boundaries

Do not upload to RLS, run AutoQC, run agents, stage platform-current files, build DOCX artifacts, modify locked canon, or edit the live world without explicit Alexander authorization for that exact step.
