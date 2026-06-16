# OV Floor-Mechanism Library and Difficulty Reference (CANONICAL)

Date: 2026-06-15. Purpose: the single OV-specific reference for designing floor tasks, built from the three sources Alexander named (the KM world's 10 banked tasks, the reference example worlds, and Raising_Task_Difficulty_Worked_Example.pdf) PLUS OV's own bench evidence. Read this before designing any new OV task.

This file SUPERSEDES the earlier OV inferences that the world is "substrate-limited / capped at one-two floors" and that the move is to "build a conflict-first next world." Those were wrong: they came from measuring OV against its own mis-executed attempts instead of the KM recipes. A clean, internally-consistent chart is the IDEAL substrate; floors are MANUFACTURED AT THE TASK LAYER on top of it. Goal: 8 floors in THIS world.

General playbooks this builds on (do not duplicate, cite): docs/task-difficulty-lessons.md (the KM difficulty playbook - already correct; it names this recipe), docs/km-tasking-playbook.md, reference/source/Raising_Task_Difficulty_Worked_Example.pdf.

================================================================
## 1. THE MASTER PRINCIPLE (the one thing) - PRIMED vs UN-PRIMED axis
================================================================
This model reads a clean chart EXTREMELY well and reflexively polices the things clinicians police. It therefore CEILINGS whenever the catch sits on a PRIMED/LOUD axis - one the model is already scrutinizing - and FLOORS only when the catch sits on an UN-PRIMED axis where the model has no reflex pulling it there.

- PRIMED / LOUD axes (model scrutinizes -> catches -> CEILING): vitals (it always re-reads a number against the trend), the deliverable's headline problem, any item the chart explicitly flags open/unresolved, patient identity (it guards against mix-ups), "don't restart meds without labs," "don't fabricate," "don't over-treat."
- UN-PRIMED axes (model has no reflex -> trusts/───skips -> FLOOR): cold outside-knowledge it lacks; a quiet axis the chart is SILENT on the status of; a finding that requires proactive synthesis the completion frame suppresses.

Every OV result below is explained by this one axis. Design rule: put the catch on an UN-PRIMED axis, and never telegraph it.

The worked-example recipe is the operational form of this: (1) PULL THE ANSWER KEY (no file states the conclusion); (2) FORCE RECONCILIATION (no single file complete); (3) DON'T SPELL OUT THE TRAP (off-text / un-primed); (4) MATCH THE GRADER TO THE STAKES (hard cap); (5) KEEP IT TRUE TO PRACTICE.

================================================================
## 2. OV BENCH-EVIDENCE LEDGER (what we have actually tested) - the empirical core
================================================================
| Lever | Mechanism | Axis | Result | Why |
|---|---|---|---|---|
| OV01 (banked) | cold outside-knowledge: stop inpatient-only enoxaparin at discharge | un-primed (no reflex) | FLOOR (banked, ~0.50 2nd-lowest) | model lacks the specific stop rule |
| OV02 Path A (fair floor) | off-text new problem (infected IV line) under a COMPLETION frame | un-primed (proactive hunt suppressed by "finish the note") | FLOOR (pilot 10/10 ~0.10, fair) | model doesn't proactively assemble a new problem while filling sections |
| OV04 CPAP/OSA over-closure (KM03 port) | propagate a FABRICATED closure inherited in a started draft ("CPAP reviewed, adherence adequate, no follow-up") | un-primed (nobody checks OSA adherence) | FLOOR - bench 3/3 PROPAGATED | verification asymmetry: model trusts an inherited assertion on a quiet axis |
| Anemia over-closure (KM04 port) | same as CPAP but on the anemia axis | PRIMED (EW18 literally flags anemia "open") + my bench telegraphed it | CEILING (bench caught) | loud axis + telegraphed; mechanism-fit error, not a family failure |
| Timeline-miss HR 50 (in-range-but-deranged vital) | off-text deterioration via a normal-range vital alarming vs the trend | PRIMED (vitals - the model always re-reads a vital vs trend) | CEILING - bench caught both framings incl. completion | HR 50 vs a documented 80-104 with no rate agent is too loud; vitals are the most-primed axis |
| Held-med restart on unverified self-report (KM05 port) | commission/withhold: don't restart on patient's "good readings" | PRIMED ("no restart without labs" reflex) | CEILING (bench caught) | model is primed to withhold |
| Cross-talk / wrong-patient contamination (Edmund T6 port) | pull a neighbor's datum (MRSA/allergy) into Vasquell's note | PRIMED (model guards patient identity) | CEILING - bench segregated + flagged the hazard | model actively guards against labeled mix-ups |
| Image-miss (OV02 v6; ABI toe-waveform OV03 image draft) | finding only in a task-level image | n/a | BROKEN | harness is image-blind (agent has only bash, "text-only environment"); not a fair floor |

KEY READS: over-closure FLOORS on an un-primed axis (CPAP) and CEILINGS on a primed one (anemia). Vitals, identity, restart-without-labs, over-treatment, fabrication are all primed -> those levers ceiling. Images are dead in this harness.

================================================================
## 3. PROVEN MECHANISM LIBRARY (the menu) - from KM + the example worlds
================================================================
Mechanism-class frequency: KM = embedded over-closure x4 (KM02/03/04/07; KM's best floor, KM02 had 6 sub-70), commission/decisiveness x3 (KM05/06/10), conflicting/wrong-authority x2 (KM01/09), off-text/omission x1 (KM08). Opus/Chen suite = off-text synthesis x6, conflicting/wrong-authority x4, baseline/number-trap x5, commission x4, embedded-wrong x3, superseded-rec x3, omission/scope x3, adversarial-noise x2 (T6). World specs (Caduceus/Pemberton/Whitfield) add: cold regulatory knowledge, copy-forward-as-false-authority, inverted data hierarchy, decoys/ghost-meds/wrong-patient bottles, confirmed-dx-only coding traps.

Families ranked by OV fit. CORRECTION 2026-06-15 (after OV04 v3 + the KM08 ledger): images are NOT harness-blind - the agent reads them unreliably, and that unreliability IS the floor (OV04 v3 CPAP report piloted a clean bimodal). And over-closure-via-propagation is UNFAIR (QA jqxv7246) while placeholder-over-closure is TOO EASY (KM08 v5). THE LIVE ENGINE is an OFF-TEXT FINDING under a plain prompt - an image (OV04) or a buried-text item (OV02) the model must proactively read - fair via construction, never telegraphed. Read the families below through that lens:
1. EMBEDDED OVER-CLOSURE on an UN-PRIMED axis (KM02/03/04/07). PROVEN on OV (CPAP). A started draft falsely CLOSES a quiet axis with a fabricated OBJECTIVE claim a clean chart rebuts. Rules (paid for by KM + anemia): fabricated-objective (not a buried fact, not a chart-coached rec); UN-PRIMED axis (chart silent on its status - NOT a chart-flagged-open item); keep ABSTRACT (no concrete wrong agent to pattern-match); TRUE placeholder (item absent/open, not routine-looking); pure-completion prompt, NO reconcile-and-correct clause; rest-of-draft correct so the model trusts it; chart-aware grader + anti-paralysis floor. NOTE: as a STANDALONE engine this is SUPERSEDED - propagation is unfair and a true placeholder is too easy (the OV04 v1/v2/v3 saga). It only works reframed as an off-text finding (OV04 v3).
2. CONFLICTING / WRONG AUTHORITY via a MOUNTED external instrument (KM01 pharmacy handoff, KM09 HIM worksheet). The wrong rec lives in a task-layer instrument the model checks against the clean chart and rejects; fairness from the external-query genre; MOUNT the actual instrument. UNTESTED on OV - bench next.
3. OFF-TEXT SYNTHESIS under a completion frame (OV02; Opus 6/7). PROVEN (OV02). The new problem is prose-silent and the "finish it" frame suppresses proactive hunting. Hard to re-use without correlating with OV02.
4. COLD outside-knowledge (OV01; Caduceus/Whitfield). PROVEN (OV01). Scarce clean cold facts left in OV.
DEPRIORITIZED on OV (ceiling on primed axes): commission/withhold (KM05/06 - model primed), decline-the-upgrade coding (KM10 - coding genre model-strong here), adversarial cross-talk (model guards identity), timeline-deterioration-on-vitals (vitals primed).

================================================================
## 4. REFINED BUILD + FAIRNESS RULES
================================================================
- Bench-first, ALWAYS, before any pilot. Cold reviewer, harness-matched, no golden/grader.
- Bench rule (text levers): reviewer-CATCH = ceiling signal -> rework/drop; reviewer-MISS/PROPAGATE = floor candidate -> pilot. (For the dead image lever this inverted, but images are out.)
- Do NOT telegraph in the bench: present the chart as the harness sees it; never pre-digest the contradiction or name the absence (the anemia-bench error).
- Fairness: the floor must be both INDEFENSIBLE-to-miss (real harm) AND FEASIBLE-to-miss (data as it really arrives). Easy+indefensible = ceiling; hard+defensible = no stakes.
- Frozen-world: task-layer artifacts only (started draft / mounted instrument / clinic note); reuse frozen files as backdrop; never edit world files (DO-NOT-REPEAT #21).
- Harness: image-blind (agent = bash, text only). No image levers. Mount only text the agent can read.
- Grader: five-block KM style, chart-aware, CAP the central failure (don't piecemeal-deduct), anti-paralysis floor (refusing to finalize is not free credit), credit correct restraint, verification-to-grader (treat output as untrusted, do not credit fabricated citations).
- FA/GA from the 2nd-LOWEST percent score (#20). One embedded re-roll then retire (#19).

================================================================
## 5. OV UN-PRIMED-AXIS INVENTORY (over-closure candidates)
================================================================
Chart is SILENT on the status of (good over-closure targets): OSA/CPAP adequacy (CONFIRMED floor); bone-health / CKD-MBD (on cholecalciferol, no DEXA/status note); health-maintenance/immunization status; foot-care self-management competency. Each distinct un-primed axis is a potential distinct over-closure floor.
LOUD/PRIMED axes - do NOT use for over-closure (chart flags them, model catches): anemia (EW18 "open item"), perfusion/PAD ("not resolved"), osteomyelitis ("not established"), held-med restart ("parameter-gated"), glycemic, and ALL vitals.

================================================================
## 6. PATH TO 8 (current)
================================================================
1. OV01 - cold knowledge (BANKED). 2. OV02 - off-text text synthesis (fair floor; needs golden self-score before bank). 3. OV04 - off-text IMAGE finding (CPAP compliance report; v3 piloted CLEAN BIMODAL, 4 floors / 6 catchers; BANKED). 4. OV05 - off-text MED-RECONCILIATION finding via a home-med-bottle photo (unlisted OTC ibuprofen, nephrotoxin in AKI/CKD; reuses the OV04-v3 engine) -> CHOSEN 2026-06-15, build + cold-bench (slot task5). 5. mounted-instrument / conflicting-authority (KM01-style external handoff with a planted unsafe rec) -> UNTESTED on OV, bench carefully (may ceiling as a primed behavior). 6-8. additional off-text findings on un-primed axes (bone-health/CKD-MBD, health-maintenance) and/or the mounted-instrument family; bench each. THE LIVE ENGINE is off-text findings (image or buried text) under a plain prompt, fair via construction - not over-closure.

================================================================
## 7. SOURCES + EVIDENCE FILES
================================================================
- General playbooks (correct, cite): docs/task-difficulty-lessons.md (names this recipe at its section 3), docs/km-tasking-playbook.md, reference/source/Raising_Task_Difficulty_Worked_Example.pdf.
- OV slate + bench detail: phase-4-pilot-review-submit/OV-PATH-TO-8-km-ported-2026-06-15.md.
- KM mechanism extraction + example-world extraction: captured in OV-WORLD-STATUS activity log (2026-06-15 entries) and this file.
- SUPERSEDED (kept for history, banners added): docs/edmund-chen-difficulty-engine-distillation.md (mechanism extraction valid; "OV substrate-limited / next-world" implications wrong); phase-4-pilot-review-submit/results/OV03-text-floor-hunt-2026-06-15.md (no-go conclusion wrong - over-closure was the untried recipe).
