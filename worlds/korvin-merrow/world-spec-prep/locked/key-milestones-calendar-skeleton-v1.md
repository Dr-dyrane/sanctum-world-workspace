# Key Milestones Calendar Skeleton v1

Date created: 2026-05-31

Status: LOCKED.

Purpose: establish the canonical date framework for World Spec construction. This is the single timeline source of truth for admission timeline, HD1-HD6 progression, world snapshot, discharge anchor, +7 day anchor, +30 day anchor, future file dates, future task dates, temporal gate compliance, and trap date-lock compliance.

This artifact does not draft World Spec sections, create a file inventory, create task architecture, create milestones with clinical content, create templates, create reference files, write prompts, create golden responses, create grader guidance, or generate synthetic files.

## Calendar Selection Rule

The calendar uses a fictional May-June 2026 timeline. Korvin Merrow's DOB is 1964-02-18, so he is 62 throughout all dates below.

All future World Spec dates should inherit from this skeleton. If any future construction step needs a new date, add it to the Key Milestones framework first so AutoQC 2.22 and 2.23 remain auditable.

Locked doctrine: +7 and +30 anchors are measured from the discharge anchor on 05/24/2026. They are not measured from HD6 world close.

## Pre-Admission Timeline

| Anchor | Date | Relative Timing | Scope |
| --- | --- | --- | --- |
| Approximate decline begins | 2026-04-27 / 04/27/2026 | About 3 weeks before admission | Pre-admission decline window begins. |
| Final pre-admission week begins | 2026-05-11 / 05/11/2026 | 7 days before admission | Late pre-admission window. |
| Day before presentation | 2026-05-17 / 05/17/2026 | 1 day before admission | Final pre-admission day. |

## Admission And Hospital Day Structure

| Hospital Day | Date | Framework Role |
| --- | --- | --- |
| HD1 | 2026-05-18 / 05/18/2026 | ED presentation and admission date. |
| HD2 | 2026-05-19 / 05/19/2026 | Inpatient hospital day 2. |
| HD3 | 2026-05-20 / 05/20/2026 | Inpatient hospital day 3. |
| HD4 | 2026-05-21 / 05/21/2026 | Inpatient hospital day 4. |
| HD5 | 2026-05-22 / 05/22/2026 | Inpatient hospital day 5. |
| HD6 | 2026-05-23 / 05/23/2026 | Inpatient hospital day 6 and world snapshot day. |

## World Snapshot

| Anchor | Timestamp | Rule |
| --- | --- | --- |
| World snapshot / world close | 2026-05-23 18:00 / 05/23/2026 18:00 | The World closes on HD6 at 18:00 during discharge planning. No world file may be dated after this timestamp unless Alexander explicitly reopens the snapshot rule. |

## Post-Snapshot Anchors

| Anchor | Date | Relationship To Snapshot | Use |
| --- | --- | --- | --- |
| Discharge anchor | 2026-05-24 / 05/24/2026 | After HD6 18:00 world close | Earliest post-snapshot discharge-facing anchor. |
| +7 day anchor | 2026-05-31 / 05/31/2026 | 7 days after discharge anchor, not world close | Post-discharge follow-up anchor. |
| +30 day anchor | 2026-06-23 / 06/23/2026 | 30 days after discharge anchor, not world close | Later safety/readmission-review anchor. |

## Temporal Consistency Review

### VERIFIED

Finding: the skeleton preserves the ratified 6-day hospitalization.

Evidence: HD1 is 05/18/2026 and HD6 is 05/23/2026.

Impact: the date framework matches the ratified temporal architecture.

Action required: future World Spec construction should not extend the world beyond HD6 18:00 without explicit physician authorization.

### VERIFIED

Finding: the world snapshot is exact.

Evidence: world close is fixed at 05/23/2026 18:00.

Impact: supports AutoQC 2.41 by creating a definite world snapshot timestamp.

Action required: all future task anchors must fall after 05/23/2026 18:00.

### VERIFIED

Finding: post-snapshot anchors are separated from the world close.

Evidence: discharge anchor is 05/24/2026, +7 day anchor is 05/31/2026, and +30 day anchor is 06/23/2026.

Impact: supports post-world task anchoring without placing tasks inside the world timeline.

Action required: future tasks may use these anchors only after task architecture is authorized.

### VERIFIED

Finding: DOB and age remain consistent.

Evidence: Korvin Merrow was born 1964-02-18 and is 62 on all dates from 04/27/2026 through 06/23/2026.

Impact: supports AutoQC 2.100 readiness.

Action required: do not move the calendar outside the age-62 window unless Alexander explicitly reopens DOB or age.

### PLAUSIBLE

Finding: the pre-admission decline window satisfies the approximately 3-week decline requirement.

Evidence: 04/27/2026 is 21 days before HD1 on 05/18/2026.

Impact: supports the ratified clinical story without adding clinical content.

Action required: later clinical narrative can inherit this timing when World Spec drafting is authorized.

### NO ISSUE

Finding: orphan milestone risk is controlled at skeleton stage.

Evidence: every date in the skeleton has an explicit framework role. No extra dates are introduced.

Impact: supports AutoQC 2.23 readiness.

Action required: when future construction adds dates for files, tasks, or narrative, each date must be represented here or in the final Key Milestones table and referenced elsewhere.

### NO ISSUE

Finding: AutoQC 2.22 readiness is preserved.

Evidence: the skeleton is the intended canonical date source for future spec dates.

Impact: future spec dates can be checked against this framework.

Action required: before World Spec upload, verify every date in filenames, task anchors, narrative, and trap timing appears in the final Key Milestones table.

### DISPUTED

Finding: none.

Evidence: no date in this skeleton conflicts with the approved Brainstorm, ratified Clinical Story Skeleton, locked Identity Package, or ratified Governance Package.

Impact: no calendar redesign required.

Action required: none.

## Final Status

Key Milestones Calendar Skeleton v1

Status: LOCKED
