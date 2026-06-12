# TASK9-STATE

## CURRENT (6/12): v2 AO correction is ready locally after the first review returned v1 for a missing original coding document. The active packet now includes exactly one task-level attachment, `him_preliminary_inpatient_coding_summary_05252026.docx`, so the requested physician coding addendum has a real preliminary coding document to addend. This is an external HIM worksheet, not a same-author physician draft. The model is fairly asked to accept, revise, or reject the worksheet against the chart.

Active local v2 files in `platform/task9/current/`:
- `prompt-task9-v2.txt`
- `him_preliminary_inpatient_coding_summary_05252026.docx`
- `golden-KM09-v2.docx`
- `grader-guidelines-task9-v2.txt`
- `RUN-INSTRUCTIONS-v2.md`

Design stance: keep the v1.1 central clinical axis. The correct addendum sequences `N39.0` urinary tract infection as principal, does not attest `A41.9` sepsis or `R65.2` severe sepsis, codes altered mental status only at symptom level, and rejects metabolic encephalopathy, acute-on-chronic systolic heart failure, organism-specific codes, and malnutrition as undocumented. The worksheet deliberately carries the severity-forward HIM framing so the model must refute unsupported coding, not merely fill a blank.

Build verification completed locally 6/12: Mode A clone from approved Epic UI artifacts, python-docx extraction including tables, core metadata scrubbed, styles.xml byte-identical to the base, fills and borders identical, no em dash, no en dash, no arrow in the v2 prompt/grader/run instructions/builder/generated DOCX text, and Quick Look rendered the worksheet and golden as one clean page each. The `Ilyana Rook` HIM author name does not collide with existing world or task files outside this v2 packet.

Studio mount gate for upload/pilot: first trajectory `find /docs` must show exactly one Task 9 task file under `/docs/filesystem`, `him_preliminary_inpatient_coding_summary_05252026.docx`. It must show no stale v1 prompt-facing task file, no golden, no grader, and nothing task-specific under `/docs/.apps_data`.

Abi-mode byte review 6/12: PASS with no blocking findings, recorded at `qa/KM09-v2-abi-mode-review-2026-06-12.md`. The only watch item is difficulty, not fairness: the HIM worksheet's open-items section names the scored decisions and may cue catchers. Keep it for the pilot; if v2 over-catches, the next revision should make the worksheet assert its codes more confidently and trim that open-items enumeration. The v2 preregistration is locked pre-pilot at `runs/KM09-v2-pilot-preregistration.md` and must not be edited after the pilot starts. v1.1 FA/GA and job `df5ba05c` are retired for submission purposes and remain difficulty evidence only.

[RECOVERY NOTE 6/10 late: this file, prompt-task9-v1.txt, grader-guidelines-task9-v1.txt, and the RUN-INSTRUCTIONS floor rules were truncated by an interrupted write during the v1.1 re-center pass; repaired 6/10 from the v1.0 parallel structure + v1.1 staged content. Grader final two blocks and this tail are reconstructions - Alexander's read-and-own pass must cover them verbatim. PREREG GAP FOUND AT AUDIT: runs/KM09-v1-pilot-preregistration.md preregisters the v1.0 MCC-central design and its read rules contradict v1.1 (it exempts simple-sepsis from flooring). v1.1 supersession draft staged at runs/KM09-v1.1-pilot-preregistration-DRAFT.md - Alexander must review and lock it BEFORE upload; v1 file kept unedited per the lock rule.]

Boundaries: no build/stage/upload/AutoQC/agent-run without explicit Alexander authorization for that exact step.
