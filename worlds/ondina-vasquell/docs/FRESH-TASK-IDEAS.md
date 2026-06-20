# OV Fresh Task-Idea Bank (RESTORED live 2026-06-15; was archived in cleanup, which is why it got lost)

RECONCILIATION (read first - this draft predates the OV04 saga and is partly stale):
- CURRENT banked/active levers, the real "do not duplicate" list: for the live and authoritative list of built levers and their status, see docs/WORLD-STATUS.md. As of 2026-06-18: OV01 cold-knowledge enoxaparin, OV02 off-text line-infection synthesis, OV03 carry-forward sliding-scale insulin, OV04 off-text CPAP image, OV05 skilled-wound-care downgrade, OV06 vascular perfusion closure, OV07 off-text wound undermining, OV08 antibiotic-route, OV09 held-med resume, OV10 bone-health over-closure. The OV0X notes further down predate OV04 and are historical.
- FAIRNESS (OV04 saga + KM08 Gate 0): "embedded-wrong, catch+correct" FLOORS, but if the wrong element sits in the model's OWN same-author draft under a finish-only prompt it is UNFAIR. Fair forms: (a) the wrong element in an EXTERNAL / other-department input the physician reviews; (b) a TRUE placeholder; (c) an OFF-TEXT finding the model must proactively read (the proven OV04-v3 engine); (d) the prompt discloses a correct-errors duty (telegraphs - risks ceiling).
- FLOOR vs CEILING (the ~12-ceiling lesson): floors live on UN-PRIMED / off-text / against-the-grain axes; DECLINE-an-external-premise and WARM/headline axes CEILING. BENCH every lever cold (harness-matched, no golden/grader) BEFORE spending a pilot; expect some to ceiling and need rework; the off-text-finding engine is the reliable fallback for any slot.
- The menu below is still valid as a STRUCTURE / lever source; implement each in a fair form and bench it cold.

---

# Ondina Vasquell - fresh task-idea bank (unburned embedded-wrong levers)

Date: 2026-06-15. Author: Claude (cowork), from a read of the gitignored example worlds (`reference/world-spec-examples/`) + the OV substrate (spec.md / OV-WORLD-STATUS) + the difficulty canon (docs/task-difficulty-lessons.md). Purpose: a bench of NEW floor-lever ideas to draw on as OV03-OV10 get rewritten and as ceilinging tasks get replaced. Not a build order - an idea menu. Develop any into a full packet on request.

## The confirmed lever (from the example worlds + OV01)
The example task packs ship the exact pattern that floors on this model: EMBEDDED-WRONG - a bad element sits inside the draft/chart the physician is finalizing, and the physician must CATCH and CORRECT/REMOVE it. Examples:
- World 003 (Marcus) T1 CCM care plan: buries a rifampin-risperidone CYP3A4 interaction, a montelukast boxed-warning, oral-iron-in-IBD, a risperidone dose error to fix, and a psychiatry dose-increase to DECLINE.
- Harold T2 wound SOAP: plants an over-staging trap and a wound-bed-dressing-on-intact-skin commission error.
All are catch + correct, NOT decline-an-external-premise. That is the OV01-enoxaparin profile (BANKED). Corollary (OV-WORLD-STATUS): SUGGESTED-wrong (decline an external bad premise) CEILINGS on this model - OV02 x3 and OV07 proved it.

## Burned / claimed levers - do NOT duplicate
OV01 enoxaparin carried to discharge (banked); OV02 AKI wrong-principal/DRG; OV03 osteomyelitis over-affirmation (CDI); OV04 false caregiver/teach-back premise; OV05 wrong non-sulfa antibiotic substitute; OV06 UR binding-vs-hedge; OV07 HEDIS A1c source-note-date; OV08 perfusion-cleared closure; OV09 PSI contributor inventory; OV10 normalize-vs-documented-restriction (transcription).

## Fresh idea bank (all chart-grounded in THIS patient; all embedded-wrong)
Patient anchors: 68F, limb-threatening diabetic foot infection, CKD 3b (eGFR ~30) with AKI, PAD with genuinely UNSETTLED perfusion (noncompressible ankles, abnormal toe pressure, vascular keeping revascularization open), EQUIVOCAL osteomyelitis (marrow edema on MRI, no bone in path, ID not signing osteo), HFpEF, anemia of CKD, SULFA allergy, Spanish-preferred (certified interpreter), lives alone 2nd-floor walk-up, daughter night-shift CNA, OFFLOADING not yet teach-backed. Snapshot HD6 05/21; tasks strictly after.

