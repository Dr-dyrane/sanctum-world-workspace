# World Pipeline Playbook (post-Korvin, for future stages and future worlds)

Date: 2026-06-04. Written at Korvin Merrow spec-submission (108/109, prednisone-by-design). Two purposes: (1) what happens next for Korvin, (2) the repeatable recipe for World #2+.

## A. Korvin: forward pipeline (stages 7-17)

Current position: Steps 1-9 COMPLETE. World created 6/5/2026 as **Healthcare_247_Merrow** (world_d50c832ac6474a68ba982a77e28a6bbe, 26 files synced, snap_0fb032e95b324710b12a7432cf7da6c1). Task 1 auto-created in Task Writing stage. Active stage: Step 10 task setup.

## A2. Step 10 verbatim requirements (instruction doc 06_02, "How to Set up Your Task in RLS" + Golden Response + Grader Guidelines sections; read 6/5)

Pre-conditions before RLS entry: golden response, grader guidelines, and world spec confirmed final; world files uploaded (done - world is live).

Per-task RLS flow: open world -> Create Task, one task at a time -> task name in the problem statement field -> Add Files (task-specific E#-T# files) -> paste prompt into prompt field -> paste grader guidelines into their field -> **golden response is UPLOADED as a file, not pasted**. **SAVE AFTER EVERY SINGLE STEP** - navigating away unsaved loses everything; after all tasks, save again and verify content before running.

Run the agent: select correct version -> latest model -> Run (~1 hr for all tasks; set up remaining tasks while first runs). After a run: Task Submission History -> latest version -> Run All QA -> wait 10-20 min -> Fetch QC Report. Default 10 trajectories per run.

Golden response rules: writer-authored, sequential to the prompt's requests; sets the ceiling (if any agent trajectory beats it on any point, improve the golden before proceeding); placeholders over fabrication ("[No documented baseline weight available]"); unambiguous calculations (rounding convention in prompt, units throughout); must score full marks under your own grader guidelines.

Grader guidelines: labeled A/B/C structure. Section A = clinical accuracy non-negotiables; Section B = scope/format/what legitimately varies + explicit fabrication clause (answers outside pre-authorized alternatives = fabrication even if defensibly argued); Section C = common failure modes from OBSERVED trajectories, not anticipated in advance, opening line verbatim "These are patterns to reason about, not items to tick off." Name what varies and what does not; task-specific direction, not generic permissions; a bad golden is worse than no golden.

Scoring calibration: <70% trajectory score = decent stumping; >70% = task may be too easy. Clinical judgment overrides the number.

QC discipline (Phase 3): resolve or dispute every finding before the next step (gated). Error-level: must fix. Warning: fix or dispute with specific justification (thumbs up to accept, thumbs down + brief note to dispute). Fix now = materially affects evaluation validity; fix later = cosmetic, document and move on. Do not accumulate unaddressed findings across runs.

Self-QC before upload (optional per doc, mandatory for us): writer prompt docs at reference/templates/ - AutoQC_Section_4_Task_Prompts_v6.6 for prompts; same flow for goldens and grader guidelines ("walk through every check, Blockers first, then Majors, then Minors").

Note: task prompts must be writer-authored (doc line 876, non-negotiable: "the actual task prompt has to come from the writer, not the LLM"). Ours are - all 6 TP locked under Alexander's authorship; Claude's role is de-hinting and format translation only.

## A3. Later-phase reminders from instruction doc 06_02

After task setup and trajectories, preserve a local backup record of QA / AutoQC responses before platform submission when the guide asks for documentation in Google Docs or Drive. Do not rely on platform cards as the only memory surface.

Failure analysis / grader analysis is later-phase work only. When authorized, read the full lowest-scoring trajectory output for each task rather than summarizing from scores alone. Grader analysis should be concrete and short enough to act on: identify the real failure pattern, explain whether the failure is prompt-side, file-side, golden-side, grader-side, or model-side, and propose specific edits to the A/B/C grader sections when needed.

Preference labeling is later-phase work only. Keep it separate from Step 10 task setup, QA response notes, and grader-guideline editing. Follow the official preference-labeling dimensions and do not pre-create labels from expected failures.

Drive sync note for the current state: Step 9 is finalized, so the world-level 26-file set may be mirrored to Drive if Alexander explicitly authorizes Drive mutation. Step 10 task setup materials should remain a separate sync package because prompts, goldens, and grader guidelines have different review/upload semantics than world-level files.

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
- docs/workspace-guardrails-lessons.md - the operational guardrails (now 12, incl. mojibake/dash discipline).
- docs/clinical-voice-lessons.md - 10 clinical-voice patterns mined from the run #1 paired corpus (writer templates vs pipeline rewrite, .meta/references/ vs filesystem/); apply at template-authoring time for World #2 so generation has less to "fix" and less occasion to over-help.
- reference/checklists/spec-autoqc-preflight.md - the 109-dimension distillation.
- worlds/korvin-merrow/reference-file-design/ - design system + approved FI-W01 sample.
- worlds/korvin-merrow/autoqc-remediation/ - remediation pattern + notes language.
- tools/generate_reference_files.py - reference-file generator (regenerate-able from design system if lost).
- Environment truths: sandbox = create/overwrite only (no delete, no git); Codex = git + deletes; user = Drive binaries + RL Studio; Drive connector = folders/text/search only.
