'use client';

import Image from 'next/image';
import { useEffect, useMemo, useState } from 'react';
import type { CSSProperties, ReactNode } from 'react';
import logo from '@/app/logo.png';
import type { TaskDocumentRow } from '@/lib/database';
import type { Stage, Task, World } from '@/lib/sanctum-data';
import { journey, statusLabels } from '@/lib/sanctum-data';

type Props = {
  worlds: World[];
  databaseConfigured: boolean;
  documents: TaskDocumentRow[];
};

type DisplayDocument = {
  id: string;
  worldId: string;
  taskId: string;
  role: string;
  filename: string;
  relativePath: string;
  mimeType: string;
  sha256: string | null;
  byteSize: number | null;
  contentText: string | null;
  contentBase64: string | null;
  uploaded: boolean;
};

type Filter = 'all' | Stage;

const filterLabels: Array<{ id: Filter; label: string }> = [
  { id: 'all', label: 'All' },
  { id: 'delivered', label: 'Delivered' },
  { id: 'ready', label: 'Ready' },
  { id: 'planned', label: 'Planned' },
  { id: 'review', label: 'Review' },
];

function meanOf(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return Number((scored.reduce((sum, task) => sum + (task.mean ?? 0), 0) / scored.length).toFixed(1));
}

function counts(task: Task) {
  const spread = task.spread ?? [];
  return {
    catchers: spread.filter(score => score >= 85).length,
    floors: spread.filter(score => score <= 40).length,
    sub70: spread.filter(score => score < 70).length,
  };
}

function statusClass(stage: string) {
  return `status-pill ${stage}`;
}

function roleLabel(role: string) {
  const labels: Record<string, string> = {
    prompt: 'Task ask',
    task_file: 'Source file',
    golden: 'Reference answer',
    grader: 'Review guide',
    run_instructions: 'Run note',
  };
  return labels[role] ?? 'Source file';
}

function roleTone(role: string) {
  if (role === 'prompt') return 'blue';
  if (role === 'task_file') return 'green';
  if (role === 'golden') return 'amber';
  if (role === 'grader') return 'purple';
  return 'gray';
}

function sourceCue(name: string) {
  const lower = name.toLowerCase();
  if (lower.includes('photo') || lower.endsWith('.png') || lower.endsWith('.jpg')) return 'Visual evidence';
  if (lower.includes('signout')) return 'Covering note';
  if (lower.includes('handoff')) return 'External handoff';
  if (lower.includes('query')) return 'Documentation query';
  if (lower.includes('coding') || lower.includes('him')) return 'Coding worksheet';
  if (lower.includes('draft') || lower.includes('started')) return 'Started document';
  return 'Supporting file';
}

function sourceName(doc: DisplayDocument) {
  if (doc.role === 'prompt') return 'Task ask';
  if (doc.role === 'golden') return 'Reference answer';
  if (doc.role === 'grader') return 'Review guide';
  if (doc.role === 'run_instructions') return 'Run note';
  return sourceCue(doc.filename);
}

