#!/usr/bin/env python3
"""Render Mrs. Lydell's telemetry rhythm strip (EW22): established, rate-controlled atrial
fibrillation, as an authored monitor printout for the off-text-image substrate.

PROVENANCE (the defence, recorded here on purpose): this is an AUTHORED data render, not a
sourced image. The waveform is computed numerically below and drawn on standard ECG paper with
matplotlib. It is therefore (1) not AI-generated imaging (Larry 06/18 bans generated photos and
films; a rendered printout is allowed, exactly like the OV rhythm strip), (2) not a real person's
ECG, so there is no PHI, no copyright, and no attribution to manage, and (3) clinically consistent
with the frozen world: Mrs. Lydell's atrial fibrillation is established and rate-controlled on
metoprolol and apixaban, documented on the 06/13 twelve-lead report (EW21) and the telemetry
summary (EW32). The strip is consistent SUBSTRATE, never the sole scored trap. The image is saved
metadata-clean. Reproduce with this script.

DISCIPLINE: machine fields only, no printed interpretation. The rhythm is irregularly irregular
with no organized P waves (PR and P axis undetectable), rate-controlled near 80. The reader infers
atrial fibrillation; the strip never prints the word. Unlike the OV strip, there is NO "no prior"
line: this afib is known and managed, not new-onset.

Patient identity matches the frozen chart: Marva Lydell, MRN ML-7782304, DOB 04/22/1953.
Dated 06/15/2025 (hospital day 3), a telemetry capture within the 06/13 to 06/19 admission.
"""
from __future__ import annotations
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/afib_rhythm_strip_06152025.jpg"
FS = 300
SECS = 10.0
rng = np.random.default_rng(20250615)
t = np.linspace(0, SECS, int(FS * SECS))

# --- atrial fibrillation lead II: irregularly irregular R-R, no P waves, fine fibrillatory baseline ---
# RATE-CONTROLLED (metoprolol on board): ventricular intervals long enough for a mean near 80 bpm,
# still irregularly irregular beat to beat. (OV used 0.38-0.70 for a rapid response; this is slower.)
rr, tot = [], 1.0
while tot < SECS + 1.0:
    iv = rng.uniform(0.58, 0.96)            # rate-controlled, irregularly irregular
    rr.append(iv); tot += iv
beats = 0.6 + np.cumsum(rr)

sig = np.zeros_like(t)
# fibrillatory baseline (f-waves), low amplitude, ~5 to 8 Hz, plus a little wander and noise
for f, a in [(6.2, 0.035), (7.7, 0.025), (4.9, 0.02)]:
    sig += a * np.sin(2 * np.pi * f * t + rng.uniform(0, 6))
sig += 0.012 * rng.standard_normal(t.size)
sig += 0.03 * np.sin(2 * np.pi * 0.25 * t)   # slow baseline wander

def beat(tc, amp):
    q = -0.10 * amp * np.exp(-((t - (tc - 0.022)) ** 2) / (2 * 0.007 ** 2))
    r =  1.20 * amp * np.exp(-((t - tc) ** 2) / (2 * 0.010 ** 2))
    s = -0.26 * amp * np.exp(-((t - (tc + 0.026)) ** 2) / (2 * 0.011 ** 2))
    tw = 0.22 * amp * np.exp(-((t - (tc + 0.205)) ** 2) / (2 * 0.050 ** 2))
    return q + r + s + tw

vr = []
for i, b in enumerate(beats):
    if b < SECS - 0.1:
        amp = rng.uniform(0.80, 1.16)        # beat-to-beat amplitude variation (afib)
        sig += beat(b, amp)
        if i > 0:
            vr.append(b - beats[i - 1])
vent_rate = int(round(60.0 / np.mean(vr)))   # mean ventricular rate (rate-controlled)

# --- draw on ECG paper (25 mm/s, 10 mm/mV): x_mm = t*25, y_mm = mV*10 ---
fig = plt.figure(figsize=(11.5, 5.2), dpi=170)
fig.patch.set_facecolor("white")
mono = {"family": "monospace", "color": "#101010"}

# header block: neutral telemetry-monitor printout (no fabricated hospital banner; this world pins
# no facility name, and the formal letterhead lives on the EW21 ECG report, not the raw strip)
ax_h = fig.add_axes([0.0, 0.74, 1.0, 0.26]); ax_h.axis("off")
ax_h.text(0.012, 0.86, "CARDIAC TELEMETRY   RHYTHM STRIP", fontsize=10.5, weight="bold", **mono)
ax_h.text(0.012, 0.62, "Lydell, Marva        MRN ML-7782304        DOB 04/22/1953   72 y   F", fontsize=9.5, **mono)
ax_h.text(0.012, 0.40, "Recorded 06/15/2025 07:42      Continuous telemetry, lead II      Acq: monitor", fontsize=8.5, **mono)
ax_h.text(0.012, 0.18, f"Vent rate {vent_rate} bpm (irregular)   PR --   QRS 90 ms   QT/QTc 360/415 ms   P axis --", fontsize=8.5, **mono)
ax_h.text(0.66, 0.40, "Speed 25 mm/s", fontsize=8.5, **mono)
ax_h.text(0.66, 0.18, "Gain 10 mm/mV", fontsize=8.5, **mono)

# strip
ax = fig.add_axes([0.012, 0.06, 0.976, 0.60])
# calibration pulse: 1 mV (10 mm) step at the very start, ~0.20 s wide
cal_t = np.array([0.00, 0.06, 0.06, 0.26, 0.26, 0.34]); cal_mm = np.array([0, 0, 10, 10, 0, 0])
xmm = np.concatenate([cal_t * 25.0, (t + 0.40) * 25.0])
ymm = np.concatenate([cal_mm, sig * 10.0])
ax.plot(xmm, ymm, color="#0a0a0a", lw=0.9, solid_capstyle="round")
ax.set_xlim(0, (SECS + 0.5) * 25); ax.set_ylim(-9, 11)
ax.set_xticks(np.arange(0, (SECS + 0.5) * 25 + 1, 5)); ax.set_yticks(np.arange(-9, 12, 5))
ax.set_xticks(np.arange(0, (SECS + 0.5) * 25 + 1, 1), minor=True); ax.set_yticks(np.arange(-9, 12, 1), minor=True)
ax.grid(which="minor", color="#f3b4b4", lw=0.4); ax.grid(which="major", color="#e06e6e", lw=0.7)
ax.set_axisbelow(True)
for s in ax.spines.values(): s.set_visible(False)
ax.set_xticklabels([]); ax.set_yticklabels([]); ax.tick_params(length=0)
ax.text(2, 8.4, "II", fontsize=11, weight="bold", **mono)

fig.savefig(OUT, dpi=170, facecolor="white", pil_kwargs={"quality": 92})
# metadata scrub: re-save through PIL to drop ancillary chunks / EXIF
try:
    from PIL import Image
    im = Image.open(OUT).convert("RGB"); im.save(OUT, "JPEG", quality=92)
except Exception:
    pass
print("rendered", OUT, "| vent rate", vent_rate, "bpm (rate-controlled)")
