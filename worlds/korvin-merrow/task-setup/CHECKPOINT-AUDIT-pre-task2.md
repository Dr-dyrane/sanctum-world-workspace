# Checkpoint Audit before Task 2 (6/6/2026)

Purpose: consolidate everything learned across Task 1 (3 human-review rounds + FA/GA + PL) and reconcile it against the new Project Sanctum Instruction Document (06_02). Task 2 (KM02 Hospital Discharge Summary) starts from this, no repeated errors. Canonical source of truth remains task1-lifecycle-log.md; this file is the forward-facing pre-flight.

## PART 1 - TASK 1 ERROR LEDGER (every mistake -> the no-repeat checklist)

Round 1 (Abi first review):
- Task files leaked the answer (request memo + handoff enumerated the solution step by step). -> A task file must carry chart-absent evidence or an adversarial trap, never the answer structure.
- Task files dated 05/24 (postdated the 05/23 task). -> Date every part of a task file to the task date; scan EVERY occurrence.
- "Date / Anchor" and "Discharge anchor" project artifacts inside a task file. -> No project-artifact labels in any task file; use real clinical fields.
- Handoff signed by BOTH hospitalist and pharmacist. -> One plausible author per document.
- Golden was body-only prose. -> Golden is a full chart document (letterhead, demographics, date, signature) from the first draft.
- FA/GA analyzed "the two lowest runs"; GA said "what I missed"; GA claimed "the grader went into the chart." -> Single lowest run only; never "what I missed"; describe the grader scoring output vs golden+guidelines, not reading the chart.

Round 2 (too easy):
- All 10 trajectories >=90, no significant clinical failure. Removing the leaking task files ALSO removed the difficulty. -> Leakage and difficulty are different axes; every task needs an engineered failure mode (>=1 run <90, ideally <70) AND a significant clinical failure.

Hardening round (my own dead ends - do not repeat):
- Built a spironolactone "premature restart" trap that the chart COACHES AGAINST (nephrology rebuts it). -> A chart-coached wrong recommendation is not a trap; grep the live world to confirm the trap is uncoached.
- ARNI VALIDITY BUG: built the grader on a nephrology "conditional door" that existed only in PIPELINE markdown, not the finalized world. Repeated the anchor-on-the-primary-artifact failure. -> Verify every trap premise by reading the FULL live note in the uploaded world snapshot, not pipeline files, not keyword-grep.
- TMP-SMX antibiotic trap was not airtight (the correct answer holds RAAS, which defuses the hyperkalemia mechanism). -> A trap whose hazard depends on what the correct answer already does is not airtight.
- Hand-built the handoff from a blank Document(); fingerprint drifted; introduced Calibri (world is Arial 24/26); assumed the saturated blue band was an outlier when 13/26 files use it. -> Build task files MODE A from the held-back pipeline original; match the world fingerprint (Arial, the standard band); verify chrome against ALL live files.
- "potassium-based salt substitute" handed the model the keyword. -> A disguised-integration trap must not name the hazard; drop the qualifier.
- Grader v8 weighting language ("most discriminating", "cap the score below the passing band", "lower-weight check") tripped No Scoring Framework + No Weight Distribution. -> No numeric weights, score-cap, or pass-band language; express clinical importance in prose only.

FA / GA / PL stage:
- FA and GA submitted as a single paragraph -> "Appropriate Length" wants MORE than one paragraph. -> Two short paragraphs each (did-well / failed; grader-right / grader-wrong).
- FA/GA ran long vs Abi's samples. -> Match her ~1 short paragraph-per-part length.
- PL: stripped the dimension labels to prose (wrong). The appendix PL example USES the dimension labels as headers AND ends with a Summary. -> FA/GA = header-free prose; PL = labeled sections + Summary. Different formats.
- Tech-issue dismissal: the dedicated RLS reasoning field (field_f53...) was under-filled with only "tech issue." -> The Section-4 thumbs-down response stays exactly "tech issue"; the dedicated reasoning field this later AutoQC reads needs one substantive sentence saying why the flag does not apply.
- Pointed to a Google Doc backup when the workspace persists. -> Save backups as files in platform/taskN/.
- Reprinted file-meta headers ("Justification (paste-ready)") into the comment box. -> Paste only the content; no meta headers.
- Did not log the PL stage in the canonical log until reminded. -> Log every stage in task1-lifecycle-log.md as it happens.

## PART 2 - INSTRUCTION DOC (06_02) ALIGNMENT - things we did NOT fully meet

### 2a. GRADER GUIDELINE FORMAT - RESOLVED by our own lived record (do NOT switch to A/B/C)
CORRECTION (6/6, after reading docs/world-pipeline-playbook.md A3): an earlier draft of this section recommended switching to the doc's A/B/C format. That is WRONG and would re-break the gate. Lived record: in Task 1 Step 11 the doc's golden-response A/B/C structure produced 4 grader-guideline FAILS (Task Context Section, Golden Answer Referenced, No Weight Distribution, Human-Written Guidelines). The grader-guideline AutoQC gate wants the NATIVE structure: (a) opening Task Context paragraph; (b) golden named by exact uploaded filename; (c) "Must be present and correct" + "Acceptable variation" + "Penalize for"; (d) varied prose; mechanism-agnostic; NO weighting/score/band language. Our v10 cleared 68/68 on exactly this. KEEP THE NATIVE FORMAT for Task 2.
Residual tension (not a blocker): the instruction doc's GG examples AND the GA checklist ("name Section A/B/C") assume A/B/C, but the live gate rejects A/B/C. The gate is binding. For the GA, reference the grader's native sections (Must be present / Acceptable variation / Penalize for) instead of forcing A/B/C labels, and still recommend a concrete grader edit. Flag to Abi for awareness only; do not change the grader format.

