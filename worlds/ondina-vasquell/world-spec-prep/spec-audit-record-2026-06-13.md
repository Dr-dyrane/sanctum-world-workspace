# World Spec Audit Record - 2026-06-13

Multi-pass audit of the Ondina Vasquell World Spec against workspace learnings, run before the DOCX build per Alexander's instruction. Source learnings: the brainstorm-submission log (the one AutoQC fail was the per-task priority label, now pre-satisfied), the AutoQC v6.3 113-check families, DO-NOT-REPEAT, the Abi nine-lens protocol, the KM Stacey and Sang and Abi corrections, and the docx-generation rules.

## Inherited brainstorm-submission lesson

The Ondina Brainstorm passed AutoQC after one fix: every task needed an explicit Priority P0 or P1 label. The spec carries Priority on all ten tasks from the start, so this class is pre-satisfied.

## Findings and fixes

| Pass | Finding | AutoQC / lesson | Fix |
|---|---|---|---|
| 1 structural | All ten tasks carry Workflow, Anchor, Capability, Priority, Difficulty, Time estimate, Expected Output, Failure Design, Task-level files, Draft Prompt | 2.28, 2.69, 2.78, 2.93 | None needed; verified 10/10 each |
| 1 structural | Each Failure Design has exactly 5 traps (matches the KM spec base) | 2.34 | None; meets the floor |
| 2 trap telegraph | Task 9 draft prompt told the model the answer: be fair about where the system failed rather than just the patient | 2.31 blocking | Removed the sentence |
| 2 trap telegraph | Tasks 2, 3, 4, 7 prompts carried mild trap-adjacent phrasing (disagree with the worksheet; push back where it does not; cannot safely go home yet; do not stretch to make a number) | 2.31 | Softened all four to neutral asks |
| 3 duplicate traps | Osteomyelitis recurs in Tasks 2 and 3, perfusion in Tasks 4, 6, 8, citing the same source files | 2.91 | Added shared world-level trap, primary in Task N markers to the secondary appearances |
| 4 workflow count | Spec used ten distinct workflows with no defense note (the brainstorm had one) | 2.107 | Added a workflow-count note to Section 2 and Note 4 to the 2c defenses |
| consistency | Big Picture file composition said 31 plus 6 plus 3 equals 40; Section 3 totals 31 plus 9 plus 3 equals 43 | 2.7, 2.45 | Corrected Big Picture to 43 |
| consistency | Three dates used in files were missing from Key Milestones: 03/15, 04/30, 05/23 | 2.22, 2.23 | Added milestone rows; table re-verified chronological |

## Passes that returned clean

- DO-NOT-REPEAT fairness: Task 10 completion uses a true placeholder, asserts nothing on the scored item; Task 6 determination uses a different-author external concurrent-review request; no false closure in any same-author draft.
- No answer-key synthesis in world-level files: stated explicitly in Section 3, and every external severity-forward surface (coding worksheet, CDI query, payer denial, concurrent-review request, pharmacy rejection) is task-level.
- Trap fairness: every scored trap is chart-contradicted or chart-mandated, never chart-silent; the photo is substrate only.
- Self-containment: no task depends on public knowledge after July 31, 2025.
- Trap substrate traceability (2.49): every Failure Design source maps to a World File Plan row.
- Formatting bans: zero em dashes, en dashes, arrows, asterisks; no letter-O PO token (routes written Oral); MM/DD/YYYY throughout; American English; name consistent.

## Disposition

The spec content passes the audit. Remaining before submission: Alexander ratifies the 51 RATIFY-flagged clinical values in the substrate pack; the spec DOCX is built by Mode A clone with the full gate chain; the reference templates and the World Spec Claude transcript are built; the upload manifest is assembled. No platform action is automated.
