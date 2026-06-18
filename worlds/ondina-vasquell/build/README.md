# Ondina Phase 3 build pipeline

Data-driven Mode A build. One canonical content module feeds two separate builders so
world files and task files never mix.

## Files
- `clinical_data.py` - single source of truth for world content (identity, roster, and derived texture values ratified from the substrate pack). Exposes WORLD_FILES, SUPPLEMENTARY.
- `task_data.py` - task-level reference artifacts (E1-T*), separate. External issuers logged in DERIVED_ISSUERS. Exposes TASK_FILES.
- `epic.py` - Epic-note renderer matching the current KM Epic note recipe (Arial, masthead, blue rule, patient storyboard, patient/encounter block, report tables, clean header/footer). GUARD() rejects banned characters before they can reach a file.
- `build_world_files.py` - clones the mapped clean KM base, clears body, rebuilds chrome + content, scrub_all_metadata, verify_no_synthetic, banned-char + styles check. Output: world-files/, supplementary-files/.
- `build_task_files.py` - delegates to build_world_files.build_one so task files render on the SAME canonical Epic template (masthead, blue bar, patient storyboard, PATIENT/ENCOUNTER block, clean Ondina header/footer), with the external issuer named in the title and filing line. Output: task-files/.
- `build_goldens.py` - renders task-setup goldens through the same build_one path; goldens carry identical Epic chrome to the world files. Golden dispositions are physician-owned drafts.

## CANONICAL RULE
Every project docx (world, supplementary, task, golden) is built through build_world_files.build_one / epic.py. Never a bare Document(). Verify fills and colors are a subset of the world-file vocabulary before calling any docx done. See DO-NOT-REPEAT.md.

## Run
```
python3 build_world_files.py        # all world + supplementary
python3 build_task_files.py         # all task files
# slices supported to stay under sandbox time limits: build_world_files.py 0 15
```

## Guarantees per file
Mode A clone (styles.xml byte-identical, no base content survives clear_body); zero
synthetic/tool tokens in ANY part incl. core/app/custom and footers; zero banned
characters; world dates <= 05/21/2026 18:00; every load-bearing value traces to the
ratified substrate; trap-carrier files describe without resolving (clinical-voice guide).

## Not built here
EW30/EW31 images are writer-produced media built from `codex-image-prompts.md`. Task prompts, goldens, graders are writer-authored per the authorship boundary.
