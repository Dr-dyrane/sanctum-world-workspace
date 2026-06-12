# TASK9-STATE

## CURRENT (6/12): v2 has piloted cleanly after AO returned v1 for a missing original coding document. Job `8ca908b5-183e-413b-b27a-974ea80084c4` scored 20, 20, 15, 15, 92, 15, 20, 15, 85, 25, mean 24.2. The first trajectory mount showed the intended task file once under `/docs/filesystem`, with no task-specific `.apps_data` copy. FA/GA is drafted from Attempt 6, run `a7259530-4336-4882-a950-09deac504264`, score 0.15.

Active local v2 files in `platform/task9/current/`:
- `prompt-task9-v2.txt`
- `him_preliminary_inpatient_coding_summary_05252026.docx`
- `golden-KM09-v2.docx`
- `grader-guidelines-task9-v2.txt`
- `RUN-INSTRUCTIONS-v2.md`

Design stance: keep the v1.1 central clinical axis. The correct addendum sequences `N39.0` urinary tract infection as principal, does not attest `A41.9` sepsis or `R65.2` severe sepsis, codes altered mental status only at symptom level, and rejects metabolic encephalopathy, acute-on-chronic systolic heart failure, organism-specific codes, and malnutrition as undocumented. The worksheet deliberately carries the severity-forward HIM framing so the model must refute unsupported coding, not merely fill a blank.

Pilot result: v2 is a clean reseed candidate. Eight runs fall below 70. Attempt 5 scored 0.92 and Attempt 9 scored 0.85, proving reachability. The selected floor, Attempt 6, read the chart well enough to reject severe sepsis, metabolic encephalopathy, acute-on-chronic heart failure, organism coding, and symptom-level AMS, but still upgraded the principal diagnosis to `A41.9` sepsis and assigned the septicemia family. The grader appropriately scored this 0.15.

Build verification completed locally 6/12: Mode A clone from approved Epic UI artifacts, python-docx extraction including tables, core metadata scrubbed, styles.xml byte-identical to the base, fills and borders identical, no em dash, no en dash, no arrow in the v2 prompt/grader/run instructions/builder/generated DOCX text, and Quick Look rendered the worksheet and golden as one clean page each. The `Ilyana Rook` HIM author name does not collide with existing world or task files outside this v2 packet.

Studio mount gate: PASSED on v2 job `8ca908b5`. First trajectory `find /docs` showed exactly one Task 9 task file under `/docs/filesystem`, `him_preliminary_inpatient_coding_summary_05252026.docx`, with no task-specific `.apps_data` copy and no golden in the agent-visible set.

Abi-mode byte review 6/12: PASS with no blocking findings, recorded at `qa/KM09-v2-abi-mode-review-2026-06-12.md`. The v2 preregistration is locked pre-pilot at `runs/KM09-v2-pilot-preregistration.md` and must not be edited after the pilot starts. The v2 result record is `runs/KM09-v2-results-and-prereg-reconciliation.md`. v1.1 FA/GA and job `df5ba05c` are retired for submission purposes and remain difficulty evidence only.

[RECOVERY NOTE 6/10 late: this file, prompt-task9-v1.txt, grader-guidelines-task9-v1.txt, and the RUN-INSTRUCTIONS floor rules were truncated by an interrupted write during the v1.1 re-center pass; repaired 6/10 from the v1.0 parallel structure + v1.1 staged content. Grader final two blocks and this tail are reconstructions - Alexander's read-and-own pass must cover them verbatim. PREREG GAP FOUND AT AUDIT: runs/KM09-v1-pilot-preregistration.md preregisters the v1.0 MCC-central design and its read rules contradict v1.1 (it exempts simple-sepsis from flooring). v1.1 supersession draft staged at runs/KM09-v1.1-pilot-preregistration-DRAFT.md - Alexander must review and lock it BEFORE upload; v1 file kept unedited per the lock rule.]

Boundaries: no platform FA/GA entry, AutoQC, preference labels, final review, or submission without explicit Alexander authorization for that exact step.
