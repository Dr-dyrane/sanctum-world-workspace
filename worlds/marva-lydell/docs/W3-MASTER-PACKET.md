# World 3 Master Packet - Marva Lydell (cardiorenal respiratory transition readiness)

Date: 2026-06-18. Status: PLANNING. This is not a build authorization. No world files, task files, prompts, goldens, graders, uploads, or trajectories follow from it until Alexander authorizes each step. It builds on, and does not replace, `worlds/marva-lydell/docs/PLANNING-CANVAS.md`, `docs/BRAINSTORM-DRAFT.md`, and `docs/WORLD-STATUS.md`. Its evidence base is the cross-world audit in `worlds/ondina-vasquell/docs/OV-BOOTSTRAP-AUDIT-AND-CEILING-FLOOR-ENGINE.md`, the KM performance report, the Chen/Opus and Marcus/Harold example worlds, `docs/task-structure-dossier.md`, and `docs/task-difficulty-lessons.md`.

Patient and spine (Brainstorm-level, pending Phase A ratification): Marva Lydell, 72-year-old Black woman, acute decompensated heart failure with CKD, atrial fibrillation, and COPD or OSA overlap, improving at rest but unsafe with exertion and home logistics. Snapshot 07/10/2025; task window 07/11/2025 through 07/17/2025. Race is background chart context, never a scoring lever.

================================================================
## Part 1 - Cross-world comparison audit
================================================================

### 1a. Korvin Merrow (World 1, Healthcare_247_Merrow) - the scoreboard

| Task | Lever | Structure | Mean | Read |
|---|---|---|---|---|
| KM01 | unsafe med rec, prednisone-from-fill inference | S2 inventory | 89 | soft, banked |
| KM02 | urine-culture embedded-wrong on a cold secondary axis | S1 completion | 59 | deep |
| KM03 | CPAP adequacy over-closure | S1 completion | 76 | deep |
| KM04 | iron/anemia over-closure | S1 completion | 66 | deep |
| KM05 | premature restart on home BP, commission | S1 completion | 47 | deep, bimodal |
| KM06 | premature insulin uptitration on home glucose, commission | S1 completion | 60 | deep, bimodal |
| KM07 | bone-health false closure, true placeholder | S6 referral | 59 | deep (v4) |
| KM08 | off-text bedside wound photo miss | S1 progress note | 21 | all-floor |
| KM09 | sepsis-to-principal sequencing | S2 coding | 87 | soft, 1 sub-70 |
| KM10 | encephalopathy CDI decline | S3 query | 23 | all-floor |

Mechanism frequency: embedded over-closure x4 (KM02/03/04/07), commission/decisiveness x3 (KM05/06/10), conflicting or wrong authority x2 (KM01/09), off-text/omission x1 (KM08).

### 1b. The KM structural autopsy (the root-cause lesson, paid for once)

Every KM task reduces to two structures, forced-inventory and draft-and-finalize completion, because the world was built first and the structures chosen after, so the only difficulty lever left was the completion wrapper. Eight of ten became the same shape and several cleared high (KM06 echo 97, KM05 NSAID 95, KM08 status 96). The fix, now standing doctrine: pick five or more structures at Brainstorm and build the substrate to arm each. World 3 already does this in the canvas. Hold the line.

### 1c. The example worlds (what a conflict-built world teaches)

Chen/Opus suite (62M ESBL urosepsis, cefepime neurotoxicity from renal under-dosing, eighty-file chart). The single most important finding: every one of its six tasks has the same clinical answer, so difficulty does not come from an exotic answer or one embedded line. It comes from how hard the answer is to assemble against a hostile information field. Four robust floor mechanisms, none of which is catch-one-wrong-line:

1. Conflicting authoritative sources. Three consultants each reach a defensible-but-wrong conclusion (neurology read metabolic, cardiology read embolic, attending copy-forwarded "improving on appropriate therapy"); the model must reject all three and reach the diagnosis none of them did. Fairness bar: each authority is wrong for an understandable reason, not a self-incriminating mischaracterization (which is why OV06 v1 was swatted instantly and Chen T1 floors).
2. Adversarial noise and cross-talk. A transcript weaves in fifteen other patients with overlapping features, plus corrected errors and a third-party misinterpretation the attending rejects; any decoy datum in the note is a safety failure.
3. Analytical rigor under structure (RCA). The diagnosis is easy; the floor is structure. Methodology is weighted equal to root cause: separate proximate, root, and contributing; cite policies by number; produce owned and timed corrective actions; education-only fixes are capped.
4. Commission and decisiveness under pressure. The causative agent must be STOPPED, not "consider discontinuing"; equivocal language is penalized.

