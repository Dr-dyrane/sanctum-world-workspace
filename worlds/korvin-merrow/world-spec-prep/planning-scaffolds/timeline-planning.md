# Timeline Planning

## Already Locked From Brainstorm

- Multi-day hospitalization begins in the ED.
- World closes on Hospital Day 6 at 18:00 during discharge planning.
- Task anchors:
  - Task 1: Hospital Day 7
  - Task 2: Hospital Day 7
  - Task 3: Hospital Day 7
  - Task 4: 7 days after discharge
  - Task 5: Hospital Day 7
  - Task 6: 30 days after discharge

## Needs Physician Decision

- Calendar date for Hospital Day 1 and world close, if required.
- Whether discharge occurs on Hospital Day 7 or remains only planned at the world close.
- Exact timing of ED arrival, admission, consultant notes, lab trends, medication holds/restarts, PT/nursing observations, family communications, and discharge planning.
- Which timeline events carry traps versus ordinary context.

## Source-Of-Truth Rule

- Every date referenced in tasks, traps, files, filenames, prompts, or clinical history must appear in Section 1.4 Key Milestones.
- Tasks must occur strictly after the latest world file timestamp.
- Tasks are independent branch encounters, not a single shared future timeline.

## Reviewer / AutoQC Risk

- Hospital-day-only timing may be insufficient once filenames and prompts require date stamps.
- A task anchored before or during world files will fail.
- Consultant recommendation traps require clear timestamps and clinical context, not just latest-note logic.

