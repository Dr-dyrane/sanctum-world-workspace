# World 3 Template Curation: Coach veteran-mode paste kit

USAGE (for you, do NOT paste this section into the Coach):
- Open a NEW chat in the Sanctum Coach Project. Say you are on Template Curation.
- Attach TWO files to that chat: the Template DataBank (`tools/Sanctum_Coach/Attach_to_Chat_at_Template_Curation/Template_DataBank.docx`) and the finished spec (`worlds/marva-lydell/submission/Alexander_World_Marva_latest_6_20.docx`, which carries the Section 3 file plan). The DataBank must be attached to the chat, not the project, so the Coach can open it with its code tool.
- Paste everything below the PASTE FROM HERE line.
- Division of labor (your call, held): the Coach drafts the DataBank and custom templates; you render the one writer-produced file (the afib rhythm strip) with our own script. Let the Coach do the DataBank-first search and flip any provisional "custom" row to a DataBank template where a real match exists (it will find Nursing Flowsheet, Patient Education, Referral Letter, Utilization Review, Respiratory Therapy Note, and others).
- Scope: world-level rows only (the EW and WS IDs). Task-level files (E#-T#) are attached at task setup, not curated here.
- Download each template the Coach produces, keep the names it gives them, and collect them into one Reference Templates folder. Then the spec docx and that folder upload together to Studio for World Spec AutoQC.

================= PASTE FROM HERE =================

VETERAN BUILD MODE

I am a physician contributor on Project Sanctum and I am on the Template Curation phase for a finished World Spec. The spec and the Template DataBank are attached. Walk my Section 3 world-level file rows, the essential world-level (EW) and supplementary world-level (WS) rows, and curate one reference per row, DataBank-first.

For each row: open the attached DataBank and extract the matching template as a downloadable .docx with its formatting preserved; draft a custom template in the clinical house style only where the DataBank genuinely has no fit; and name the official source for any public-domain form. Do not call a row custom before searching the real DataBank, since the embedded catalog is not exhaustive.

Reuse aggressively at the type level: one inpatient progress-note template covers all the daily hospitalist notes; one specialty-consult template covers cardiology, nephrology, pulmonology, and endocrine; one flowsheet template covers the labs, vitals, weights, and the medication administration record; one diagnostic-report template covers the echocardiograms and the ECG report. Point the matching rows at the shared template rather than making duplicates.

One row is writer-produced and is not a template: the atrial fibrillation rhythm strip, afib_rhythm_strip_06152025.jpg. I produce that separately with my own tool, so list it as writer-produced and do not generate it.

Keep filenames to the convention: templates and reference files get generic names with no datestamp, and that name is what goes in the Reference File Origin column; the writer-produced strip keeps its final datestamped name. Task-level files are out of scope.

Give me each extracted or drafted template as a downloadable .docx, and a running list of what is DataBank, custom, public-domain, and writer-produced, so I can assemble the Reference Templates folder.

================= END PASTE =================

## Steps (the runbook)

1. New Coach chat, Template Curation phase. Attach the Template DataBank and the spec docx. Activate the veteran path and paste the block above.
2. Walk the world-level rows in installments. For each: download the DataBank extract or the drafted custom .docx. Confirm reuse where the Coach proposes it.
3. The two public-domain rows (the Medicare discharge-rights notice WS2, the hospital admission consent WS4): download the official blank from the named source and scrub metadata with a screenshot.
4. The one writer-produced row (EW22 afib_rhythm_strip_06152025.jpg): render it here with our ECG render script (clean of any printed interpretation), keep the datestamped name. I can do that render for you on request.
5. Assemble the Reference Templates folder: one file per world-level row, generic undatestamped names for templates, the datestamped strip for the writer-produced row, no synthetic or training markers anywhere.
6. Self-QC: every world-level row has a file or a clear source note; every file traces to a row; the world-level count still meets the 30 minimum; names match the Reference File Origin column.
7. Upload the spec docx and the Reference Templates folder to Studio as separate files, not zipped, then run World Spec AutoQC.

## Notes

- The DataBank-first flips are expected and fine; we left the spec's origin marks provisional on purpose so the Coach resolves them against the real DataBank here.
- If the Coach pushes back on a workflow lane or the June dates, that is the stale endpoint again; Template Curation does not touch lanes or dates, so it should not come up, but hold our locks if it does.
- After the templates folder is built and uploaded with the spec, the next gate is World Spec AutoQC, then reviewer approval, which triggers engineering's generation of the world files.
