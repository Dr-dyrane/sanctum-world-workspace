#!/usr/bin/env python3
"""EW22: Mrs. Lydell's repeat 12-lead ECG, established rate-controlled atrial fibrillation,
authored render in the house ECG style (the standard 3x4 layout plus a lead II rhythm strip,
matching the med-data ECG Pro layout the contributor used on the site).

PROVENANCE (the defence, recorded here on purpose): AUTHORED data render, not a sourced image.
The waveform is computed numerically below and drawn on standard ECG paper with matplotlib. It is
(1) not AI-generated imaging (Larry 06/18 bans generated photos/films; a rendered printout is
allowed), (2) not a real person's ECG, so no PHI, no copyright, no attribution, and (3) consistent
with the frozen world: Mrs. Lydell's atrial fibrillation is established and rate-controlled on
metoprolol and apixaban, named on the 06/13 twelve-lead report (EW21) and the telemetry summary
(EW32). Saved metadata-clean. Reproduce with this script.

DISCIPLINE: machine fields only, NO printed interpretation. Rhythm is irregularly irregular with no
organized P waves (PR and P axis undetectable), rate-controlled near 78. The reader infers atrial
fibrillation; the image never prints the word, and there is no "Simulation"/tool watermark.

Identity matches the frozen chart: Marva Lydell, MRN ML-7782304, DOB 04/22/1953.
Dated 06/15/2025 (hospital day 3), within the 06/13 to 06/19 admission.
"""
from __future__ import annotations
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ecg_12lead_06152025.jpg"
FS = 400
DUR = 10.0
rng = np.random.default_rng(20250615)
t = np.linspace(0, DUR, int(FS * DUR), endpoint=False)

# rate-controlled afib: irregularly irregular R-R, mean near 78 bpm (metoprolol on board)
rr, tot = [], 0.45
while tot < DUR + 1.0:
    rr.append(rng.uniform(0.60, 0.95)); tot += rr[-1]
beats = 0.45 + np.cumsum(rr)
beats = beats[beats < DUR - 0.05]

def fib(tt):  # fibrillatory baseline, no P waves
    s = np.zeros_like(tt)
    for f, a in [(6.0, 0.030), (7.5, 0.022), (4.7, 0.018)]:
        s += a * np.sin(2 * np.pi * f * tt + rng.uniform(0, 6))
    s += 0.010 * rng.standard_normal(tt.size)
    s += 0.022 * np.sin(2 * np.pi * 0.23 * tt + 1.1)
    return s

def qrs_n(tt, tc, amp):   # normal-ish QRST
    return (-0.08*amp*np.exp(-((tt-(tc-0.020))**2)/(2*0.006**2))
            +1.00*amp*np.exp(-((tt-tc)**2)/(2*0.0090**2))
            -0.22*amp*np.exp(-((tt-(tc+0.024))**2)/(2*0.010**2))
            +0.20*amp*np.exp(-((tt-(tc+0.200))**2)/(2*0.048**2)))

def qrs_rs(tt, tc, amp):  # V1/V2: small r, deep S
    return ( 0.25*amp*np.exp(-((tt-(tc-0.006))**2)/(2*0.007**2))
            -1.00*amp*np.exp(-((tt-(tc+0.018))**2)/(2*0.012**2))
            +0.18*amp*np.exp(-((tt-(tc+0.210))**2)/(2*0.050**2)))

# lead: (amplitude in mV-ish, morphology); aVR inverted, V1/V2 rS
LEADS = {'I':(1.05,'n'),'II':(1.25,'n'),'III':(0.72,'n'),
         'aVR':(-0.82,'n'),'aVL':(0.55,'n'),'aVF':(0.85,'n'),
         'V1':(0.82,'rs'),'V2':(1.20,'rs'),'V3':(1.00,'n'),
         'V4':(1.40,'n'),'V5':(1.28,'n'),'V6':(1.05,'n')}

def lead_signal(tt, amp, morph):
    s = fib(tt) * (1.0 if amp >= 0 else 0.8)
    for b in beats:
        if tt[0]-0.30 <= b <= tt[-1]+0.30:
            s += qrs_rs(tt, b, abs(amp))*np.sign(amp) if morph == 'rs' else qrs_n(tt, b, amp)
    return s

