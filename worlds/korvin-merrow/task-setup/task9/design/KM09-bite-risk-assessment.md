# KM09 bite-risk assessment (6/10) - grounded in the 8-pilot suite data
Question from Alexander: does KM09 kill it (clear no-moderate with a genuine failure) AND is it genuinely not a draft-and-finalize task?

## Answer 1: Is it structurally NOT draft-and-finalize? YES, solidly.
KM09 is S2 forced-inventory: no mounted draft, the deliverable schema (a code list with a verdict per diagnosis) is the forcing function. The model synthesizes codes from the closed record; there is no pre-written claim to ratify. That is a different cognitive task and a different artifact from KM02-KM08's completion wrapper. Variety mandate satisfied.

## Answer 2: Will it bite? NOT guaranteed - the data warns it may clear high. Here is the honest read.

What the suite data proves about this world:
- The reliable DEEP floor = completion + a buried false claim on a cold axis (KM02 59, KM04 66, KM05 36, KM06 60, KM07 36).
- Variety-first / no-wrapper tasks tend to CLEAR: KM07 v1 from-scratch 93.8, KM08 v3 status 96.4. Logged in TASK8-STATE as the structural finding.
- The one forced-inventory data point we have, KM01 (med rec), cleared at mean 89, zero sub-70 - genuine failures (dropped metformin) but a FAIR CLEARER, not a deep floor.

The specific risk for KM09's central trap as currently designed:
The planted failure is "don't capture undocumented MCCs (metabolic encephalopathy, acute-on-chronic HF)." By our own 4-point trap test (task-difficulty-lessons.md), that fails point 3 (against-the-default): coding ONLY what is documented IS the model's trained caution. Catching the trap = free caution. That is the exact pattern that made KM07 v1 and KM08 v3 too easy (correct = the safe default = free clear). A frontier model that reads all 26 files and knows "do not code an undocumented diagnosis" sweeps the MCC trap for free.

The counter-bet (why it might still bite): the EAGER move in coding is revenue/specificity capture. A model RLHF'd toward thoroughness may over-capture the encephalopathy because the AMS is loud in the chart, to look complete. Whether helpfulness-driven over-capture beats the don't-fabricate reflex is empirical. But the base rate from this world says forced-inventory leans toward clearing.

## The fix that raises the bite WITHOUT changing the structure: re-center on the principal-diagnosis slot.
Move the central scored failure from MCC-capture (free caution) to PRINCIPAL DIAGNOSIS SEQUENCING (fights a real model bias):
- The eager/wrong move is coding A41.9 sepsis as principal - it is the admission impression, the most severe framing, and the higher-weighted DRG. Severity-anchoring is a documented model tendency, NOT free caution.
- The correct move codes the urinary-source infection per the inpatient suspected-at-discharge rule (sepsis is documented only as "physiology," never as a diagnosis; no infection-linked organ dysfunction). This requires resisting the salience of the admission framing and applying the coding rule correctly - a genuine forced value with a tempting wrong answer.
- Keep MCC-capture (encephalopathy, acute HF) as the SECONDARY axis. A response can fail on either or both.

This is "against the default" in the right way: it exploits the model's pull toward the most salient/severe diagnosis, the same class of bias KM02-KM06 exploit, but inside a forced-inventory coding artifact instead of a completion draft. Substrate is byte-verified (sepsis always qualified, cultures pending, no organ-dysfunction linkage).

## Honest expectation and the lever
Even re-centered, KM09 is the suite's least-certain bite because forced-inventory is the structure most prone to clearing on this model. Treat it as PILOT-AND-SEE with a redesign lever pre-loaded:
- If the pilot clusters >=85 (free-caution swept it): the redesign is to mount a coder's worksheet or encoder-suggestion sheet that has ALREADY assigned the wrong principal + the undocumented MCC, converting it to a ratify-or-refute (closer to the KM02 lever that reliably floors). That keeps it out of completion-draft territory (it is a coding worksheet, not a clinical note to finalize) while adding the adversarial forcing.

## If the priority is a GUARANTEED bite + variety, KM10 is the safer one.
KM10 (CDI query response, S3 ratify-or-refute) pressures the model toward the wrong move via administrative authority + helpfulness - the documented KM02-class lever - so it is more likely to floor than KM09's forced-inventory. If only one of KM09/KM10 must bite hard, bet KM10; run KM09 as the variety/coverage task that may clear like KM01 (which is an APPROVED outcome: genuine failures, fair clearer).

## Recommendation
1. Re-center KM09's golden + grader on the principal-diagnosis sepsis-anchoring failure (central), MCC-capture secondary. Alexander owns the principal-dx stance.
2. Preregister the spread before pilot; expect fair-clearer-to-mid, not a guaranteed deep floor.
3. Hold the ratify-or-refute coder-worksheet redesign as the lever if the pilot clears >=85.
4. Lean on KM10 as the harder-biting variety task; let KM09 carry coverage + capability breadth.
