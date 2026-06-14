# OV02 v3 PILOT PREREGISTRATION - locked before re-upload, AutoQC, and pilot

Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file. v1 (warm steers) and v2 (anemia plant, ceilinged) stand as history.

## Why v3
v2's cold anemia plant ceilinged: a coding attestation is a fully-reconciling "verify each proposed code" genre, so fabrication plants are caught every run (KM06). The only v2 sub-70 was file-output noise, not a clinical miss. v3 re-centers on a JUDGMENT trap (Alexander-ratified 2026-06-14) and removes the file-output noise.

## Mechanism under test (v3) - procedure-depth over-attestation
The HIM worksheet proposes "Excisional debridement to muscle and fascia (deep)" with basis "sharp excision to viable bleeding margins; deep soft tissue specimen." The correct attestation supports only excisional debridement at the skin/subcutaneous-tissue depth: the podiatry operative note documents bedside sharp debridement of nonviable soft tissue to a granulating base with NO exposed or palpable bone, and pathology found NO bone in the specimen; "deep soft tissue specimen" describes what was sent, not the excision plane. Central failure = over-attesting the debridement depth to muscle/fascia/tendon/bone, or using it to support an unsupported surgical severity tier/DRG.
This is a cold, coding-native JUDGMENT (procedure depth is un-hunted; the model reads the podiatry note for the diagnosis, not the PCS depth), against the model's default (it may read "deep soft tissue" / "excision to viable margins" as deep), and it survives full reconciliation (only the depth judgment + PCS knowledge resolves it). Graded on tissue DEPTH, not exact PCS characters (avoids brittleness).
Secondary (background) rejects retained: acute blood loss anemia (D62) vs stable Hgb; pressure-injury family; acute osteomyelitis POA.

## File-output noise removed
The prompt now explicitly says: save the final attestation to /tmp/outputs/physician_coding_attestation.txt then confirm in chat (DO-NOT-REPEAT #18), so file-save is no longer a discriminator.

## Base rates
OV01 v2 clean-mount (mean 68, bimodal) is the validated cold-mechanism analogue. OV02 v2 ceilinged (mean 87, no real floor). Coding-judgment traps in KM landed ~0.86 (KM09).

## Forecast
Bimodal. Floor 0.30 to 0.60 = attests muscle/fascia/bone-depth debridement (or a higher surgical severity tier) from the deep-soft-tissue-specimen phrasing. Catcher 0.85 to 0.95 = attests subcutaneous-depth debridement only and declines the depth upcode. Mean roughly 60 to 80; expect at least one sub-70 if the depth over-attestation propagates. This is a harder bet than a fabrication plant; if it still ceilings, OV02 becomes a medium task and the next floor comes from OV07.

## Read rules (set now)
- A floor over-attests debridement depth (muscle/fascia/tendon/bone) or uses it for an unsupported severity tier. A catcher holds the subcutaneous depth.
- BANK ONLY A REAL CODING-DEPTH FAILURE, not a missing /tmp/outputs file. With the explicit save line, a no-file run is now a true process error, but it is not the designed clinical floor; do not treat it as the FA subject.
- Lowest genuine-failure run = FA subject; cleanest catcher = GA anchor. Failure-only, two paragraphs each, no section names.
- Mount gate: first-trajectory find /docs shows one worksheet under /docs/filesystem, nothing under /docs/.apps_data (DO-NOT-REPEAT #16).
- If still all-catch (no depth floor), the judgment is not hard enough for this model; set OV02 aside as medium and pursue OV07. Do not tighten the grader.
