# Phase 3 Build Plan - Ondina Vasquell reference templates and task files

Scope: how every reference file in the World Spec file plan (section 3) gets built. Three things the user asked to lock before authoring: (1) world files and task files stay correctly separated, (2) the recurrent synthetic-doc error does not leak this time - including in metadata, (3) every file is a Mode A clone of an approved, clean Epic-UI base, carrying the pipeline-returned SOAP and clinical-voice standard. Read with `clinical-voice-and-file-grammar-guide.md` (voice + native grammar per file) and `docs/clinical-voice-lessons.md` (the source standard).

## 1. World files vs task files - the separation is load-bearing

The file plan already splits them; this is the build-time rule that keeps the split real.

- World-level files (EW1-EW31, plus supplementary WS1-WS3) are the shared chart. They provide raw material only - never an answer-key synthesis. There is no shared discharge summary, no final ID antibiotic plan, no final vascular recommendation, no coding or CDI conclusion at world level. These mount once in the shared world filesystem and are visible to every task.
- Task-level files (E1-T1 ... E1-T10) are the severity-forward external surfaces - the unreconciled discharge order set, the HIM coding worksheet, the CDI query, the MA denial, the PBM rejection, the concurrent-review request, the quality abstraction worksheet, the safety-event intake, the started discharge-instruction draft. Each is wrong-by-genre or incomplete on purpose. They are keyed to exactly one task (the E1-T<n> id names the task) and must NOT sit in the shared world mount, or they would pre-answer their own task.

Mount discipline (the KM mount-coherence lesson): exactly the EW + WS set under the shared world `filesystem/`; each E1-T file travels only with its task's input set; nothing task-specific under shared `.apps_data`; no duplicate volumes; no E1-T file leaking into the world mount. Verify the mounted tree before any pilot.

## 2. Mode A base map - clone clean, inherit the right grammar

Every file is a Mode A clone: clone an approved artifact of the same Epic UI so `styles.xml` is byte-identical, clear the body, rebuild content, scrub metadata, fingerprint-diff to zero. NEVER a blank `Document()` and NEVER `generate_reference_files.py` - both re-inject the synthetic footer (cost KM01 and KM08 v1 a round).

Base pool: the KM benchmark-facing set at `worlds/korvin-merrow/file-review/upload/filesystem/`. Twenty of its files are already clean (no synthetic token, scrubbable metadata) and are the preferred clone bases. Six are NOT clean and are banned as bases: `admission_history_and_physical`, `cardiology_consultation`, `hospitalist_progress_hd1_hd2`, `initial_medication_reconciliation_note`, `nursing_observation_flowsheet_summary`, `problem_list_history_snapshot` - each still carries SYNTHETIC TRAINING. Where an Ondina file's natural analog is one of these, clone a clean sibling of the same grammar instead (named below).

| Ondina file | Native grammar | Clean KM base to clone |
|---|---|---|
| EW1 ed_physician_note | ED note | ed_provider_assessment_05182026 |
| EW2 admission_hp | full H&P arc | ed_provider_assessment (clean; rebuild to H&P arc) - do NOT clone the tokened KM H&P |
| EW3/EW4/EW5 hospitalist_progress | SOAP | hospitalist_progress_hd3 / hospitalist_progress_hd4 (both clean) - not hd1_hd2 |
| EW6 podiatry_debridement_note | operative note | hospitalist_progress_hd3 (clean note shell) rebuilt to procedure grammar |
| EW7 mri_foot_report | radiology report | nephrology_consultation (clean) rebuilt to report grammar, or ED report shell |
| EW8 id_consult_note | consult skeleton | endocrinology_consultation / nephrology_consultation (both clean) |
| EW9 abi_tbi_study_report | vascular lab report | renal_infection_hemodynamic_trend_summary (clean) rebuilt to study-report grammar |
| EW10 vascular_consult_note | consult skeleton | nephrology_consultation (clean) |
| EW11 foot_pathology_report | surgical path report | nephrology_consultation (clean) rebuilt to path grammar |
| EW12 wound_care_consult | wound consult | physical_therapy_assessment (clean) rebuilt to wound-consult grammar |
| EW13 pt_evaluation | therapy eval | physical_therapy_assessment (clean) |
| EW14 ot_evaluation | therapy eval | occupational_therapy_assessment (clean) |
| EW15 case_management_note | case-mgmt note | case_management_social_work_discharge_note (clean) |
| EW16 mar | MAR grid | medication_administration_record (clean) |
| EW17 renal_lab_trend | lab flowsheet | renal_infection_hemodynamic_trend_summary (clean) |
| EW18 cbc_inflammatory_trend | lab flowsheet | renal_infection_hemodynamic_trend_summary (clean) |
| EW19/EW20 culture_report | micro report | renal trend (clean) rebuilt to micro grammar, or report shell |
| EW21 endocrine_glycemic_note | consult/education | endocrinology_consultation (clean) |
| EW22 home_med_list | EMR med list | pharmacy_refill_history_report (clean) - not the tokened med-rec note |
| EW23 outpatient_primary_care_summary | outpatient summary | primary_care_outpatient_baseline_summary (clean) |
| EW24 nursing_offloading_flowsheet | nursing flowsheet | medication_administration_record (clean grid) - not the tokened nursing flowsheet |
| EW25 medication_hold_orders | signed order set | medication_administration_record (clean) rebuilt to order-set grammar |
| EW26 antibiotic_plan_note | plan note | hospitalist_progress_hd4 (clean) rebuilt to plan-note grammar |
| EW27 vital_signs_flowsheet | vitals flowsheet | medication_administration_record (clean grid) |
| EW28 diabetic_eye_exam_result | ophthalmology result | nephrology_consultation (clean) rebuilt to result grammar |
| EW29 family_communication_note | family meeting note | family_communication_care_conference (clean) |
| EW30 wound_photo | image | Writer Produced - see codex-image-prompts.md |
| EW31 abi_tbi_tracing | image | Writer Produced - see codex-image-prompts.md |
| E1-T2 him_coding_worksheet | coder worksheet | discharge_facing_plan_snapshot or a clean HIM shell (KM HIM coding summary is in task-setup; clone its clean current version) |
| E1-T* external surfaces | issuer voice | clone the nearest clean external-correspondence shell; rebuild in the issuing party's authentic voice |

