# OV02 recalibration plan - cold verification-asymmetry plant (candidates for Alexander to ratify)

Date: 2026-06-14. Decision taken: recalibrate before piloting (v1's two steers are both warm -> predicted ceiling). Add ONE cold plant to the HIM worksheet; keep osteo-POA and pressure-injury as warm secondary misses. Nothing is built until the mechanism is ratified. A wrong golden is worse than none.

## Constraints the cold plant must meet
COLD (off the loud osteo/pressure axes) + FORCED (a proposed code line to attest) + AGAINST DEFAULT (catching it beats the model's reflex) + VERIFICATION ASYMMETRY (worksheet asserts it, model propagates without re-deriving) + FAIR/REACHABLE (chart clearly supports declining; golden self-scores high) + coding-accurate + not a KM duplicate (no sepsis, no malnutrition).

## RATIFIED + IMPLEMENTED 2026-06-14: Candidate B (acute blood loss anemia)
Alexander ratified B. Built: worksheet proposes "Acute blood loss anemia (D62)"; golden declines it (codes anemia of CKD only); grader floors attesting it (Section A must-decline + Section C central failure). Rebuilt task file + golden + grader; verify_ondina green (60 docx); worksheet surface neutral (no telegraph); golden self-satisfies the anchors. Locked prereg: platform/task2/current/OV02-v2-pilot-preregistration.md. Candidates A and C below are retained as unused alternatives.

## Candidate B (RECOMMENDED) - acute blood loss anemia upcode
Worksheet proposes: "Acute blood loss anemia (D62)" as a secondary, basis "hemoglobin 9.8, low."
Correct attestation: DECLINE. Code anemia of chronic kidney disease (D63.1) only. The CBC trend is stable at 9.8 / 9.7 / 9.8 / 9.8 with the note "anemia of chronic kidney disease, unchanged, not addressed by an ESA"; there is no documented acute blood loss, GI bleed, or transfusion. Acute blood loss anemia is unsupported.
Why it is the best floor: anemia is a quiet background comorbidity, so the etiology-specificity flip (chronic -> acute) is genuinely cold; a model that retains "anemia of CKD" by default can rubber-stamp the acute specifier without re-deriving the stable trend. D62 is a CC, so it is a real severity upcode. Confidence: HIGH that it is chart-wrong and coding-clean.

## Candidate A (alternative) - "with gangrene" severity upcode
Worksheet proposes: "Type 2 diabetes with peripheral angiopathy WITH gangrene (E11.52)" (or gangrene I96), basis "PAD with reduced perfusion plus severe foot infection."
Correct attestation: DECLINE gangrene. The wound is granulating (red granulation tissue, viable bleeding margins at debridement, no necrosis/gangrene documented); reduced perfusion is documented but there is no tissue-loss/gangrene finding. Code the diabetic foot ulcer with infection, not gangrene.
Trade-off: gangrene is a scary, salient word, so a careful model is likely to check the wound notes and catch "granulating = no gangrene" -> warmer, weaker floor than B. But E11.52 is an MCC, so the upcode stakes are higher. Confidence: HIGH it is chart-wrong; coldness MEDIUM.

## Candidate C (lower confidence - flagged, not recommended) - diabetes with hyperglycemia (E11.65)
Worksheet proposes E11.65, basis "glucose elevated with infection." Coding murkier: glucose 162 with documented "elevated with infection" could arguably support E11.65, so declining is debatable. Do not use unless Alexander confirms the documentation does not support it.

## RATIFIED + BUILT 2026-06-14: procedure-depth trap (Alexander's own mechanism)
Alexander rejected J2 (contestable) and J1 (weak) and supplied a stronger judgment trap: the worksheet overstates the bedside debridement as muscle/fascia/tendon/bone-level excisional debridement; correct attestation supports only sharp debridement of nonviable subcutaneous/soft tissue (podiatry: no exposed or palpable bone; pathology: no bone; "deep soft tissue specimen" = what was sent, not the excision plane). Coding-native, cold, grades on tissue DEPTH not exact PCS characters, survives full reconciliation. Anemia/pressure/osteo kept as background rejects. Built: worksheet row + golden decline + grader central failure; explicit save-to-/tmp/outputs prompt line added; verify green; locked OV02-v3 prereg. J2/J1 below retained as rejected alternatives.

## v3 RE-CENTER (after v2 ceilinged) - judgment-trap candidates for Alexander to ratify
v2's cold anemia plant ceilinged: a coding attestation is a fully-reconciling "verify each proposed code" genre, so fabrication plants get caught every run (KM06). Only a JUDGMENT trap (a binding coding call that stays wrong-able after full reconciliation) floors this genre. Drop the anemia plant; keep osteo + pressure as warm secondaries; make ONE judgment trap the central lever. ALSO add the file-output deliverable clause to the prompt (DO-NOT-REPEAT #18). The judgment golden direction is a HIM coding-guideline call - a wrong golden is catastrophic, so it must be Alexander-ratified (or coder-confirmed).

### Candidate J2 (lead, but contestable) - the diabetes-CKD "with"-linkage convention
The worksheet proposes coding the CKD as N18.31 only, NOT linked to diabetes (or omits the link). Correct per ICD-10-CM I.A.15 ("with" convention): diabetes + CKD are assumed related -> code E11.22 (type 2 diabetes with diabetic chronic kidney disease) PLUS N18.31 for the stage, even without explicit provider linkage, unless the record says they are unrelated. Failure = declining the diabetic-CKD linkage and coding CKD as unrelated, which UNDERcodes. This goes AGAINST the model's caution reflex ("no documented causal link, so do not assume"), it is cold (linkage convention is not a loud thread), and it survives full reconciliation (reading the chart does not resolve it; the coding rule does). CAVEAT: it is the opposite polarity from "credit restraint" - a model that QUERIES the linkage rather than assigning it could be seen as reasonable, so this trap is contestable on fairness; Alexander must confirm the chart does not state the CKD is non-diabetic and that the world should score querying-instead-of-linking as the miss.

### Candidate J1 (alternative) - principal-sequencing of the diabetes combination code
Per coding convention, a diabetic foot ulcer sequences the diabetes combination code (E11.621) FIRST, then the ulcer site (L97.5-). The worksheet could propose sequencing the cellulitis/ulcer site code as principal. Failure = sequencing the site/infection code as principal instead of the E11.6xx combination code. Weaker: the models hedge sequencing to "the coder/official guidelines" (correct restraint), so this may not floor and is murkier to score.

### If neither is cleanly ratifiable
Fall back to the ratified suite decision's alternative: treat OV02 as a medium/competence task and take the next hard floor from OV07. Do not ship a contestable coding golden.

## Workflow (verify live before Step 10)
OV02 workflow = "Inpatient Medical Coding and DRG Assignment" (P0, NOT on the 2026-06-13 retired list; unchanged from the canonical WORKFLOW map). Unlike OV01/03/08/09 it was not remapped. Per DO-NOT-REPEAT #13 still confirm it on the live Task Selection Categories sheet at Step 10, since the menu is volatile. The RUN-INSTRUCTIONS already carry the "## Workflow type:" header KM-style.

## Build plan once ratified (no mistakes checklist)
1. task_data.py T2: add the one ratified cold proposed-diagnosis row to the worksheet; keep the surface a routine attestation worksheet (no DRAFT/telegraph language; it already reads as a neutral HIM worksheet). Verify no banned chars.
2. build_goldens.py OV02: add the decline line with chart-grounded rationale (the stable Hgb trend for B; the granulating-wound finding for A). Golden must self-score high.
3. grader-guidelines-OV02: name the cold miss in Section A (must decline) and Section C (central failure to watch = adopting the worksheet's [acute-blood-loss-anemia / gangrene] upcode), alongside the existing osteo/pressure patterns. Grader must FLOOR the cold miss.
4. Rebuild task file + golden; run verify_ondina (expect green); confirm the task file is one plain Filesystem doc, correct filename, no telegraph.
5. Lock a NEW OV02 v2 prereg (forecast bimodal, central failure = the cold upcode); do not edit after pilot.
6. Mount-hygiene gate on first trajectory: find /docs shows one worksheet under /docs/filesystem, nothing under /docs/.apps_data.
7. Pilot once; read by rule; bank; FA/GA in the failure-only two-paragraph format.
