# OV Stage-9 file-review plan (Ready for Pipeline Fixes)

Date: 2026-06-14. Use when the pipeline finishes and the task flips to "Ready for Pipeline Fixes." Distilled from KM's Stage-9 logs (file-review/, pipeline-output/.meta/), the official Instruction Doc Section 5 (World File Generation and Editing Overview), and Larry's 6/14 finalize note. Companion: KM-TASK-LESSONS.md, docs/anti-hallucination.md, DO-NOT-REPEAT.md.

## Official Section 5 sequence (the canonical process this plan executes)
1. World spec submitted to pipeline (done).
2. Synthetic files created (pipeline generates the world files from the spec).
3. Files reviewed with AutoQC results (file integrity, schema, consistency).
4. Files edited to address issues (writer resolves flagged findings + anything off).
5. Revisions uploaded - upload ALL files, edited AND unedited; REMOVE every task-level file first (any file uploaded becomes part of the finished world; leaving a task file causes tasking errors).
6. Final file AutoQC re-run; if it flags legitimate issues, back to step 4 (check with the reviewer if unsure a flag is valid).
   Then: World finalized and created. NAME IT: `Healthcare_Vasquell_###` (format `Healthcare_[Patient Last Name]_[###]`; pick the next available ### from the world count in Studio). Note: this is NOT the old KM pattern `Healthcare_247_Merrow`; the ordering is last name then number.

Official quick review checklist (Section 5): verify clinical content (dates, names, doses, cross-document consistency); confirm intended trap content survived generation; identify and correct any new inconsistencies; remove task files before upload; be 100% confident before finalizing. The steps below execute this checklist plus the KM-learned extras the doc does not mention.

## The reframe (why OV's Stage 9 is lighter than KM's)
KM's files were Custom Made, so engineering GENERATED them and introduced the defects: answer-key/meta leakage, traps editorialized, selective bold added, letterhead drift. OV is Writer-produced, so engineering should NOT regenerate ours. Verified pre-pipeline (2026-06-14) on our 29 built world files: leakage tokens 0, task-level files in world set 0, content/value bold 0 (bold is structural-only and symmetric). So OV Stage 9 reduces to ONE decisive check, then a short confirm list.

## Step 1 - the decisive check: integrity diff (verify, do not assume)
Compare each returned/generated file against our committed source bytes. If they match, we inherit the verified-clean state and Steps 2-3 are confirmation only. If any file differs, engineering altered a writer-produced file: KM's FULL defect list (below) then applies to the diff, repair in place.

## Step 2 - trap-survival per anchor (only if files differ from source)
- Renal trend: a trend approaching but NOT returning to baseline; not collapsed to one value or "normalized"; consistent across every file (no value drift).
- Equivocal osteomyelitis: stays equivocal; no file declares it established or ruled out; no sentence weighing it for the reader.
- Open perfusion: stays open; no consultant note resolves it or enumerates the decision parameters (KM EW14 failure).
- Culture hierarchy: deep-tissue over swab preserved; no single definitive organism/source stated.
- Dated eye-exam lookback (EW28): date intact and correct; not silently changed.
- Med holds: hold/give cadence internally consistent across MAR days; held agents carry no numeric dose if deliberately unverifiable.
- Two images (EW30 wound photo, EW31 ABI/TBI tracing): present, render, integrity intact, no embedded answer/coaching text, metadata clean, in the world set.
- No physician/summary note editorializes a buried-evidence item as central, important, or easy to overlook.

## Step 3 - universal finalize checks (every time, per Larry 6/14)
- NO task-level files (E1-T) in the final world folder; world files only. Hold task files for Step 10.
- Metadata scrubbed on every file; zip the filesystem folder and run the scrub before re-upload.
- Dates intact: nothing altered by generation; all world content at or before the snapshot; nothing future-dated past today.
- Bold structural-only and symmetric; no mid-sentence or single-data-row emphasis on clinical/trap content.
- No leakage tokens: world close, locked world, EW-ids in body, golden/grader/grading, trap/friction/anchor, coaching sentences.
- Letterhead/chrome uniform across same-type documents.
- EW cross-references correct (KM cited EW16 where it meant EW12) - check every pointer against the manifest.
- find /docs after upload: exactly one intended set, no duplicate or .apps_data/calendar volume.
- Filenames match the spec file plan exactly; no duplicate-suffixed " N.docx".

## Platform mechanics (cost KM the most wall-clock)
- Verify against the DOCX (with table cells), never the .md mirrors (stale after the repair loop).
- Apply edits from the REVISION page, never the run-page Actions row (that one reverts to the original). Verify the file count and spot-check content after every apply.
- The task-card Final Files AutoQC can re-audit a STALE pre-revision snapshot; verify the snapshot source before treating a persistent flag as real.
- NEVER re-run the pipeline (~46h); fix in place or contact the reviewer.
- Run an independent cold-audit (fresh Claude session, final zip + checklist, PASS/FAIL with quotes) before re-upload.
