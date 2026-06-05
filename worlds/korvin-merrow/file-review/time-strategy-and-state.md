# Step 9 Time Strategy (6 hrs/week cap) + Current State + Claude Kickoff Prompt

Date: 2026-06-04.

## 1. Current state (single source of truth)

- World Spec APPROVED (Stacey, 6/4). Pipeline run #1 complete (10:20 AM PDT 6/4): 167 output files (33 generated world docx + 134 .meta).
- World Files AutoQC: 74/76 pass. Both fails are access-failure routing (auditor sandbox could not read files; pipeline self-report ship_status="needs_review") - by design, this stage IS the human review.
- Findings to triage: 95 actionable, 13 red-team, 71 cross-doc (in the .meta files).
- Hours: cap auto-updated to 6 hrs/week (stage budget, confirmed automatic in #sanctumhelp - Rachel C, Lead EPM). Insightful project Sparta-Sanctum, task timer working; 1:00 onboarding hour logged.
- $2,000 onboarding milestone: condition met 6/4 (spec approved within attempts). Mercor payouts run WEDNESDAYS (per #sanctumhelp). Expect 6/10. Escalate in #sanctumhelp only if missing after that.
- Official workflow video confirms: writers use Claude for pipeline fixes with (a) latest world spec, (b) writer self-AutoQC prompt doc `AutoQC_Section_3_World_Files_v6.6_writer.docx` (get from channel links/pins), (c) zipped world files.
- Protocol: worlds/korvin-merrow/file-review/file-review-protocol.md (triage taxonomy FIX/PROTECT/NOTE + trap-fidelity checklist).

## 2. The 6-hour split (clock ONLY during these blocks; hit play on Sparta-Sanctum - Task)

Principle: Claude does the mechanical work off your clock (inventory, extraction, diffs, draft triage, candidate edits). Your clocked time is physician judgment and platform actions only.

| Block | Time | On-clock activity |
|---|---|---|
| B1 | 0.5h | Watch rest of video; collect self-AutoQC writer doc; Download All from run page; drop into workspace |
| B2 | 1.5h | Review Claude's findings-triage draft; rule on every FIX/PROTECT/NOTE call; rule on prednisone-adjacent findings personally |
| B3 | 2.0h | Review + approve candidate edits; spot-check edited files (trap-fidelity checklist); sign off file by file |
| B4 | 1.0h | Run self-AutoQC prompt on revised set; Upload revision on run page; Rerun 2 failing; verify |
| B5 | 1.0h | Buffer: regeneration requests if majors found; Slack comms; Apply to Task |

Rules:
- Never clock idle waiting (renders, downloads, Claude runs). Pause the timer.
- Batch platform work - RL Studio actions in one sitting.
- If triage reveals majors needing engineering regeneration, that's a send-back, not your hours - flag early in B2.
- Week boundary: if 6h runs out mid-stage, stop, note position in continuation log, resume next week. Quality of the trap review beats speed.

## 3. Kickoff prompt for the Claude working session (paste when output files are in place)

> I'm at Step 9 (Ready for Pipeline Fixes) for the Korvin Merrow world. The pipeline output is now at `worlds/korvin-merrow/file-review/pipeline-output/` (33 generated world docx + 134 .meta files). The writer self-AutoQC prompt doc is at [path after download].
>
> Off-clock prep, in order:
> 1. Inventory the 33 generated files against the spec file plan (set equality on names; integrity gate each file).
> 2. Extract every finding from the .meta files (95 actionable, 13 red-team, 71 cross-doc) into `findings-triage.md`, each pre-labeled FIX/PROTECT/NOTE per file-review-protocol.md section 3. Anything touching prednisone, EW22 completeness, EW17-EW19 burial, or consultant disagreement defaults to PROTECT pending my ruling.
> 3. Run the trap-fidelity checklist (protocol section 4) and report violations - especially any generated prednisone dose/frequency anywhere (grep all paragraphs AND table cells) and any canon-dose drift against the 12 approved values.
> 4. Prepare candidate edits for clear FIX items (object model, content locators, integrity gate, keep last-valid copies) but DO NOT apply anything labeled PROTECT and do not apply edits until I review the triage.
> Then give me the B2 review packet: triage table, trap-fidelity report, candidate-edit list with before/after.

## 4. Open admin items

- [ ] $2,000 milestone: check payout Wednesday 6/10; escalate in #sanctumhelp after only.
- [ ] Collect `AutoQC_Section_3_World_Files_v6.6_writer.docx` from channel links/pins; save to reference/.
- [ ] No Slack ask needed on hours (cap auto-updated). Optional one-liner to Stacey: "Files generated - starting my review."

## 5. Claude provenance rule for this phase

- Claude may assist with inventory, metadata extraction, trap-fidelity checking, candidate edit drafting, and review packet organization.
- Track Claude-assisted outputs in this folder as phase-specific review/remediation provenance, especially `findings-triage.md`, future edit logs, and final response notes.
- Do not append this work to the original onboarding Claude transcript unless the platform explicitly requests a new transcript package.
- Alexander's physician rulings remain authoritative for every `[A]` item, prednisone-adjacent finding, trap-preservation decision, and upload/revision action.
