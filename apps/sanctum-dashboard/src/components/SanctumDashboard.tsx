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
type IconName =
  | 'activity'
  | 'arrow-right'
  | 'chevron-down'
  | 'check-circle'
  | 'eye'
  | 'file-check'
  | 'folder-open'
  | 'moon'
  | 'shield'
  | 'sun'
  | 'x';

const filterLabels: Array<{ id: Filter; label: string }> = [
  { id: 'all', label: 'All' },
  { id: 'delivered', label: 'Delivered' },
  { id: 'ready', label: 'Ready' },
  { id: 'planned', label: 'Planned' },
  { id: 'review', label: 'Review' },
];

function Icon({ name, className = '' }: { name: IconName; className?: string }) {
  const common = {
    className: `lucide-icon ${className}`.trim(),
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 2,
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
    'aria-hidden': true,
  };

  if (name === 'activity') {
    return (
      <svg {...common}>
        <path d="M22 12h-4l-3 8-6-16-3 8H2" />
      </svg>
    );
  }

  if (name === 'arrow-right') {
    return (
      <svg {...common}>
        <path d="M5 12h14" />
        <path d="m12 5 7 7-7 7" />
      </svg>
    );
  }

  if (name === 'chevron-down') {
    return (
      <svg {...common}>
        <path d="m6 9 6 6 6-6" />
      </svg>
    );
  }

  if (name === 'check-circle') {
    return (
      <svg {...common}>
        <path d="M9 12l2 2 4-5" />
        <circle cx="12" cy="12" r="9" />
      </svg>
    );
  }

  if (name === 'eye') {
    return (
      <svg {...common}>
        <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7Z" />
        <circle cx="12" cy="12" r="3" />
      </svg>
    );
  }

  if (name === 'file-check') {
    return (
      <svg {...common}>
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z" />
        <path d="M14 2v6h6" />
        <path d="m9 15 2 2 4-5" />
      </svg>
    );
  }

  if (name === 'folder-open') {
    return (
      <svg {...common}>
        <path d="M6 14l1.5-3A2 2 0 0 1 9.3 10H20a2 2 0 0 1 1.8 2.9l-2.1 4.2A2 2 0 0 1 17.9 18H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h7a2 2 0 0 1 2 2v2" />
      </svg>
    );
  }

  if (name === 'moon') {
    return (
      <svg {...common}>
        <path d="M12 3a6.8 6.8 0 0 0 8.9 8.9A9 9 0 1 1 12 3" />
      </svg>
    );
  }

  if (name === 'shield') {
    return (
      <svg {...common}>
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z" />
        <path d="m9 12 2 2 4-5" />
      </svg>
    );
  }

  if (name === 'sun') {
    return (
      <svg {...common}>
        <circle cx="12" cy="12" r="4" />
        <path d="M12 2v2" />
        <path d="M12 20v2" />
        <path d="m4.93 4.93 1.41 1.41" />
        <path d="m17.66 17.66 1.41 1.41" />
        <path d="M2 12h2" />
        <path d="M20 12h2" />
        <path d="m6.34 17.66-1.41 1.41" />
        <path d="m19.07 4.93-1.41 1.41" />
      </svg>
    );
  }

  return (
    <svg {...common}>
      <path d="M18 6 6 18" />
      <path d="m6 6 12 12" />
    </svg>
  );
}

function meanOf(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return Number((scored.reduce((sum, task) => sum + (task.mean ?? 0), 0) / scored.length).toFixed(1));
}

function criticalRunIndexes(task: Task) {
  if (task.criticalRuns?.length) return task.criticalRuns;
  return (task.spread ?? [])
    .map((score, index) => score <= 40 ? index : -1)
    .filter(index => index >= 0);
}

function counts(task: Task) {
  const spread = task.spread ?? [];
  const criticalRuns = criticalRunIndexes(task);
  return {
    catchers: spread.filter(score => score >= 85).length,
    floors: criticalRuns.length,
    sub70: spread.filter(score => score < 70).length,
  };
}

function lowestRunIndex(task: Task) {
  const criticalRuns = criticalRunIndexes(task);
  if (criticalRuns.length) return criticalRuns[0];
  if (!task.spread.length) return -1;
  return task.spread.reduce((lowestIndex, score, index) => score < task.spread[lowestIndex] ? index : lowestIndex, 0);
}

