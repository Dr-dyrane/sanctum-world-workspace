# Reference Templates - what is here and how to use it

> Voice: all output text built from these templates follows `docs/alexander-voice-dna.md`. Enforced by `tools/verify/verify_voice.py`.

This folder holds two different kinds of reference material. Know which you are reading.

## 1. The client's latest-guidance WORKED EXAMPLE (Quill CDI) - added 2026-06-11

Source: King P (Medicine Team Lead), #general 6/10, "[UPDATED WORLD EXAMPLES]" - shared as the example that "reflects the latest guidance from this recent delivery," authored by veteran writer David B. It is a complete world + one task (Clinical Documentation Improvement Query, P0) for the world `Healthcare_Hyperammonemia_Quill` (patient Zephyrus Quill, a CF hyperammonemic-decompensation case). These are markdown captures of David B's Drive deliverables.

| File | What it is |
|---|---|
| `Brainstorm_Quill.docx.md` | World-level brainstorm: scenario, frictions, the 16-trap table (5 world-level + 11 task-level), task slate. The model for a strong brainstorm. |
| `WorldSpec_Quill.docx.md` | The full World Spec (Section 1 clinical scenario, patient profile, home-med table with inpatient changes, etc.). The model for spec structure + clinical voice. |
| `Task prompt.md` | The CDI task prompt - ONE in-role sentence, zero enumerated constraints. |
| `Golden Response.md` | The golden: a CDI physician query set (3 queries: sacral pressure injury stage+POA, malnutrition/sarcopenia, principal-dx/etiology), each non-leading with balanced options and an "undetermined" out. |
| `Grader Guidelines.md` | The grader for the CDI task. |
| `FA_GA.md` | Failure Analysis + Grader Analysis on a 0.28 trajectory. |
| `Preferential Labeling.md` | A worked A-vs-B preference label (Scale A+). |

WHY IT MATTERS HERE: KM10 (our CDI Query Response) is the all-floor, reachability-open task. This is a worked CDI example showing what a reachable, compliant, balanced answer looks like - the golden affirmatively queries what the chart supports and DECLINES what it does not (no ascites-off-diuretics query, no over-query of a settled mood screen). Read it before touching any CDI / coding / external-ratify (S3) task. It also maps to `docs/task-structure-dossier.md` structure S3.

### Deltas vs our KM (Vaguspod) conventions - reconcile, do not blindly copy

The philosophy is the same; some labels and formats differ. Two of these are genuine conflicts with our standing pod rules - do not copy them into a Vaguspod task without checking.

- GRADER SECTION LABELS differ. Quill uses **Deliverable / Register note / Non-Negotiables / Scope and Legitimate Variation / Common Failure Modes**; our KM graders use **Preamble / Register Note / Section A (Must be present) / Section B (Acceptable variation + the verbatim two-failure-mode clause) / Section C (patterns to reason about)**. The substance is identical: both name the golden, both carry a register note, both frame failures as "patterns to reason about, not items to tick off," both credit correct restraint, and both apply the same fabrication test - *"if the source files support it, it is not fabrication; if they do not, it is."* Our KM five-block is the structure that has PASSED the live Task AutoQC gate (`docs/grader-guidelines-lessons.md` Lesson 1); keep using it unless the live AutoQC gate or a reviewer tells you otherwise. Treat Quill as confirmation of the philosophy and as the reference for CDI content, not as a license to relabel a grader that already passes.
- FA/GA FORMAT differs and CONFLICTS with our rule. The Quill `FA_GA.md` is the older BOTH-SIDES format - its FA notes what the model did well ("correctly follows compliance language") and its GA notes what the grader got right. Vaguspod follows **Abi's 6/9 FAILURE-ONLY rule**: FA documents only what the model did poorly, GA only what the grader did poorly, and neither names "Section A/B/C" (`docs/grader-guidelines-lessons.md`, "ABI UPDATE 2026-06-09"). Do NOT copy the Quill both-sides shape into a KM FA/GA. (The Quill GA's closing "one constructive grader-refinement" line IS compatible with our GA and worth keeping.)
- PROMPT style MATCHES us and confirms the rule: a short, first-person, in-role instruction with no how-to and no enumerated answer domains. Good external precedent for our `undisclosed_constraints` QA rebuttals (the required stance is disclosed by the chart, not the prompt).
- PL AXES differ in labeling. Quill uses an A+/.. scale across Scale Selection / Prompt adherence / Correctness / Completeness / Methodology / Quality and clarity; our PL uses the A4-B4 scale across the official seven-section justification. Use ours for submission; read Quill for how the comparison reasoning reads.

## 2. The generic Sanctum SECTION TEMPLATES (AutoQC section guides)

`AutoQC_Section_2_World_Spec_*.docx`, `AutoQC_Section_3_World_Files_*.docx`, `AutoQC_Section_4_Task_Prompts_*.docx`, `World_Spec_Template_05_06.docx`, and the local `brainstorm.*` / `template-links.md` are the project's blank section templates and self-QC checklists (use the highest version number present). They tell you the required SHAPE of each deliverable and the AutoQC checks it must pass. The Quill files above are a filled, approved INSTANCE of those shapes.

Companion docs: `docs/clinical-voice-lessons.md` (the voice these examples are written in), `docs/grader-guidelines-lessons.md` (our grader structure + length), `docs/task-structure-dossier.md` (where CDI sits in the 8 structures), `docs/task-difficulty-lessons.md` (the fairness + difficulty rules a CDI task must still meet).