### TOP 3 (strongest - high-stakes, cold genre, no collision)

1. PREMATURE AMPUTATION in a podiatry/surgical plan. Artifact: a started limb-salvage / OR-planning or surgical-consult note that already lists amputation as the plan. Embedded error: commits to amputation. Catch + reverse: perfusion is genuinely unsettled (noncompressible ankles + abnormal toe pressure; vascular keeps revascularization open), so a revascularization assessment must precede any amputation decision (limb salvage). Why it floors: high-stakes commission embedded in a surgical-planning genre (cold, not the infection headline); the model must integrate the vascular study to reverse, not just be cautious. Workflow candidate: Operative/Procedure planning or Specialist Referral (surgical). BENCHED 2026-06-19 = CEILING, DEAD on this chart: a fresh agent reversed the pre-listed amputation to limb-salvage on the chart's merits (improving wound, no osteomyelitis, unsettled perfusion). Amputation is the most-primed over-treatment axis and the surgical referral's headline, so it is caught like OV05 v2's Dakin's. "Cold, not the infection headline" was wrong: amputation IS the headline of a surgical referral.

2. OFFLOADING-CONTRADICTING discharge / patient-education instruction. Artifact: a diabetes-foot-care or discharge-instruction draft that tells her to "resume normal walking / weight-bearing as tolerated." Embedded error: weight-bearing instruction. Catch + correct: the chart's central unsafe-disposition driver is STRICT non-weight-bearing offloading, not yet teach-backed; correct to offloading device + non-weight-bearing + interpreter teach-back before any home-mobility clearance. Why it floors: it inverts the model's "encourage mobility/rehab" default (against-the-grain), it is the documented operational landmine, and it is currently unused. Workflow candidate: Patient Education / Discharge Instruction.

3. WOUND-DRESSING commission error (SOAP). Artifact: a wound-care SOAP draft (Harold-proven pattern) recommending a wound-bed / antimicrobial dressing (silver, alginate, hydrocolloid) or a cytotoxic topical on the clean granulating post-debridement bed - or over-staging the wound. Catch + correct: dressing must match the actual bed; moisture/contact layer appropriate, antimicrobial/cytotoxic agents and over-staging are errors. Why it floors: proven commission pattern, distinct SOAP artifact, embedded. Workflow candidate: Wound Care SOAP / Clinical Progress Note.

### ADDITIONAL (solid, develop if a slot needs it)

4. CONTRAST IMAGING ORDER in AKI-on-CKD. Artifact: a vascular-workup draft that orders a CT-angiogram with IV contrast (or gadolinium MRA) for perfusion. Embedded error: contrast study. Catch + remove: eGFR ~30 with active AKI courts contrast nephropathy / NSF; the toe-pressure/duplex already answers perfusion, so cancel/substitute a renal-safe path. Novel imaging/CDS axis. Workflow candidate: Imaging Order Entry with Clinical Decision Support / Diagnostic Test Result Review.

5. INTERPRETER / HEALTH-EQUITY omission. Artifact: a consent or discharge-education draft that documents teach-back/education in English with no certified-interpreter documentation, for a Spanish-preferred patient. Catch: the CLAS / informed-consent / teach-back failure; require certified interpreter and re-document. Novel equity axis, fully chart-grounded. Workflow candidate: Discharge Instruction / Consent documentation.

6. HFpEF FLUID-ORDER commission (weaker - adjacent to the renal thread, listed for completeness). Artifact: a draft resuscitation/maintenance order pushing aggressive crystalloid. Catch + moderate: HFpEF + improving renal function -> volume-overload risk; titrate cautiously. Adjacent to renal axis; lower novelty.

## Build-readiness notes (apply OV template)
World is FROZEN (DO-NOT-REPEAT #21) - every idea above is TASK-LAYER only (mounted draft + golden + grader + prereg), no world edits. Each must: pass the All-Tasks-Physician-Produced gate (physician-authored deliverable; any worksheet/draft is the quality/dept input the physician corrects), use one Filesystem task file with a clean filename + first-trajectory `find /docs` mount gate (#16), de-telegraph the draft surface, name the exact P0/P1 workflow string from Abi's 06/13 tracker, and be self-contained pre-July-2025 (#14). FA/GA from the 2nd-LOWEST run (#20). Floor target ~0.30-0.55 with >=1 catcher >0.85; judge by failure materiality, never tune the grader to fake depth.
