# EMR template fidelity: how KM addressed the demographics/encounter block vs OV (2026-06-15)

Question (Alexander): how did the previous world (KM) handle the EMR template - specifically the PATIENT/ENCOUNTER demographics block - and how does OV compare? Method: probed KM clean bases + KM goldens + OV files with python-docx (table vs paragraph structure of the demographics metadata).

## Finding: KM is HETEROGENEOUS - two patterns by note type
PATTERN A - rich storyboard table, NO paragraph encounter block. A 3-row x 4-col storyboard table packs all demographics into the table (Date, Unit/Room, Allergies, Code Status, Attending, FIN, Service, Document), then the note goes straight to clinical content. No separate "PATIENT / ENCOUNTER" block. Used by KM's physician-deliverable goldens: KM07, KM08, KM09, KM10; also the admission H&P and the discharge snapshot.
  Example (golden-KM10-v3) TABLE 2 (3x4): row0 = NAME / age / sex / DOB / (MRN); row1 = Date | Unit/Room | Allergies | Code Status; row2 = Attending | FIN | Service | Document. Then paragraphs go straight to "Item 1 ...".

PATTERN B - lean storyboard table (2-row) + a paragraph "PATIENT / ENCOUNTER" block. The 2-row storyboard table carries only Date/Author/Allergies/Document; a separate paragraph block then lists Patient / Sex-DOB / MRN-FIN / Unit-Room / Code / Allergies / Attending / Service / DoS / Language. Used by KM cardiology/ED consults and golden KM06.

## OV: uniform Pattern B everywhere
OV's renderer standardized on Pattern B for ALL note types: epic.storyboard = the lean 2-row table; epic.encounter_block = the paragraph "PATIENT / ENCOUNTER" block ("metadata as labeled body lines"). OV faithfully cloned KM's STYLES (masthead, blue bar, storyboard chrome, fonts) but flattened the encounter-metadata LAYOUT to one pattern rather than varying it by note type. Verified across OV world files (admission H&P), OV01, OV02, and OV04 - all Pattern B; verify_ondina template-parity is green precisely because they all agree.

## So Alexander's observation, made precise
For the genre OV04 imitates (a physician completion/transition note - closest KM analogs are the KM07/08/09/10 and discharge-summary goldens), KM used Pattern A (demographics in a table). OV04 uses Pattern B. Pattern B is NOT invented - it is a genuine KM pattern, but KM reserved it for consults/interval notes, not for these deliverable goldens.

## Impact + decision
- Cosmetic/structural only: the demographics layout does not touch the trap, the fairness construction, or the floor. It is a header-block rendering choice.
- OV is internally consistent (all Pattern B), already shipped and banked (OV01 banked, OV02 piloted) with this layout, and template-parity green.
- Aligning OV to Pattern A would mean reshaping all 34 FROZEN world files plus the banked/piloted tasks - a freeze violation (DO-NOT-REPEAT #21) and a full re-ship, for a header block that has already cleared review and a pilot.
- Minor realism nit in Pattern B: Allergies and Date repeat in both the storyboard table and the paragraph block (Pattern A avoids the repeat). Acceptable - real Epic notes repeat the header banner.
- DECISION: keep OV uniform on Pattern B; OV04 stays as shipped-OV style. The divergence is LOCKED and recorded so OV04 (or any task) is not "fixed" to a table per-task and broken out of parity. If full Pattern-A alignment is ever wanted, it is a world-rebuild decision, out of scope while driving OV to 8 tasks.
