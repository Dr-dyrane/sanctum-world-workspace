# OV02 (v6, Path A) human review - Kathy G, 2026-06-15 - SEND BACK
Task: Vasquell SNF transfer, line-site synthesis lever. Job context: Path A re-pilot d0795803 (fair floor). Status: revisions requested before advance.

## Reviewer feedback (verbatim)
Kathy G 6/15/2026
Nice work. Before it can advance I want to flag the golden and the grader for some revisions:
GOLDEN. There seems to be a conflict between the golden and the grader on the line-site photo in this task (Vasquell SNF transfer), since it affects how responses get scored. The grader is clear on this point in a few places: the line-site infection has to be reachable from the transfer-day text on its own, without seeing the photo, and responses should not get credit for inventing detail about what the photo shows. A text-only answer that works the the finding out from the signals is supposed to earn full credit.
The golden, though, states as fact that the photo "shows erythema and purulent drainage at the catheter site." That is the kind of visual claim the grader tells us not to credit when a response makes it. So the reference answer models the behavior the rubric is meant to penalize, which puts a grader in an awkward spot and could lead to inconsistent scoring.
My suggested fix is to rewrite the golden so the finding rests on the transfer-day signals rather than the image: the photo was taken that day, the temperature rose to 38.0 against an afebrile baseline, and IV antibiotics are running through that line. From there the golden can call for inspecting the line and holding the transfer, without claiming to know what the photo shows. That keeps the golden consistent with a text-only answer earning full credit.
GRADER. The length of the GG is too long, it should be about 1 page, 1.5 max. I would also get in the habit of applying the section titles more closely to those cited in the project instructions going forward, as I see a fair number of folks get penalized for drifting from that. It's just one less issue to be reviewed on.
Let me know if you have questions.

## Classification (reviewer-response-protocol)
1. GOLDEN visual claim conflicts with grader = REQUIRED (consistency). Golden asserts the photo "shows erythema and purulent drainage"; the grader says do not credit invented visual detail -> golden models penalized behavior. Fix (per Kathy): rest the finding on the transfer-day text signals (photo taken that day + 38.0 vs afebrile + IV abx through the line), call for inspect + hold, no claim about what the photo shows. Does NOT change the clinical answer.
2. GRADER length = REQUIRED structural. 897 words -> ~1 page (~480; KM/Sang rule, 1.5 max).
3. GRADER section titles = REQUIRED structural (habit). Keep the exact five-block titles + verbatim clauses; confirm no drift.
None are physician-judgment conflicts. Re-pilot NOT needed: scoring logic is unchanged (the grader already credits text-only catches; this only removes the golden's unsupported visual claim and trims grader length). Re-AutoQC, then Alexander resubmits.

## Root cause (carry forward)
Self-inflicted in the Path A recut: golden reframed to "photo = corroboration" but a visual assertion was left in. KM lessons not carried: (a) golden must not model penalized behavior; (b) grader <=1 page. Systemic fix: add a golden-vs-grader consistency check to the verify gate so this class of contradiction is caught automatically.
