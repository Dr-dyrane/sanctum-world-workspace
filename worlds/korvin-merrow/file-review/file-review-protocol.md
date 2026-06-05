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

## 5. Edit and revision workflow

- Minor FIX items: edit the generated docx directly (object model, content locators, integrity gate after every save - docs/docx-generation-method.md). Keep last-valid copies.
- Major FIX items (structural, many-file, or trap-destroying): list for "Re-run Pipeline" / send back rather than hand-patching.
- When edits are complete: use the run page's **Upload revision** ("Upload a revised snapshot to start a chain of edits on this run's output"), then "Rerun 2 failing" on AutoQC, then Apply to Task.
- Record every edit in `file-review-log.md` (file, finding ID, label, change, integrity-gate result).

## 6. Outputs of this stage

1. `findings-triage.md` - all 95+13+71 findings, each labeled FIX/PROTECT/NOTE with disposition.
2. `file-review-log.md` - per-edit record.
3. Revised snapshot uploaded; AutoQC rerun green (or remaining fails note-justified); task moved forward.
