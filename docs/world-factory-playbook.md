# World Factory Playbook - the repeatable brainstorm -> spec -> reference-files pipeline

Date: 2026-06-14. Purpose: make the Ondina speedup reproducible. Korvin Merrow took about a week from brainstorm to a submitted spec; Ondina Vasquell was created 06/12 and the spec was submitted 06/13 - roughly a day, with the heavy build measured in hours. That gain was not luck; it came from separating the part of the work that is mechanical and deterministic from the part that is clinical judgment, automating the first to the hilt and gating the second. This document names every step and every decision gate so the next world inherits the speed, and so a generator script can implement the mechanical spine directly. Companion docs: `world-pipeline-playbook.md` (the original post-KM recipe this supersedes for the spec phase), `DO-NOT-REPEAT.md` (the class-level rules), `task-difficulty-lessons.md` (why a task is hard and fair).

## 1. The one principle

Every phase has two layers:

- **The deterministic spine** - structure, formatting, file plumbing, metadata, cross-checks, gates. Same inputs always produce the same bytes. This layer is automatable and should be one command.
- **The judgment gates** - the trap ideas, the ratified clinical values, the goldens, the prompts, the grader standards, the workflow choice. These require a physician and they are never auto-filled, because (a) the platform requires writer-authored prompts and physician-owned goldens, (b) difficulty can only be proven by piloting, not asserted, and (c) auto-filled clinical content drifts into plausible-but-wrong.

The factory automates the spine and leaves clearly-marked holes at the gates. "Deterministic from here down" means: once the physician fills a gate, everything downstream of it rebuilds identically with one command.

## 2. The pipeline, phase by phase

Each phase lists: INPUT, SPINE (automatable), GATE (physician), OUTPUT, PASS (the check that must be green before moving on).

### Phase 0 - Pre-brainstorm
- INPUT: a case note of choice (the right entry point - richer than a bare title).
- SPINE: copy the world folder skeleton; snapshot the live instruction doc and the live Task Selection Categories sheet; open the planning canvas.
- GATE: confirm the domain is worth a world; pick 5+ distinct task structures BEFORE the patient (cap completion/draft tasks at 1-2); declare the snapshot date and a varied post-snapshot anchor per task; verify every workflow string verbatim against the LIVE categories sheet and note claim counts.
- OUTPUT: a filled planning canvas; a structures-first task slate.
- PASS: brainstorm checklist variety + canvas + temporal-anchor gates.

### Phase 1 - Brainstorm
- INPUT: the canvas + case note.
- SPINE: fill the brainstorm template; run Brainstorm AutoQC; build the brainstorm DOCX deterministically; assemble a sanitized transcript.
- GATE: the domain, the patient sketch, and the ten task structures with their traps and frictions - the intellectual core. The trap idea is the lever; a weak idea dies here cheaply.
- OUTPUT: brainstorm DOCX + transcript, AutoQC green.
- PASS: every Brainstorm AutoQC flag is a pass or a justified note; the trap taxonomy survives a hostile-review pass.

### Phase 2 - Substrate ratification
- INPUT: approved brainstorm.
- SPINE: assemble the substrate proposal pack (identity, comorbidity profile, meds with holds, renal/infection/perfusion/bone anchors, roster, timeline); every derived value is FLAGGED, never asserted.
- GATE: the physician ratifies or strikes each value in one pass. Ratified values become the single source of truth.
- OUTPUT: a ratified substrate pack + the DERIVED registry (texture values flagged + physician-ratified).
- PASS: no value asserted as fact without ratification.

### Phase 3 - Spec assembly
- INPUT: ratified substrate + task slate.
- SPINE: write the spec sections from the template in place; render the **file table in KM's canonical 7-column format** (# | ID | Filename.type | Date | Reference File Origin | Description | Pearls), with Reference File Origin tagged per the four-option convention with filename in parentheses (Public Domain / Custom Made (file) / Databank template (file) / Writer produced (file)), and the file plan in a **landscape section** so no column clips; enforce the 30-file world-level floor with task-level files kept separate; build the spec DOCX deterministically.
- GATE: task prompts (persona voice), expected-output anchors, failure design per task - physician-authored; the workflow label per task chosen from the LIVE sheet.
- OUTPUT: spec DOCX + reference/template file set + transcripts.
- PASS: run the spec AutoQC preflight criterion-by-criterion locally INCLUDING "every task deliverable is physician-produced" and a brainstorm-vs-spec diff of every task's requester/format/register; then the live Spec AutoQC.