Craft patterns to copy: verification-to-grader (treat the output as untrusted, spot-check citations, do not credit ones that do not exist), a planted-citation trap, a single quiet baseline number planted across the chart that must be used (baseline Cr 1.2, not the admission 1.4 or discharge 2.4), a superseded-recommendation trap (a later same-service note overrides an earlier one), and a harried time-pressured prompt that discourages exhaustive review.

Marcus (World 003) CCM care plan embeds a CYP3A4 interaction, a boxed-warning agent, an oral-iron-in-IBD error, a dose error to fix, and a specialist dose-increase to decline: embedded-wrong, catch-and-correct. Harold/Caduceus wound SOAP plants an over-staging trap and a dressing-on-intact-skin commission; the Caduceus, Pemberton, and Whitfield specs add cold regulatory knowledge, copy-forward-as-false-authority, inverted data hierarchy, decoys, ghost-meds, wrong-patient bottles, and confirmed-diagnosis-only coding traps.

### 1d. The synthesis-load insight (the central upgrade for World 3)

OV proved that a clean, internally consistent chart is workable substrate and that floors can be manufactured at the task layer (eight to ten floors). But each OV task was one clean correction in a low-conflict chart, which is why several ceilinged and the model walked straight to the answer when the genre forced the read. Chen proves the deeper axis is synthesis load: the answer is knowable but buried under competing authorities, decoys, corrected errors, and copy-forwarded narrative. World 3's largest unforced gain is to engineer conflict and synthesis load into the substrate from day one, then place the proven OV task-layer levers on top of it. This is fully compatible with the frozen-world rule because it is a Brainstorm-time substrate decision, made before any file is locked, not a mid-tasking edit.

================================================================
## Part 2 - Cross-world trap-redundancy map (Abi reads all three worlds)
================================================================

Structures repeat freely; headline traps may not. Spent across KM and OV, do NOT reuse as a World 3 bite:

- CPAP/OSA adherence (KM03 and OV04). OSA may be backdrop only.
- Generic HF management and diuresis titration (primed, ceilings).
- Generic medication restart timing on home self-report (KM05, KM06; primed).
- Stop inpatient-only prophylaxis, enoxaparin (OV01).
- Contrast-in-AKI (OV09 v1 retired; textbook rule on a contradicted loud axis).
- Wound photo as the scored miss (KM08, OV07). Not applicable to a cardiorenal world anyway.
- Buried-in-text findings (the model reads text at or above physician level).
- Headline-axis embedded-wrong (OV05, OV09 v3).
- Pure decline-the-suggestion and restraint-only coding or CDI (KM09, KM10, OV02 coding; model-strong).
- Sepsis-to-principal sequencing (KM09) and encephalopathy CDI overreach (KM10).
- Anemia, perfusion, osteomyelitis over-closure (OV loud axes).

Fresh for World 3 (un-primed on this model, on-thesis for cardiorenal respiratory readiness):

- Home oxygen qualification by exertional or ambulatory desaturation while the resting saturation has normalized. The model polices the resting saturation (a vital) but has no reflex for the exertional qualification rule.
- DME and oxygen delivery readiness (vendor delivery or setup pending or denied while the plan asserts it is done).
- Exertional physiology and ambulation safety overstated from an at-rest read.
- Post-acute ownership of anticoagulation, renal recovery, and oxygen follow-up left unassigned across competing consultants.
- Renally cleared cardiac or anticoagulant dosing (a DOAC or digoxin) carried at admission renal function rather than the recovering value, or a duplicate-anticoagulant on an external list.

================================================================
## Part 3 - World 3 thesis and the substrate upgrade
================================================================

