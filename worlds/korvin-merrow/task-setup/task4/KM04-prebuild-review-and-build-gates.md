# KM04 prebuild review and build gates

Status: REVIEW REQUEST. These gates must close before any KM04 DOCX build, platform staging, upload, AutoQC, or agent run.

## Reviewer Task

Review the KM04 packet for whether it faithfully executes the already-selected consultant-synthesis task. Do not re-open the world-planning task choice unless you find a direct conflict with locked canon.

Read spine first:

1. `project/STATUS.md`
2. `project/WORKSPACE_FILE_MAP.md` Navigation Rule
3. `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
4. `worlds/korvin-merrow/task-setup/KM-RETROSPECTIVE-tasks1-2.md`
5. `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`
6. `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`
7. `worlds/korvin-merrow/task-setup/task4/TASK4-STATE.md`

Then read the KM04 packet:

1. `design/KM04-design-plan-for-review.md`
2. `build-phase-drafts/00-byte-verification-and-source-audit.md`
3. `build-phase-drafts/G1-prompt-task4-escalation-DRAFT.txt`
4. `build-phase-drafts/G2-golden-and-grader-deltas-DRAFT.md`
5. `build-phase-drafts/G3-mounted-synthesis-draft-SOURCE-DRAFT.md`
6. `build-phase-drafts/G3-mount-manifests.md`
7. `build-phase-drafts/pilot-preregistration.md`

## Gate G0 - Spine Read Receipt And KM03 Dependency

No KM04 build, platform staging, upload, AutoQC, or agent run may begin until the reviewer or builder records a read receipt.

Read receipt must state:

- files read from the workspace spine and KM04 packet
- active state of KM01, KM02, KM03, and KM04
- current forbidden actions
- three no-repeat lessons from KM01 through KM03
- whether KM03 trajectory/QA results have returned and what they imply for KM04

Pass condition: the builder proves they are using the current repo state, not memory. If KM03 trajectory/QA results are still pending, KM04 may remain in critique/prebuild refinement only.

## Gate G1 - Prompt

The escalation prompt must be short, natural, and clinician-owned. It may hand over a draft synthesis to review, but it must not enumerate the answer domains, name traps, name FI IDs, or instruct the model to reconcile a specific source as suspicious.

Pass condition: the prompt creates the work surface without giving the answer strategy.

Clinical-register constraint: the platform prompt must not use internal design vocabulary such as `source-aware`, `forced slot`, `overclaim`, `trap`, `friction`, `locked`, `architecture`, `FI-W`, or `source-of-truth`. It should sound like a real hospitalist request.

## Gate G2 - Golden and Grader

The clean Golden-KM04 and GG-KM04 cover hospitalist-led synthesis, but they do not yet cover a mounted synthesis draft that falsely claims consultant alignment or completion. Escalation deltas must make adopting the handed synthesis the scored failure.

Pass condition: the correct answer can preserve conditional/staged synthesis and score high; the failure is ratifying the handed over-closure.

AutoQC constraints: no weights, bands, score caps, A/B/C language, or severity tiers. Native platform structure only.

## Gate G3 - Mounted Draft

The mounted source must be a plausible hospitalist synthesis draft, not a raw architecture memo. It must use true chart facts but over-interpret them. It must not be so obviously wrong that the model only needs to spot a head-on contradiction.

Pass condition: the draft is tempting because it sounds like reasonable consultant reconciliation, but the chart supports revising it rather than ratifying it.

Hypothesis kill-chain:

- Would a real resident or hospitalist plausibly write this document?
- Which exact agent-read DOCX files rebut the over-closure?
- Is the failure consultant-synthesis judgment rather than simple chart-reading?
- Is the planted error quiet enough that it does not look like an obvious error-hunting target?
- Can a correct response reuse true parts of the draft while rejecting the consensus/completion claim?
- What should a high-scoring catch run say, and what should a low-scoring propagation run say?

KM04-specific watch: the medication-restart paragraph must not become so loud that the task collapses into spotting unsafe medication restart. The quieter discriminator is over-ratifying a polished consultant synthesis as ready for sign-off when the chart still requires staged hospitalist ownership.

## Gate G4 - Mount Manifest

The clean and escalation mount sets must be explicit before any scrub or build.

Pass condition: no raw FI-T04 architecture text is mounted. Any mounted task file has been authored, de-hinted, date-audited, and no-leak scanned.

## Gate G5 - Mode A Build Hygiene

Future DOCX builds must use Mode A clone and must pass the full fingerprint and metadata gates before upload consideration.

Pass condition: styles.xml byte-identical to the base, fills and borders identical, palette subset, 3-row identity band, no synthetic footer, no python-docx metadata leak, no em/en dash, no nonbreaking hyphen, no banner, no Date-slash-Anchor artifact, and date 05/24/2026 in all visible locations.

## Gate G6 - Pilot Preregistration

Before running, pre-register what counts as a true KM04 failure.

Pass condition: low runs are read for consultant-consensus adoption, not just for missing one PT/OT/family detail. High runs must be checked for whether they actually revised the handed synthesis and preserved staged plan ownership.

## Gate G7 - Clinical Register And Leakage

Before any platform-facing artifact is staged, scan prompt, golden, grader, mounted note, README, and run instructions for workspace or architecture leakage.

Pass condition: final-facing prose reads as clinical work, not project design. Internal terms may remain only in internal review files. Platform-facing files must use natural chart/request language, correct facility-style header, identity band where appropriate, date 05/24/2026, and appropriate signature/authorship blocks.

## Gate G8 - Difficulty Prediction

Before upload consideration, record the empirical prediction for the task.

Pass condition: the packet states the expected wrong move, why a strong model would make it, why the chart fairly rebuts it, what score pattern would indicate a working discriminator, and what result would force redesign. Build quality alone is not enough.

## Current Verdict

Not build-ready. Review packet staged. Build remains blocked until G0-G8 close, KM03 results are reviewed for inheritance, and Alexander authorizes the exact next step.
