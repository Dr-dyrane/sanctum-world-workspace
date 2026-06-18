# Second-pass style audit - Ondina reference files vs KM world documents

Trigger: "compare styles with km world documents... it doesnt quite match the recent world files... using an old script note mode a... audit km world files, golden in task." First-pass files were built but diverged from the KM design system, and a header/footer leak was found. This records the gap and the fix.

## How measured

Doc method (docs/docx-generation-method.md) RECON: fingerprint (sizes, colors, fills, borders) + structure dump on a same-genre pair: KM `pipeline-output/filesystem/hospitalist_progress_hd4_05212026.docx` (TARGET) vs my `world-files/hospitalist_progress_hd4_05192026.docx`. Ground-truth design constants read from `tools/generate_reference_files.py` (the generator that produced the 33 KM reference files).

## Gap 1 - design system colors/fills/sizes did not match KM

| Element | KM target | First pass (wrong) | Fix |
|---|---|---|---|
| Body text color | INK 232830 | hard-coded 000000 | INK 232830 |
| Section header | BLUE 4472C4 bold 10pt, bottom rule C9D4EA | bold black, rule BFBFBF | BLUE 4472C4 + C9D4EA rule |
| Note title | NAVY 1F3864 bold 14pt | black 12pt | NAVY 14pt |
| Patient storyboard fill | CARD light-blue EDF2FA | gray EAEAEA | EDF2FA |
| Table header | B_HEX blue 4472C4 + WHITE text, alt rows CARD | gray EAEAEA, black text | 4472C4 + white + CARD alt |
| Rule / border color | C9D4EA | BFBFBF | C9D4EA |
| Masthead facility | NAVY 11pt bold + dept GRAY 8pt; Confidential BLUE 8.5pt | facility black + gray date | match KM |
| Blue accent bar (1x1 B_HEX) | present | MISSING | added |
| PATIENT / ENCOUNTER block | present (metadata as body lines) | MISSING | added |

Net: first pass invented a gray-and-black approximation; KM is a navy/blue/light-blue system. The fingerprint vocabularies did not intersect (KM fills {4472C4, EDF2FA} vs mine {EAEAEA}; KM colors style-default vs mine {000000, 595959}).

## Gap 2 - header/footer leak (the serious one)

clear_body() removes only body children; header and footer parts are separate and were inherited from the KM clone base. verify_no_synthetic checked synthetic/tool tokens but NOT KM identifiers. Result: 3 files (antibiotic_plan_note, podiatry_debridement_note, nursing_shift_narrative, all cloned from the progress base) carried "Korvin Merrow | MRN KM-6427819" in header1.xml. Nine of the clean bases carry KM identifiers in their header/footer, so any clone that did not rebuild them was exposed.

Fix: clear ALL header/footer parts on every section and write a clean running header ("Ondina Vasquell | MRN OV-3358104") and footer ("facility | document type | Confidential", no synthetic, no KM). New gate verify_no_km_identifiers scans every part for Korvin, Merrow, KM-6427819, Mercy Vale, CSN-204418827, and the KM roster names.

## Mode A confirmation

KM reference files were Mode B (design-system generation) per the method doc; the World Spec was Mode A (template fill). Ondina world files use a hybrid: clone a clean base for byte-identical styles.xml, then rebuild body AND chrome AND header/footer from the KM design constants, scrub all metadata, and run both gates. This keeps styles.xml parity while guaranteeing no KM body/header/footer content survives.

## Status

Second pass rewrites epic.py to the KM constants and clears/rebuilds header/footer; both builders rerun; re-fingerprinted against the KM target and re-scanned for KM + synthetic identifiers; re-rendered for visual parity.
