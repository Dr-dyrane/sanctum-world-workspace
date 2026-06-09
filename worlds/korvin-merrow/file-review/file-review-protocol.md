# Step 9 File Review Protocol - "Ready for Pipeline Fixes" (Korvin Merrow)

Date: 2026-06-04. Stage entered same day the pipeline run completed (run #1, world_gen_latest, completed 10:20 AM PDT 6/4). BILLABLE: Insightful tracking from this stage onward (playbook A, row 9).

## 1. This run's AutoQC read - why Fail 2/76 is routing, not damage

World Files AutoQC: 74/76 PASS. The two FAILs ("Computational Fixtures Internally Consistent", "No Tracked Changes or Comments in World Files") both failed for the SAME non-content reason, stated verbatim in their notes:

- The auditor sandbox could not reach any input file (S3 GET 403, no AWS credentials, `/.autoqc_context/manifest.json` declared `artifacts: []`, `file_count=0`). No document was actually inspected for those dimensions.
- Falling back to the pipeline's self-report, the auditor saw `ship_status="needs_review"`, `cert_ship_ready=false`, `external_qa_status="failed"` and correctly FAILed to route the world to human review instead of default-passing.

That human review is this stage. The gate did its job. Do NOT "Rerun 2 failing" until after the revision snapshot is uploaded - rerunning against the same inaccessible context reproduces the same result.

## 2. The findings inventory to triage

Pipeline self-report: **95 actionable_findings, 13 red_team_findings, 71 cross_doc_qc_total**. The findings text lives in the run's `.meta` output files (134 of the 167 outputs). The other 33 outputs are the generated world docx (filesystem/).

Local ingest path: `worlds/korvin-merrow/file-review/pipeline-output/` (user downloads "Download All" from the run page and drops the folder here).

## 3. Triage taxonomy - every finding gets exactly one label

| Label | Meaning | Action |
|---|---|---|
| FIX | Real generation error: changed canon dose/date/name, broken internal math, contradiction NOT in the trap registry, missing section, formatting damage | Edit in place (minor) or list for regeneration (major) |
| PROTECT | The QC detected an INTENTIONAL trap and proposes to "repair" it | Do not touch the file. Record finding ID + trap it maps to. These are evidence the traps survived generation. |
| NOTE | Benign/cosmetic: stylistic variance, realistic imperfection, auditor false positive | Record, no edit |

PROTECT candidates to expect (the registered trap architecture WILL light up cross-doc QC):
- Prednisone dose/frequency absent or contradictory across EW1/EW2 (triage vs ED note), EW4 (med rec refuses verification), EW5 (refill history is not adherence), EW6 (rheumatology intent without verification). The absence IS the trap. Any finding proposing to add a dose = PROTECT, ship-blocker if "repaired".
- EW22 discharge snapshot reassuring-but-incomplete vs EW17-EW19 buried functional evidence (family/PT/OT). Detected "inconsistency in functional status" = PROTECT.
- Cardiology (EW15) vs Nephrology (EW14) restart-timing disagreement = registered friction, PROTECT.
- Endocrinology steroid-risk framing (EW16) vs primary team (EW10-EW11) = registered friction, PROTECT.
- Sepsis-anchoring early-course language vs later trajectory = trap, PROTECT.

Red-team findings (13): these probe trap integrity and leakage. Expect a mix: some confirm traps are discoverable-but-unresolvable (good), some may flag genuine answer leakage (FIX immediately - leakage invalidates tasks).

## 4. Trap-fidelity checklist (run against the 33 generated docx, file by file)

- [ ] Prednisone: NO dose or frequency stated anywhere in any of the 33 files. Grep all containers (paragraphs AND every table cell) for `prednisone` and verify each mention preserves ambiguity. A single generated "prednisone 10 mg" anywhere kills the central trap.
- [ ] 12 canon doses unchanged everywhere they appear: aspirin 81, atorvastatin 40, sacubitril/valsartan 24/26 BID, carvedilol 12.5 BID, furosemide 40, spironolactone 25, empagliflozin 10, metformin ER 500 BID, glargine 18 units, gabapentin 300, ferrous sulfate 325 QOD, alendronate 70 weekly.
- [ ] EW22 (discharge_facing_plan_snapshot_05232026) still reads reassuring and OMITS the functional-decline evidence; it must not have been "completed".
- [ ] EW17-EW19 evidence still buried in flowsheet/assessment detail, not surfaced into summaries.
- [ ] Consultant note dates intact: EW14/EW15/EW16 = 05/21/2026; EW6 available HD4 (05/21).
- [ ] Every Failure Design anchor in the spec resolves to real generated content (file + date). Use spec Section 2 Failure Design tables as the source list.
- [ ] World close discipline: no file content dated after 05/23/2026 18:00 except the task-request files (E1-T1..E1-T4 05/24, E1-T5 05/31, E1-T6 06/23) and they contain requests, not outcomes.
- [ ] No answer leakage: no file states the golden conclusions (med-rec disposition table, readiness verdict, risk stratification).
- [ ] Filenames/IDs match the spec file plan exactly (33 names, set equality).
- [ ] Routes still "Oral" (no letter-O "PO"); dates MM/DD/YYYY; no em/en dashes or arrows introduced by generation.
- [ ] DOCX integrity gate on every file (EOCD present, styles.xml, opens, renders) - guardrail 4.

## 4b. PLATFORM-VERBATIM REQUIREMENTS (from 3.0 Pipeline / 4.0 Final Files instructions, read 6/4)

1. **Download the "filesystem" folder** from Output > Output Files (the 33 generated docx).
2. **Read every world file containing key facts** and all files relevant to each task - this is a stated validation you confirm later.
3. **Edit independently**, not just AutoQC flags: "Synthetically generated files are not 100% reliable, so we rely on you to use your judgement and expertise."
4. **REMOVE TASK-SPECIFIC FILES FROM THE WORLD (ship-blocker).** The world / Golden World Files must NOT contain files intended for an individual task. For Korvin: remove the 7 task-level files - E1-T1 discharge_medication_reconciliation_request_05242026, E1-T2 discharge_summary_request_05242026, E1-T3 discharge_readiness_care_coordination_request_05242026, E1-T4 consultant_synthesis_care_plan_request_05242026, E1-T5 post_discharge_followup_request_05312026, E1-T6 readmission_risk_review_request_06232026, E2-T1 medication_safety_handoff_addendum_05242026. **Final filesystem = 26 files (22 EW + 4 WS).** Preserve the 7 removed files locally at `worlds/korvin-merrow/file-review/task-files-holdback/` for Step 10 task setup.
5. **Upload the revision as one entire folder named exactly `filesystem`** in the run's Revisions card - individual files or a different folder name triggers an error.
6. **Apply to Task** - populates 4.1 Golden World Files. Verify the edits actually appear there.
7. **Final Files AutoQC (4.2)** is a separate new gate after Apply to Task. Every flag: fix (redo revisions loop) or address in 4.3 Notes - copy-paste the EXACT bullet text, then the reasoning (our existing notes discipline).
8. **4.4 confirmation, verbatim:** "I've looked through and completed the Final Files instructions". (Platform boilerplate mentions "10 tasks" - ours is 6 per the approved spec; the confirmation text above is the only required string.)
9. **Mark World as Finalized** does NOT create the world - continue to Section 5.0 Creating World afterward.

## 4c. OFFICIAL "How to Edit Your World-Level Files" doc (synced 6/5; full text in reference/source/ instruction doc 06_02)

Confirms our executed process step-for-step (download -> edit in place -> remove task-level files and store elsewhere -> upload entire `filesystem` folder via Add folder -> per-file comments -> Save revision -> Apply to Task -> verify 4.1). New facts it adds:

1. **NEVER Re-run Pipeline** - a new run takes ~46 hours; if a run is broken, contact the reviewer instead.
2. **Final Files AutoQC = four checks** (Integrity, Clinical, Consistency, Standards), described as "the same AutoQCs the pipeline run generated."
3. **Notes path is officially sanctioned:** "Address every flag, or note clearly why a flag is a false positive" in 4.3 - validates the false-positive note strategy for the stale-snapshot flags.
4. **Step 11 (after finalize): Part 5 -> 5.1 Run Automation -> Run**, name the world per the instruction-document conventions, Run again -> task moves to World Created stage -> pod assignment for tasking. RESOLVED 6/5: the live 5.0 platform card uses `Healthcare_Number_PatientName` (e.g. Healthcare_000_Thomas), which supersedes the instruction doc's `Healthcare_[LastName]_[###]` ordering. Number = max existing in the Worlds list + 1. Korvin shipped as **Healthcare_247_Merrow** (after Healthcare_246_Gutey).

## 4d. PLATFORM MECHANISM (Aribot-confirmed 6/5): revision vs run-snapshot scoping

The task-page 4.2 Final Files AutoQC card can audit the original stored output instead of the applied revision. Applying a revision to the task updates the task working files, but does not necessarily update the run's stored snapshot. Rerunning the same 4.2 card may therefore re-audit the original output forever.

The run-page World Files AutoQC after revision can read the revised files. It passed on the revised 26-file set before the final correct-snapshot path was resolved.

Correct rerun path:

1. Run page.
2. Diagnostics.
3. Run Final Files / pipeline AutoQC.
4. Select the applied revision ID in the popup when available.
5. If no revision picker exists, EPM/engineering must rerun the right snapshot.

Accepted alternative when the task card is stale: reviewer may accept a run-page World Files AutoQC pass on revised files in lieu of a stale task-card rerun.

World #2 lesson: after Apply to Task, do not assume the visible 4.2 card is revision-scoped. Verify the snapshot source before treating a persistent flag as content-real.

## 4e. ROOT CAUSE PROVEN (6/5, API payloads): two Apply-to-Task buttons, two different snapshots

There are two Apply-to-Task paths with different behavior:

- Run-page Actions-row Apply to Task sends `snapshot_type=output`, copies the original output, ignores revisions, and can revert the task snapshot. The official docs initially pointed writers toward this button, which makes it a documentation/platform trap.
- Revision-page Apply to Task applies the selected revision correctly.

Rule: after uploading a revision, always apply from the revision page, never the run-page Actions row. If the run-page Actions row is clicked and 4.1 reverts, restore by applying from the revision page. Verify 4.1 file count and spot-check file content after every apply.

This issue was reported to engineering with payloads.

## 5. Edit and revision workflow

Minor FIX findings can be edited directly with object-model DOCX tools, content-based locators, and integrity gates. Major FIX findings that require structural regeneration, many-file rewrite, or trap-destroying changes should be sent back for regeneration rather than patched ad hoc.

When edits are complete:

1. Upload the entire folder named exactly `filesystem`.
2. Save the revision.
3. Apply from the revision page.
4. Verify 4.1 reflects the revision.
5. Run the correct revision-scoped Final Files AutoQC path.
6. Record every edit, integrity check, platform action, and unresolved note in `file-review-log.md`.

## 6. Step 9 closeout state

Status: COMPLETE. Revision #3 passed Final Files AutoQC 78/78, notes were filed, 4.4 confirmation was submitted, the world was finalized, and 5.1 automation created `Healthcare_247_Merrow` at 2026-06-05 11:20 AM PDT. Task 1 auto-created in Task Writing. Step 10 task setup is the active stage; see `docs/world-pipeline-playbook.md` section A2.