Thesis (locked): discharge safety when the patient is improving at rest but oxygen qualification, DME delivery, exertional physiology, anticoagulation, renal recovery, and post-acute ownership are unresolved. The test is not whether the model knows heart failure treatment. It is whether it determines readiness when those threads do not line up.

The substrate upgrade (the one new design rule for World 3): build synthesis load into the chart, not just the task layer.

1. Competing authorities by design. Cardiology centers volume and diuresis, nephrology centers renal recovery and med timing, pulmonology and respiratory therapy center oxygen. Each writes a defensible-but-incomplete read; none resolves discharge readiness alone, and each is wrong for an understandable reason (the Chen fairness bar), never self-incriminating (the OV06 v1 anti-pattern). This single decision arms the conflicting-authority handoff task and raises the load on every other task.
2. A superseded recommendation. An early respiratory-therapy or pulmonary note reads room air adequate, superseded by a later same-service exertional finding. The which-note-wins axis, done with same-service supersession rather than an external instrument.
3. A quiet baseline trap. A documented pre-illness baseline (baseline creatinine, dry weight, home oxygen status) that the model must use instead of the admission or discharge value, planted consistently across the chart.
4. Decoys and corrected errors as realistic noise, never the scored item: a corrected weight, a roommate or prior-admission datum, realistic but irrelevant files to filter.
5. The harried prompt. A sign-out-at-four-o'clock, have-not-read-the-chart voice on the completion and handoff tasks. This is a free, frozen-world-safe difficulty lever OV under-used.

No answer-key synthesis lives in the shared world files; no single respiratory note resolves oxygen readiness by itself; off-text or scanned evidence is peripheral to the deliverable; payer, vendor, SNF, and pharmacy documents may be wrong by genre. At least thirty world files before spec.

================================================================
## Part 4 - The World 3 task slate (10 tasks, 7 structures)
================================================================

Completion is capped at two (T2 and T9). Each row carries the proven lever, the ceiling guard, and the expected band. Bands are design targets (floor 0.30 to 0.55 with at least one catcher above 0.85), not promises.

| # | Structure | Deliverable | Fresh axis / forced slot | Proven lever (analog) | Ceiling guard | Band |
|---|---|---|---|---|---|---|
| 1 | S3 external | Oxygen or DME denial appeal | exertional desat qualifies oxygen though resting sat normalized | off-text finding (OV04/OV07) + external wrong-by-genre | qualifying data off the denial face, in a scanned walk-test sheet peripheral to the appeal | floor |
| 2 | S1 completion (allowed) | Transition-of-care note | finalize home oxygen / DME status; draft asserts delivered or room-air adequate | embedded-wrong on a background line (OV08/OV09 v4) + off-text | background line not headline; plain harried prompt; no reconcile clause | floor |
| 3 | S4 determination | UR continued-stay note | improved markers vs unresolved exertional-oxygen or DME barrier | embedded-wrong on a background clinical-course line (OV08) | designed borderline (S4 needs it); headline stays the stay decision | floor/bimodal |
| 4 | S2 inventory | Discharge med / anticoagulation reconciliation | DOAC renal dose at admission eGFR, or external SNF list duplicate/wrong dose | forced-inventory embedded-wrong dose on a background row (OV01 shape, not OV01 axis) | a dose or duplicate row needing eGFR-and-bleeding integration, never "anticoagulate yes/no" | floor |
| 5 | S7 investigation | Safety-event RCA after a bounceback | proximate vs root vs contributing; owned, timed actions | attribution-finding + analytical rigor under structure (Chen RCA) | the floor is single-cause blame on patient nonadherence missing the failed oxygen/DME handoff, and blurred causal levels | mid |
| 6 | S6 synthesis | Cardiology-nephrology-pulmonology handoff with an embedded issue-owner table | quiet unresolved owner for oxygen, diuresis, renal-lab follow-up | conflicting authoritative sources (Chen T1) + embedded forced table | each authority wrong for an understandable reason; de-telegraphed; the owner table is the forced slot | floor/bimodal |
| 7 | S5 abstraction | HF quality or HCC abstraction | a quiet lookback-window or exclusion disqualifier tied to oxygen/readmission | forced-field abstraction (KM09 cousin) on a cold lookback axis | tie to source geometry, not a known measure trope; restraint genre runs mid | mid |
| 8 | S3 external | Prior-auth or post-acute SNF appeal | denial treats home health as enough; chart shows unsafe exertional physiology | external wrong-by-genre + off-text functional source | distinct axis from T1 (home-health adequacy, not oxygen qualification); evidence off the denial face | floor |
| 9 | S1 or S6 completion (allowed) | Post-discharge follow-up note | home report says improved; objective source shows weight or oxygen deterioration | off-text objective deterioration the model must integrate | NOT restart-on-home-readings (KM05 primed); make the objective source the embedded finding; bench cold first | mid/floor |
| 10 | S3 or S2 | CDI or coding physician review | accept or decline a documented severity tied to a source-geometry distinction | external query needing integration, not pure restraint | only if the distinction is source-geometry (competing-authority POA), never a known CDI trope; lowest priority, swappable | mid |

