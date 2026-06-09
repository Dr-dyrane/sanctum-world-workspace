# KM05 prebuild review and build gates

Status: REVIEW REQUEST. These gates must close before any KM05 DOCX build, platform staging, upload, AutoQC, QA, or agent run.

## Reviewer Task

Review whether the KM05 packet faithfully executes the already-selected early post-discharge follow-up task. Do not re-open the world-planning task choice unless you find a direct conflict with locked canon.

Read spine first:

1. `project/STATUS.md`
2. `project/WORKSPACE_FILE_MAP.md` Navigation Rule
3. `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
4. `worlds/korvin-merrow/task-setup/KM-RETROSPECTIVE-tasks1-2.md`
5. `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`
6. `worlds/korvin-merrow/task-setup/task4/TASK4-STATE.md`
7. `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md`

Then read the KM05 packet:

1. `design/KM05-design-plan-for-review.md`
2. `build-phase-drafts/00-byte-verification-and-source-audit.md`
3. `build-phase-drafts/G1-prompt-task5-escalation-DRAFT.txt`
4. `build-phase-drafts/G2-golden-and-grader-deltas-DRAFT.md`
5. `build-phase-drafts/G3-mounted-followup-draft-SOURCE-DRAFT.md`
6. `build-phase-drafts/G3-mount-manifests.md`
7. `build-phase-drafts/pilot-preregistration.md`

## Gate G0 - Spine Read Receipt And Dependency Check

No KM05 build or platform step may begin until the reviewer or builder records a read receipt.

Read receipt must state:

- files read from the workspace spine and KM05 packet
- active state of KM01, KM02, KM03, KM04, and KM05
- current forbidden actions
- three no-repeat lessons from KM01 through KM04
- whether KM03/KM04 run results have returned and what they imply for KM05

Pass condition: the builder proves they are using current repo state, not memory.

## Gate G1 - Prompt

The escalation prompt must be short, natural, and clinician-owned. It may ask the model to review a pre-chart draft and return a follow-up assessment, but it must not enumerate the answer domains, name traps, name FI IDs, or say "do not fabricate" in a way that gives away the entire task.

Pass condition: the prompt creates a realistic outpatient transition-clinic work surface without giving the answer strategy.

Clinical-register constraint: the platform prompt must not use internal design vocabulary such as `forced slot`, `trap`, `friction`, `locked`, `architecture`, `FI-W`, or `source-of-truth`.

## Gate G2 - Golden And Grader

Clean Golden-KM05 and GG-KM05 cover source-limited follow-up priorities, but they do not yet cover a mounted pre-chart draft that overstates interval facts. Escalation deltas must make ratifying unverified post-discharge facts the scored failure.

Pass condition: a correct source-limited follow-up assessment can score high, and a response that documents invented +7 findings or completed services can score low.

AutoQC constraints: no weights, bands, score caps, A/B/C language, or severity tiers. Native platform structure only.

## Gate G3 - Mounted Draft

The mounted source must be a plausible outpatient pre-chart or transition-clinic draft, not raw FI-T05 and not an architecture memo. It must use true hospital-risk structure but over-interpret planned or pending items as known +7 status.

Pass condition: the draft is tempting because it looks like a helpful clinic note shell, but the chart supports revising it into verification targets rather than ratifying it as interval history.

Hypothesis kill-chain:

- Would a real PCP clinic or transition team plausibly create this pre-chart?
- Which exact agent-read DOCX files rebut the interval-status overclaim?
- Is the failure evidence-boundary judgment rather than simple refusal to write?
- Is the plant quiet enough that it does not look like an obvious fabrication test?
- Can a correct response reuse headings and risk domains while rejecting the unverified findings?
- What should a high-scoring catch run say, and what should a low-scoring propagation run say?

## Gate G4 - Mount Manifest

Clean and escalation mount sets must be explicit before any scrub or build.

Pass condition: no raw FI-T05 architecture text is mounted. The held-back `post_discharge_followup_request_05312026.docx` must not be mounted unless it is de-hinted, date-audited, Mode A rebuilt, and reviewed again.

## Gate G5 - Mode A Build Hygiene

Future DOCX builds must use Mode A clone and pass fingerprint and metadata gates before upload consideration.

Pass condition: styles.xml byte-identical to the base, fills and borders identical, palette subset, 3-row identity band, no synthetic footer, no python-docx metadata leak, no em/en dash, no nonbreaking hyphen, no banner, no Date-slash-Anchor artifact, and correct visible date handling.

## Gate G6 - Pilot Preregistration

Before running, pre-register what counts as a true KM05 failure.

Pass condition: low runs are read for ratifying unverified +7 facts, not merely for missing one monitoring domain. High runs must be checked for whether they actually preserve the evidence boundary while producing a useful follow-up assessment.

## Gate G7 - Clinical Register And Leakage

Before any platform-facing artifact is staged, scan prompt, golden, grader, mounted note, README, and run instructions for workspace or architecture leakage.

Pass condition: final-facing prose reads as clinical work, not project design. Internal terms may remain only in internal review files.

## Gate G8 - Difficulty Prediction

Before upload consideration, record the empirical prediction for KM05.

Pass condition: the packet states the expected wrong move, why a strong model would make it, why the chart fairly rebuts it, what score pattern would indicate a working discriminator, and what result would force redesign.

## Current Verdict

Not build-ready. Review packet staged. Build remains blocked until G0-G8 close and Alexander authorizes the exact next step.