# ---- paper geometry (mm; 25 mm/s, 10 mm/mV) ----
Wmm, Hmm = 266.0, 190.0
colx = [8.0, 70.5, 133.0, 195.5]            # 4 columns, 62.5 mm (2.5 s) each
ybase = [150.0, 113.0, 76.0]                 # 3 lead rows
ystrip = 34.0                                # lead II rhythm strip
grid = {(0,0):'I',(1,0):'II',(2,0):'III',(0,1):'aVR',(1,1):'aVL',(2,1):'aVF',
        (0,2):'V1',(1,2):'V2',(2,2):'V3',(0,3):'V4',(1,3):'V5',(2,3):'V6'}

fig = plt.figure(figsize=(Wmm/25.4, Hmm/25.4), dpi=200)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, Wmm); ax.set_ylim(0, Hmm)
ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor('white')

# ECG grid
for x in np.arange(0, Wmm+0.1, 1):  ax.plot([x,x],[0,Hmm], color='#f4c6c6', lw=0.3, zorder=0)
for y in np.arange(0, Hmm+0.1, 1):  ax.plot([0,Wmm],[y,y], color='#f4c6c6', lw=0.3, zorder=0)
for x in np.arange(0, Wmm+0.1, 5):  ax.plot([x,x],[0,Hmm], color='#e59a9a', lw=0.6, zorder=0)
for y in np.arange(0, Hmm+0.1, 5):  ax.plot([0,Wmm],[y,y], color='#e59a9a', lw=0.6, zorder=0)

mono = dict(family='monospace', color='#0a0a0a')
# header machine fields (no diagnosis)
ax.text(8, 185.5, "NAME: Marva Lydell        ID: ML-7782304", fontsize=8.5, weight='bold', **mono)
ax.text(8, 181.4, "SEX: Female    AGE: 72    DOB: 04/22/1953", fontsize=8, **mono)
ax.text(8, 177.6, "Recorded 06/15/2025 07:42    Lead II monitored continuously", fontsize=7.6, **mono)
ax.text(8, 173.8, "VR 78 bpm (IRREG)   PR --   QRS 90 ms   QT/QTc 360/415 ms   P axis --", fontsize=7.6, **mono)
ax.text(8, 170.0, "25 mm/s    10 mm/mV    Filter 150 Hz ~ 60 Hz Notch", fontsize=7.6, **mono)
ax.text(Wmm-8, 185.5, "06/15/2025", fontsize=8, ha='right', **mono)

# calibration pulse (1 mV = 10 mm) at far left of the strip
cx = np.array([2.0,3.0,3.0,7.0,7.0,8.0]); cy = ystrip + np.array([0,0,10,10,0,0])
ax.plot(cx, cy, color='#101010', lw=0.9)

# 12 leads, 3x4
for (r, c), name in grid.items():
    amp, morph = LEADS[name]
    w0 = c*2.5; m = (t >= w0) & (t < w0+2.5)
    tt = t[m]; sig = lead_signal(tt, amp, morph)
    ax.plot(colx[c] + (tt-w0)*25.0, ybase[r] + sig*10.0, color='#101010', lw=0.85, solid_capstyle='round')
    ax.text(colx[c]+1.0, ybase[r]+12.5, name, fontsize=8.5, weight='bold', **mono)
    if c > 0:  # thin column separator tick
        ax.plot([colx[c]-0.3, colx[c]-0.3], [ybase[r]-9, ybase[r]+9], color='#101010', lw=0.5)

# lead II rhythm strip, full 10 s
amp, morph = LEADS['II']; sig = lead_signal(t, amp, morph)
ax.plot(8.0 + t*25.0, ystrip + sig*10.0, color='#101010', lw=0.85, solid_capstyle='round')
ax.text(9.0, ystrip+12.5, "II", fontsize=8.5, weight='bold', **mono)

fig.savefig(OUT, dpi=200, facecolor='white', pil_kwargs={"quality": 92})
try:
    from PIL import Image
    Image.open(OUT).convert('RGB').save(OUT, "JPEG", quality=92)  # drop ancillary metadata
except Exception:
    pass
print("rendered", OUT, "| beats:", len(beats), "| mean RR ms:", round(1000*np.mean(np.diff(beats))), "| ~bpm:", round(60/np.mean(np.diff(beats))))
