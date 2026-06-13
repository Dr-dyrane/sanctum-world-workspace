# Ondina Phase 3 build pipeline

Data-driven Mode A build. One canonical content module feeds two separate builders so
world files and task files never mix.

## Files
- `clinical_data.py` - single source of truth for world content (identity + roster ratified from the substrate pack; texture values in the DERIVED registry pending one-pass ratification). Exposes WORLD_FILES, SUPPLEMENTARY.
- `task_data.py` - task-level reference artifacts (E1-T*), separate. External issuers logged in DERIVED_ISSUERS. Exposes TASK_FILES.
- `epic.py` - Epic-note renderer matching the KM byte recipe (Arial; bold-black section headers; EAEAEA banner; margins). GUARD() rejects banned characters before they can reach a file.
- `build_world_files.py` - clones the mapped clean KM base, clears body, rebuilds chrome + content, scrub_all_metadata, verify_no_synthetic, banned-char + styles check. Output: world-files/, supplementary-files/.
- `build_task_files.py` - same pipeline, no Epic patient banner (these are external/draft surfaces). Output: task-files/.

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
EW30/EW31 images -> Codex (codex-image-prompts.md). Task prompts, goldens, graders ->
writer-authored (per-task-build-checklist.md authorship boundary).