Where a clean base of the exact genre does not exist, clone the closest clean shell for styles parity and rebuild the body to the target grammar from the clinical-voice guide - the styles must be inherited; the content is always rebuilt.

## 3. Recurrent synthetic-doc error - the anti-leak protocol (including metadata)

Evidence this is real and reaches upload: in KM's own benchmark-facing `upload/filesystem/`, six of twenty-six files still carry SYNTHETIC TRAINING, and the approved reference templates also carry `python-docx` in `core.xml` and `Microsoft`/template fingerprints in `app.xml`. The marker leaks in four places at once - body (`document.xml`), footer (`footer*.xml`), `core.xml`, and `app.xml`. The current Ondina World Spec DOCX is clean (no docProps parts, zero tokens anywhere), which is the bar every world and task file must also clear.

Tooling gap to close before building world files: the existing `scrub_core()` only empties `docProps/core.xml`. It does NOT remove a SYNTHETIC footer, a body token, or `app.xml`/`custom.xml` fingerprints. Phase 3 adds and runs two helpers (additive, do not alter the spec path):

- `scrub_all_metadata(path)` - empty `core.xml` (creator, description, lastModifiedBy, python-docx), neutralize `app.xml` (Application, Company, Template), drop `custom.xml`; and strip any "Synthetic"/"SYNTHETIC TRAINING" run from every `footer*.xml`, `header*.xml`, and `document.xml`.
- `verify_no_synthetic(path)` - assert that NO part (every `.xml` and `.rels`, including all headers and footers and all three docProps) contains, case-insensitively, any of: `synthetic`, `synthetic training`, `python-docx`, and that `core/app/custom` carry no authoring-tool or company fingerprint.

Per-file gate before a file is called done: Mode A fingerprint diff empty; `verify_no_synthetic` passes on all parts; zero banned characters (em/en dash, arrow, asterisk, bracket) in body and footer; dates at or before the 05/21/2026 18:00 snapshot for world files (task-level external surfaces may post-date per their own dates in the plan); render to PDF and eyeball before staging; world facts read back from the docx with python-docx (table cells included), never from a markdown convenience copy.

No-synthesis gate (the other recurrent leak): trap-carrier files use the plainest prose, never weight sources, never sequence the answer, never declare readiness; no world-level file contains a final synthesis. Confirm against the trap-carrier flags in the clinical-voice guide.

## 4. Build order

1. World files EW1-EW31 first (they are the substrate every task reads), grouped by clone base to reuse the cleared shell.
2. Supplementary WS1-WS3.
3. Task-level E1-T files last, each verified to assert nothing about its own task's scored decision (re-attribution for external/weak-source docs; true placeholder for the same-author started draft E1-T10).
4. Images EW30/EW31 from the Codex prompt specs.
5. Mount-coherence check, then hand to Alexander for RLS upload and AutoQC. No platform actions are automated here.