function formatBytes(value: number | null) {
  if (!value) return 'No preview';
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${Math.round(value / 102.4) / 10} KB`;
  return `${Math.round(value / 1024 / 102.4) / 10} MB`;
}

function scoreText(task: Task) {
  return typeof task.mean === 'number' ? String(task.mean) : 'TBD';
}

function scorePercent(task: Task) {
  if (typeof task.mean !== 'number') return '0%';
  return `${Math.max(0, Math.min(100, task.mean))}%`;
}

function failurePercent(task: Task) {
  if (typeof task.mean !== 'number') return '0%';
  return `${Math.max(0, Math.min(100, 100 - task.mean))}%`;
}

function fallbackDocuments(worldId: string, task: Task): DisplayDocument[] {
  return [
    {
      id: `${task.id}:prompt:fallback`,
      worldId,
      taskId: task.id,
      role: 'prompt',
      filename: task.packet.prompt,
      relativePath: '',
      mimeType: 'text/plain',
      sha256: null,
      byteSize: null,
      contentText: 'Task ask preview pending.',
      contentBase64: null,
      uploaded: false,
    },
    ...task.packet.files.map((file, index) => ({
      id: `${task.id}:task_file:${index}:fallback`,
      worldId,
      taskId: task.id,
      role: 'task_file',
      filename: file,
      relativePath: '',
      mimeType: 'application/octet-stream',
      sha256: null,
      byteSize: null,
      contentText: `${sourceCue(file)}. Preview pending.`,
      contentBase64: null,
      uploaded: false,
    })),
    {
      id: `${task.id}:golden:fallback`,
      worldId,
      taskId: task.id,
      role: 'golden',
      filename: task.packet.golden,
      relativePath: '',
      mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      sha256: null,
      byteSize: null,
      contentText: 'Reference answer preview pending.',
      contentBase64: null,
      uploaded: false,
    },
    {
      id: `${task.id}:grader:fallback`,
      worldId,
      taskId: task.id,
      role: 'grader',
      filename: task.packet.grader,
      relativePath: '',
      mimeType: 'text/plain',
      sha256: null,
      byteSize: null,
      contentText: 'Review guide preview pending.',
      contentBase64: null,
      uploaded: false,
    },
  ];
}

function uploadedDocuments(documents: TaskDocumentRow[], worldId: string, taskId: string): DisplayDocument[] {
  return documents
    .filter(doc => doc.worldId === worldId && doc.taskId === taskId)
    .filter(doc => doc.role !== 'run_instructions')
    .map(doc => ({
      ...doc,
      sha256: doc.sha256,
      byteSize: doc.byteSize,
      uploaded: true,
    }));
}

function previewText(doc: DisplayDocument) {
  if (doc.contentText) return doc.contentText;
  if (doc.contentBase64) return 'Image ready.';
  if (doc.uploaded) return 'No preview for this file type.';
  return 'Preview pending.';
}

function isMarkdown(doc: DisplayDocument) {
  return doc.mimeType === 'text/markdown' || doc.filename.toLowerCase().endsWith('.md');
}

function cleanInlineMarkdown(value: string) {
  return value
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/__([^_]+)__/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_([^_]+)_/g, '$1')
    .trim();
}

function renderTextPreview(text: string, markdown: boolean) {
  const lines = text.split('\n');
  const nodes: ReactNode[] = [];
  let codeLines: string[] = [];
  let inCode = false;

  function flushCode(key: string) {
    if (!codeLines.length) return;
    nodes.push(<pre className="md-code" key={key}>{codeLines.join('\n')}</pre>);
    codeLines = [];
  }

  lines.forEach((line, index) => {
    const trimmed = line.trim();

    if (markdown && trimmed.startsWith('```')) {
      if (inCode) flushCode(`code-${index}`);
      inCode = !inCode;
      return;
    }

    if (inCode) {
      codeLines.push(line);
      return;
    }

    if (!trimmed) {
      return;
    }

    if (markdown) {
      const heading = trimmed.match(/^(#{1,6})\s+(.+)$/);
      if (heading) {
        nodes.push(<h4 key={index}>{cleanInlineMarkdown(heading[2])}</h4>);
        return;
      }

      const bullet = trimmed.match(/^[-*+]\s+(.+)$/);
      if (bullet) {
        nodes.push(<p className="md-list" key={index}>{cleanInlineMarkdown(bullet[1])}</p>);
        return;
      }

      const numbered = trimmed.match(/^\d+[.)]\s+(.+)$/);
      if (numbered) {
        nodes.push(<p className="md-number" key={index}>{cleanInlineMarkdown(numbered[1])}</p>);
        return;
      }

      const quote = trimmed.match(/^>\s+(.+)$/);
      if (quote) {
        nodes.push(<blockquote key={index}>{cleanInlineMarkdown(quote[1])}</blockquote>);
        return;
      }
    }

    nodes.push(<p key={index}>{markdown ? cleanInlineMarkdown(trimmed) : trimmed}</p>);
  });

  flushCode('code-final');

  return <div className={markdown ? 'markdown-preview document-copy' : 'document-copy'}>{nodes}</div>;
}

function renderDocumentPreview(doc: DisplayDocument) {
  return renderTextPreview(previewText(doc), isMarkdown(doc));
}

function primaryFailure(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return scored.reduce((lowest, task) => (task.mean ?? 100) < (lowest.mean ?? 100) ? task : lowest, scored[0]);
}

