  /* ════════════════════════════════════════════════════════════
     MODULE 4 · UTILS
     Pure functions only. All band logic lives here.
     ════════════════════════════════════════════════════════════ */
  const U = {
    runBand:  v => CONFIG.runBands.find(b => v >= b.min),
    hasMean: t => Number.isFinite(t.mean),
    meanBand: m => Number.isFinite(m)
      ? CONFIG.meanBands.find(b => m >= b.min)
      : { id:'pending', css:'b-pending', tag:'Pending', plain:'No pilot scores yet' },
    scoreSortValue: t => Number.isFinite(t.mean) ? t.mean : null,
    isCatcher: v => v >= 85,
    isFloor:   v => v <= 40,
    counts(t){
      const spread = Array.isArray(t.spread) ? t.spread : [];
      const c = spread.filter(U.isCatcher).length;
      const f = spread.filter(U.isFloor).length;
      const sub70 = spread.filter(v => v < 70).length;
      return { catchers:c, floors:f, sub70, confirmed:spread.length };
    },
    fmtMean: t => U.hasMean(t) ? (t.approx ? '≈' : '') + t.mean : 'TBD',
    esc: s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'),
    /* Wrap known glossary keywords in already-safe strings (labels only, not freeform data) */
    term: (key, text) => `<button class="term" data-g="${key}">${text}</button>`,
  };
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  Object.values(WORLDS).forEach(world => {
    world.tasks.forEach(t => {
      if (Array.isArray(t.spread) && t.runsTotal > 0 && t.spread.length === t.runsTotal) {
        const computed = t.spread.reduce((sum, v) => sum + v, 0) / t.spread.length;
        t.mean = Number(computed.toFixed(1));
      }
    });
  });

  /* ════════════════════════════════════════════════════════════
     MODULE 5 · STATE
     Persisted UI state (localStorage, versioned, migrating).
     Levels: component (aria) to session (filter/sort/expanded)
     to preference (theme/mute) to URL (hash wins) to system.
     ════════════════════════════════════════════════════════════ */
  const KMState = (function(){
    const KEY = 'km-dash-v3';
    const defaults = { theme:null, muted:null, filter:'all', sort:'position', expanded:[], world:null };
    let s;
    try { s = { ...defaults, ...(JSON.parse(localStorage.getItem(KEY)) || {}) }; }
    catch { s = { ...defaults }; }
    /* migrate v1 once */
    try {
      const v1 = JSON.parse(localStorage.getItem('km-dash-v1'));
      if (v1 && localStorage.getItem(KEY) === null){
        s = { ...s, ...v1 };
        if (v1.filter === 'complete') s.filter = 'delivered';
        if (v1.filter === 'pending')  s.filter = 'review';
        localStorage.removeItem('km-dash-v1');
      }
    } catch {}
    const subs = {};
    function save(){ try { localStorage.setItem(KEY, JSON.stringify(s)); } catch {} }
    save();
    return {
      get: k => s[k],
      set(k, v){ s[k] = v; save(); (subs[k]||[]).forEach(fn=>fn(v)); },
      on(k, fn){ (subs[k] = subs[k]||[]).push(fn); },
    };
  })();

  /* ════════════════════════════════════════════════════════════
     MODULE 5.5 · WORLD CONTROL
     Owns the active world. `tasks` is the live alias every view
     reads; WorldCtl.set() swaps it and re-renders everything.
     ════════════════════════════════════════════════════════════ */
  const WorldCtl = (function(){
    let id = WORLDS[KMState.get('world')] ? KMState.get('world') : DEFAULT_WORLD;
    return {
      get id(){ return id; },
      get world(){ return WORLDS[id]; },
      set(newId){
        if (!WORLDS[newId] || newId === id) return;
        id = newId;
        KMState.set('world', id);
        tasks = WORLDS[id].tasks;
        history.replaceState(null,'', location.pathname + location.search);  /* clear stale hash */
        renderWorld();
      },
    };
  })();
  let tasks = WorldCtl.world.tasks;

  /* ════════════════════════════════════════════════════════════
     MODULE 6 · COMPONENTS
     Small render functions returning HTML strings. No state.
     ════════════════════════════════════════════════════════════ */
  const C = {

    /* Score ring: task mean as a radial fill, color by mean band */
    scoreRing(t){
      const circ = 2 * Math.PI * 36;
      if (!U.hasMean(t)) {
        return `<div class="score-ring pending">
          <svg width="92" height="92" viewBox="0 0 92 92" aria-hidden="true">
            <circle class="ring-track" cx="46" cy="46" r="36" stroke-width="5"/>
          </svg>
          <div class="ring-val">
            <span class="font-mono font-bold text-[1.05rem]" style="color:var(--fg-faint)">TBD</span>
          </div>
        </div>`;
      }
      const offset = circ * (1 - t.mean/100);
      const band = U.meanBand(t.mean);
      const valColor = band.id==='soft' ? 'var(--accent-a)' : band.id==='mid' ? 'var(--accent-b)' : 'var(--warn)';
      return `<div class="score-ring">
        <svg width="92" height="92" viewBox="0 0 92 92" aria-hidden="true">
          <circle class="ring-track" cx="46" cy="46" r="36" stroke-width="5"/>
          <circle class="ring-fill ${band.css}" cx="46" cy="46" r="36" stroke-width="5"
            stroke-dasharray="${circ.toFixed(1)}" stroke-dashoffset="${circ.toFixed(1)}"
            data-target="${offset.toFixed(1)}"
            transform="rotate(-90 46 46)"/>
        </svg>
        <div class="ring-val">
          <span class="font-mono font-bold text-[1.3rem]" style="color:${valColor}">${U.fmtMean(t)}</span>
          <span class="font-mono text-[0.6rem]" style="color:var(--fg-faint)">%</span>
        </div>
      </div>`;
    },

    /* Ten run dots; unknown runs render as hollow dots */
    dots(t){
      const spread = Array.isArray(t.spread) ? t.spread : [];
      const out = spread.map((v,i)=>{
        const b = U.runBand(v);
        const isFloor = b.id==='floor';
        const op = b.id==='catcher' ? 1 : b.id==='high' ? 0.6 : b.id==='mid' ? 0.35 : 0.5;
        const bg = isFloor ? 'var(--warn-soft)' : 'var(--accent-a)';
        return `<span class="dot ${isFloor?'pulse':''}" role="img"
          aria-label="Run ${i+1}: ${v} percent, ${b.label}"
          title="Run ${i+1}: ${v}% · ${b.label}${t.approx?' (approximate)':''}"
          style="width:13px;height:13px;border-radius:9999px;display:inline-block;background:${bg};opacity:${op}"></span>`;
      });
      for (let i = spread.length; i < t.runsTotal; i++){
        out.push(`<span class="dot empty" role="img" aria-label="Run ${i+1}: not yet confirmed"
          title="Run ${i+1}: not yet confirmed"
          style="width:13px;height:13px;border-radius:9999px;display:inline-block"></span>`);
      }
      return out.join('');
    },

    /* Sparkline of the spread (floors in amber) */
    sparkline(spread){
      if (!spread.length) return `<svg class="sparkline" width="64" height="28" viewBox="0 0 64 28" aria-hidden="true"><line class="spark-pending" x1="4" y1="14" x2="60" y2="14" stroke-width="1.5"/></svg>`;
      const W=64, H=28, pad=3;
      const mn=Math.min(...spread), mx=Math.max(...spread);
      const range = mx - mn || 1;
      const pts = spread.map((v,i)=>({
        x: pad + i*(W-pad*2)/Math.max(spread.length-1,1),
        y: H - pad - ((v-mn)/range)*(H-pad*2)
      }));
      const poly = pts.map(p=>`${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(' ');
      const dots = pts.map((p,i)=>
        `<circle class="spark-dot${U.isFloor(spread[i])?' low':''}" cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="2"/>`).join('');
      return `<svg class="sparkline" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" aria-hidden="true">
        <polyline class="spark-line" points="${poly}"/>${dots}
      </svg>`;
    },

    /* Pipeline stepper: where this task sits in the lifecycle */
    stepper(t){
      const stageIdx = { planned:0, built:1, piloted:2, review:3, ready:4, delivered:4 };
      const currentIdx = stageIdx[t.stage] ?? 3;
      const steps = CONFIG.stages.map((s,i)=>{
        const done = t.stage === 'delivered' ? true : i < currentIdx;
        const current = t.stage !== 'delivered' && i === currentIdx;
        const doneFinal = t.stage === 'delivered' && s.id === 'delivered';
        const dateNote = (s.id==='delivered' && t.delivered) ? ` · ${t.delivered.slice(5).replace('-','/')}` : '';
        return `<span class="step ${done?'done':''} ${current?'current':''} ${doneFinal?'done-final':''}">
          <span class="step-dot"></span>
          <span class="step-label">${s.label}${dateNote}</span>
        </span>` + (i < CONFIG.stages.length-1 ? `<span class="step-bar ${done?'done':''}"></span>` : '');
      }).join('');
      const plain = t.stage === 'delivered'
        ? `Accepted and handed off${t.delivered ? ' on ' + t.delivered : ''}.`
        : t.stage === 'ready'
        ? 'Reviewed and cleared; queued for delivery on the platform.'
        : t.stage === 'planned'
        ? 'Incoming task placeholder. No pilot data exists yet.'
        : 'Piloted; a human expert is reviewing the task before it can be accepted.';
      return `<div class="stepper stepper-labels-hide" role="img" aria-label="Pipeline: ${plain}">${steps}</div>`;
    },

    /* Counts strip: catchers / floors / sub-70, with glossary terms */
    countsStrip(t){
      const k = U.counts(t);
      const denom = t.runsTotal ? (k.confirmed < t.runsTotal ? `${k.confirmed} confirmed` : `${t.runsTotal}`) : 'not started';
      const approx = t.approx ? '≈ ' : '';
      return `<div class="flex flex-wrap gap-x-4 gap-y-1 mt-2 text-[12px]" style="color:var(--fg-soft)">
        <span>${approx}${U.term('catcher','Catchers')}: <b class="font-mono" ${k.catchers>0?'style="color:var(--ok)"':''}>${k.catchers}</b></span>
        <span>${approx}${U.term('floor','Floors')}: <b class="font-mono" ${k.floors>0?'style="color:var(--warn)"':''}>${k.floors}</b></span>
        <span>${approx}Sub-70: <b class="font-mono">${k.sub70}/${denom}</b></span>
      </div>`;
    },

    /* Single visible data graphic: lower mean creates higher failure signal */
    signal(t){
      if (!U.hasMean(t)) {
        return `<div>
          <div class="flex items-center justify-between gap-3 text-[12px] mb-2" style="color:var(--fg-soft);max-width:320px">
            <span>Failure signal</span>
            <span class="font-mono font-semibold" style="color:var(--fg-faint)">Pending</span>
          </div>
          <div class="signal-track" aria-hidden="true">
            <div class="signal-fill" style="width:0"></div>
          </div>
        </div>`;
      }
      const failure = Math.max(0, Math.min(100, 100 - t.mean));
      const band = U.meanBand(t.mean);
      const color = band.id === 'soft' ? 'var(--accent-a)' : 'var(--warn)';
      return `<div>
        <div class="flex items-center justify-between gap-3 text-[12px] mb-2" style="color:var(--fg-soft);max-width:320px">
          <span>Failure signal</span>
          <span class="font-mono font-semibold" style="color:${color}">${failure.toFixed(1).replace(/\\.0$/,'')}%</span>
        </div>
        <div class="signal-track" aria-hidden="true">
          <div class="signal-fill" style="width:${failure}%"></div>
        </div>
      </div>`;
    },

    /* Data-quality badge */
    qualityBadge(t){
      const q = CONFIG.quality[t.quality];
      return `<span class="badge ${t.quality}" title="${q.plain}">${q.label}</span>`;
    },

    artifactTile(role, fileText, note, icon, status){
      return `<article class="artifact-tile">
        <div class="artifact-icon" aria-hidden="true"><i data-lucide="${icon}" style="width:17px;height:17px"></i></div>
        <div class="min-w-0">
          <div class="artifact-head">
            <span>${U.esc(role)}</span>
            <span>${U.esc(status)}</span>
          </div>
          <div class="artifact-name">${U.esc(fileText)}</div>
          <p class="artifact-note">${U.esc(note)}</p>
        </div>
      </article>`;
    },

    /* Reachability line */
    reachLine(t){
      const r = CONFIG.reachability[t.reach];
      const icon = t.reach==='proven' ? 'check-circle-2' : t.reach==='watch' ? 'eye' : t.reach==='pending' || t.reach==='notstarted' ? 'clock' : 'help-circle';
      const color = t.reach==='proven' ? 'var(--ok)' : t.reach==='notstarted' ? 'var(--fg-faint)' : 'var(--warn)';
      return `<div class="flex items-center gap-1.5 text-[12.5px]" title="${r.plain}" style="color:${color}">
        <i data-lucide="${icon}" style="width:14px;height:14px"></i>
        ${U.term('reachability','Ideal answer reachable')}: <b>${r.label}</b>
      </div>`;
    },

    /* Run-detail grid + provenance block */
    runDetail(t){
      const spread = Array.isArray(t.spread) ? t.spread : [];
      const cells = spread.map((v,i)=>{
        const b = U.runBand(v);
        const color = b.id==='floor' ? 'var(--warn)' : b.id==='mid' ? 'var(--fg-soft)' : null;
        const cls = color ? '' : 'accent-text';
        return `<div class="surf-2 py-3 text-center" style="border-radius:14px" title="${b.label}: ${b.plain}">
          <div class="font-mono text-[10px]" style="color:var(--fg-faint)">R${i+1}</div>
          <div class="font-mono text-[15px] font-bold mt-0.5 ${cls}" ${color?`style="color:${color}"`:''}>${v}</div>
        </div>`;
      });
      for (let i = spread.length; i < t.runsTotal; i++){
        cells.push(`<div class="surf-2 py-3 text-center" style="border-radius:14px;opacity:.55" title="Not yet confirmed">
          <div class="font-mono text-[10px]" style="color:var(--fg-faint)">R${i+1}</div>
          <div class="font-mono text-[15px] font-bold mt-0.5" style="color:var(--fg-faint)">?</div>
        </div>`);
      }
      const prov = t.provNote ? `<p class="mt-4 text-[12.5px] leading-relaxed" style="color:var(--fg-soft)">${U.esc(t.provNote)}</p>` : '';
      return `<div class="grid grid-cols-5 sm:grid-cols-10 gap-2 pt-5">${cells.join('')}</div>
        ${prov}
        <p class="mt-3 font-mono text-[11px]" style="color:var(--fg-faint)">
          ${U.term('job','Evidence')}: ${t.quality === 'planned' ? 'Planned task slate' : 'Project Sanctum / Mercor review records'}. Data ${CONFIG.quality[t.quality].label.toLowerCase()}.
        </p>`;
    },

    /* Full task card */
    card(t){
      const band = U.meanBand(t.mean);
      const barColor = t.stage==='delivered' ? 'var(--accent-a)' : 'var(--accent-b)';
      const tagColor = band.id==='pending' ? 'var(--fg-faint)' : band.id==='soft' ? 'var(--accent-a)' : band.id==='mid' ? 'var(--accent-b)' : 'var(--warn)';
      const meanUnit = U.hasMean(t) ? '<span class="text-[15px]" style="color:var(--fg-faint)">%</span>' : '';
      const scoreLabel = U.hasMean(t) ? U.fmtMean(t) : 'TBD';
      const fam = CONFIG.failureFamilies[t.family] || { label:'Clinical signal' };
      return `
      <article class="card-inner card surf w-full px-4 sm:px-5 md:px-6 py-4 sm:py-5" style="border-radius:var(--r-card);--card-bar:${barColor}" tabindex="-1" data-open-task="${t.id}">
        <div class="flex flex-col sm:flex-row sm:items-center gap-4">
          <div class="flex items-start gap-4 min-w-0 flex-1">
            <div class="task-index">${String(t.position).padStart(2,'0')}</div>
            <div class="min-w-0">
              <div class="flex flex-wrap items-center gap-2">
                <span class="font-mono text-[12px] font-bold accent-text">${t.id}</span>
                <span class="surf-2 px-3 py-1.5 text-[10px] font-mono inline-flex items-center gap-1.5" style="border-radius:var(--r-pill);color:var(--fg-soft)"><span class="pill-dot ${t.stage}"></span>${CONFIG.cats[t.stage].pill}</span>
                <span class="micro-label">${U.esc(fam.label)}</span>
              </div>
              <h2 class="text-[19px] sm:text-[22px] font-semibold mt-2 leading-tight text-balance" style="max-width:min(34ch,100%)">${U.esc(t.name)}</h2>
              <div class="mt-3 flex flex-wrap gap-2" style="max-width:260px">${C.dots(t)}</div>
            </div>
          </div>
          <div class="flex items-center gap-3 sm:ml-auto">
            <div class="score-capsule">
              <div class="micro-label mb-1">${U.term('mean','Mean')}</div>
              <div class="font-mono font-bold text-[28px] leading-none" style="color:${tagColor}">${scoreLabel}${meanUnit}</div>
              <div class="font-mono text-[10px] mt-1" style="color:${tagColor}">${band.tag}</div>
            </div>
            <button class="openTaskBtn btn-icon surf-2 w-10 h-10 grid place-items-center open-task" style="border-radius:var(--r-pill)" aria-label="Open ${U.esc(t.id)} focus">
              <i data-lucide="arrow-up-right" style="width:17px;height:17px"></i>
            </button>
          </div>
        </div>
      </article>`;
    },
  };

  /* ════════════════════════════════════════════════════════════
     MODULE 7 · VIEWS
     Wires components into the DOM. Order: chrome to hero to
     glossary to cards to controls to summary to fab to keyboard.
     ════════════════════════════════════════════════════════════ */

  /* ---------- 7.1 Theme ---------- */
  const root = document.documentElement;
  const themeBtn = document.getElementById('themeToggle');
  const sysDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  function applyTheme(){
    const pref = KMState.get('theme');
    const dark = pref ? pref === 'dark' : sysDark;
    root.classList.toggle('dark', dark);
    themeBtn.setAttribute('aria-pressed', dark ? 'true' : 'false');
  }
  applyTheme();
  themeBtn.addEventListener('click', () => {
    KMState.set('theme', root.classList.contains('dark') ? 'light' : 'dark');
    applyTheme();
  });

  /* ---------- 7.2 Clock ---------- */
  const clock = document.getElementById('clock');
  function tick(){ clock.textContent = new Date().toLocaleTimeString([], {hour12:false}); }
  tick(); setInterval(tick, 1000);

  /* ---------- 7.3 Hero title type-in ---------- */
  (function(){
    const el = document.getElementById('heroTitle');
    if (reduceMotion) return;
    const text = el.textContent; el.textContent = '';
    [...text].forEach((ch, i) => {
      const s = document.createElement('span');
      s.className = 'type-char'; s.style.animationDelay = (i*30)+'ms';
      s.textContent = ch === ' ' ? ' ' : ch;
      el.appendChild(s);
    });
  })();

  /* ---------- 7.4 Glossary popover (event-delegated, single instance) ---------- */
  (function(){
    const pop = document.getElementById('glossPop');
    const titleEl = pop.querySelector('.g-title');
    const bodyEl = pop.querySelector('.g-body');
    let openFor = null;

    function place(btn){
      const r = btn.getBoundingClientRect();
      pop.style.left = '0px'; pop.style.top = '0px';     /* reset to measure */
      const pw = pop.offsetWidth, ph = pop.offsetHeight;
      let x = r.left + r.width/2 - pw/2;
      x = Math.max(10, Math.min(x, window.innerWidth - pw - 10));
      let y = r.top - ph - 10;
      if (y < 10) y = r.bottom + 10;
      pop.style.left = x+'px'; pop.style.top = y+'px';
    }
    function show(btn){
      const g = GLOSSARY[btn.dataset.g];
      if (!g) return;
      titleEl.textContent = g.title;
      bodyEl.textContent = g.body;
      pop.classList.add('show');
      place(btn);
      if (openFor) openFor.setAttribute('aria-expanded','false');
      openFor = btn;
      btn.setAttribute('aria-expanded','true');
    }
    function hide(){
      pop.classList.remove('show');
      if (openFor){ openFor.setAttribute('aria-expanded','false'); openFor = null; }
    }
    document.addEventListener('click', e=>{
      const btn = e.target.closest('.term');
      if (btn){ e.preventDefault(); (openFor === btn) ? hide() : show(btn); return; }
      if (!e.target.closest('#glossPop')) hide();
    });
    document.addEventListener('mouseover', e=>{
      const btn = e.target.closest('.term');
      if (btn && btn !== openFor) show(btn);
    });
    document.addEventListener('mouseout', e=>{
      const btn = e.target.closest('.term');
      if (btn && !e.relatedTarget?.closest('#glossPop')) hide();
    });
    document.addEventListener('keydown', e=>{ if (e.key === 'Escape') hide(); });
    window.addEventListener('scroll', ()=>{ if (openFor) hide(); }, {passive:true});
  })();

  /* ---------- 7.5 Radial chart (re-renderable) ---------- */
  const radialTip = document.getElementById('radialTip');
  function renderRadial(){
    const svg = document.getElementById('radial');
    svg.innerHTML = '';
    const NS = 'http://www.w3.org/2000/svg';
    const cx = 280, cy = 280, R = 190;
    const scored = tasks.filter(U.hasMean);
    const sorted = [...tasks].sort((a,b)=>{
      const av = U.scoreSortValue(a), bv = U.scoreSortValue(b);
      if (av === null && bv === null) return a.position - b.position;
      if (av === null) return 1;
      if (bv === null) return -1;
      return bv - av;
    });   /* strongest at 12 o'clock, sweep clockwise */
    const pts = sorted.map((t,i)=>{
      const ang = (-90 + i*(360/sorted.length)) * Math.PI/180;
      return { t, x: cx + R*Math.cos(ang), y: cy + R*Math.sin(ang) };
    });

    const defs = document.createElementNS(NS,'defs');
    defs.innerHTML = `<linearGradient id="arcGrad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="var(--accent-a)"/>
        <stop offset="100%" stop-color="var(--accent-b)"/>
      </linearGradient>`;
    svg.appendChild(defs);

    const d = pts.map((p,i)=> (i===0?'M':'L')+p.x.toFixed(1)+' '+p.y.toFixed(1)).join(' ') + ' Z';
    const arc = document.createElementNS(NS,'path');
    arc.setAttribute('d', d);
    arc.setAttribute('fill','none');
    arc.setAttribute('stroke','url(#arcGrad)');
    arc.setAttribute('stroke-width','1.5');
    arc.setAttribute('opacity','0.5');
    arc.setAttribute('stroke-linejoin','round');
    if(!reduceMotion) arc.classList.add('arc-anim');
    svg.appendChild(arc);

    /* center label: suite mean when scored, incoming marker when not */
    const anyApprox = tasks.some(t=>t.approx);
    const mom = scored.length ? scored.reduce((s,t)=>s+t.mean,0)/scored.length : null;
    const ctl = document.createElementNS(NS,'text');
    ctl.setAttribute('x',cx); ctl.setAttribute('y',cy-10);
    ctl.setAttribute('text-anchor','middle'); ctl.setAttribute('fill','var(--fg)');
    ctl.setAttribute('font-size','12'); ctl.setAttribute('font-family','var(--font-mono, monospace)');
    ctl.setAttribute('opacity','0.5'); ctl.setAttribute('letter-spacing','0');
    ctl.textContent = scored.length ? 'Suite mean' : 'Incoming';
    const ctl2 = document.createElementNS(NS,'text');
    ctl2.setAttribute('x',cx); ctl2.setAttribute('y',cy+20);
    ctl2.setAttribute('text-anchor','middle'); ctl2.setAttribute('fill','var(--fg)');
    ctl2.setAttribute('font-size','26'); ctl2.setAttribute('font-weight','700');
    ctl2.textContent = scored.length ? (anyApprox?'≈':'') + mom.toFixed(1).replace(/\.0$/,'') + '%' : `${tasks.length} tasks`;
    svg.appendChild(ctl); svg.appendChild(ctl2);

    pts.forEach((p,i)=>{
      const hasMean = U.hasMean(p.t);
      const failure = hasMean ? 100 - p.t.mean : 0;
      const r = hasMean ? 14 + failure*0.34 : 24;
      const intensity = hasMean ? 0.30 + (failure/100)*0.70 : 0.32;

      const g = document.createElementNS(NS,'g');
      g.setAttribute('class','node');
      g.style.cursor = 'pointer';
      g.setAttribute('tabindex','0');
      g.setAttribute('role','button');
      g.setAttribute('aria-label', hasMean
        ? `${p.t.id}, ${p.t.name}, mean ${U.fmtMean(p.t)} percent, ${CONFIG.cats[p.t.stage].label}`
        : `${p.t.id}, ${p.t.name}, planned placeholder, ${CONFIG.cats[p.t.stage].label}`);

      const halo = document.createElementNS(NS,'circle');
      halo.setAttribute('cx',p.x); halo.setAttribute('cy',p.y); halo.setAttribute('r',r+10);
      halo.setAttribute('fill','var(--accent-a)'); halo.setAttribute('opacity', (intensity*0.12).toFixed(3));

      const c = document.createElementNS(NS,'circle');
      c.setAttribute('cx',p.x); c.setAttribute('cy',p.y); c.setAttribute('r',r);
      c.setAttribute('fill', hasMean ? 'var(--accent-a)' : 'var(--fg-faint)');
      c.setAttribute('opacity', intensity.toFixed(3));
      if(!reduceMotion){ c.classList.add('node-anim'); halo.classList.add('node-anim');
        c.style.animationDelay = (i*100)+'ms'; halo.style.animationDelay = (i*100)+'ms'; }

      const lbl = document.createElementNS(NS,'text');
      lbl.setAttribute('x',p.x); lbl.setAttribute('y',p.y+4);
      lbl.setAttribute('text-anchor','middle'); lbl.setAttribute('fill','#fff');
      lbl.setAttribute('font-size','11'); lbl.setAttribute('font-weight','700');
      lbl.setAttribute('pointer-events','none');
      lbl.textContent = p.t.id.replace(/^[A-Z]+/,'');

      const tipLabel = hasMean
        ? `${p.t.id} · ${U.fmtMean(p.t)}% · ${CONFIG.cats[p.t.stage].pill}`
        : `${p.t.id} · Planned · ${CONFIG.cats[p.t.stage].pill}`;
      const showTip = (mx, my)=>{
        radialTip.textContent = tipLabel;
        radialTip.classList.add('show');
        const tw = radialTip.offsetWidth, th = radialTip.offsetHeight;
        let tx = mx + 12, ty = my - th - 8;
        if (tx + tw > window.innerWidth - 8) tx = mx - tw - 12;
        if (ty < 8) ty = my + 16;
        radialTip.style.left = tx+'px'; radialTip.style.top = ty+'px';
      };
      const hideTip = ()=> radialTip.classList.remove('show');
      const expand = ()=>{ c.setAttribute('r', r+5); };
      const reset  = ()=>{ c.setAttribute('r', r); hideTip(); };
      g.addEventListener('mouseenter', e=>{ expand(); showTip(e.clientX, e.clientY); });
      g.addEventListener('mousemove',  e=>{ showTip(e.clientX, e.clientY); });
      g.addEventListener('mouseleave', reset);
      g.addEventListener('focus', ()=>{
        expand();
        const rect = g.getBoundingClientRect();
        showTip(rect.left + rect.width/2, rect.top);
      });
      g.addEventListener('blur', reset);
      g.addEventListener('touchstart', e=>{
        e.preventDefault();
        expand();
        const t0 = e.touches[0];
        showTip(t0.clientX, t0.clientY);
        setTimeout(()=>{ reset(); }, 2000);
      }, {passive:false});
      const go = ()=>{
        document.getElementById('card-'+p.t.id)?.scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'center'});
        history.replaceState(null,'','#'+p.t.id);
      };
      g.addEventListener('click', go);
      g.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); go(); }});

      g.appendChild(halo); g.appendChild(c); g.appendChild(lbl);
      svg.appendChild(g);
    });
  }

  /* ---------- 7.5.5 Focus sheet ---------- */
  const Focus = (function(){
    const overlay = document.getElementById('focusOverlay');
    const sheet = document.getElementById('focusSheet');
    const closeBtn = document.getElementById('focusClose');
    const eyebrow = document.getElementById('focusEyebrow');
    const title = document.getElementById('focusTitle');
    const body = document.getElementById('focusBody');
    let activeId = null;
    let activeTab = 'overview';

    function taskById(id){ return tasks.find(t=>t.id === id); }
    function metric(label, value, hint=''){
      return `<div class="focus-metric">
        <div class="micro-label">${label}</div>
        <div class="mt-2 text-[22px] font-bold leading-none">${value}</div>
        ${hint ? `<div class="mt-2 text-[12px] leading-snug" style="color:var(--fg-soft)">${hint}</div>` : ''}
      </div>`;
    }
    function sectionTitle(text){
      return `<div class="micro-label mb-2">${text}</div>`;
    }
    function tabs(){
      const items = [
        ['overview', 'Overview'],
        ['packet', 'Packet'],
        ['runs', 'Runs'],
        ['review', 'Review'],
      ];
      return `<div class="focus-tabs" role="tablist" aria-label="Task focus sections">
        ${items.map(([id,label])=>`<button class="focus-tab" role="tab" data-focus-tab="${id}" aria-selected="${activeTab === id ? 'true' : 'false'}">${label}</button>`).join('')}
      </div>`;
    }
    function overview(t){
      const k = U.counts(t);
      const band = U.meanBand(t.mean);
      const fam = CONFIG.failureFamilies[t.family] || { label:'Clinical signal', plain:'' };
      const score = U.hasMean(t) ? U.fmtMean(t) + '%' : 'TBD';
      const floorLine = k.confirmed ? `${k.floors} floor${k.floors === 1 ? '' : 's'}` : 'Not piloted';
      return `
        <div class="focus-metric-grid">
          ${metric('Mean', score, band.tag)}
          ${metric('Status', CONFIG.cats[t.stage].label, CONFIG.quality[t.quality].label)}
          ${metric('Signal', floorLine, `${k.sub70} sub-70`)}
        </div>

        <div class="focus-section">
          ${sectionTitle('What this tests')}
          <p class="text-[15px] leading-relaxed font-medium">${U.esc(t.plain)}</p>
        </div>

        <div class="focus-section">
          ${sectionTitle('Failure family')}
          <p class="text-[14px] leading-relaxed"><b>${U.esc(fam.label)}.</b> <span style="color:var(--fg-soft)">${U.esc(fam.plain || '')}</span></p>
        </div>

        <div class="focus-section">
          ${sectionTitle('Verdict')}
          <p class="text-[14px] leading-relaxed">${U.esc(t.verdict)}</p>
        </div>

        <div class="focus-section">
          ${sectionTitle('Mechanism')}
          <p class="text-[13.5px] leading-relaxed" style="color:var(--fg-soft)">${U.esc(t.mechanism)}</p>
        </div>
      `;
    }
    function packet(t){
      const p = t.packet || {};
      const status = p.planned ? 'Planned' : 'Current';
      const fileList = Array.isArray(p.files) ? p.files : [];
      return `<div class="packet-intro">
          <h3>Task packet</h3>
          <p>Four artifacts define the task. The dashboard shows roles and sanitized filenames only, so the teaching layer explains the build without exposing local file paths.</p>
        </div>
        <div class="artifact-grid">
          ${C.artifactTile('Prompt', p.prompt || 'Planned prompt', 'The in-role request that sets the workflow and output boundary.', 'message-square-text', status)}
          ${C.artifactTile('Task files', fileList.join(' + ') || 'No task file mounted', 'The mounted material the model must use or rebut. This is where format, noise, and fair traps live.', 'folder-open', status)}
          ${C.artifactTile('Golden', p.golden || 'Planned golden reference', 'The physician reference answer. It defines the clinical target, not a script to copy.', 'badge-check', status)}
          ${C.artifactTile('Grader', p.grader || 'Planned grader guidelines', 'The scoring rules. A good grader credits safe restraint and penalizes the central failure.', 'list-checks', status)}
        </div>`;
    }
    function runs(t){
      const k = U.counts(t);
      const band = U.meanBand(t.mean);
      const score = U.hasMean(t) ? U.fmtMean(t) + '%' : 'TBD';
      return `<div class="focus-metric-grid">
          ${metric('Mean', score, band.tag)}
          ${metric('Catchers', String(k.catchers), '85 or higher')}
          ${metric('Floors', String(k.floors), '40 or lower')}
        </div>
        <div class="focus-section">
          ${sectionTitle('Pilot runs')}
          ${C.runDetail(t)}
        </div>`;
    }
    function review(t){
      return `<div class="focus-section">
          ${sectionTitle('Lifecycle')}
          ${C.stepper(t)}
          <div class="mt-5 grid sm:grid-cols-2 gap-4">
            <div>
              ${sectionTitle('Workflow')}
              <div class="text-[14px] font-medium leading-snug">${U.esc(t.workflow)}</div>
            </div>
            <div>
              ${sectionTitle('Reviewer')}
              <div class="text-[14px] font-medium">${U.esc(t.reviewer)}</div>
            </div>
          </div>
          <div class="mt-5">${C.reachLine(t)}</div>
        </div>
        <div class="focus-section">
          ${sectionTitle('Current judgment')}
          <p class="text-[14px] leading-relaxed">${U.esc(t.verdict)}</p>
        </div>`;
    }
    function content(t){
      const views = { overview, packet, runs, review };
      return `${tabs()}<div class="focus-panel">${(views[activeTab] || overview)(t)}</div>`;
    }
    function renderActive(){
      const t = taskById(activeId);
      if (!t) return;
      body.innerHTML = content(t);
      lucide.createIcons();
    }
    body.addEventListener('click', e=>{
      const btn = e.target.closest('[data-focus-tab]');
      if (!btn) return;
      activeTab = btn.dataset.focusTab;
      renderActive();
    });
    function open(id){
      const t = taskById(id);
      if (!t) return;
      activeId = id;
      activeTab = 'overview';
      const fam = CONFIG.failureFamilies[t.family] || { label:'Clinical signal' };
      eyebrow.textContent = `${t.id} · ${fam.label}`;
      title.textContent = t.name;
      renderActive();
      overlay.hidden = false;
      sheet.hidden = false;
      document.body.style.overflow = 'hidden';
      requestAnimationFrame(()=>{
        overlay.classList.add('open');
        sheet.classList.add('open');
        lucide.createIcons();
        closeBtn.focus({ preventScroll:true });
      });
    }
    function close(){
      overlay.classList.remove('open');
      sheet.classList.remove('open');
      document.body.style.overflow = '';
      setTimeout(()=>{
        overlay.hidden = true;
        sheet.hidden = true;
        activeId = null;
      }, reduceMotion ? 0 : 320);
    }
    overlay.addEventListener('click', close);
    closeBtn.addEventListener('click', close);
    document.addEventListener('keydown', e=>{
      if (e.key === 'Escape' && activeId) close();
    });
    return { open, close };
  })();

  /* ---------- 7.5.6 Failure-family signal strip ---------- */
  function renderSignalStrip(){
    const strip = document.getElementById('signalStrip');
    const headline = document.getElementById('signalHeadline');
    const first = document.getElementById('openFirstSignal');
    const groups = tasks.reduce((acc,t)=>{
      const key = t.family || 'closure';
      (acc[key] ||= []).push(t);
      return acc;
    }, {});
    const entries = Object.entries(groups).sort((a,b)=> b[1].length - a[1].length || a[1][0].position - b[1][0].position);
    headline.textContent = tasks.every(t=>t.stage === 'planned') ? 'What this world is built to test' : 'Where the model breaks';
    strip.innerHTML = entries.map(([key,items], idx)=>{
      const fam = CONFIG.failureFamilies[key] || { label:'Clinical signal', plain:'' };
      const ids = items.map(t=>t.id).join(', ');
      return `<button class="signal-chip" data-focus="${items[0].id}" style="transition-delay:${idx*45}ms" title="${U.esc(fam.plain || '')}">
        <span class="count">${items.length}</span>
        <span class="label">${U.esc(fam.label)}</span>
        <span class="ids">${U.esc(ids)}</span>
      </button>`;
    }).join('');
    strip.querySelectorAll('[data-focus]').forEach(btn=>{
      btn.addEventListener('click', ()=> Focus.open(btn.dataset.focus));
    });
    first.onclick = ()=> {
      const id = entries[0]?.[1]?.[0]?.id;
      if (id) Focus.open(id);
    };
  }

  /* ---------- 7.6 Cards (re-renderable) ---------- */
  function renderCards(){
    const wrap = document.getElementById('cards');
    wrap.innerHTML = '';
    document.getElementById('srTable').innerHTML = '';
    tasks.forEach(t=>{
      const sec = document.createElement('section');
      sec.id = 'card-'+t.id;
      sec.dataset.id = t.id;
      sec.dataset.status = t.stage;
      sec.dataset.mean = t.mean;
      sec.dataset.pos = t.position;
      sec.className = 'km-card flex items-center py-3 sm:py-4';
      sec.innerHTML = C.card(t);
      sec.querySelector('article').style.transitionDelay = (t.position * 55) + 'ms';
      wrap.appendChild(sec);

      /* screen-reader table row */
      const k = U.counts(t);
      const scoreText = U.hasMean(t) ? `${U.fmtMean(t)}%` : 'TBD';
      const runText = k.confirmed
        ? `${t.spread.join(', ')}${k.confirmed < t.runsTotal ? ` (${k.confirmed} of ${t.runsTotal} confirmed)` : ''}`
        : 'No pilot scores yet';
      document.getElementById('srTable').insertAdjacentHTML('beforeend',
        `<tr><td>${t.id}</td><td>${U.esc(t.name)}</td><td>${scoreText}</td>
         <td>${runText}</td>
         <td>${CONFIG.cats[t.stage].label}</td><td>${CONFIG.quality[t.quality].label}</td></tr>`);
    });
    wrap.querySelectorAll('[data-open-task]').forEach(card=>{
      card.addEventListener('click', e=>{
        if (e.target.closest('.term')) return;
        Focus.open(card.dataset.openTask);
      });
      card.addEventListener('keydown', e=>{
        if (e.key === 'Enter' || e.key === ' '){
          e.preventDefault();
          Focus.open(card.dataset.openTask);
        }
      });
    });
  }

  /* ════════════════════════════════════════════════════════════
     MODULE 8 · CONTROLLER (re-renderable)
     Filter / sort / deep links. Hash state: #KM07 (any task id),
     #filter=delivered|review, #sort=position|high|low,
     #world=<registry id>.
     ════════════════════════════════════════════════════════════ */
  function renderControls(){
    const cardsWrap = document.getElementById('cards');
    const empty = document.getElementById('emptyState');
    const filterWrap = document.getElementById('filterChips');
    const sortWrap = document.getElementById('sortChips');
    filterWrap.innerHTML = ''; sortWrap.innerHTML = '';
    const SORTS = {
      position: { label:'Order',   fn:(a,b)=> a.position-b.position },
      high:     { label:'Highest', fn:(a,b)=> {
        const av = U.scoreSortValue(a), bv = U.scoreSortValue(b);
        if (av === null && bv === null) return a.position-b.position;
        if (av === null) return 1;
        if (bv === null) return -1;
        return bv-av;
      } },
      low:      { label:'Lowest',  fn:(a,b)=> {
        const av = U.scoreSortValue(a), bv = U.scoreSortValue(b);
        if (av === null && bv === null) return a.position-b.position;
        if (av === null) return 1;
        if (bv === null) return -1;
        return av-bv;
      } },
    };
    const state = {
      filter: KMState.get('filter') || 'all',
      sort:   KMState.get('sort')   || 'position',
    };
    if (state.filter !== 'all' && !CONFIG.cats[state.filter]) state.filter = 'all';
    if (!SORTS[state.sort]) state.sort = 'position';

    function makeChip(label){
      const b = document.createElement('button');
      b.className = 'chip surf-2';
      b.style.cssText = 'border-radius:var(--r-pill);padding:5px 14px;font-size:12px;font-family:ui-monospace,monospace;font-weight:600;color:var(--fg-soft)';
      b.textContent = label;
      return b;
    }
    function paintChips(wrap, current){
      [...wrap.children].forEach(c=>
        c.setAttribute('aria-pressed', c.dataset.val === current ? 'true' : 'false'));
    }

    const presentCats = [...new Set(tasks.map(t=>t.stage))];
    [['all','All'], ...presentCats.map(c=>[c, CONFIG.cats[c].label])].forEach(([val,label])=>{
      const chip = makeChip(label);
      chip.dataset.val = val;
      chip.addEventListener('click', ()=> setState({filter:val}));
      filterWrap.appendChild(chip);
    });
    Object.entries(SORTS).forEach(([val,{label}])=>{
      const chip = makeChip(label);
      chip.dataset.val = val;
      chip.addEventListener('click', ()=> setState({sort:val}));
      sortWrap.appendChild(chip);
    });

    function apply(){
      const ordered = [...tasks].sort(SORTS[state.sort].fn);
      ordered.forEach(t=>{
        const el = document.getElementById('card-'+t.id);
        if (el) cardsWrap.appendChild(el);
      });
      let visible = 0;
      document.querySelectorAll('.km-card').forEach(el=>{
        const show = state.filter==='all' || el.dataset.status===state.filter;
        el.style.display = show ? '' : 'none';
        if (show) visible++;
      });
      empty.classList.toggle('hidden', visible>0);
      paintChips(filterWrap, state.filter);
      paintChips(sortWrap, state.sort);
    }

    function syncHash(){
      const parts = [];
      if (state.filter!=='all') parts.push('filter='+state.filter);
      if (state.sort!=='position') parts.push('sort='+state.sort);
      const hash = parts.join('&');
      history.replaceState(null,'', hash ? '#'+hash : location.pathname+location.search);
    }
    function setState(patch, opts={}){
      Object.assign(state, patch);
      if ('filter' in patch) KMState.set('filter', state.filter);
      if ('sort'   in patch) KMState.set('sort',   state.sort);
      apply();
      if (!opts.silent) syncHash();
    }
    function readHash(){
      const h = location.hash.replace(/^#/,'');
      if (!h) return;
      /* deep link to one card: works for any world's task ids */
      if (/^[A-Z0-9-]+$/i.test(h)){
        const el = document.getElementById('card-'+h.toUpperCase());
        if (el){
          el.scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'center'});
          return;
        }
      }
      const params = new URLSearchParams(h);
      /* world switch via hash, e.g. #world=korvin-merrow */
      const w = params.get('world');
      if (w && WORLDS[w] && w !== WorldCtl.id){ WorldCtl.set(w); return; }
      const f = params.get('filter'), s = params.get('sort');
      const patch = {};
      /* accept legacy hashes from shared links */
      const legacyF = { complete:'delivered', pending:'review' };
      const ff = legacyF[f] || f;
      if (ff && (ff==='all' || CONFIG.cats[ff])) patch.filter = ff;
      if (s && SORTS[s]) patch.sort = s;
      if (Object.keys(patch).length) setState(patch, {silent:true});
    }

    apply();
    readHash();
    renderControls._readHash = readHash;
    if (!renderControls._wired){
      window.addEventListener('hashchange', ()=> renderControls._readHash?.());
      renderControls._wired = true;
    }
  }

  /* ---------- 8.2 Summary (re-renderable) ---------- */
  function renderSummary(){
    const M = WorldCtl.world.meta;
    const delivered = tasks.filter(t=>t.stage==='delivered');
    const ready = tasks.filter(t=>t.stage==='ready');
    const review = tasks.filter(t=>t.stage==='review');
    const planned = tasks.filter(t=>t.stage==='planned');
    const scored = tasks.filter(U.hasMean);
    const anyApprox = tasks.some(t=>t.approx);
    const mom = scored.length ? scored.reduce((s,t)=>s+t.mean,0)/scored.length : null;
    const means = scored.map(t=>t.mean);
    const allScores = tasks.flatMap(t=>t.spread);
    const sub70 = allScores.filter(v=>v < 70).length;
    const totalRuns = allScores.length;
    const lo = scored.length ? scored.reduce((a,b)=> a.mean<b.mean?a:b) : null;
    const hi = scored.length ? scored.reduce((a,b)=> a.mean>b.mean?a:b) : null;

    let primary;
    if (planned.length === tasks.length) {
      primary = {
        label: 'Planned tasks',
        metric: String(tasks.length),
        caption: 'Incoming task slate. No pilot data is shown until real runs exist.',
        insight: `${tasks.length} task placeholders are staged. Next move: build the first task from the approved world plan.`,
        pill: 'Incoming',
        pillClass: 'planned',
        action: 'View task slate',
        filter: 'planned',
      };
    } else if (ready.length) {
      primary = {
        label: 'Ready tasks',
        metric: String(ready.length),
        caption: `${ready.map(t=>t.id).join(', ')} are queued for delivery or final action.`,
        insight: `${delivered.length} of ${tasks.length} tasks are delivered. The active closure work is the ready queue.`,
        pill: 'Ready queue',
        pillClass: 'ready',
        action: 'Show ready tasks',
        filter: 'ready',
      };
    } else if (review.length) {
      primary = {
        label: 'In review',
        metric: String(review.length),
        caption: 'Human review is the active gate.',
        insight: `${review.length} task${review.length === 1 ? '' : 's'} need expert review before delivery.`,
        pill: 'Review',
        pillClass: 'review',
        action: 'Show review tasks',
        filter: 'review',
      };
    } else {
      primary = {
        label: 'Delivered',
        metric: `${delivered.length}/${tasks.length}`,
        caption: totalRuns ? `${sub70} of ${totalRuns} scored runs are sub-70 training signal.` : 'World closed.',
        insight: `${delivered.length} of ${tasks.length} tasks are delivered. This world is closed unless a reviewer reopens a task.`,
        pill: 'Closed',
        pillClass: 'delivered',
        action: 'Review task list',
        filter: 'all',
      };
    }

    document.getElementById('deliveredCount').innerHTML = delivered.length+'<span class="unit">/ '+tasks.length+'</span>';
    document.getElementById('reviewCount').textContent = review.length;
    document.getElementById('readyCount').textContent = ready.length || planned.length;
    document.getElementById('meanOfMeans').innerHTML = scored.length
      ? (anyApprox?'≈':'')+mom.toFixed(1).replace(/\.0$/,'')+'<span class="unit">%</span>'
      : 'TBD';
    document.getElementById('spreadRange').textContent = scored.length ? Math.min(...means)+' to '+Math.max(...means) : 'pending';

    const statePill = document.getElementById('heroStatePill');
    statePill.textContent = primary.pill;
    statePill.className = 'status-pill ' + primary.pillClass;
    document.getElementById('heroInsight').textContent = primary.insight;
    document.getElementById('primaryActionText').textContent = primary.action;
    document.getElementById('scrollHint').dataset.filter = primary.filter;
    document.getElementById('heroPrimaryMetric').textContent = primary.metric;
    document.getElementById('heroPrimaryLabel').textContent = primary.label;
    document.getElementById('heroPrimaryCaption').textContent = primary.caption;
    document.getElementById('heroDelivered').textContent = delivered.length+'/'+tasks.length;
    document.getElementById('heroReview').textContent = review.length;
    document.getElementById('heroReady').textContent = ready.length || planned.length;
    document.getElementById('heroHardest').textContent = lo ? lo.id : 'TBD';
    const track = document.getElementById('worldTrack');
    track.style.setProperty('--task-count', tasks.length);
    track.innerHTML = tasks.map(t=>
      `<button class="track-step ${t.stage}" title="${t.id}: ${CONFIG.cats[t.stage].label}" aria-label="${t.id}, ${CONFIG.cats[t.stage].label}" data-jump="${t.id}"></button>`
    ).join('');
    track.querySelectorAll('[data-jump]').forEach(btn=>{
      btn.addEventListener('click', ()=>{
        document.getElementById('card-'+btn.dataset.jump)?.scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'center'});
      });
    });

    document.getElementById('summarySentence').innerHTML = scored.length
      ? `${delivered.length} of ${tasks.length} tasks are delivered. ` +
        `${lo.id} is currently the hardest at ${U.fmtMean(lo)}%; ${hi.id} is the gentlest at ${U.fmtMean(hi)}%. ` +
        `Low scores matter only when the failure is fair and reachable.`
      : `${planned.length} planned tasks are staged for this incoming world. No pilot scores, FA/GA, preference labels, or delivery states are displayed yet.`;

    document.getElementById('provenance').textContent =
      `${tasks[0].id} to ${tasks[tasks.length-1].id}. Data synced ${M.dataSyncedOn}. ${M.world}. ${M.patient}. ` +
      `${M.provenance} Evidence: ${M.evidence}.`;
  }

  /* ---------- 8.3 Scroll progress ---------- */
  (function(){
    const bar = document.getElementById('progress');
    const onScroll = ()=>{
      const h = document.documentElement;
      const p = h.scrollTop / (h.scrollHeight - h.clientHeight);
      bar.style.transform = `scaleX(${Math.min(1,Math.max(0,p))})`;
      bar.style.width = '100%';
    };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  })();

  document.getElementById('scrollHint').addEventListener('click', ()=>{
    const preferred = document.getElementById('scrollHint').dataset.filter;
    if (preferred) {
      KMState.set('filter', preferred);
      renderControls();
    }
    document.getElementById('cards').scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'start'});
  });

  /* ---------- 8.4 Intersection reveal + dim + ring animation (rebindable) ---------- */
  function bindObservers(){
    bindObservers._io?.disconnect();
    const io = new IntersectionObserver((entries)=>{
      entries.forEach(e=>{
        if (e.isIntersecting){
          e.target.classList.add('in'); e.target.classList.remove('dim');
          if (!e.target.dataset.ringFired){
            e.target.dataset.ringFired = '1';
            e.target.querySelectorAll('.ring-fill[data-target]').forEach(arc=>{
              requestAnimationFrame(()=> arc.style.strokeDashoffset = arc.dataset.target);
            });
          }
        } else if (e.target.classList.contains('in')){ e.target.classList.add('dim'); }
      });
    }, { threshold: 0.35 });
    document.querySelectorAll('.card').forEach(c=> io.observe(c));
    bindObservers._io = io;
  }

  /* ---------- 8.5 Quick-jump FAB (menu re-renderable, wiring once) ---------- */
  const Fab = (function(){
    const fab = document.getElementById('fab');
    const menu = document.getElementById('fabMenu');
    const icon = document.getElementById('fabIcon');
    let open = false;
    function setOpen(v){
      open = v; fab.setAttribute('aria-expanded', v);
      menu.style.opacity = v?'1':'0';
      menu.style.transform = v?'scale(1)':'scale(0.9)';
      menu.style.pointerEvents = v?'auto':'none';
      icon.setAttribute('data-lucide', v?'x':'navigation');
      lucide.createIcons();
    }
    fab.addEventListener('click', ()=> setOpen(!open));
    function render(){
      menu.innerHTML = '';
      tasks.forEach(t=>{
        const b = document.createElement('button');
        b.className = 'btn-pill surf-2';
        b.style.cssText = 'border-radius:var(--r-pill);padding:6px 16px;font-size:13px;font-family:ui-monospace,monospace;font-weight:600;color:var(--fg)';
        b.textContent = t.id;
        b.addEventListener('click', ()=>{
          document.getElementById('card-'+t.id).scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'center'});
          history.replaceState(null,'','#'+t.id);
          setOpen(false);
        });
        menu.appendChild(b);
      });
    }
    return { render };
  })();

  /* ---------- 8.6 Keyboard nav between cards ---------- */
  (function(){
    document.addEventListener('keydown', e=>{
      if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
      if (['INPUT','TEXTAREA'].includes(document.activeElement.tagName)) return;
      e.preventDefault();
      const cards = [...document.querySelectorAll('.km-card')].filter(c=> c.style.display !== 'none');
      if (!cards.length) return;
      const mid = window.innerHeight/2;
      let cur = 0, best = Infinity;
      cards.forEach((c,i)=>{
        const r = c.getBoundingClientRect();
        const d = Math.abs((r.top + r.height/2) - mid);
        if (d < best){ best = d; cur = i; }
      });
      const next = Math.min(cards.length-1, Math.max(0, cur + (e.key==='ArrowDown'?1:-1)));
      const el = cards[next];
      el.scrollIntoView({behavior: reduceMotion?'auto':'smooth', block:'center'});
      history.replaceState(null,'','#'+el.dataset.id);
    });
  })();

  /* ════════════════════════════════════════════════════════════
     MODULE 9 · SOUND (Web Audio, pure synthesis, OPT-IN)
     Muted by default: this dashboard is shown to reviewers.
     Unmute persists via KMState. Reduced-motion stays silent.
     ════════════════════════════════════════════════════════════ */
  const SFX = (function(){
    let ctx = null;
    let muted = KMState.get('muted') !== null ? KMState.get('muted') : true;  /* opt-in */
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches && KMState.get('muted') === null) muted = true;

    function getCtx(){
      if (!ctx) ctx = new (window.AudioContext || window.webkitAudioContext)();
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    }
    function env(gainNode, at, peak, holdEnd, rel, end){
      const t = getCtx().currentTime;
      gainNode.gain.cancelScheduledValues(t);
      gainNode.gain.setValueAtTime(0, t);
      gainNode.gain.linearRampToValueAtTime(peak, t + at);
      gainNode.gain.setValueAtTime(peak, t + holdEnd);
      gainNode.gain.exponentialRampToValueAtTime(0.0001, t + end);
      gainNode.gain.setValueAtTime(0, t + end);
    }

    const sfx = {
      load(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const buf = c.createBuffer(1, c.sampleRate * 1.2, c.sampleRate);
        const d = buf.getChannelData(0);
        for (let i = 0; i < d.length; i++) d[i] = (Math.random()*2-1);
        const src = c.createBufferSource(); src.buffer = buf;
        const bpf = c.createBiquadFilter(); bpf.type = 'bandpass';
        bpf.frequency.setValueAtTime(400, t);
        bpf.frequency.exponentialRampToValueAtTime(3200, t + 1.0);
        bpf.Q.value = 3.5;
        const g = c.createGain();
        g.gain.setValueAtTime(0, t);
        g.gain.linearRampToValueAtTime(0.09, t + 0.08);
        g.gain.exponentialRampToValueAtTime(0.0001, t + 1.1);
        src.connect(bpf); bpf.connect(g); g.connect(c.destination);
        src.start(t); src.stop(t + 1.2);
      },
      cardReveal(mean){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const pct = Math.max(0, Math.min(1, ((mean ?? 55) - 25) / 70));
        const freq = 320 + pct * 780;
        const osc = c.createOscillator(); osc.type = 'sine'; osc.frequency.value = freq;
        const g = c.createGain();
        env(g, 0.004, 0.10, 0.004, 0.28, 0.32);
        const osc2 = c.createOscillator(); osc2.type = 'sine'; osc2.frequency.value = freq * 2.01;
        const g2 = c.createGain();
        env(g2, 0.004, 0.028, 0.004, 0.18, 0.22);
        osc.connect(g); g.connect(c.destination);
        osc2.connect(g2); g2.connect(c.destination);
        osc.start(t); osc.stop(t + 0.35);
        osc2.start(t); osc2.stop(t + 0.25);
      },
      chip(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'square'; osc.frequency.value = 1050;
        osc.frequency.exponentialRampToValueAtTime(420, t + 0.025);
        const g = c.createGain();
        env(g, 0.001, 0.07, 0.001, 0.04, 0.06);
        const lpf = c.createBiquadFilter(); lpf.type = 'lowpass'; lpf.frequency.value = 3000;
        osc.connect(lpf); lpf.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.07);
      },
      expand(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'sine';
        osc.frequency.setValueAtTime(180, t);
        osc.frequency.exponentialRampToValueAtTime(900, t + 0.38);
        const g = c.createGain();
        env(g, 0.01, 0.09, 0.01, 0.30, 0.42);
        osc.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.44);
      },
      collapse(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'sine';
        osc.frequency.setValueAtTime(820, t);
        osc.frequency.exponentialRampToValueAtTime(160, t + 0.32);
        const g = c.createGain();
        env(g, 0.01, 0.07, 0.01, 0.24, 0.36);
        osc.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.38);
      },
      fabOpen(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        [0, 0.07].forEach((delay, i) => {
          const osc = c.createOscillator(); osc.type = 'sine';
          osc.frequency.value = i === 0 ? 520 : 780;
          const g = c.createGain();
          env(g, 0.003, 0.08, 0.003, 0.08, 0.14);
          osc.connect(g); g.connect(c.destination);
          osc.start(t + delay); osc.stop(t + delay + 0.16);
        });
      },
      fabClose(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        [0, 0.07].forEach((delay, i) => {
          const osc = c.createOscillator(); osc.type = 'sine';
          osc.frequency.value = i === 0 ? 780 : 520;
          const g = c.createGain();
          env(g, 0.003, 0.06, 0.003, 0.07, 0.13);
          osc.connect(g); g.connect(c.destination);
          osc.start(t + delay); osc.stop(t + delay + 0.14);
        });
      },
      theme(){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        [880, 1108, 1320, 1760].forEach((f, i) => {
          const osc = c.createOscillator(); osc.type = 'sine'; osc.frequency.value = f;
          const g = c.createGain();
          const delay = i * 0.045;
          g.gain.setValueAtTime(0, t + delay);
          g.gain.linearRampToValueAtTime(0.055, t + delay + 0.015);
          g.gain.exponentialRampToValueAtTime(0.0001, t + delay + 0.18);
          osc.connect(g); g.connect(c.destination);
          osc.start(t + delay); osc.stop(t + delay + 0.20);
        });
      },
      navTick(dir){
        if (muted) return;
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'triangle';
        osc.frequency.value = dir === 'down' ? 420 : 560;
        const g = c.createGain();
        env(g, 0.003, 0.055, 0.003, 0.05, 0.09);
        osc.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.10);
      },
      muteOn(){
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'sine'; osc.frequency.value = 660;
        osc.frequency.exponentialRampToValueAtTime(330, t + 0.14);
        const g = c.createGain();
        env(g, 0.004, 0.07, 0.004, 0.10, 0.18);
        osc.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.20);
      },
      muteOff(){
        const c = getCtx(), t = c.currentTime;
        const osc = c.createOscillator(); osc.type = 'sine'; osc.frequency.value = 330;
        osc.frequency.exponentialRampToValueAtTime(660, t + 0.14);
        const g = c.createGain();
        env(g, 0.004, 0.07, 0.004, 0.10, 0.18);
        osc.connect(g); g.connect(c.destination);
        osc.start(t); osc.stop(t + 0.20);
      },
    };

    const muteBtn = document.getElementById('muteToggle');
    const muteIcon = document.getElementById('muteIcon');
    function applyMuteVisual(){
      muteIcon.setAttribute('data-lucide', muted ? 'volume-x' : 'volume-2');
      muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
      lucide.createIcons();
    }
    applyMuteVisual();
    muteBtn.addEventListener('click', ()=>{
      muted = !muted;
      KMState.set('muted', muted);
      applyMuteVisual();
      if (muted) sfx.muteOn(); else sfx.muteOff();
    });

    return { ...sfx, isMuted: () => muted };
  })();

  /* ---------- 9.2 Wire sounds into interactions ---------- */
  (function(){
    let fired = false;
    function onGesture(){
      if (fired) return; fired = true;
      SFX.load();
      window.removeEventListener('pointerdown', onGesture);
      window.removeEventListener('keydown', onGesture);
    }
    window.addEventListener('pointerdown', onGesture);
    window.addEventListener('keydown', onGesture);
  })();
  document.getElementById('themeToggle').addEventListener('click', ()=> SFX.theme());
  document.getElementById('scrollHint').addEventListener('click', ()=> SFX.scrollHint?.());
  document.getElementById('filterChips').addEventListener('click', ()=> SFX.chip());
  document.getElementById('sortChips').addEventListener('click', ()=> SFX.chip());
  function bindCardSounds(){
    bindCardSounds._io?.disconnect();
    const io2 = new IntersectionObserver((entries)=>{
      entries.forEach(e=>{
        if (e.isIntersecting && !e.target.dataset.sfxFired){
          e.target.dataset.sfxFired = '1';
          const task = tasks.find(t=> t.id === e.target.dataset.id);
          SFX.cardReveal(task?.mean);
        }
      });
    }, { threshold: 0.5 });
    document.querySelectorAll('.km-card').forEach(c=> io2.observe(c));
    bindCardSounds._io = io2;
  }
  document.getElementById('cards').addEventListener('click', e=>{
    const btn = e.target.closest('.expandBtn');
    if (!btn) return;
    const isOpen = btn.getAttribute('aria-expanded') === 'true';
    setTimeout(()=> isOpen ? SFX.collapse() : SFX.expand(), 0);
  });
  (function(){
    const fab = document.getElementById('fab');
    let prevOpen = false;
    const obs = new MutationObserver(()=>{
      const nowOpen = fab.getAttribute('aria-expanded') === 'true';
      if (nowOpen !== prevOpen){
        prevOpen = nowOpen;
        if (nowOpen) SFX.fabOpen(); else SFX.fabClose();
      }
    });
    obs.observe(fab, { attributes: true, attributeFilter: ['aria-expanded'] });
  })();
  document.addEventListener('keydown', e=>{
    if (e.key === 'ArrowDown') SFX.navTick('down');
    else if (e.key === 'ArrowUp') SFX.navTick('up');
  }, { capture: true });

  /* ════════════════════════════════════════════════════════════
     MODULE 10 · WORLD SWITCHER + BOOT
     Header dropdown lists every world in the WORLDS registry.
     renderWorld() repaints all data-driven views in one pass.
     ════════════════════════════════════════════════════════════ */
  function renderWorld(){
    const w = WorldCtl.world;
    document.getElementById('worldTitle').textContent = w.title;
    document.getElementById('heroTitle').textContent = w.title;
    document.getElementById('heroKicker').textContent = w.kicker;
    document.getElementById('heroSub').textContent = w.blurb;
    const dl = document.getElementById('driveLink');
    if (w.driveUrl){ dl.style.display = ''; dl.href = w.driveUrl; }
    else dl.style.display = 'none';
    document.title = w.title + ' · Sanctum';

    renderRadial();
    renderCards();
    renderControls();
    renderSignalStrip();
    renderSummary();
    Fab.render();
    bindObservers();
    bindCardSounds();
    lucide.createIcons();
  }

  /* World dropdown */
  (function(){
    const btn = document.getElementById('worldBtn');
    const menu = document.getElementById('worldMenu');
    function build(){
      menu.innerHTML = '';
      Object.entries(WORLDS).forEach(([id,w])=>{
        const active = id === WorldCtl.id;
        const b = document.createElement('button');
        b.className = 'btn-pill w-full text-left px-3 py-2.5 text-[13px] font-medium flex items-center gap-2.5';
        b.style.cssText = 'border-radius:12px;color:var(--fg)';
        b.setAttribute('role','menuitemradio');
        b.setAttribute('aria-checked', active);
        b.innerHTML = `<span class="pill-dot" style="background:${active?'var(--accent-a)':'var(--fg-faint)'};opacity:${active?1:.5}"></span>
          <span class="min-w-0">
            <span class="block truncate">${U.esc(w.title)}</span>
            <span class="block font-mono text-[10px] mt-0.5" style="color:var(--fg-faint)">${U.esc(w.meta.world)} · ${w.tasks.length} tasks</span>
          </span>
          ${active ? '<i data-lucide="check" class="ml-auto" style="width:14px;height:14px;color:var(--accent-a);flex:none"></i>' : ''}`;
        b.addEventListener('click', ()=>{ WorldCtl.set(id); close(); });
        menu.appendChild(b);
      });
      const hint = document.createElement('div');
      hint.className = 'px-3 pt-2 pb-1 text-[11px] leading-relaxed';
      hint.style.color = 'var(--fg-faint)';
      hint.textContent = 'Choose a world to inspect.';
      menu.appendChild(hint);
      lucide.createIcons();
    }
    function open(){
      build();
      const r = btn.getBoundingClientRect();
      menu.classList.remove('hidden');
      const mw = menu.offsetWidth;
      let x = r.left;
      if (x + mw > window.innerWidth - 10) x = window.innerWidth - mw - 10;
      menu.style.left = x+'px';
      menu.style.top = (r.bottom + 10)+'px';
      btn.setAttribute('aria-expanded','true');
    }
    function close(){ menu.classList.add('hidden'); btn.setAttribute('aria-expanded','false'); }
    btn.addEventListener('click', e=>{
      e.stopPropagation();
      menu.classList.contains('hidden') ? open() : close();
    });
    document.addEventListener('click', e=>{
      if (!e.target.closest('#worldMenu') && !e.target.closest('#worldBtn')) close();
    });
    document.addEventListener('keydown', e=>{ if (e.key === 'Escape') close(); });
  })();

  /* Boot */
  renderWorld();
