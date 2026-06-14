# OV Stage-9 revision record (Ready for Pipeline Fixes)

Date: 2026-06-14. Pipeline run: World Gen (latest) run #1, world_gen_latest, completed 2026-06-14 04:11 PDT.

## What the pipeline produced
filesystem/ = 43 files. World AutoQC: Fail 1/23 (Clinical Code Validity) - two ICD-10 codes mismatched in the synthesized `tasks/task2_coding/him_preliminary_coding_worksheet_05212026.docx` (M86.171 right-foot used for a left-foot osteomyelitis; E11.3211 right-eye-with-ME used for a bilateral no-ME finding). Root cause: the pipeline generated EVERY file in the spec file plan into one folder, including the 9 task-level files (Section 3.2), and re-rendered our writer-produced world files with embellishments not in our source (Spanish added to the foot-care handout, an invented "Renal Anchor" MAR construct, a "friction lesions" exam line). KM hit the identical task-file leak (removed 7 to land 26).

## Decision: Option B - restore writer-produced source
Because all files are Writer-produced and our committed source is verified-clean (English-only, metadata-scrubbed, deterministic, designed traps intact), we replaced the pipeline's regenerated world files with our source versions rather than surgically repairing the pipeline copies. This guarantees zero generation drift.

## What we uploaded (revision/filesystem)
34 world files (32 docx + 2 images: abi_tbi_tracing, wound_photo), our source content mapped into the pipeline's subfolder layout (admin, clinical, diagnostics, education, imaging, labs, medications, nursing, orders, therapy). The 9 task-level files (tasks/) were removed - they travel with their tasks at Step 10, never the Golden World Files. Pre-upload checks: 34 files, 0 task files, metadata-dirty 0, Spanish 0, eval-leakage 0.

## Verified on the LIVE applied download (verify the bytes, do not assume)
Downloaded the post-revision filesystem from Studio and diffed it against our source:
- 34 files (32 docx + 2 images); 0 task files; no tasks/ folder.
- All 32 docx content matches our source EXACTLY (0 mismatches) - the live Golden World Files are our writer-produced content, not the pipeline's regenerated copies.
- metadata-dirty 0; Spanish 0; eval-leakage 0.
The only prior AutoQC fail (task-2 ICD codes) left the world with the task files. The coding worksheet error was never in our source (our version uses code families, L89, not specific codes); no correction needed on our end. If specific codes are wanted at Step 10, correct ones are M86.172 (left-foot osteo) and E11.3293 (bilateral mild NPDR without ME).

## Temporal-ordering fix (added 2026-06-14, Final AutoQC "Document Chronology and Sequencing")
Final AutoQC flagged three notes signed BEFORE the same-day events they describe. Fixed at the source (clinical_data.py) by shifting each citing note after its cited event:
- HD2 progress 05/17 0930 -> 1700 (after debridement 1440).
- ID consult 05/18 1540 -> 1745 (after MRI finalized 1705).
- HD4 progress 05/19 0915 -> 1730 (after vascular consult 1635).
Swept every same-day cluster (05/16-05/21); no other conflicts. Also made the three 05/21 task files strictly after the 18:00 close so tasking has no date ambiguity (KM had repeated date corrections at tasking): T1 order set 1800 -> 1830, T2 coding worksheet and T10 started draft dated 05/21 1830. Rebuilt world + task files, regenerated revision/filesystem, gate green; HD2 1700 / ID 1745 / HD4 1730 confirmed in the revision.

## Next
Final file AutoQC on the revised world; if green, finalize and create the world as Healthcare_Vasquell_### (next available number in Studio). Task files and workflow remaps are handled at Step 10 per WORKFLOW-MAP.md and STAGE-9-FILE-REVIEW-PLAN.md.