### Phase 4 - Reference files
- INPUT: the spec file plan + ratified substrate (as `clinical_data.py` constants).
- SPINE: every docx renders through the ONE canonical Epic template (`epic.py` / `build_one`) by Mode A clone of a clean approved base - styles byte-identical, headers/footers rebuilt, metadata scrubbed, timestamps pinned, fingerprint diffed to zero; world files and task-level files built and PLACED separately (task files copied into each `platform/taskN/current/`).
- GATE: physician confirms the trap-bearing content and any texture values; writer-produced images are delegated to a strict prompt spec and eye-verified.
- OUTPUT: all world + task + supplementary docx, all images.
- PASS: the one-command gate green (no synthetic, no prior-world identifier, no banned chars, scrubbed metadata, template parity, filename match, cross-file anchor consistency).

### Phase 5 - Transcripts
- SPINE: build brainstorm + world-spec transcripts deterministically; sanitize - no benchmark/eval register, no internal tooling, no prior-world identifiers; preserve only the real share URL and run id.
- GATE: none beyond the writer-name decision.
- PASS: zero benchmark/tooling/prior-world tokens.

### Phase 6 - Task setup (Step 10, post spec GO)
- INPUT: approved spec + live world.
- SPINE: package each task (prompt, golden-as-file, grader, run-instructions, prereg, A0.5) and copy the uploadable set into `platform/taskN/current/`; the deterministic build of every docx.
- GATE: PHYSICIAN owns prompts, goldens, grader standards. Difficulty is PROVEN by piloting (a fair, bankable, sub-ceiling failure), not asserted. This phase is held until the spec is approved.
- PASS: Task AutoQC; a fair bimodal pilot with a legitimate clinical failure.

## 3. The invariants the factory encodes (no judgment, always true)

- One world folder skeleton, copied per world.
- One canonical Epic template for EVERY docx (world, supplementary, task, golden); never a bare `Document()`.
- Single source of truth: each clinical value lives once in `clinical_data.py` / `task_data.py`, ratified from the substrate pack; change once, rebuild, re-gate.
- The KM 7-column file table + four-option origin convention + landscape section for wide tables.
- 30+ world-level files; task-level files separate and never in the world bucket.
- Temporal law: every task encounter and deliverable strictly after the world snapshot; nothing future-dated past the real present.
- Deterministic build: pinned zip timestamps + core dates, pinned toolchain (`requirements.txt`), LF line endings.
- Sanitized transcripts; scrubbed metadata on every docx.
- The one-command gate green before any stage.

## 4. The decision-gate inventory (the holes the generator leaves)

These are the only places a human is required. The generator emits each as an explicit `<<PHYSICIAN: ...>>` marker:

1. The ten task structures + each trap/friction (Phase 1).
2. Every clinical value in the substrate pack - ratify or strike (Phase 2).
3. Each task's prompt (persona voice), expected-output anchors, and failure design (Phase 3).
4. Each task's workflow label, chosen from the LIVE categories sheet (Phase 3).
5. Trap-bearing reference-file content + image prompt specs (Phase 4).
6. Prompts, goldens, grader standards, and the pilot read (Phase 6).

## 5. The toolchain map

- `tools/mode_a_clone.py` - clone, clear body, rebuild headers/footers, scrub metadata, verify no-synthetic / no-prior-world, `make_deterministic`.
- `build/epic.py` - the canonical Epic renderer (masthead, blue bar, storyboard, PATIENT/ENCOUNTER block, blue table headers).
- `build/clinical_data.py` + `build/task_data.py` - single source of truth.
- `build/build_world_files.py` / `build_task_files.py` / `build_goldens.py` / `build_task_packages.py` - all route through `build_one`.
- `tools/build/build-docx-*-worldspec.py` and the transcript builders - spec + transcripts, 7-col + landscape.
- `build/build_all.py` - one-command deterministic rebuild + gate.
- `tools/verify/verify_ondina.py` - the one-command gate (generalize to `verify_world.py` parameterized by the substrate, per DO-NOT-REPEAT 12).

## 6. What made Ondina fast (the reusable accelerators)

- Structures chosen before the patient, so substrate armed every task (KM's costliest lesson, avoided).
- The whole DO-NOT-REPEAT ledger inherited cold - the build mistakes were pre-paid.
- Mode A clone of a proven approved artifact instead of designing chrome from scratch.
- Single source of truth + a one-command gate, so a value change propagated and re-verified in seconds.
- Deterministic builds, so rebuilds never churned SHAs or re-introduced drift.
- A filled planning canvas before any document existed.

## 7. Next step - the generator

This doc is the spec. The generator (`tools/new_world.py`, proposed) takes a case note and emits: the folder skeleton, a templated brainstorm and spec pre-filled with all the Section 3 invariants and the `<<PHYSICIAN>>` decision markers, the wired builders and a `clinical_data.py` stub, and a green gate from the first commit. The physician fills the six gates; everything downstream is one command and byte-reproducible. Build the generator only after this recipe is ratified, so it implements an agreed spine rather than a guessed one.
