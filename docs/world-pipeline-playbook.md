# World Pipeline Playbook (post-Korvin, for future stages and future worlds)

Date: 2026-06-04. Written at Korvin Merrow spec-submission (108/109, prednisone-by-design). Two purposes: (1) what happens next for Korvin, (2) the repeatable recipe for World #2+.

## A. Korvin: forward pipeline (stages 7-17)

Current position: Step 5 complete (Spec AutoQC), Step 6 complete (Human Spec Review APPROVED by Stacey S). The engineering pipeline run / synthetic generation is in progress externally; the workspace is awaiting the platform stage "Ready for Pipeline Fixes."

| Stage | What happens | Workspace surface | Our head start |
|---|---|---|---|
| 6 Human Spec Review | GO or SEND BACK | reviews/ + remediation/ if needed | reviewer-response-protocol.md exists; remediation pattern proven |
| 7 Synthetic Generation | Engineering builds world files from spec + our 33 templates | QA Folder (Drive) | Templates are content-complete, not just boilerplate |
| 8 World AutoQC | Automated file integrity check | QA Folder/AutoQC | - |
| 9 Writer Reviews Files (platform stage: "Ready for Pipeline Fixes" - writer reviews AND edits generated files directly) | Verify traps survived generation: prednisone ambiguity intact, EW22 reassuring-but-incomplete, buried EW17-EW19 evidence, consultant note DATES correct; minor issues edited in place, major issues sent back for regeneration. BILLABLE: log Insightful time from this stage onward. | new: worlds/korvin-merrow/file-review/ | Trap-substrate map = file-inventory matrices + Failure Design anchors |
| 10 Task Setup in RLS | Upload task prompts, goldens, grader guidelines | Task-level Folder subfolders (already created) | TP-KM01-06, EO-KM01-06, Golden-KM01-06, GG-KM01-06 ALREADY DRAFTED AND LOCKED under worlds/korvin-merrow/{task-prompts,expected-outputs,goldens,grader-guidance}/locked/ - need only: ID translation (FI->EW/E#-T#), de-hinting pass per preflight checklist, DOCX export in house style |
| 11 Run Agent | ~1 hr platform run | - | - |
| 12-13 Task AutoQC + Taiga QC | Iterate | QA Folder | Use "rerun failing only" discipline |
| 14-15 FA + PL | Failure analysis, preference labels | new folders when authorized | Physician-perspective rule already recorded |
| 16-17 Final review | Sign-off | - | - |

Key risk at stage 9: engineering regeneration may flatten trap fidelity ("a single changed dose, date, or fact invalidates the trap" - guide line 1333). Review every Failure Design anchor against the generated files.

Key job at stage 10: the locked TP/EO/Golden/GG were written before the AutoQC voice lessons. Before upload: apply the preflight prompt rules (persona voice, no hints, no rubric-speak) to prompts; verify goldens against final generated file content; translate all FI-* IDs.

## B. Recipe for World #2+ (what we'd repeat, what we'd skip)

REPEAT (worked):
1. Brainstorm with hostile-review pass before submission (caught trap taxonomy issues pre-reviewer).
2. Locked-package architecture (identity -> governance -> timeline -> meds/comorbidity -> providers -> tasks) with ratification gates - zero canon drift across 300+ files.
3. Medication dose approval sheet pattern: physician signs every numeric value ONCE; no silent invention ever.
4. The beautiful-but-structured reference-file design (design system + one approved sample -> mass production).
5. Continuation logs + per-bit commits for interruption-proofing.

DO DIFFERENTLY (cost us rounds):
1. Apply reference/checklists/spec-autoqc-preflight.md at AUTHORING time, not remediation time (saves ~5 QC rounds).
2. Use EW/E#-T#/WS IDs and Writer_World_Patient filename from day one.
3. Write draft prompts persona-voice-first; never paste TP request bodies into the spec.
4. Build the spec DOCX by filling the official template in place from the start (never rebuild); integrity gate after every save.
5. Reference files: generate with date-stamped final filenames from day one.
6. Sequence: get RL Studio field reality (screenshots) BEFORE resolving upload architecture on paper.

STRUCTURE for worlds/<new-world>/: copy korvin-merrow's folder skeleton (active/, world-spec-prep/{locked,ratifications,planning-scaffolds,reviews,decision-logs}, file-inventory/, synthetic-files/, task-context-files/, supplementary-files/, task-prompts/, expected-outputs/, goldens/, grader-guidance/, autoqc-remediation/, reviews/, remediation/, submission/). Reuse: brainstorm template, design system (reference-file-design/epic-note-design-system.md - swap facility/patient), tools/generate_reference_files.py, transcript design, Drive tree pattern.

## C. Standing infrastructure (do not lose)
- docs/workspace-guardrails-lessons.md - the 11 operational guardrails.
- reference/checklists/spec-autoqc-preflight.md - the 109-dimension distillation.
- worlds/korvin-merrow/reference-file-design/ - design system + approved FI-W01 sample.
- worlds/korvin-merrow/autoqc-remediation/ - remediation pattern + notes language.
- tools/generate_reference_files.py - reference-file generator (regenerate-able from design system if lost).
- Environment truths: sandbox = create/overwrite only (no delete, no git); Codex = git + deletes; user = Drive binaries + RL Studio; Drive connector = folders/text/search only.