function families(tasks: Task[]) {
  const byFamily = new Map<string, Task[]>();
  for (const task of tasks) {
    const list = byFamily.get(task.family) ?? [];
    list.push(task);
    byFamily.set(task.family, list);
  }
  return Array.from(byFamily.entries()).map(([family, list]) => {
    const scored = list.filter(task => typeof task.mean === 'number');
    const mean = scored.length ? meanOf(scored) : null;
    const floorCount = list.reduce((sum, task) => sum + counts(task).floors, 0);
    return { family, tasks: list, mean, floorCount };
  });
}

function runDots(task: Task) {
  return Array.from({ length: task.runsTotal }).map((_, index) => {
    const value = task.spread[index];
    const className = typeof value !== 'number'
      ? 'dot empty'
      : value <= 40
        ? 'dot floor'
        : value >= 85
          ? 'dot catcher'
          : 'dot mid';
    return <span key={`${task.id}-${index}`} className={className} title={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`} />;
  });
}

export default function SanctumDashboard({ worlds, databaseConfigured, documents }: Props) {
  const [worldId, setWorldId] = useState(worlds[0]?.id ?? 'korvin-merrow');
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [activeDocId, setActiveDocId] = useState<string | null>(null);
  const [materialsOpen, setMaterialsOpen] = useState(false);
  const [worldMenuOpen, setWorldMenuOpen] = useState(false);
  const [activeSignalFamily, setActiveSignalFamily] = useState<string | null>(null);
  const [filter, setFilter] = useState<Filter>('all');
  const [darkMode, setDarkMode] = useState(false);
  const [themeReady, setThemeReady] = useState(false);
  const [scrollProgress, setScrollProgress] = useState(0);

  const world = worlds.find(item => item.id === worldId) ?? worlds[0];
  const hardest = world ? primaryFailure(world.tasks) : null;
  const selected = world?.tasks.find(task => task.id === selectedId) ?? hardest ?? world?.tasks.find(task => task.stage === 'ready') ?? world?.tasks[0];

  useEffect(() => {
    setActiveDocId(null);
  }, [selected?.id, world?.id]);

  useEffect(() => {
    setActiveSignalFamily(null);
  }, [world?.id]);

  useEffect(() => {
    const stored = window.localStorage.getItem('sanctum-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const nextDark = stored ? stored === 'dark' : prefersDark;
    setDarkMode(nextDark);
    document.documentElement.classList.toggle('dark', nextDark);
    document.documentElement.style.colorScheme = nextDark ? 'dark' : 'light';
    setThemeReady(true);
  }, []);

  useEffect(() => {
    if (!themeReady) return;
    document.documentElement.classList.toggle('dark', darkMode);
    document.documentElement.style.colorScheme = darkMode ? 'dark' : 'light';
    window.localStorage.setItem('sanctum-theme', darkMode ? 'dark' : 'light');
  }, [darkMode, themeReady]);

  useEffect(() => {
    function updateProgress() {
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      setScrollProgress(maxScroll > 0 ? Math.min(100, Math.max(0, (window.scrollY / maxScroll) * 100)) : 0);
    }

    updateProgress();
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);

    return () => {
      window.removeEventListener('scroll', updateProgress);
      window.removeEventListener('resize', updateProgress);
    };
  }, []);

  useEffect(() => {
    if (!worldMenuOpen) return;

    function onPointerDown(event: PointerEvent) {
      const target = event.target as HTMLElement | null;
      if (!target?.closest('.world-menu-wrap')) setWorldMenuOpen(false);
    }

    function onKeyDown(event: KeyboardEvent) {
      if (event.key === 'Escape') setWorldMenuOpen(false);
    }

    document.addEventListener('pointerdown', onPointerDown);
    window.addEventListener('keydown', onKeyDown);

    return () => {
      document.removeEventListener('pointerdown', onPointerDown);
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [worldMenuOpen]);

  useEffect(() => {
    if (!materialsOpen) return;

    function onKeyDown(event: KeyboardEvent) {
      if (event.key === 'Escape') setMaterialsOpen(false);
    }

    document.body.style.overflow = 'hidden';
    window.addEventListener('keydown', onKeyDown);

    return () => {
      document.body.style.overflow = '';
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [materialsOpen]);

  const summary = useMemo(() => {
    if (!world) return { delivered: 0, ready: 0, review: 0, mean: null, sourceFiles: 0 };
    const delivered = world.tasks.filter(task => task.stage === 'delivered').length;
    const ready = world.tasks.filter(task => task.stage === 'ready').length;
    const review = world.tasks.filter(task => task.stage === 'review').length;
    const sourceFiles = documents.filter(doc => doc.worldId === world.id).length;
    return { delivered, ready, review, mean: meanOf(world.tasks), sourceFiles };
  }, [documents, world]);

  const visibleTasks = useMemo(() => {
    if (!world) return [];
    return world.tasks.filter(task => filter === 'all' || task.stage === filter);
  }, [filter, world]);

  const familySignals = useMemo(() => world ? families(world.tasks) : [], [world]);
  const activeSignal = familySignals.find(signal => signal.family === activeSignalFamily) ?? null;

  const taskDocuments = useMemo(() => {
    if (!world || !selected) return [];
    const uploaded = uploadedDocuments(documents, world.id, selected.id);
    return uploaded.length ? uploaded : fallbackDocuments(world.id, selected);
  }, [documents, selected, world]);

  if (!world || !selected) return null;

  const activeDoc = taskDocuments.find(doc => doc.id === activeDocId) ?? taskDocuments[0];
  const selectedCounts = counts(selected);
  const sourceStatus = summary.sourceFiles ? `${summary.sourceFiles} files` : databaseConfigured ? 'Sources ready' : 'Sources pending';

  return (
    <>
      <div className="scroll-progress" style={{ width: `${scrollProgress}%` }} />
      <header className="top-chrome" aria-label="World navigation">
        <div className="chrome-bar">
          <Image src={logo} alt="Sanctum" className="logo-mark" width={28} height={28} priority />
          <strong>Sanctum</strong>
          <span className="chrome-separator" />
          <div className="world-menu-wrap">
            <button
              type="button"
              className="world-menu-button"
              aria-haspopup="menu"
              aria-expanded={worldMenuOpen}
              onClick={() => setWorldMenuOpen(open => !open)}
            >
              <span>{world.title}</span>
              <span className="menu-chevron" aria-hidden="true" />
            </button>
            {worldMenuOpen ? (
              <div className="world-menu surf" role="menu" aria-label="Switch world">
                {worlds.map(item => (
                  <button
                    key={item.id}
                    type="button"
                    role="menuitem"
                    className={item.id === world.id ? 'active' : ''}
                    onClick={() => {
                      setWorldId(item.id);
                      setSelectedId(null);
                      setFilter('all');
                      setMaterialsOpen(false);
                      setActiveSignalFamily(null);
                      setWorldMenuOpen(false);
                    }}
                  >
                    <span>{item.title}</span>
                    <small>{item.kicker}</small>
                  </button>
                ))}
              </div>
            ) : null}
          </div>
          <span className="chrome-separator" />
          <span className="chrome-stat">{sourceStatus}</span>
          <button
            type="button"
            className="theme-toggle"
            aria-label={darkMode ? 'Use light appearance' : 'Use dark appearance'}
            aria-pressed={darkMode}
            onClick={() => setDarkMode(value => !value)}
          >
            <span className="theme-icon" aria-hidden="true" />
          </button>
        </div>
      </header>

      <main className="app-shell">
        <section className="hero-section">
          <div className="cockpit surf" aria-label="World status cockpit">
            <div className="cockpit-top">
              <p className="micro-label">{world.title} | {world.kicker}</p>
              <span className={statusClass(summary.ready ? 'ready' : 'planned')}>
                {summary.ready ? `${summary.ready} ready` : 'Planning'}
              </span>
            </div>

            <div className="cockpit-grid">
              <div className="hero-copy">
                <h1>Task Suite</h1>
                <p>{world.blurb}</p>
                <p className="hero-insight">
                  {hardest ? `Sharpest signal: ${hardest.id}. ${hardest.plain}` : 'No pilot signal yet.'}
                </p>
                <button
                  type="button"
                  className="primary-cta"
                  onClick={() => setMaterialsOpen(true)}
                >
                  Open {selected.id} materials
                </button>
              </div>

              <aside className="metric-pane">
                <span>Lowest mean</span>
                <strong>{hardest?.mean ?? 'TBD'}</strong>
                <p>{hardest?.name ?? selected.name}</p>
              </aside>
            </div>

            <div className="world-track" aria-label="Task status timeline">
              {world.tasks.map(task => (
                <button
                  key={task.id}
                  type="button"
                  className={`track-step ${task.stage} ${selected.id === task.id ? 'active' : ''}`}
                  title={`${task.id}: ${task.name}`}
                  onClick={() => setSelectedId(task.id)}
                />
              ))}
            </div>

            <div className="mini-stat-grid">
              <div className="mini-stat"><strong>{summary.delivered}/{world.tasks.length}</strong><span>Delivered</span></div>
              <div className="mini-stat"><strong>{summary.ready}</strong><span>Ready</span></div>
              <div className="mini-stat"><strong>{summary.review}</strong><span>Review</span></div>
              <div className="mini-stat"><strong>{summary.mean ?? 'TBD'}</strong><span>Suite mean</span></div>
            </div>
          </div>

          <details className="native-details surf">
            <summary>
              <span>Task map</span>
              <span>{world.tasks.length} tasks</span>
            </summary>
            <div className="map-grid">
              {world.tasks.map(task => (
                <button
                  key={task.id}
                  type="button"
                  className={`map-cell ${task.stage}`}
                  onClick={() => setSelectedId(task.id)}
                >
                  <span>{task.id}</span>
                  <strong>{scoreText(task)}</strong>
                </button>
              ))}
            </div>
          </details>
        </section>

        <section className="signal-panel surf" aria-label="Failure signal families">
          <div className="section-head">
                <p className="micro-label">Clinical challenge groups</p>
                <h2>Model miss map</h2>
          </div>
          <div className="signal-strip">
            {familySignals.map(signal => (
              <button
                key={signal.family}
                type="button"
                className={`signal-chip ${activeSignalFamily === signal.family ? 'active' : ''}`}
                aria-expanded={activeSignalFamily === signal.family}
                onClick={() => setActiveSignalFamily(activeSignalFamily === signal.family ? null : signal.family)}
              >
                <span>{signal.family}</span>
                <strong>{signal.mean ?? 'TBD'}</strong>
                <small>{signal.tasks.length} tasks, {signal.floorCount} critical misses</small>
              </button>
            ))}
          </div>
          {activeSignal ? (
            <div className="signal-popover surf-2" role="region" aria-label={`${activeSignal.family} details`}>
              <div>
                <p className="micro-label">{activeSignal.family}</p>
                <strong>{activeSignal.mean ?? 'TBD'} mean</strong>
                <span>{activeSignal.tasks.map(task => task.id).join(', ')}</span>
              </div>
              <button
                type="button"
                className="inline-action compact"
                onClick={() => {
                  setSelectedId(activeSignal.tasks[0]?.id ?? null);
                  setActiveSignalFamily(null);
                }}
              >
                View first task
              </button>
            </div>
          ) : null}
        </section>

        <section className="view-options surf-2">
          <div>
            <p className="micro-label">Tasks</p>
            <strong>{filter === 'all' ? 'All tasks' : `${statusLabels[filter]} tasks`}</strong>
          </div>
          <div className="filter-chips" role="group" aria-label="Filter tasks by status">
            {filterLabels.map(item => (
              <button
                key={item.id}
                type="button"
                className={filter === item.id ? 'active' : ''}
                onClick={() => setFilter(item.id)}
              >
                {item.label}
              </button>
            ))}
          </div>
        </section>

        <section className="task-card-list" aria-label="Task cards">
          {visibleTasks.map(task => {
            const taskCounts = counts(task);
            return (
              <article
                id={`task-${task.id}`}
                key={task.id}
                className={`task-card surf ${task.stage} ${selected.id === task.id ? 'selected' : ''}`}
              >
                <button type="button" className="task-card-button" onClick={() => setSelectedId(task.id)}>
                  <span className="task-id">{task.id}</span>
                  <span className={statusClass(task.stage)}>{statusLabels[task.stage]}</span>
                  <span className="task-title-block">
                    <strong>{task.name}</strong>
                    <small>{task.family}</small>
                  </span>
                  <span className="score-ring" style={{ '--score': scorePercent(task) } as CSSProperties}>
                    <strong>{scoreText(task)}</strong>
                  </span>
                </button>
                {selected.id === task.id ? (
                  <div className="task-card-body" role="region" aria-label={`${task.id} summary`}>
                    <p>{task.plain}</p>
                    <div className="signal-track" aria-label="Failure signal">
                      <span style={{ width: failurePercent(task) }} />
                    </div>
                    <div className="run-dots">{runDots(task)}</div>
                    <div className="counts-strip">
                      <span>Safe runs <strong>{taskCounts.catchers}</strong></span>
                      <span>Critical misses <strong>{taskCounts.floors}</strong></span>
                      <span>Under 70 <strong>{taskCounts.sub70}/{task.runsTotal}</strong></span>
                    </div>
                    <button type="button" className="inline-action" onClick={() => setMaterialsOpen(true)}>
                      Open materials
                    </button>
                  </div>
                ) : null}
              </article>
            );
          })}
        </section>

        <section className="summary-panel surf">
          <p className="micro-label">Suite summary</p>
          <div className="summary-grid">
            <div><strong>{summary.delivered}</strong><span>Delivered tasks</span></div>
            <div><strong>{summary.ready}</strong><span>Ready to deliver</span></div>
            <div><strong>{summary.sourceFiles || '-'}</strong><span>Source files</span></div>
            <div><strong>{summary.mean ?? 'TBD'}</strong><span>Mean, 10 tasks</span></div>
          </div>
          <p className="summary-note">
            Open the ask, source files, reference answer, and review guide.
          </p>
          <div className="journey-row">
            {journey.map(item => (
              <span key={item.label}>{item.label}</span>
            ))}
          </div>
        </section>
      </main>

      {materialsOpen ? (
        <div className="modal-root" role="presentation">
          <button type="button" className="modal-backdrop" aria-label="Dismiss materials" onClick={() => setMaterialsOpen(false)} />
          <section className="materials-modal surf" role="dialog" aria-modal="true" aria-label={`${selected.id} materials`}>
            <div className="focus-head">
              <div>
                <p className="micro-label">{selected.id} materials</p>
                <h2>{selected.name}</h2>
              </div>
              <div className="modal-actions">
                <span className={statusClass(selected.stage)}>{statusLabels[selected.stage]}</span>
                <button type="button" className="close-button" aria-label="Close materials" onClick={() => setMaterialsOpen(false)}>
                  Close
                </button>
              </div>
            </div>

            <div className="focus-grid">
              <section className="focus-summary">
                <p>{selected.plain}</p>
                <div className="detail-grid">
                  <div><span>Mean</span><strong>{scoreText(selected)}</strong></div>
                  <div><span>Critical misses</span><strong>{selectedCounts.floors}</strong></div>
                  <div><span>Files</span><strong>{taskDocuments.length}</strong></div>
                </div>
                <div className="mechanism-box">
                  <span>Scored challenge</span>
                  <p>{selected.mechanism}</p>
                </div>
              </section>

              <section className="document-renderer">
                <div className="section-head compact">
                  <p className="micro-label">Task materials</p>
                  <h3>Source packet</h3>
                </div>
                <div className="doc-tabs" aria-label="Task source files">
                  {taskDocuments.map(doc => (
                    <button
                      key={doc.id}
                      type="button"
                      className={activeDoc?.id === doc.id ? 'active' : ''}
                      onClick={() => setActiveDocId(doc.id)}
                    >
                      <span className={`role-dot ${roleTone(doc.role)}`} />
                      <strong>{roleLabel(doc.role)}</strong>
                      {sourceName(doc) !== roleLabel(doc.role) ? <small>{sourceName(doc)}</small> : null}
                    </button>
                  ))}
                </div>

                {activeDoc && (
                  <article className="doc-preview">
                    <header>
                      <div>
                        <span className="micro-label">{roleLabel(activeDoc.role)}</span>
                        <strong>{sourceName(activeDoc)}</strong>
                      </div>
                      <span>{formatBytes(activeDoc.byteSize)}</span>
                    </header>

                    {activeDoc.contentBase64 ? (
                      <img src={`data:${activeDoc.mimeType};base64,${activeDoc.contentBase64}`} alt={`${sourceName(activeDoc)} preview`} />
                    ) : (
                      renderDocumentPreview(activeDoc)
                    )}

                    <footer>
                      <span>{activeDoc.uploaded ? 'Ready' : 'Pending'}</span>
                      <span>{activeDoc.sha256 ? 'Checked' : 'Unchecked'}</span>
                    </footer>
                  </article>
                )}
              </section>
            </div>
          </section>
        </div>
      ) : null}
    </>
  );
}
