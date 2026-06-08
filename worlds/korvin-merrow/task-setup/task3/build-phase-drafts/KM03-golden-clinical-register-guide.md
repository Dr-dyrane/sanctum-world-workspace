# KM03 golden - clinical-register elevation guide (for Alexander to author in his own words)

Purpose: the golden already carries your clinical intent; this guide helps you make it READ like the pipeline-generated world files rather than a summary, while keeping the trap intact. You author the golden text; this is a register checklist and exemplar pointer, not a rewrite. Source of the standard: `docs/clinical-voice-lessons.md` (logged 2026-06-04, after the pipeline engineering team returned the generated world files and we mined the paired corpus `.meta/references/` vs `filesystem/`).

## In-world exemplars to mirror (open these and match their voice)
The closest register models for a discharge-planning / transition golden, all in `file-review/upload/filesystem/`:
- `hospitalist_discharge_planning_progress_hd5_hd6_05232026.docx` - attending's own discharge-planning synthesis; the native grammar and voice for this deliverable.
- `discharge_facing_plan_snapshot_05232026.docx` - the discharge-facing layout, follow-up table, return precautions, named providers/agencies.
- `case_management_social_work_discharge_note_05222026.docx` - how pending coordination items are phrased in-register.
The paired corpus (`.meta/references/` terse templates vs `filesystem/` clinical files) is the best style reference we own; the difference between them IS the register you are reaching for.

## Register checklist for the golden (apply the patterns that fit a discharge-planning summary)
1. Native document grammar. Keep the discharge / transition-of-care structure with the standard headings (reason for transition, functional status, cognition and medication management, ongoing conditions by problem, home services, supervision and family, transportation and follow-up, return precautions). Problem-oriented, attending voice.
2. Attending signature furniture. Author line and "Electronically signed by Elian Vossmere, MD | Hospital Medicine" - already present; keep it.
3. Name the chart realistically. Use the real providers and agencies where they belong: PCP Talia Quenor, MD; Cardiology Maris Caldrane, MD; Nephrology Iven Solthar, MD; Endocrinology Nerea Veylorn, MD; Rheumatology Soren Halvek, MD; Keystone HomeCare Services; Harbor Crest Community Pharmacy; case management Priya Ostroff, RN and social work Devra Aimes, LCSW. Identifiers and named staff are cheap realism multipliers.
4. Concrete over abstract. Where the chart supports it, write the specific (rolling walker not cane; Morse Fall Scale 65; ferrous sulfate every other day; weekday-morning supervision gap; the named follow-up windows) rather than a category summary.
5. Time-anchor in the chart's idiom. "filed reflecting the record through hospital day 6," precise where labs/dates are precise, approximate where the story is.
6. Do not duplicate header metadata in the body. Demographics live in the band once.
7. Keep it terse where terse is right. The grader already says "judge against the chart, not the terse golden," so do not pad. Elevate the register (voice, specificity, naming), not the length.

## CRITICAL caution - the CPAP line stays plain (the trap carrier)
From the log's caution section: polished clinical voice loves synthesis, and synthesis is what kills a buried-evidence trap. The golden's OSA/CPAP line is the trap carrier and must read as the plainest, most factual prose in the document - no flourish, no weighting, no "reassuring" synthesis. It should simply record the chart: the only sleep study on file is the 2019 diagnostic polysomnography, there is no recent in-lab titration, adherence is variable per home report and not device-verified, no recent CPAP review or adequate-adherence determination is documented this admission, and CPAP efficacy and adherence are to be confirmed at outpatient follow-up. Note the OSA/heart-failure relevance plainly if you wish, but do not let the line perform a judgment the chart has not made. Same restraint for the genuinely-pending coordination items: name them as to-be-confirmed in plain register, do not narrate them as resolved.

## Authorship note
You write the golden text in your own words; this guide and the exemplars are reference only. After you elevate it, I can run the build hygiene (Mode A clone, fingerprint, metadata scrub, date-audit, leak scan) and a content-preservation diff so nothing clinical is dropped - but the prose is yours.
