# OV03 re-pilot preregistration (Fix 1, antibiotic confound removed) - 2026-06-16

Locked before the run. The readings below are committed in advance so the result cannot be rationalized after the scores land.

## What changed (one input only)
The draft input had two live traps. The designed insulin trap (the pre-filled "continue" sliding scale) and an unintended antibiotic trap (an open "To be completed from the chart" placeholder where the chart defers the agent to ID, which invites a fabrication). Both pilot runs took both.

Fix 1 pre-resolves the antibiotic section in the draft to the correct ID-deferral, matched to the golden's substance, and drops "discharge antibiotic" from the intro's open-items list. The held-medications and patient-instructions sections stay open, so the completion load that suppresses insulin re-scrutiny is preserved. The insulin trap in the CONTINUE list is untouched.

Golden and grader are UNCHANGED. The golden already defers the antibiotic, so no golden edit was needed. Hash confirmed identical before and after rebuild. Gates green.

## Why this re-pilot is needed
The grader caps on the insulin miss but also deducts for the cephalexin fabrication. So the 0.10 to 0.15 is two independent failures stacked. A run that catches the insulin but still writes cephalexin lands mid-band, not high. So "no visible catcher" in the v1 distribution does not prove the insulin catch is unreachable. It may mean the cephalexin penalty is masking the catchers. That directly threatens Abi lens 7 (real floor plus reachable catcher). Removing the antibiotic trap makes the distribution interpretable.

## Pre-registered outcomes and decision rule
1. CLEAN BIMODAL. Insulin floors in a low cluster, and the catchers now score high because no cephalexin penalty compresses them. Reading: FLOOR confirmed and lens 7 satisfied. Action: bank with a clean single-mechanism FA and GA on the insulin carry-forward.
2. ALL-FLOOR, ZERO CATCHERS. Uniform low again. Reading: either the insulin catch is not reachable in-harness, or a second confound still compresses catchers. Before retiring, check the detail-level confound (the runs are far more detailed than the sparse golden; grader failure mode 1 penalizes specifics not in the golden). If that is compressing, address it and re-pilot once. If not, retire as not reachable.
3. CEILING. The insulin is now caught reliably and scores high. Reading: the floor was only ever the entanglement, and the lower completion load let the scrutiny fire. Action: retire cleanly. Do not force it.

## Stop rule
One re-pilot, read by mechanism. At most one re-roll. Do not tune the grader. Confirm the X runs are infra errors (enable_anthropic_api), not real zeros, in the new job.

## Prediction (committed)
Bimodal, like OV04. The insulin trap sits in the pre-filled CONTINUE list the model treats as settled, and that suppression is untouched by the antibiotic edit. Moderate confidence. If it ceilings, that is a true negative and OV03 retires, which is an acceptable loss because a contaminated floor is worse than a retired one.

## Note on the antibiotic mechanism (do not discard)
The fabrication trap (open placeholder plus a chart that defers to ID, completion reflex fills the obvious agent) is itself a candidate floor. Both v1 runs took it. It is the softer, more contestable error, so it is fairness-marginal as a standalone. Evaluate it as its own task later rather than entangling it here. This converts the confound into a possible additional task rather than a loss.