Instruction-doc note: the 06_02 appendix examples use A/B/C labels, but our live Task AutoQC result is more specific for this world. Treat A/B/C as conceptual guidance only. The platform-safe grader upload format is native sections: Task Context, Golden Reference, Must be present and correct, Acceptable variation, Penalize for.

### 2b. GRADER ANALYSIS - our Task 1 GA was non-conformant to the official checklist
The GA checklist requires concise prose, focus on the grader not the agent, identify both what the grader caught and missed, comment on whether the score was fair, recommend at least one concrete edit to the grader guidelines, and flag any failure mode to add. Because our uploaded grader guidelines use native sections rather than A/B/C, Task 2 GA should reference the native section names (`Must be present and correct`, `Acceptable variation`, `Penalize for`) instead of forcing A/B/C labels.

### 2c. FAILURE ANALYSIS - meet the content standards, not just the prose format
Official FA standards: be specific not generic; NAME THE DOCUMENT(S) the reviewer should check to verify; separate clinical error from formatting preference; QUANTIFY the consequence (thresholds, mortality, mechanism); write for a non-specialist; distinguish severity tiers. Our Task 1 FA was correct prose but did not cite the specific files to verify or quantify the consequence. -> Task 2 FA: name the files, quantify the harm, keep Abi's prose-no-header format.

### 2d. GOLDEN RESPONSE - rules to bake in
- The golden SETS THE CEILING: no agent output may be better in any respect; if a trajectory beats it, improve the golden before proceeding.
- PLACEHOLDERS over fabrication: where the world files lack a value, write an explicit placeholder ("[No documented baseline weight available]"), never a plausible invented value. The golden must model this.
- The golden must receive FULL MARKS under your own grader guidelines; if not, fix one or the other.
- Match the deliverable format, length, and audience the prompt implies (a discharge summary is written as the discharge summary).
- The grader guideline must NOT penalize anything the golden response itself does (explicit QC checklist item).

## PART 3 - TASK 2 (KM02 Hospital Discharge Summary) PRE-FLIGHT CHECKLIST

Design:
- [ ] Engineered failure mode decided FIRST. KM02's designed trap (per brainstorm) is narrative copy-forward: the summary must NOT import the early sepsis-only framing as the final hospital course after later documents clarify the multifactorial, noninfectious contributors. The forced-choice/disguised-integration discriminator should be confirmed against the live world (what can a strong model not avoid). Concentrate the hardest stumping in KM04/KM06; KM02 may, like KM01, top out at a forced-choice discriminator.
- [ ] Confirm the trap is UNCOACHED in the live world (grep the snapshot; do not rely on pipeline files).
- [ ] If a task file is used, it carries a trap or chart-absent evidence, single author, task-dated, no project artifacts, built MODE A from a pipeline original, Arial + standard chrome.

Prompt:
- [ ] Short clinician ask in the writer's voice; no enumerated answer structure; scope only what a real attending would say.

Golden (golden-response-task2):
- [ ] Written AS the discharge summary, full chart document, demographics header AT TOP, date 05/23 (prepared for 05/24), signature block.
- [ ] Placeholders not fabrication for any gap; sets the ceiling; would earn full marks under the Task 2 grader.
- [ ] Physician sign-off (Alexander owns the clinical ceiling).

Grader (grader-guidelines-task2):
- [ ] Native platform-safe structure: Task Context, exact Golden Reference filename, Must be present and correct, Acceptable variation, Penalize for.
- [ ] Include fabrication protection in Acceptable variation / Penalize for language without turning it into A/B/C labels.
- [ ] Importance as clinical prose only; NO numeric weights, score caps, bands, or grader-ranking labels.
- [ ] Names the exact golden filename; does not penalize anything the golden itself does.

Run + QC:
- [ ] Task AutoQC: rerun N failing only; justify variance flags after reading exact text; fix structural flags.
- [ ] Taiga QC: respond to EVERY Env Linter + Data Quality flag. Tech issue = thumbs down + Section-4 response exactly "tech issue" AND a one-sentence substantive reason in the dedicated reasoning field.
- [ ] Pull the lowest-run grading transcript before FA/GA; read both shipped docs in full for PL.

FA / GA / PL:
- [ ] FA: prose, two short paragraphs, single lowest run, name the files, quantify consequence, separate error from style.
- [ ] GA: prose, focus on grader, reference native grader sections, caught vs missed, score fairness, recommend >=1 concrete grader edit.
- [ ] PL: labeled sections (Preferred output / Justification / Prompt adherence / Correctness / Completeness / Methodology / Quality and clarity / Summary); tier matches the gap (a "1" if both are clinically correct); read both docs in full; no clinical-error claim unless one exists.
- [ ] Backups as workspace files; log every stage in the lifecycle log as it happens.

Pre-submit:
- [ ] Reach out to Abi before submitting where a judgment call is borderline; she offered the pre-check.

## OPEN ITEMS TO RAISE WITH ABI
1. Confirm with Abi only if challenged: native grader structure is the upload-safe format for Korvin despite A/B/C examples in the instruction appendix.
2. Confirm the forced-choice discriminator is an acceptable clearance pattern for the med-rec-adjacent tasks, with the deep stumping concentrated in KM04/KM06.
