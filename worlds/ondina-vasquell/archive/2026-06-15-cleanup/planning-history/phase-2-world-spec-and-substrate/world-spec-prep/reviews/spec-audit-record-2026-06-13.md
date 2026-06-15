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
| 6/13 deep audit | Section 3 used the older Quill-style seven-column file-plan shape and omitted explicit Source and Tool columns | 2.42, 2.85, 2.113 | Patched all 43 file rows to the current eight-column AutoQC shape: #, ID, Filename.type, Source, Tool, Reference File Origin, Description, Pearls, Traps, and Friction. Document rows now say Custom Built by Writer and DOCX Template; image rows now say Writer Produced Media and Writer Image Tool |

## Passes that returned clean

- DO-NOT-REPEAT fairness: Task 10 completion uses a true placeholder, asserts nothing on the scored item; Task 6 determination uses a different-author external concurrent-review request; no false closure in any same-author draft.
- No answer-key synthesis in world-level files: stated explicitly in Section 3, and every external severity-forward surface (coding worksheet, CDI query, payer denial, concurrent-review request, pharmacy rejection) is task-level.
- Trap fairness: every scored trap is chart-contradicted or chart-mandated, never chart-silent; the photo is substrate only.
- Self-containment: no task depends on public knowledge after July 31, 2025.
- File-plan row completeness: all 43 file rows include populated Source, Tool, Reference File Origin, Description, and Pearls, Traps, and Friction fields; media rows preserve final upload filenames.
- Trap substrate traceability (2.49): every Failure Design source maps to a World File Plan row.
- Formatting bans: zero em dashes, en dashes, arrows, asterisks; no letter-O PO token (routes written Oral); MM/DD/YYYY throughout; American English; name consistent.

## Disposition

The spec content passes the audit. Remaining before submission: Alexander ratifies the 51 RATIFY-flagged clinical values in the substrate pack; the spec DOCX is built by Mode A clone with the full gate chain; the reference templates and the World Spec Claude transcript are built; the upload manifest is assembled. No platform action is automated.

## Pass: clinical-voice / linguo + provenance (2026-06-12)

Trigger: "read logs and mention of clinical voice and linguo and make sure we are at par, avoid leakages and other mistakes made in km world."

Source of truth read: docs/clinical-voice-lessons.md (the 10 patterns + the "polish hurts" caution).

Findings:
- POLISH-HURTS / SYNTHESIS-LEAK scan of the spec: file-plan Description column stays descriptive; the only "weight incorrectly" phrase sits in the Pearls/Traps column, which is the spec's job. PASS.
- 1.3 Clinical History holds the discharge tension OPEN the way KM does (13x "unresolved", "stays unsafe", "operationally unsafe", "not yet", "still required"); no premature resolution of a scored decision. PASS.
- Leakage re-scan of the submission DOCX visible text: zero internal/benchmark/architecture register; banned chars (em/en dash, arrow, asterisk) = 0. PASS.
- Provenance bug CAUGHT and FIXED in 00-START-HERE.md: both the Brainstorm and World Spec DOCX entries carried the same stale SHA256 (b9a82f48...). Recomputed and corrected: Brainstorm e16934678722b523..., World Spec 4d96332b9dea55b4...; World Spec page-count corrected to 101 paras / 33 tables; Mode A fingerprint re-verified EMPTY vs KM base.

New supporting doc: phase-3-build-task-artifacts/clinical-voice-and-file-grammar-guide.md - locks the 10 voice patterns, native document grammar per file, trap-carrier "plainest prose" flags, and the DO-NOT-REPEAT build lessons onto the Phase 3 file build before authoring (the "Application for World #2" action the lessons call for).

## Pass: Source and Tool column rebuild (2026-06-13)

Trigger: deep Ondina catch-up audit before image generation.

Finding: the current v6.3 local AutoQC master requires every file-plan row to include Source and Tool. Ondina had inherited the older Quill seven-column table shape, which was exemplar-consistent but no longer checker-safe.

Fix: patched `submission/Ondina_Vasquell_World_Spec.md` Section 3 so all three file-plan tables use the current eight-column header. Rebuilt `submission/Alexander_World_Vasquell_latest_6_13.docx` with `tools/build/build-docx-ondina-worldspec.py`. Rebuild passed Mode A integrity and fingerprint against the approved KM base. Direct DOCX readback confirms the eight-column header appears in all three file-plan tables, Custom Built by Writer appears on 42 rows, Writer Produced Media and Writer Image Tool appear on the media rows, the stale Date plus Reference File Origin header appears zero times, and visible-text leakage terms AutoQC, RLS, Mercor, workspace, database, benchmark, synthetic, Codex, and Claude appear zero times. All XML parts have zero em dashes, en dashes, arrows, bullets, asterisks, brackets, Synthetic, SYNTHETIC, or python-docx. Final DOCX SHA256 after the EMR wording cleanup rebuild: 34632be5e71fefe3ec753119e5ea4be86ba8feb482792d84cd2bba95516a1b82.

## Pass: writer-produced media completion (2026-06-13)

EW30 and EW31 are complete from `phase-3-build-task-artifacts/codex-image-prompts.md`. Accepted copies are in both `phase-3-build-task-artifacts/synthetic-files/` and `phase-3-build-task-artifacts/world-files/`.

EW30 `wound_photo_05202026.jpg`: SHA256 2cb1eea1e4f1019b31568e475599723b2d08224aa578dc8d1e1f37487b207afa. Visual check confirms a plantar diabetic forefoot wound, no exposed bone, no visible joint, no identifiers, and no image-only answer to the osteomyelitis question. EXIF length is 0.

EW31 `abi_tbi_tracing_05192026.jpg`: SHA256 d0354413c690f53aae74ada2efd0de739c7acb84efafbaa92058873ca7ae4ef0. Visual check confirms raw ABI/TBI tracing with the synthetic Ondina EMR header, Ordered by Lillian Everet, MD, bilateral ankle PT and DP marked NC, bilateral ankle-brachial index noncompressible, toe values R 92 / 0.84 and L 55 / 0.50, no interpretation paragraph, and no revascularization language. EXIF length is 0.

Follow-up fix from the image audit: harmonized `abi_tbi_study_report_05192026.docx`, `vascular_consult_note_05192026.docx`, and the Phase 3 manifest to the image values of left toe pressure 55 mmHg and left TBI 0.50. Rebuilt world files and task files after removing non-clinical filed/register wording from DOCX content. Visible and XML leakage scans are clean across world-files, supplementary-files, task-files, and the World Spec DOCX.

## Pass: EMR result realism sync (2026-06-13)

Trigger: Alexander flagged that labs and radiology should look like native EMR artifacts with patient details, not generic summaries.

Fix: patched `phase-3-build-task-artifacts/build/clinical_data.py` so MRI, ABI/TBI, pathology, deep micro, superficial micro, renal trend, and inflammatory trend files carry realistic accession, order, specimen, collection, received, reported, ordering clinician, source, and report-status blocks while preserving the same clinical conclusions. Rebuilt world-files and supplementary-files with the current Epic chrome: masthead, blue rule, patient storyboard, patient/encounter block, clean header/footer, and `verify_no_km_identifiers`. Rebuilt task-files after header/footer scrub. Updated the ABI tracing image to match the report accession and synthetic patient header while leaving the perfusion interpretation open.
