# PL format template (house format)

Copy this for each preference label. Replace every `<...>`. Keep the field labels
exactly as written. Lead the pasted block with the Scale Selection line (official
Part 7 template). Do not use em or en dashes.

The paste-ready part is the `## Justification` block, from "Scale Selection:"
through the end of "Summary:". That is what goes in the platform Comments box. The
Scale Selection line states the Button and the language only (for example
"A++ (moderately better)"), never a numeric or tier score. We cap at A1-B3, so the
Button is plain, one plus, or two plus, never three plus.

---

```
# <TASK> Preference Label <N> - Transcript A vs B (workspace backup)

Stage: Step 15 Preference Labeling (<World> - Task <id>, batch <YYYYMMDD_HHMMSS>).
Current status: DRAFT for read-and-own. No platform entry without the writer's authorization for that exact step.

Studio-selected pair:
- Transcript A = <score>, <steps> steps, <time>.
- Transcript B = <score>, <steps> steps, <time>.
- Bundle IDs not shown in the pasted transcript; record from the download icons on submit.

Evidence read: both deliverable summaries read against `golden-<TASK>.docx` and `grader-guidelines-<TASK>.txt`. The central capped failure for <TASK> is <one-sentence central failure>. <Frame the pair: both-pass / both-floor / pass-vs-floor, and where each score sits relative to the floor band and the catcher>. The verdict is decided against that central failure, with the conservative-margin calibration.

KEY FINDING: <Who is better and why, in a paragraph. Name what both got right, then the central item, then the single decider, then the margin reasoning (why this tier and not one step up or down).>

VERDICT: <A1/A2/A3 or B1/B2/B3>. Button = <plain A | A+ | A++ | plain B | B+ | B++>. (Internal tracking line, not pasted.)

## Justification

Scale Selection: <A or B with plus signs> (<marginally | slightly | moderately> better)

Preferred output: <A or B>

<Opening preference paragraph: the core argument for the preferred output, centered on the central item.>

Justification: <Why this tier. The central-item argument plus the cap reasoning (why not higher, why not lower).>

Prompt adherence: <Did both answer the requested workflow and format. Usually a tie.>

Correctness: <Clinical accuracy against the golden, central item first. Usually the deciding dimension.>

Completeness: <Coverage of required items and secondary catches.>

Methodology: <How each read and reconciled the chart.>

Quality and clarity: <Organization and readability. The grader is told not to weight formatting, so usually neutral; say so.>

Summary: <Restate the preference, the tier, and why it is not one step higher or lower.>

## Guardrails (must survive any edit)
1. Preferred output is <A or B>. Button = <...>.
2. The decider is <the central-item handling>. Do not drift it onto prose, formatting, or step count.
3. Margin is <tier>, not <one step up> and not <one step down>, because <reason tied to the cap rule>.
4. The deciding gap is <the discrete error, or the degree difference>. Record it.
5. Both are correct on <the shared items>. Do not treat those as differentiators.
6. PL <N> of 3 for <TASK>. <Note distinct trajectories.>

## Submit mechanics
Select <Button> (no plus / one plus / two plus; never three plus), paste from "Scale Selection:" through the Summary into Comments, submit the preference, confirm it appears in submission history, then run Preference Labels AutoQC. Do not submit until the writer authorizes this exact step.
```
