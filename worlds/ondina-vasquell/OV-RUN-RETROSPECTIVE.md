# Ondina Vasquell run retrospective - lessons from a fast build

Date: 2026-06-12. Why this exists: the world ran fast (decisions 11 to 13 collapsed the review gates to run continuous to an upload-ready package). Speed is fine only if the lessons are captured, the hallucination sources are removed, and the canonicals are hardened so the same misses are caught automatically next time. Companion ledger: `DO-NOT-REPEAT.md` (class-level rules). One-command gate added this run: `tools/verify_ondina.py`.

## 1. What was built
Brainstorm (content, DOCX, transcript), World Spec (content, DOCX, transcript), 29 world + 3 supplementary + 9 task reference DOCX, 2 writer-produced images, and 10 full task-setup packages (prompt, golden draft, grader, run-instructions, prereg, A0.5, task file). All on the canonical Epic template, committed and pushed.

## 2. Mistakes caught this run (root cause, fix, where canonicalized)

1. World-file design drifted from KM (gray/black approximation instead of KM navy/blue/light-blue). Root cause: re-derived the look from memory instead of extracting KM's actual recipe. Fix: read the constants from `generate_reference_files.py` and matched the fills/colors vocabulary as a verified subset. Canonical: DO-NOT-REPEAT "Canonical docx template rule" + "match KM from bytes" rule below.

2. Header/footer leak of a prior-world identifier. Root cause: Mode A clone bases carry the prior patient's name and MRN in the running header and footer, and `clear_body` only clears the body. Fix: clear and rebuild every header and footer part; added `verify_no_km_identifiers` scanning all parts. Canonical: new DO-NOT-REPEAT entry.

3. Golden built as a plain note, off-template. Root cause: hand-built with a bare `Document()`. Fix: route goldens through `build_goldens.py` and the one Epic renderer. Canonical: docx template rule.

4. Task files built without the storyboard, and not placed in their task folders. Root cause: assumed external docs were a different genre; missed that KM applies the house Epic chrome to task files and that task files upload WITH the task. Fix: task files render through `build_one` and a copy lands in each `platform/taskN/current/`. Canonical: new DO-NOT-REPEAT entry.

5. Filename collision: a task file was committed as `... 2.docx` (an OS or sync duplicate suffix), and the canonical name was missing. Root cause: a duplicate-named artifact slipped into git. Fix: rebuilt under the canonical name, removed the duplicate, made the copy step reproducible. Canonical: new DO-NOT-REPEAT entry plus a filename check in the gate.

6. Benchmark register in the transcripts ("the model"). Root cause: design-conversation language not sanitized. Fix: reframed to clinician language; re-verified zero benchmark or tooling register. Canonical: new DO-NOT-REPEAT entry.

## 3. Hallucination sources removed or guarded
- Multiple sources of truth for one clinical value. Risk: a value (for example the toe pressure, which moved from 38 to 55 mid-run) lives in the substrate pack, `clinical_data.py`, the goldens, and the task files, and can drift into a contradiction the reader treats as fact. Guard: the substrate pack is the single ratified source; `tools/verify_ondina.py` now cross-checks the key anchors across every docx and fails on any contradictory variant.
- Inventing clinical specifics. Guard already in place: decision 12 no-invention rule, the DERIVED registry (texture values flagged and physician-ratified), and physician-confirm flags inside each golden. Kept and reaffirmed.
- Building from memory or convenience copies. Guard: verify on the agent-read docx bytes, and match KM by extracting from KM bytes, never approximating from memory.
- Ad-hoc docx building. Guard: the canonical renderer is the only path; the gate fails any docx whose fills or colors are not a subset of the world-file vocabulary.
- Stale provenance. Risk: stale SHAs and counts in the cockpit (caught earlier when the Brainstorm and World Spec SHAs were duplicated). Guard: regenerate the manifest with live SHAs; do not hand-copy hashes.

## 4. What protected us (keep these)
The DERIVED ratification registry, the A0.5 fairness gate run against built bytes, the no-synthetic and no-KM-identifier gates, the world-versus-task separation, and verifying fills and colors as a subset of the world vocabulary. These caught the leaks and kept invention out. The new one-command gate bundles them so the next world runs them in one step.

## 5. Run the gate before any stage
`python3 tools/verify_ondina.py` - checks every docx for synthetic tokens, prior-world identifiers, banned characters, scrubbed metadata, template parity (fills and colors subset), filename match to the plan with no duplicate-suffixed files, and cross-file consistency of the ratified anchors. Green before upload, every time.
