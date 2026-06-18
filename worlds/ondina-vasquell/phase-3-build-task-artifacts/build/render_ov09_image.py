#!/usr/bin/env python3
"""Render the OV09 v2 off-text image IN-REPO (no Codex / Nanobanara needed), as a transfer-day
foot radiograph report in the world's study-as-image style (matches abi_tbi_tracing JPG). The
finding is locked to golden-OV09-v1.docx: cortical destruction at the second metatarsal head,
new versus the equivocal 05/18 MRI, consistent with osteomyelitis. No banned glyphs; no real ids.
Output: platform/task9/current/foot_radiograph_05242026.jpg
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "platform/task9/current/foot_radiograph_05242026.jpg"
W, H = 1000, 820
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
REG = "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf"
BLD = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
def f(sz, bold=False): return ImageFont.truetype(BLD if bold else REG, sz)
y = 46
def line(t, sz=22, bold=False, gap=8, color=(20, 20, 20), x=60):
    global y; d.text((x, y), t, font=f(sz, bold), fill=color); y += sz + gap
def rule(c=(150, 150, 150)):
    global y; y += 6; d.line((60, y, W - 60, y), fill=c, width=2); y += 14

line("HARBOR CREST REGIONAL MEDICAL CENTER", 26, True, 4, (15, 40, 90))
line("DIAGNOSTIC RADIOLOGY", 20, True, 4, (15, 40, 90))
line("Confidential", 16, False, 6, (120, 120, 120))
rule()
line("DIAGNOSTIC IMAGING REPORT", 22, True, 10)
for t in ["Patient: Ondina Vasquell, 68 y        MRN: OV-3358104",
          "DOB: 03/14/1958        Sex: Female        CSN: CSN-308852140",
          "Study Date: 05/24/2026 0915        Status: Final        Accession HCR-XR-26-0731",
          "Ordering: Hospital Medicine, transfer evaluation",
          "Author: Radiology"]:
    line(t, 19, False, 6, (40, 40, 40))
rule()
line("EXAMINATION", 19, True, 6); line("Left foot, two views (AP and oblique).", 20, False, 12)
line("CLINICAL HISTORY", 19, True, 6)
line("Diabetic foot infection, plantar forefoot ulcer. Evaluate for osteomyelitis prior to transfer.", 20, False, 4)
line("Prior MRI 05/18/2026 reported marrow edema, equivocal for osteomyelitis.", 20, False, 12)
line("FINDINGS", 19, True, 6)
for t in ["There is new cortical destruction at the second metatarsal head with a moth-eaten",
          "lucent appearance and loss of the normal cortical margin, not present on the prior study.",
          "Adjacent plantar soft-tissue swelling is noted. The remaining metatarsals, the tarsals,",
          "and the phalanges are intact, with no additional erosion or fracture. No radiopaque",
          "foreign body. Postsurgical changes from recent debridement are seen in the soft tissues."]:
    line(t, 20, False, 4)
y += 8
line("IMPRESSION", 19, True, 6, (15, 40, 90))
for t in ["Cortical destruction at the second metatarsal head, new compared with the prior MRI,",
          "consistent with osteomyelitis.",
          "Recommend correlation with infectious disease for an osteomyelitis treatment course."]:
    line(t, 21, True, 4)
y += 18; rule()
line("Electronically signed by Radiology on 05/24/2026 1005", 17, False, 4, (90, 90, 90))
img.save(str(OUT), "JPEG", quality=88)
print("rendered", OUT, img.size)
