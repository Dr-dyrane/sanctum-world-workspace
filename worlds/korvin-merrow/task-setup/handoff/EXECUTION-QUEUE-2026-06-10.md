# Execution queue + throughput note + commit plan (6/10/2026 late)

SUPERSEDED STATUS NOTE, 2026-06-13: this queue is historical and must not be executed as current platform guidance. Current Korvin state is: KM01 through KM06 delivered, KM07/KM08/KM10 Ready for Delivery, and KM09 Awaiting Final Review after wording-clean job `212c496b`, FA/GA, and three post-rerun PLs. Use `AGENTS.md`, root `WORKSPACE_FILE_MAP.md`, `KM-WORLD-PERFORMANCE-REPORT.md`, the dashboard, and active `TASKN-STATE.md` files for live work.

Prepared under Alexander's "follow recommendations" direction. Three sections: the PL submission queue (ready now), the Slack throughput note (paste-ready), the real-environment commit plan.

## 1. PL submission queue - all twelve drafts ready, verified current-generation

Audit result: KM03, KM04, KM05, KM06 each have three PL drafts on STUDIO-SELECTED pairs. Pair-to-run verification: KM03 pair scores (0.90/0.88) match post-Sang rerun 8e97cdd7; KM04 (0.40/0.35) match post-Sang 979dccde, NOT the superseded 709be0e8; KM06 justification content confirms v5 insulin task (hold-at-18 profile). Six files carried "Section A/B/C" references; all reworded to spelled-out content 6/10 per Abi's self-containment update, zero remaining across all twelve. The old KM04/KM05/KM06 recommended-verdicts DRAFT files cite earlier jobs - they are planning history, NOT the entry text; enter from the PL1/PL2/PL3 files only.

Submission order (Alexander operates; run Preference Labels AutoQC after EACH per pod rule):
1. KM03 PL1 -> PL AutoQC -> PL2 -> AutoQC -> PL3 -> AutoQC -> request final review (Sang)
2. KM04 PL1-3 same cadence -> final review
3. KM05 PL1-3 -> final review
4. KM06 PL1-3 -> first human review continues in parallel
Each PL: paste the labeled-section + Summary format (PL keeps its dimension labels; only grader Section-letter references were removed). Read both transcripts end to end before entering the verdict, per the standing rule.

## 2. Throughput note to Rose/Abi (historical 6/10 draft, do not paste as current)

Historical 6/10 draft: Quick delivery-context note from the Korvin Merrow world (Healthcare_247_Merrow). At that point, six tasks were RFD or one PL-step from final review, KM07 was in pilot, and KM08-KM10 were staged. Current 2026-06-13 state is materially later: KM01 through KM06 delivered, KM07/KM08/KM10 Ready for Delivery, and KM09 Awaiting Final Review after wording-clean job `212c496b`, FA/GA, and three post-rerun PLs. Use the board, dashboard, and task cockpits for any fresh throughput note.

## 3. Real-environment commit plan (sandbox does not commit; guardrail)

Verify tree, then:
git add worlds/korvin-merrow/task-setup/platform/task7 worlds/korvin-merrow/task-setup/platform/task8 worlds/korvin-merrow/task-setup/platform/task9 worlds/korvin-merrow/task-setup/platform/task10 worlds/korvin-merrow/task-setup/task7 worlds/korvin-merrow/task-setup/task8 worlds/korvin-merrow/task-setup/task9 worlds/korvin-merrow/task-setup/task10 worlds/korvin-merrow/task-setup/task4/preference-labeling worlds/korvin-merrow/task-setup/task5/preference-labeling worlds/korvin-merrow/task-setup/task6/preference-labeling worlds/korvin-merrow/task-setup/handoff tools/build docs/task-structure-dossier.md docs/world-pipeline-playbook.md docs/agent-workflow.md docs/CONTRIBUTING.md docs/git-workflow.md docs/reviewer-response-protocol.md docs/status-dashboard.md reference/checklists/brainstorm-checklist.md reference/world-spec-guidelines/POD-ANNOUNCEMENT-2026-06-10-delivery-day-and-operating-rules.md reference/source/task-selection-categories-snapshot-2026-06-10.csv WORKSPACE_FILE_MAP.md worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md

git commit -m "checkpoint 6/10: KM07v2+KM08v4.1 staged, KM09/KM10 v1 packets built, PL set section-name fix, structure dossier + variety gate wired, cold-start repairs, pod rules recorded"

Also delete (already absent in sandbox view; verify gone): platform/task8/current/neuropathic_pain_sleep_addendum_draft_05222026.docx and stale .git/index.lock (both handled 6/10 via granted delete access; confirm on the real tree).

## 4. One-line addendum for TASK2-STATE (entered 6/10)
The local platform/task2/current base copies carry python-docx core-metadata stamps (post-upload local re-save); the platform copies passed AutoQC and derived task files are scrubbed at build, but do NOT re-upload these local copies anywhere without a scrub_core pass first.
