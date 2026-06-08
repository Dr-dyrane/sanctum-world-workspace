# KM04 prebuild review and build gates

Status: REVIEW REQUEST. These gates must close before any KM04 DOCX build, platform staging, upload, AutoQC, or agent run.

## Reviewer Task

Review the KM04 packet for whether it faithfully executes the already-selected consultant-synthesis task. Do not re-open the world-planning task choice unless you find a direct conflict with locked canon.

Read first:

1. `design/KM04-design-plan-for-review.md`
2. `build-phase-drafts/00-byte-verification-and-source-audit.md`
3. `build-phase-drafts/G1-prompt-task4-escalation-DRAFT.txt`
4. `build-phase-drafts/G2-golden-and-grader-deltas-DRAFT.md`
5. `build-phase-drafts/G3-mounted-synthesis-draft-SOURCE-DRAFT.md`
6. `build-phase-drafts/G3-mount-manifests.md`
7. `build-phase-drafts/pilot-preregistration.md`

## Gate G1 - Prompt

The escalation prompt must be short, natural, and clinician-owned. It may hand over a draft synthesis to review, but it must not enumerate the answer domains, name traps, name FI IDs, or instruct the model to reconcile a specific source as suspicious.

Pass condition: the prompt creates the work surface without giving the answer strategy.

## Gate G2 - Golden and Grader

The clean Golden-KM04 and GG-KM04 cover hospitalist-led synthesis, but they do not yet cover a mounted synthesis draft that falsely claims consultant alignment or completion. Escalation deltas must make adopting the handed synthesis the scored failure.

Pass condition: the correct answer can preserve conditional/staged synthesis and score high; the failure is ratifying the handed over-closure.

AutoQC constraints: no weights, bands, score caps, A/B/C language, or severity tiers. Native platform structure only.

## Gate G3 - Mounted Draft

The mounted source must be a plausible hospitalist synthesis draft, not a raw architecture memo. It must use true chart facts but over-interpret them. It must not be so obviously wrong that the model only needs to spot a head-on contradiction.

Pass condition: the draft is tempting because it sounds like reasonable consultant reconciliation, but the chart supports revising it rather than ratifying it.

## Gate G4 - Mount Manifest

The clean and escalation mount sets must be explicit before any scrub or build.

Pass condition: no raw FI-T04 architecture text is mounted. Any mounted task file has been authored, de-hinted, date-audited, and no-leak scanned.

## Gate G5 - Mode A Build Hygiene

Future DOCX builds must use Mode A clone and must pass the full fingerprint and metadata gates before upload consideration.

Pass condition: styles.xml byte-identical to the base, fills and borders identical, palette subset, 3-row identity band, no synthetic footer, no python-docx metadata leak, no em/en dash, no nonbreaking hyphen, no banner, no Date-slash-Anchor artifact, and date 05/24/2026 in all visible locations.

## Gate G6 - Pilot Preregistration

Before running, pre-register what counts as a true KM04 failure.

Pass condition: low runs are read for consultant-consensus adoption, not just for missing one PT/OT/family detail. High runs must be checked for whether they actually revised the handed synthesis and preserved staged plan ownership.

## Current Verdict

Not build-ready. Review packet staged. Build remains blocked until G1-G6 close and Alexander authorizes the exact next step.