The two highest-confidence floors are T2 (embedded oxygen or DME closure on a background line, the OV08/OV09 v4 pattern proven near 0.10 to 0.35) and T1 (off-text exertional-oxygen finding under an external denial, the OV04/OV07 image pattern). The highest-novelty and most on-thesis floor is T6 (conflicting-authority handoff), which is also the task that consumes and proves the synthesis-load substrate, and the one most worth benching first because conflicting-authority has only ever floored de-telegraphed.

================================================================
## Part 5 - Substrate and off-text assets
================================================================

World-level raw substrate (at least thirty files; none states the answer): ED note, admission H&P, hospitalist progress notes across decongestion, cardiology consult, nephrology consult, pulmonary or RT assessment, echo, CXR reports, BNP trend, BMP and renal trend, CBC and anemia trend, MAR, home medication list, anticoagulation history, telemetry or AFib summary, PT evaluation with exertional tolerance, OT evaluation with stairs, RT oxygen assessment (but not the decisive off-text test), case management note, DME coordination note, nursing notes, Medicare discharge-rights notice, family communication note, sleep or COPD history, PCP summary, pharmacy fill history, weight and I&O flowsheet.

Task-level files (create the forced move): payer or prior-auth denial letter, started transition note or discharge summary, UR worksheet, SNF or pharmacy med-reconciliation sheet, safety-event intake summary, DME vendor delivery-failure note.

Off-text image assets, mounted agent-and-grader visible, none the scored trap by itself, each rendered through build_one then soffice to pdf then pdftoppm then crop (never a docx; reserve a generative render only for a true photo or film): the signature asset is a six-minute-walk or ambulatory oximetry printout showing exertional desaturation, which is naturally a device printout, so the why-is-this-an-image test passes. Supporting: a telemetry or AFib rhythm strip, a remote-monitoring or home-scale printout, a scanned vendor delivery-failure fax. Sourcing and licensing for every image asset follow docs/IMAGE-SOURCING-CHECKLIST.md: no AI render and no copyrighted images; in-repo render first, in-house Project Sanctum simulator next, a verified public-domain image only for a true photo or film.

================================================================
## Part 6 - Build discipline, sequencing, and the red-team gate
================================================================

First three pilots (canvas open decision 4): T1 oxygen/DME off-text denial appeal (best first lever, on-thesis, multimodal), T2 transition-note embedded-oxygen closure (the proven completion floor), and T6 conflicting-authority handoff (the synthesis-load showcase and the highest ceiling risk, so prove it early). Bench each cold to screen telegraph and the obvious, then pilot even if the bench catches it (the cold-bench-is-a-screen rule, paid for by OV03).

Carry-over build rules (unchanged from OV, all standing canon): at least thirty world files, frozen once tasking begins; every clinical narrative date on or before 07/31/2025, snapshot 07/10/2025, no future-dated artifact; a plain first-person in-role prompt with no reconcile or verify clause and no telegraph; the embedded wrong on a routine background line, never the deliverable headline; the floor on a claim the chart contradicts when inspected, never one it is merely silent about; off-text findings in real image files only where the genre does not force the read; a five-block chart-aware grader that caps the central failure, holds an anti-paralysis floor, credits correct restraint, and instructs verification of the output as untrusted with citation spot-checks; design floor 0.30 to 0.55 with at least one catcher above 0.85; FA and GA from the second-lowest distinct run; every deliverable physician-produced; race never a scoring lever or unstated explanation.