function readinessFor(task: Task) {
  if (task.stage === 'planned') return { label: 'Not built', tone: 'planned' };
  if (task.stage === 'review') return { label: 'Needs review', tone: 'review' };
  if (task.stage === 'delivered') return { label: 'Delivered', tone: 'delivered' };
  if (task.reach === 'watch' || task.reach === 'open') return { label: 'Ready with watch', tone: 'watch' };
  return { label: 'Ready', tone: 'ready' };
}

function reachLabel(task: Task) {
  if (task.reach === 'proven') return 'Proven';
  if (task.reach === 'watch') return 'Watch';
  if (task.reach === 'open') return 'Open';
  return 'Pending';
}

function readinessGates(task: Task) {
  const taskCounts = counts(task);
  const built = task.stage !== 'planned';
  const proofComplete = task.stage === 'delivered' || task.stage === 'ready';
  return [
    {
      icon: 'activity' as IconName,
      label: 'Clinical miss',
      value: built ? `${taskCounts.floors}/${task.runsTotal}` : 'Pending',
      state: taskCounts.floors > 0 ? 'pass' : built ? 'watch' : 'pending',
    },
    {
      icon: 'shield' as IconName,
      label: 'Fairness',
      value: built ? 'Clean' : 'Pending',
      state: built ? 'pass' : 'pending',
    },
    {
      icon: 'eye' as IconName,
      label: 'Reach',
      value: reachLabel(task),
      state: task.reach === 'proven' ? 'pass' : task.reach === 'notstarted' ? 'pending' : 'watch',
    },
    {
      icon: 'file-check' as IconName,
      label: 'Proof',
      value: proofComplete ? 'Complete' : 'Pending',
      state: proofComplete ? 'pass' : 'pending',
    },
  ];
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
    const state = runScoreClass(value, task, index);
    const className = state === 'pending'
      ? 'dot empty'
      : state === 'floor'
        ? 'dot floor'
        : state === 'catcher'
          ? 'dot catcher'
          : 'dot mid';
    return <span key={`${task.id}-${index}`} className={className} title={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`} />;
  });
}

function runScoreClass(value: number | undefined, task?: Task, index?: number) {
  if (task && typeof index === 'number' && criticalRunIndexes(task).includes(index)) return 'floor';
  if (typeof value !== 'number') return 'pending';
  if (value <= 40) return 'floor';
  if (value >= 85) return 'catcher';
  return 'middle';
}

function RadialTaskMap({
  tasks,
  selectedId,
  onSelect,
}: {
  tasks: Task[];
  selectedId: string;
  onSelect: (id: string) => void;
}) {
  const cx = 280;
  const cy = 280;
  const radius = 190;
  const sorted = [...tasks].sort((a, b) => {
    const av = typeof a.mean === 'number' ? a.mean : -1;
    const bv = typeof b.mean === 'number' ? b.mean : -1;
    if (av === bv) return a.position - b.position;
    return bv - av;
  });
  const points = sorted.map((task, index) => {
    const angle = (-90 + index * (360 / sorted.length)) * Math.PI / 180;
    return {
      task,
      x: cx + radius * Math.cos(angle),
      y: cy + radius * Math.sin(angle),
    };
  });
  const path = points.map((point, index) => `${index === 0 ? 'M' : 'L'}${point.x.toFixed(1)} ${point.y.toFixed(1)}`).join(' ') + ' Z';
  const scored = tasks.filter(task => typeof task.mean === 'number');
  const suiteMean = scored.length ? meanOf(scored) : null;

  return (
    <div className="radial-wrap">
      <svg className="radial-chart" viewBox="0 0 560 560" role="img" aria-label="Task map by mean score">
        <defs>
          <linearGradient id="radialArc" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="var(--accent-a)" />
            <stop offset="100%" stopColor="var(--accent-b)" />
          </linearGradient>
        </defs>
        <path className="radial-arc" d={path} />
        <text className="radial-center-label" x={cx} y={cy - 12} textAnchor="middle">Suite mean</text>
        <text className="radial-center-value" x={cx} y={cy + 22} textAnchor="middle">{suiteMean ?? 'TBD'}</text>
        {points.map(({ task, x, y }) => {
          const hasMean = typeof task.mean === 'number';
          const failure = hasMean ? 100 - (task.mean ?? 0) : 0;
          const nodeRadius = hasMean ? 14 + failure * 0.34 : 24;
          const opacity = hasMean ? 0.32 + (failure / 100) * 0.62 : 0.34;
          const active = selectedId === task.id;

          return (
            <g
              key={task.id}
              className={`radial-node ${task.stage} ${active ? 'active' : ''}`}
              tabIndex={0}
              role="button"
              aria-label={`${task.id}. ${task.name}. Mean ${scoreText(task)}.`}
              onClick={() => onSelect(task.id)}
              onKeyDown={event => {
                if (event.key === 'Enter' || event.key === ' ') {
                  event.preventDefault();
                  onSelect(task.id);
                }
              }}
            >
              <circle className="radial-halo" cx={x} cy={y} r={nodeRadius + 10} opacity={opacity * 0.12} />
              <circle className="radial-dot" cx={x} cy={y} r={active ? nodeRadius + 5 : nodeRadius} opacity={opacity} />
              <text className="radial-node-label" x={x} y={y + 4} textAnchor="middle">{task.id.replace(/^[A-Z]+/, '')}</text>
            </g>
          );
        })}
      </svg>
    </div>
  );
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
  const defaultTask = world?.tasks.find(task => task.stage === 'ready' && (task.reach === 'watch' || task.reach === 'open'))
    ?? world?.tasks.find(task => task.stage === 'ready')
    ?? hardest
    ?? world?.tasks[0];
  const selected = world?.tasks.find(task => task.id === selectedId) ?? defaultTask;

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
      if (!target?.closest('.world-menu-wrap, .world-menu-popover')) setWorldMenuOpen(false);
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
    if (!world) return { delivered: 0, ready: 0, review: 0, planned: 0, mean: null, sourceFiles: 0 };
    const delivered = world.tasks.filter(task => task.stage === 'delivered').length;
    const ready = world.tasks.filter(task => task.stage === 'ready').length;
    const review = world.tasks.filter(task => task.stage === 'review').length;
    const planned = world.tasks.filter(task => task.stage === 'planned').length;
    const sourceFiles = documents.filter(doc => doc.worldId === world.id).length;
    return { delivered, ready, review, planned, mean: meanOf(world.tasks), sourceFiles };
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
  const lensCounts: Record<Filter, number> = {
    all: world.tasks.length,
    delivered: summary.delivered,
    ready: summary.ready,
    planned: summary.planned,
    review: summary.review,
  };
  const selectedReadiness = readinessFor(selected);
  const selectedGates = readinessGates(selected);
  const selectedLowestRun = lowestRunIndex(selected);
  const selectedRunCount = counts(selected);

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
              <Icon name="chevron-down" className="menu-chevron" />
            </button>
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
            <Icon name={darkMode ? 'moon' : 'sun'} />
          </button>
        </div>
        {worldMenuOpen ? (
          <div className="world-menu world-menu-popover surf" role="menu" aria-label="Switch world">
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
      </header>

      <main className="app-shell">
        <section className="hero-section">
          <div className={`readiness-stage surf ${selectedReadiness.tone}`} aria-label="Task readiness">
            <div className="readiness-top">
              <div>
                <p className="micro-label">{world.title}</p>
                <span>Task readiness</span>
              </div>
              <span className={statusClass(selectedReadiness.tone)}>{selectedReadiness.label}</span>
            </div>

            <div className="readiness-grid">
              <div className="verdict-stack">
                <span className="task-token">{selected.id}</span>
                <h1>{selectedReadiness.label}</h1>
                <p>{selected.plain}</p>
                <div className="readiness-actions">
                  <button type="button" className="primary-cta" onClick={() => setMaterialsOpen(true)}>
                    Open proof
                    <Icon name="folder-open" />
                  </button>
                  <a className="quiet-link" href={`#task-${selected.id}`}>View task</a>
                </div>
              </div>

              <aside className="score-stage" aria-label={`${selected.id} score`}>
                <span>Mean</span>
                <strong>{scoreText(selected)}</strong>
                <p>{selected.name}</p>
              </aside>
            </div>

            <div className="trajectory-panel" aria-label="Trajectory score shape">
              <div className="trajectory-head">
                <div>
                  <span>Score shape</span>
                  <strong>{selectedRunCount.sub70}/{selected.runsTotal} under 70</strong>
                </div>
                <div>
                  <span>Critical misses</span>
                  <strong>{selectedRunCount.floors}</strong>
                </div>
              </div>
              <div className="trajectory-strip">
                {Array.from({ length: selected.runsTotal }).map((_, index) => {
                  const value = selected.spread[index];
                  const state = runScoreClass(value, selected, index);
                  return (
                    <span
                      key={`${selected.id}-run-${index}`}
                      className={`run-cell ${state} ${index === selectedLowestRun ? 'proof' : ''}`}
                      style={{ '--i': index } as CSSProperties}
                      aria-label={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
                      title={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
                    >
                      <small>{index + 1}</small>
                      <strong>{typeof value === 'number' ? value : '-'}</strong>
                    </span>
                  );
                })}
              </div>
            </div>

            <div className="gate-grid" aria-label="Readiness gates">
              {selectedGates.map(gate => (
                <div key={gate.label} className={`gate-card ${gate.state}`}>
                  <Icon name={gate.icon} />
                  <span>{gate.label}</span>
                  <strong>{gate.value}</strong>
                </div>
              ))}
            </div>

            <div className="world-track" aria-label="Task status timeline">
              {world.tasks.map(task => (
                <button
                  key={task.id}
                  type="button"
                  className={`track-step ${task.stage} ${selected.id === task.id ? 'active' : ''}`}
                  aria-label={`${task.id}. ${task.name}. ${statusLabels[task.stage]}.`}
                  aria-current={selected.id === task.id ? 'true' : undefined}
                  title={`${task.id}: ${task.name}`}
                  onClick={() => setSelectedId(task.id)}
                />
              ))}
            </div>
          </div>

          <details className="native-details surf">
            <summary>
              <span>Task map</span>
              <span className="details-control">{world.tasks.length} tasks <Icon name="chevron-down" /></span>
            </summary>
            <RadialTaskMap tasks={world.tasks} selectedId={selected.id} onSelect={setSelectedId} />
          </details>
        </section>

        <section className="signal-panel surf" aria-label="Failure signal families">
          <div className="section-head">
                <p className="micro-label">Challenge groups</p>
                <h2>Where models stumble</h2>
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
                <Icon name="arrow-right" />
              </button>
            </div>
          ) : null}
        </section>

        <section className="task-lens-panel surf-2" aria-label="Task view">
          <div className="lens-meta">
            <p className="micro-label">View</p>
            <strong>{filter === 'all' ? 'All tasks' : statusLabels[filter]}</strong>
          </div>
          <div className="lens-dock" role="group" aria-label="Choose task status lens">
            {filterLabels.map(item => (
              <button
                key={item.id}
                type="button"
                className={`lens-button ${filter === item.id ? 'active' : ''}`}
                aria-pressed={filter === item.id}
                onClick={() => setFilter(item.id)}
              >
                <span className={`lens-dot ${item.id}`} />
                <span>{item.label}</span>
                <strong>{lensCounts[item.id]}</strong>
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
                <button
                  type="button"
                  className="task-card-button"
                  aria-expanded={selected.id === task.id}
                  aria-controls={selected.id === task.id ? `task-${task.id}-summary` : undefined}
                  onClick={() => setSelectedId(task.id)}
                >
                  <span className="task-id">{task.id}</span>
                  <span className={statusClass(task.stage)}>{statusLabels[task.stage]}</span>
                  <span className="task-title-block">
                    <strong>{task.name}</strong>
                    <small>{task.family}</small>
                    <span className="task-mini-runs">{runDots(task)}</span>
                  </span>
                  <span className="score-ring" style={{ '--score': scorePercent(task) } as CSSProperties}>
                    <strong>{scoreText(task)}</strong>
                  </span>
                  <Icon name="chevron-down" className="task-chevron" />
                </button>
                {selected.id === task.id ? (
                  <div id={`task-${task.id}-summary`} className="task-card-body" role="region" aria-label={`${task.id} summary`}>
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
                      Open packet
                      <Icon name="folder-open" />
                    </button>
                  </div>
                ) : null}
              </article>
            );
          })}
        </section>

        <section className="summary-panel surf">
          <p className="micro-label">Snapshot</p>
          <div className="summary-grid">
            <div><strong>{summary.delivered}</strong><span>Delivered tasks</span></div>
            <div><strong>{summary.ready}</strong><span>Ready to deliver</span></div>
            <div><strong>{summary.sourceFiles || '-'}</strong><span>Files</span></div>
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
                  <Icon name="x" />
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
