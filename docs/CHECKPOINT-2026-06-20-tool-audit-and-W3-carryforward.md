# Checkpoint 2026-06-20: OV tool audit, world inventory, and World 3 carry-forward

Snapshot taken after OV12 floored and the procedural docs were updated. OV is the mined-out reference world; World 3 (Marva Lydell) is at brainstorm, reviewed by Larry 2026-06-20.

## 1. Tooling audit

The cross-world gates and helpers live in `tools/`. The OV build scripts are world-local in `worlds/ondina-vasquell/build/`. Two layers.

### Cross-world gates (durable; World 3 inherits)
- `tools/verify/verify_voice.py` (14 refs) - repo-wide Dr. Alexander voice gate (banned AI transitions, scaffolding, register). Cross-world, runs as-is.
- `tools/verify/presubmit_task_gate.py` (10 refs) - per-task gate: banned glyphs, BANNED_BOILERPLATE, mount manifest + referenced-file existence, FA/GA structure and char count, the Studio FIELD MAP, the Section B verbatim clause. Mostly generalizable; carries an OV task map that World 3 must extend.
- `tools/verify/lint_fa_ga.py` (1 ref, the skill) - FA/GA linter: opens "On trajectory N", single run, the Overall Failure Score line, a dated citation, two paragraphs, under 1000 chars, no dashes, no rating word, no banned credit phrases, sentence-length warns. Cross-world, new this era.
- `tools/verify/verify_world_factory.py` (8 refs) - generic factory verification gate for a world-local build factory.
- `tools/verify/verify_ondina.py` (16 refs) - OV preflight gate (no-synthetic, no-KM-identifiers, metadata, golden-grader consistency, grader length cap 540 + five-block sectioning, template parity, filenames, anchor consistency). OV-HARDCODED. World 3 needs its own verify_marva (clone + repoint), this does not run on another world.

### Cross-world build pattern + helpers
- `worlds/ondina-vasquell/build/build_world_files.py` (`build_one`) - the ONE canonical Epic renderer. The core of the build pattern; the factory bootstrap clones it.
- `worlds/ondina-vasquell/build/epic.py` - Epic-note renderer matching the KM design system exactly.
- `tools/mode_a_clone.py` (5 refs) - Mode A docx clone, the canonical task-artifact build method.
- `tools/build/bootstrap_world_factory.py` (6 refs) - bootstraps a new world from the OV factory pattern. World 3's build pipeline starts here.
- `tools/generate_reference_files.py` (20 refs) - reference-file generator. DEPRECATED for task artifacts (AGENTS.md guardrail 1: regressed to a 2-row band + synthetic footer). Use mode_a_clone for task docx; this lingers for some world-file history only.