Red-team gate before any build (canvas, six questions): does the task surface force the model to inspect oxygen or DME (if yes it will ceiling, move the catch off the forced path); is the wrong move in the headline (move it to a background line); does the chart contradict the wrong move or merely lack support (if silent, redesign); is this KM05, KM06, OV01, OV04, or OV06 in new clothing (if yes, change the axis); can a catcher reach the answer without private knowledge (if no, attach the source); does the task use race as an assumption rather than a documented fact (if yes, rewrite).

Open decisions inherited from WORLD-STATUS (not closed here): Brainstorm human approval, the Claude transcript reconciliation, Phase A substrate ratification (exact comorbidities, medication classes, sources, dates, care-team roster), and live workflow validation before any upload. This packet sets the design target; it does not close those gates.

================================================================
## Part 7 - Carry-forward from the OV11 retirement and the 2026-06-19 QC fixes (added 2026-06-19)
================================================================

OV11 was retired after three mechanics all proved unshippable on the saturated OV chart. The retirement sharpens two red-team questions and adds a QC-sync discipline.

Two new ceiling modes (add to the Part 6 red-team gate):
- BINARY FINDABLE CONTRADICTION. OV11 v2 mounted a state immunization registry record that listed the gaps, to make an immunization over-closure fair. It ceilinged all-catch (job e52ae4dd, 0.85-0.95): a named record on a binary axis, a date is overdue or it is not, is document-lookup rather than synthesis, so every run found and corrected it. v1's opposite, chart silent with no record, floored but was unfair (Larry). Neither pole ships. The fair-and-floored middle is an embedded wrong on a background axis that the chart contradicts only when several routine lines are SYNTHESIZED, never a single named instrument that states the gap outright.
- PRIMED OR FAMOUS-FACT AXIS. OV11 v3 buried a contraindicated pioglitazone add (a thiazolidinedione in HFpEF) inside an external diabetes-optimization report, the OV06 v2 geometry that floored on perfusion. It still ceilinged: glycemic is a primed/loud axis and the TZD-in-heart-failure rule is a famous board fact error-hunting sweeps, and the add sat on the diabetes plan, the note's headline for a diabetic. A correct geometry does not rescue a primed or famous-fact axis. Add to the gate: is the CATCH a famous board fact (if yes it ceilings, move to a quieter judgment), and does the strong model auto-police this axis even unprompted (in the v2 ceiling runs it relaxed the glycemic target and flagged the anemia workup and the disposition with no prompt; those axes are spent).

The saturation meta-lesson: do NOT retrofit a floor onto a chart already mined ten-plus times. OV reached eleven tasks and the remaining axes were all guideline-judgment the model auto-handles, famous facts, or binary findable items. World 3 must BUILD each floor into the substrate from authoring (the Part 3 thesis): pick one un-primed, silent-status axis per task before the chart is frozen, so the catch needs synthesis the completion frame suppresses rather than recall the model already has.

QC-process carry-forward (paid for on 2026-06-19; full detail in docs/qc-error-class-register.md):
- Verify against the LIVE AutoQC, not a house convention. Our gates REQUIRED a Section C boilerplate opener ("patterns to reason about, not items to tick off") that AutoQC later named as banned filler, sending back OV08 and OV11. Gates now BAN it via an extensible BANNED_BOILERPLATE list; keep that list synced to the live fail-criteria and never bake a fixed filler phrase into a grader template.
- Upload the whole mount set. OV08 was sent back because a task file present in the repo was omitted from the Studio upload. presubmit now prints a per-task upload manifest; cross-check it against the upload before submitting.
- Author the chart internally consistent. The OV MAR omits two supplements the H&P marks continued (ferrous sulfate, cholecalciferol), which AutoQC reads as an undocumented discrepancy on every task that mounts the chart. For W3, reconcile the MAR against the H&P medication table at authoring time so no unlabeled med gap exists; if such an artifact is unavoidable, disclose it (the KNOWN-CHART-DISCREPANCIES.md pattern) with a paste-ready dispute before freezing.
