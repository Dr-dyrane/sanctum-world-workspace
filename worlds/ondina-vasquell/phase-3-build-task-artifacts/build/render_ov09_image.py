#!/usr/bin/env python3
"""REFERENCE IMPLEMENTATION. OV09 moved off the image engine in v3 (now an embedded-wrong
carry-forward, no image), so this script no longer feeds a live task. It is kept as the canonical
reference for rendering off-text REPORT images in-repo, cited by docs/docx-generation-method.md
section 5, AGENTS.md rule 1, and OV-FLOOR-MECHANISM-LIBRARY.md.

Render an off-text report image through the canonical Epic renderer (build_one) + LibreOffice,
so the radiograph report image carries the EXACT world house chrome (masthead, blue bar, patient
storyboard, PATIENT/ENCOUNTER block), indistinguishable from the other charts. Build a DIAGNOSTIC
IMAGING REPORT docx, convert to PDF then PNG, crop to content, save as
platform/task9/current/foot_radiograph_05242026.jpg. Finding locked to golden-OV09-v1.docx.
No Codex. Needs soffice + pdftoppm (present in the build sandbox; broken on the Mac).
"""
from __future__ import annotations
import sys, subprocess, tempfile
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import warnings; warnings.filterwarnings("ignore")
import build_world_files as W
from PIL import Image, ImageOps

T9 = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts/platform/task9/current"
OUT = T9 / "foot_radiograph_05242026.jpg"
tmp = Path(tempfile.mkdtemp())

REPORT = (
    "foot_radiograph_report_05242026.docx", "progress", "DIAGNOSTIC IMAGING REPORT", "05/24/2026",
    [
        ("title", "LEFT FOOT RADIOGRAPH - DIABETIC FOOT INFECTION"),
        ("filing", "Author: Radiology - Diagnostic Imaging | Date of Service: 05/24/2026 0915 | "
                   "Status: Final | Accession HCR-XR-26-0731"),
        ("section", "EXAMINATION"),
        ("body", "Left foot, two views (AP and oblique)."),
        ("section", "CLINICAL HISTORY"),
        ("body", "Diabetic foot infection, plantar forefoot ulcer. Evaluate for osteomyelitis prior to "
                 "transfer. Prior MRI 05/18/2026 reported marrow edema, equivocal for osteomyelitis."),
        ("section", "FINDINGS"),
        ("body", "There is new cortical destruction at the second metatarsal head with a moth-eaten lucent "
                 "appearance and loss of the normal cortical margin, not present on the prior study. Adjacent "
                 "plantar soft-tissue swelling is noted. The remaining metatarsals, tarsals, and phalanges are "
                 "intact, with no additional erosion or fracture. No radiopaque foreign body. Postsurgical "
                 "changes from recent debridement are present in the soft tissues."),
        ("section", "IMPRESSION"),
        ("body", "Cortical destruction at the second metatarsal head, new compared with the prior MRI, "
                 "consistent with osteomyelitis. Recommend correlation with Infectious Disease for an "
                 "osteomyelitis treatment course."),
        ("sig", "Electronically signed by Radiology on 05/24/2026 1005"),
    ],
)

docx = W.build_one(REPORT, outdir=tmp)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(docx)],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
pdf = tmp / (docx.stem + ".pdf")
subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1", str(pdf), str(tmp / "pg")],
               check=True, timeout=60)
im = Image.open(tmp / "pg-1.png").convert("RGB")
# crop trailing whitespace: bbox of non-white content on an inverted grayscale copy
bbox = ImageOps.invert(im.convert("L")).getbbox()
if bbox:
    im = im.crop((0, 0, im.width, min(im.height, bbox[3] + 55)))
im.save(str(OUT), "JPEG", quality=88)
print("rendered via epic+soffice ->", OUT, im.size)
