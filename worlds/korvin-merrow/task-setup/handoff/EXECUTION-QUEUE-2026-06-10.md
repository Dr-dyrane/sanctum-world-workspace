# Execution queue + throughput note + commit plan (6/10/2026 late)
Prepared under Alexander's "follow recommendations" direction. Three sections: the PL submission queue (ready now), the Slack throughput note (paste-ready), the real-environment commit plan.

## 1. PL submission queue - all twelve drafts ready, verified current-generation

Audit result: KM03, KM04, KM05, KM06 each have three PL drafts on STUDIO-SELECTED pairs. Pair-to-run verification: KM03 pair scores (0.90/0.88) match post-Sang rerun 8e97cdd7; KM04 (0.40/0.35) match post-Sang 979dccde, NOT the superseded 709be0e8; KM06 justification content confirms v5 insulin task (hold-at-18 profile). Six files carried "Section A/B/C" references; all reworded to spelled-out content 6/10 per Abi's self-containment update, zero remaining across all twelve. The old KM04/KM05/KM06 recommended-verdicts DRAFT files cite earlier jobs - they are planning history, NOT the entry text; enter from the PL1/PL2/PL3 files only.

Submission order (Alexander operates; run Preference Labels AutoQC after EACH per pod rule):
1. KM03 PL1 -> PL AutoQC -> PL2 -> AutoQC -> PL3 -> AutoQC -> request final review (Sang)
2. KM04 PL1-3 same cadence -> final review
3. KM05 PL1-3 -> final review
4. KM06 PL1-3 -> first human review continues in parallel
Each PL: paste the labeled-section + Summary format (PL keeps its dimension labels; only grader Section-letter references were removed). Read both transcripts end to end before entering the verdict, per the standing rule.

## 2. Throughput note to Rose/Abi (paste-ready, verified numbers)

Quick delivery-context note from the Korvin Merrow world (Healthcare_247_Merrow). Current state: six tasks RFD or one PL-step from final review (KM01-06), one in pilot (KM07), three more fully staged for entry (KM08-10), target ten per the new guidance. Getting the six banked tasks past the no-moderate difficulty bar took repeated empirical redesign on a fixed world: across the suite we ran roughly twenty 10-trajectory pilot cycles (KM02 x3, KM03 x3, KM04 x3, KM05 x3, KM06 x5 including the all-catch rerun, KM07 x1, KM08 x1, plus KM01), retiring too-easy versions at 93-98 means until each task produced genuine clinical failures. The published timebox prices one task end-to-end at 8-10 hours; the redesign-to-bite reality on a fixed world ran well past that per task, with most build/verification work done off-clock. Sharing so tracked hours are read against delivered scope, and because the variety guidance for future worlds (which we have adopted: a structure-first dossier now gates our next brainstorm) should reduce redesign cycles substantially on World #2.

## 3. Real-environment commit plan (sandbox does not commit; guardrail)

Verify tree, then:
git add worlds/korvin-merrow/task-setup/platform/task7 worlds/korvin-merrow/task-setup/platform/task8 worlds/korvin-merrow/task-setup/platform/task9 worlds/korvin-merrow/task-setup/platform/task10 worlds/korvin-merrow/task-setup/task7 worlds/korvin-merrow/task-setup/task8 worlds/korvin-merrow/task-setup/task9 worlds/korvin-merrow/task-setup/task10 worlds/korvin-merrow/task-setup/task4/preference-labeling worlds/korvin-merrow/task-setup/task5/preference-labeling worlds/korvin-merrow/task-setup/task6/preference-labeling worlds/korvin-merrow/task-setup/handoff tools/build docs/task-structure-dossier.md docs/world-pipeline-playbook.md docs/agent-workflow.md docs/CONTRIBUTING.md docs/git-workflow.md docs/reviewer-response-protocol.md docs/status-dashboard.md reference/checklists/brainstorm-checklist.md reference/world-spec-guidelines/POD-ANNOUNCEMENT-2026-06-10-delivery-day-and-operating-rules.md reference/source/task-selection-categories-snapshot-2026-06-10.csv WORKSPACE_FILE_MAP.md worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md

git commit -m "checkpoint 6/10: KM07v2+KM08v4.1 staged, KM09/KM10 v1 packets built, PL set section-name fix, structure dossier + variety gate wired, cold-start repairs, pod rules recorded"

Also delete (already absent in sandbox view; verify gone): platform/task8/current/neuropathic_pain_sleep_addendum_draft_05222026.docx and stale .git/index.lock (both handled 6/10 via granted delete access; confirm on the real tree).

## 4. One-line addendum for TASK2-STATE (entered 6/10)
The local platform/task2/current base copies carry python-docx core-metadata stamps (post-upload local re-save); the platform copies passed AutoQC and derived task files are scrubbed at build, but do NOT re-upload these local copies anywhere without a scrub_core pass first.