### Image-render patterns (proven, cross-world)
- `worlds/ondina-vasquell/build/render_ecg.py` - NEW this session. Authored-tracing renderer: a matplotlib plot of a synthesized waveform on standard ECG paper, raw fields with no printed diagnosis, metadata-clean. The template for any authored ECG / telemetry / rhythm strip. World 3's planned afib strip clones this.
- `worlds/ondina-vasquell/build/render_ov09_image.py` - reference implementation of the report-as-image method (build_one then soffice to pdf then pdftoppm then crop). The template for any device-printout or scanned-report image.
- `worlds/ondina-vasquell/build/composite_ov07_wound_annotation.py` - OV07 wound-photo compositing, historical (OV07 dropped the photo under Larry's AI-image ban).

### OV world-local (OV-specific)
- `clinical_data.py`, `task_data.py` - OV canonical content sources.
- `build_all.py`, `build_goldens.py`, `build_task_files.py`, `build_task_packages.py` - OV orchestration.
- `build_ov03.py` ... `build_ov12.py` - per-task builders (OV01/02 predate the per-task script convention).

### KM-era and dead
- `tools/build/build-docx-km*.py`, `tools/verify/verify-km08-*.py`, `tools/build/build-dashboard.py`, `tools/build-world-performance-xlsx.py` - KM world (delivered), historical.
- `tools/archive/*` - dead (old KM05/06/07/08/10 versions, qc-km05). Provenance only.

### Tooling gaps
- World 3 needs a verify_marva (verify_ondina is OV-hardcoded) and its own per-task map in presubmit_task_gate.
- generate_reference_files is a deprecation trap; the canon is mode_a_clone + build_one. Keep guardrail 1 loud.
- Run provenance: only task5/8/10/12 have a saved `pilot/runs/` file; OV01-04/06/07/09 FA/GA exist but their verbatim runs were not filed under runs/. Acceptable for delivered tasks, but the runs-first rule is newer than they are.

## 2. OV world inventory

Ten floored tasks across eight lanes (OV12 floored 2026-06-20; golden self-score pending before banking). Governed by `worlds/ondina-vasquell/docs/WORLD-STATUS.md`.

| Task | Lane | Mechanism | Pilot | State |
|---|---|---|---|---|
| OV01 | Medication Reconciliation | cold knowledge (stop enoxaparin) | FLOOR | Delivered |
| OV02 | Medical Transcription | off-text text synthesis (line infection) | FLOOR ~0.10 | Delivered |
| OV03 | Medical Transcription | carry-forward sliding-scale insulin | FLOOR 0.05-0.20 | Delivered |
| OV04 | Medical Transcription | off-text IMAGE (CPAP adherence) | FLOOR bimodal | Delivered |
| OV05 | Wound Care SOAP | embedded commission (silver alginate) | FLOOR ~0.12 | Floored; FA/GA pending |
| OV06 | Referral Intake/Triage | embedded wrong (perfusion closure) | FLOOR 0.39 | Delivered |
| OV07 | Claims Denial/Appeal | appeal overreach (osteomyelitis) | v3 awaiting re-pilot | Long-shot; retire if it ceilings |
| OV08 | Utilization Review | embedded wrong (antibiotic route) | FLOOR ~0.57 | Awaiting first human review |
| OV09 | Post-Acute Coordination | embedded wrong (held meds resumed) | FLOOR ~0.62 | Awaiting review; FA/GA submitted |
| OV10 | Discharge Summary | over-closure via subordinate (bone health) | FLOOR ~0.15 | Awaiting review; FA/GA submitted |
| OV11 | (vacated) Treatment Plan CDM | RETIRED (three mechanics ceilinged) | - | Retired 2026-06-19 |
| OV12 | Acute Care Discharge Planning | off-text IMAGE (new-onset afib ECG) | FLOOR ~0.37 bimodal (49eadf4e) | Floored; FA/GA drafted; golden self-score pending |

- Mechanism coverage: cold-knowledge x1, off-text text-synthesis x1, off-text IMAGE x2 (OV04, OV12), embedded-wrong x5, over-closure-via-subordinate x1.
- World files: ~31 frozen (29 docx + 2 images), snapshot 05/21/2026, never edited during tasking (DO-NOT-REPEAT #21).
- Retired packets (5): task5 skilled-wound, task11 treatment-plan, OV02 coding x2, OV04 appeal-concession.
- World canon (`worlds/ondina-vasquell/docs/`): WORLD-STATUS, WORKFLOW-MAP, FLOOR-MECHANISM-LIBRARY, KNOWN-CHART-DISCREPANCIES, FRESH-TASK-IDEAS, TASK-IDEA-AUDIT, APPROACH-MEMO, CANDIDATE-QUEUE, OV-BOOTSTRAP-AUDIT, EMR-TEMPLATE-FIDELITY-DIAGNOSIS.
- Cross-world canon (`docs/`, 32 files): fa-ga-canonical, qc-dispositions, qc-error-class-register, authored-image-artifact-menu, task-difficulty-lessons, task-structure-dossier, grader-guidelines-lessons, alexander-voice-dna, world-factory-playbook, world-pipeline-playbook, docx-generation-method, reasoning-discipline, anti-hallucination, and the rest.

## 3. World 3 (Marva) carry-forward needs

W3 is at brainstorm (reviewed by Larry 2026-06-20). It already carries `W3-MASTER-PACKET.md`, `IMAGE-SOURCING-CHECKLIST.md`, and the brainstorm/planning docs.

### Inherit by cloning or repointing
- The gate set runs cross-world (verify_voice, presubmit_task_gate, lint_fa_ga, verify_world_factory). Build a verify_marva from verify_ondina and add a Marva task map to presubmit_task_gate.
- The build pattern (build_world_files/build_one + epic.py + mode_a_clone) via bootstrap_world_factory.
- The image-render patterns: render_ecg.py (authored tracings, the planned afib strip) and render_ov09_image.py (device printouts and reports). No AI, no sourced image needed.

### New lessons from this session that W3 must apply
- The off-text IMAGE engine is the under-mined exception to saturation; OV12 proved it on a fresh lane. `docs/authored-image-artifact-menu.md` lists which medical images are authorable license-clean and the report-substitute rule for photos and true diagnostic images.
- Raw-finding image discipline (strip the printed interpretation) and the bench-method limit (a capable-agent cold-bench shows catcher-reachability and fairness but cannot measure the skip floor; the floor is a pilot measurement). Both now in FLOOR-MECHANISM-LIBRARY.
- Workflow-string discipline: pick from the Difficulty-Suggestions catalog, then CONFIRM the exact string and tier against Appendix A / the live Step-10 sheet before locking. Snapshots disagree with Appendix A (the OV12 "Specialty Consultation Note" -> "Acute Care Discharge Planning" saga; AGENTS.md guardrail 13 sharpened).
- Larry's trap-fairness line (2026-06-20): a true off-text finding the model must read is fair; intentionally planting false information in a task file and dinging the model for trusting it is not. The model presumes a record statement is accurate.
- Workspace-leak discipline: no repo paths, build- or render-script names, internal world-numbers, or builder jargon in any platform-facing text (writer's comment, disclosures, task files).
- Image disclosure for the writer's comment: writer-produced / custom-made, not AI-generated, not sourced, no PHI, metadata scrubbed (no method-authorship claim, physician voice).
- qc-dispositions dispute discipline: stay inside the sanctioned TaigaQA reasons; a valid flag is fixed, not argued, dismissals are reviewed externally.
- fa-ga-canonical now encodes the 06/19 Phase-3 standards (the over-70 too-easy gate, the grader-rating bands, the three GA rules).

### Larry's 2026-06-20 open items for W3 (APPLIED 2026-06-20)
- Sanctum Coach: merge model written (`docs/sanctum-coach-merge.md`). Workspace governs and produces; the Coach is adopted for template-file sourcing and run in the veteran path for a matching transcript. Package is in `tools/Sanctum_Coach/`. Working log at `docs/W3-WORKING-LOG.md`; chat-reference copy at `worlds/marva-lydell/coach/W3-Coach-ChatRef.md`.
- Traps and input files: fairness pass done (reconciliation section 2). World chart stays accurate; wrongs live in task-level inputs; Tasks 4 and 6 build as true placeholders.
- Workflow remaps: LOCKED to Larry. Task 2 Discharge Medication Reconciliation (P0); Task 6 Specialist Referral Letter and Documentation Preparation (P0); Task 10 CDI Query Response Review tier to P0. The canonical 06/19 doc corroborates Tasks 2 and 10; Task 6 is Larry's latest addition.
- Authority note (do not repeat the error): the Sanctum Coach's live workflow endpoint is BEHIND Larry's cut (the EPMs have not updated it). It is NOT authoritative for lane names, tiers, or saturation. Source those from the canonical 06/19 doc and Larry. An earlier pass this session wrongly treated the endpoint as authoritative and was reversed.

### Appendix A (located 2026-06-20) and the version split
Appendix A is `reference/source/task-selection-categories/Sanctum_Task_Selection_Categories_Combined_06_19.docx` (Project Sanctum: Approved Task Selection Categories, 237 workflows). It IS in the repo. OV12's lane "Acute Care Discharge Planning" is in it at P1 with a work product (documented discharge plan) that matches the deliverable exactly - confirmed. BUT Larry's 06/20 review quotes strings that are not verbatim in the 06/18/19 files: he recommends Specialist Referral Documentation and Discharge Medication Reconciliation (both P0) and treats Specialty Consultation Note as gone, while the files carry a misspelled P1 "...Discharge Medication Reconcilliation" and no "Specialist Referral Documentation." For W3, confirm each workflow string and tier verbatim against the file or with Larry before locking (name-check is a Major). For OV12 the 06/19 confirmation plus Dyrane's live-sheet check is sufficient. AGENTS.md guardrail 13 and the reference READMEs now name the 06/19 Appendix A and keep the verify-against-latest rule.

## 4. Open items and cleanup
- Get Appendix A / the latest instruction document into the repo (above).
- OV12: confirm the golden self-score in Studio, then run the Studio sequence (TaigaQA, FA/GA entry + AutoQC, first human review, preference labels), each on authorization.
- OV05 FA/GA pending its pilot; OV07 awaiting re-pilot (retire if it ceilings).
- Build verify_marva and extend presubmit_task_gate's task map when W3 reaches tasking.
- `CLAUDE.md` is an untracked stray at the repo root; decide keep or remove.
