# Task Difficulty Lessons - what makes an RL eval task hard (Korvin Merrow, tasks 1-6)

Date: 2026-06-08. Source: the full KM01-KM06 build/pilot history. Companion: `docs/grader-guidelines-lessons.md` (structure + length), `docs/clinical-voice-lessons.md` (golden register), `docs/reviewer-response-protocol.md`. This is the difficulty playbook: read it before designing any new task.

## 1. The core principle: the IDEA is the lever, not the writing

Writing quality and the trap idea are two different axes governing two different outcomes:
- Writing (clinical voice, Sang grader structure, house style, length) governs whether the task PASSES REVIEW. Necessary, but it does nothing for difficulty.
- The trap IDEA governs DIFFICULTY - the entire score spread. A well-written task with a weak idea clears high every time.

Proof both ways: KM05-NSAID and KM06-orthostatic were clean prose with textbook graders and both scored ~93 (failed). The wins (KM02/03/04) share the same IDEA, not the same prose. So judge the idea on reasoning first; a weak idea dies cheap in the workspace and only a real idea earns a pilot.

## 2. The 4-point trap test (run before writing a line)

1. Cold - is the axis un-hunted, NOT primed by the chart's loud threads, the other tasks, or the deliverable's own headline?
2. Forced - is there one wrong move, so caution is not free?
3. Against the default - does catching it require something other than the model's trained "be cautious / don't fabricate" reflex? If free caution passes, it is too easy.
4. Direction - invert what the model is primed to police (it guards "don't restart too fast" -> plant a de-escalation; it guards "don't add false facts" -> plant a reassuring one it accepts).

## 3. The one reliable mechanism

Completion genre + a single buried fabricated objective result in an otherwise-correct draft, on a COLD axis the chart can cleanly contradict but where the model has no reason to suspect error. It works because: the draft is 95%+ correct so the model trusts it; the planted line is plausible; the chart has clear contradicting evidence but requires active lookup; and the model self-verifies its OWN additions, never re-verifying what it inherited from the draft. That verification asymmetry is the universal exploit.

## 4. COLD beats WARM (the rule that decides difficulty)

A fabrication on a WARM axis (primed; the model is already hunting it) gets caught universally. A COLD axis (un-hunted background) gets propagated. The deliverable's own subject makes its headline axis WARM.

Measured evidence (ran and scored):
| Task | Axis | Genre | Warm/Cold | Mean | Result |
|------|------|-------|-----------|------|--------|
| KM01 | unsafe rec (nitrofurantoin etc.) | med rec | bright/known | 89 | clears, soft |
| KM02 | urine culture (E. coli) | discharge summary | cold secondary | 59 | DEEP win |
| KM03 v1 | cardiorenal restart | discharge planning | warm/primed | ~94 | killed |
| KM03 v2.2 | CPAP adequacy | discharge planning | cold secondary | 76 | DEEP win |
| KM04 v1 | (renal/primed) | care plan | warm | 91 | failed |
| KM04 v2 | iron studies / anemia | care plan | cold secondary | 66 | DEEP win |
| KM05 v2 | +7 interval observation | transition note | chart-silent | (killed) | unfair |
| KM05 v3 | NSAID-in-CKD | transition note | bright/known | 95 | failed |
| KM05 v4-pilot1 | home-BP+weight+immun (3 plants) | transition note | chart-silent | 20 | unfair, all-floor |
| KM05 v4 | premature restart on home BP | transition note | cold + forced | 36 | DEEP win, bimodal |
| KM06 v1 | orthostatic vitals | fall-risk SAFETY REVIEW | WARM (headline) | 93 | failed |
| KM06 v2 | echo / LVEF recovery | transition summary | cold secondary | pilot pending | - |

Two refinements the suite paid for:
- Chart-SILENT is not the same as chart-CONTRADICTED. A fair, deep failure must be something the record CONTRADICTS or explicitly mandates, never something it is merely silent about. KM05 v4-pilot1 (home BP/weight at +7) floored every run but was UNFAIR and would be bounced, because the +7 home data is silent in the chart and the model cannot be faulted for trusting it. Re-centering onto the premature restart (which the chart explicitly defers to outpatient cardiology/nephrology) gave a fair bimodal spread.
- A REVIEW genre is anti-cold. Reviewing IS verifying, so the whole document is warm; KM06-orthostatic put the plant on the fall-risk headline of a fall-risk review and every run caught it. Use a DOCUMENTATION genre (summary/plan/note) where the plant sits in a BACKGROUND section the model finishes without special scrutiny.

## 5. Fairness (the symmetric-spread test)

A bankable deep task is BIMODAL: a clear floor (the propagators) AND clear catchers (0.85-0.95) proving a strong model can pass. All-floor (no catcher) reads as an unfair gotcha and gets bounced. The grader must score the floor on the planted failure and reward the correct restraint at the ceiling. Confirm fairness by reading a catcher transcript, not just the mean.

## 6. Reading a pilot

- Read by PER-AXIS propagation rate / disposition, not the headline mean.
- For a propagation task: do the floors carry the fabricated line forward, and do the catchers correct it and score high?
- If it clusters too high (no floor): the axis is too warm/bright or the plant too obvious - re-center the IDEA (colder axis, sharper plant), do NOT just rewrite prose.
- If it is all-floor (no catcher): check the plant is chart-CONTRADICTED, not chart-silent; if silent, it is unfair - re-center onto the chart-mandated move (the KM05 v4 fix).
- The lowest-floor run is the FA subject; a clean catcher is the GA symmetry anchor.

## 7. One-line summary

Difficulty is a property of the idea: a cold, chart-contradicted, forced fabrication that inverts what the model polices, buried in an otherwise-correct document. Everything else (voice, structure, length) is for passing review.
