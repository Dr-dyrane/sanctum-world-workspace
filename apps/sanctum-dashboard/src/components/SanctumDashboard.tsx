'use client';

import { useEffect, useMemo, useState } from 'react';
import type { CSSProperties } from 'react';
import type { TaskDocumentRow } from '@/lib/database';
import type { Task, World } from '@/lib/sanctum-data';
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

function meanOf(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return Math.round(scored.reduce((sum, task) => sum + (task.mean ?? 0), 0) / scored.length);
}

function countFloors(task: Task) {
  return task.spread.filter(score => score <= 40).length;
}

function scorePercent(task: Task) {
  if (typeof task.mean !== 'number') return '0%';
  return `${Math.max(0, Math.min(100, task.mean))}%`;
}

function statusClass(stage: string) {
  return `status ${stage}`;
}

function roleLabel(role: string) {
  const labels: Record<string, string> = {
    prompt: 'Prompt',
    task_file: 'Task file',
    golden: 'Golden',
    grader: 'Grader',
    run_instructions: 'Run notes',
  };
  return labels[role] ?? 'Document';
}

function roleTone(role: string) {
  if (role === 'prompt') return 'blue';
  if (role === 'task_file') return 'green';
  if (role === 'golden') return 'gold';
  if (role === 'grader') return 'purple';
  return 'gray';
}

function artifactCue(name: string) {
  const lower = name.toLowerCase();
  if (lower.includes('photo') || lower.endsWith('.png') || lower.endsWith('.jpg')) return 'Visual evidence';
  if (lower.includes('signout')) return 'Covering note';
  if (lower.includes('handoff')) return 'External handoff';
  if (lower.includes('query')) return 'Documentation query';
  if (lower.includes('coding') || lower.includes('him')) return 'Coding worksheet';
  if (lower.includes('draft') || lower.includes('started')) return 'Started document';
  return 'Mounted file';
}

function formatBytes(value: number | null) {
  if (!value) return 'Not synced';
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${Math.round(value / 102.4) / 10} KB`;
  return `${Math.round(value / 1024 / 102.4) / 10} MB`;
}

function fallbackDocuments(worldId: string, task: Task): DisplayDocument[] {
  const docs: DisplayDocument[] = [
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
      contentText: 'This packet has not been synced from Neon yet. Run npm run seed:docs from the Next app to load task documents.',
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
      contentText: `${artifactCue(file)}. Not synced from Neon yet.`,
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
      contentText: 'Golden reference preview is waiting for Neon sync.',
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
      contentText: 'Grader preview is waiting for Neon sync.',
      contentBase64: null,
      uploaded: false,
    },
  ];

  return docs;
}

function uploadedDocuments(documents: TaskDocumentRow[], worldId: string, taskId: string): DisplayDocument[] {
  return documents
    .filter(doc => doc.worldId === worldId && doc.taskId === taskId)
    .map(doc => ({
      ...doc,
      sha256: doc.sha256,
      byteSize: doc.byteSize,
      uploaded: true,
    }));
}

function previewText(doc: DisplayDocument) {
  if (doc.contentText) return doc.contentText;
  if (doc.contentBase64) return 'Image payload synced to Neon. Preview renders from the database payload below.';
  if (doc.uploaded) return 'This file is synced to Neon as binary metadata. No text preview is available for this type.';
  return 'Not synced yet.';
}

function primaryFailure(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return scored.reduce((lowest, task) => (task.mean ?? 100) < (lowest.mean ?? 100) ? task : lowest, scored[0]);
}

export default function SanctumDashboard({ worlds, databaseConfigured, documents }: Props) {
  const [worldId, setWorldId] = useState(worlds[0]?.id ?? 'korvin-merrow');
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [activeDocId, setActiveDocId] = useState<string | null>(null);

  const world = worlds.find(item => item.id === worldId) ?? worlds[0];
  const selected = world?.tasks.find(task => task.id === selectedId) ?? world?.tasks.find(task => task.stage === 'ready') ?? world?.tasks[0];
  const lowest = world ? primaryFailure(world.tasks) : null;

  useEffect(() => {
    setActiveDocId(null);
  }, [selected?.id, world?.id]);

  const summary = useMemo(() => {
    if (!world) return { delivered: 0, ready: 0, mean: null, docs: 0 };
    const delivered = world.tasks.filter(task => task.stage === 'delivered').length;
    const ready = world.tasks.filter(task => task.stage === 'ready').length;
    const docs = documents.filter(doc => doc.worldId === world.id).length;
    return { delivered, ready, mean: meanOf(world.tasks), docs };
  }, [documents, world]);

  const taskDocuments = useMemo(() => {
    if (!world || !selected) return [];
    const uploaded = uploadedDocuments(documents, world.id, selected.id);
    return uploaded.length ? uploaded : fallbackDocuments(world.id, selected);
  }, [documents, selected, world]);

  if (!world || !selected) return null;

  const activeDoc = taskDocuments.find(doc => doc.id === activeDocId) ?? taskDocuments[0];

  return (
    <main className="app-shell">
      <nav className="topbar" aria-label="World navigation">
        <div className="brand-mark">
          <span>Sanctum</span>
        </div>
        <div className="topbar-title">
          <span className="caption">Project Sanctum</span>
          <strong>{world.title}</strong>
        </div>
        <div className="world-switcher">
          {worlds.map(item => (
            <button
              key={item.id}
              type="button"
              className={item.id === world.id ? 'active' : ''}
              onClick={() => {
                setWorldId(item.id);
                setSelectedId(null);
              }}
            >
              {item.title}
            </button>
          ))}
        </div>
      </nav>

      <section className="focus-hero">
        <div className="focus-copy">
          <span className="caption">{world.kicker}</span>
          <h1>{summary.ready ? `${summary.ready} tasks ready` : 'World in planning'}</h1>
          <p>{world.blurb}</p>
          <div className="hero-actions" aria-label="Primary actions">
            <button type="button" className="primary-action" onClick={() => setSelectedId(selected.id)}>
              Inspect {selected.id} packet
            </button>
            <span>{databaseConfigured && summary.docs ? `${summary.docs} docs in Neon` : 'Neon sync pending'}</span>
          </div>
        </div>

        <aside className="signal-card">
          <span className="caption">Primary inference</span>
          <strong>{lowest?.name ?? selected.name}</strong>
          <p>{lowest?.plain ?? selected.plain}</p>
          <div className="signal-meter">
            <span>Lowest mean</span>
            <strong>{lowest?.mean ?? 'TBD'}</strong>
          </div>
        </aside>

        <div className="metric-ribbon" aria-label="World metrics">
          <div>
            <span>Delivered</span>
            <strong>{summary.delivered}/{world.tasks.length}</strong>
          </div>
          <div>
            <span>Ready</span>
            <strong>{summary.ready}</strong>
          </div>
          <div>
            <span>Suite mean</span>
            <strong>{summary.mean ?? 'TBD'}</strong>
          </div>
          <div>
            <span>Neon</span>
            <strong>{summary.docs ? `${summary.docs} docs` : databaseConfigured ? 'Linked' : 'Off'}</strong>
          </div>
        </div>
      </section>

      <section className="story-strip" aria-label="World journey">
        <div>
          <span className="caption">World journey</span>
          <h2>Build the world, then stress it task by task.</h2>
        </div>
        <div className="journey-track">
          {journey.map(item => (
            <article key={item.label} className={`journey-step ${item.status}`}>
              <span>{item.status}</span>
              <strong>{item.label}</strong>
            </article>
          ))}
        </div>
      </section>

      <section className="workspace-grid">
        <div className="task-list-panel">
          <div className="section-head">
            <span className="caption">Task queue</span>
            <h2>One chart. Ten forced moves.</h2>
          </div>
          <div className="task-list">
            {world.tasks.map(task => (
              <button
                key={task.id}
                type="button"
                className={`task-row ${selected.id === task.id ? 'selected' : ''}`}
                style={{ '--score': scorePercent(task) } as CSSProperties}
                onClick={() => setSelectedId(task.id)}
              >
                <span className={statusClass(task.stage)}>{statusLabels[task.stage]}</span>
                <span className="task-main">
                  <span>{task.id}</span>
                  <strong>{task.name}</strong>
                  <small>{task.family}</small>
                </span>
                <span className="task-score">
                  <strong>{task.mean ?? 'TBD'}</strong>
                  <small>{countFloors(task)} floors</small>
                </span>
                <span className="score-track" aria-hidden="true"><span /></span>
              </button>
            ))}
          </div>
        </div>

        <aside className="detail-panel" aria-label={`${selected.id} detail`}>
          <div className="detail-header">
            <span className={statusClass(selected.stage)}>{statusLabels[selected.stage]}</span>
            <span>{selected.workflow}</span>
          </div>
          <h2>{selected.name}</h2>
          <p className="lede">{selected.plain}</p>

          <div className="detail-grid">
            <div><span>Mean</span><strong>{selected.mean ?? 'TBD'}</strong></div>
            <div><span>Reach</span><strong>{selected.reach}</strong></div>
            <div><span>Docs</span><strong>{taskDocuments.length}</strong></div>
          </div>

          <section className="mechanism-panel">
            <span className="caption">Trap surface</span>
            <p>{selected.mechanism}</p>
          </section>

          <section className="document-renderer">
            <div className="section-head compact">
              <span className="caption">Packet renderer</span>
              <h3>Read the actual task artifacts.</h3>
            </div>

            <div className="doc-tabs" aria-label="Task packet documents">
              {taskDocuments.map(doc => (
                <button
                  key={doc.id}
                  type="button"
                  className={activeDoc?.id === doc.id ? 'active' : ''}
                  onClick={() => setActiveDocId(doc.id)}
                >
                  <span className={`role-dot ${roleTone(doc.role)}`} />
                  <strong>{roleLabel(doc.role)}</strong>
                  <small>{doc.filename}</small>
                </button>
              ))}
            </div>

            {activeDoc && (
              <article className="doc-preview">
                <header>
                  <div>
                    <span className="caption">{roleLabel(activeDoc.role)}</span>
                    <strong>{activeDoc.filename}</strong>
                  </div>
                  <span>{formatBytes(activeDoc.byteSize)}</span>
                </header>

                {activeDoc.contentBase64 ? (
                  <img
                    src={`data:${activeDoc.mimeType};base64,${activeDoc.contentBase64}`}
                    alt={`${activeDoc.filename} preview`}
                  />
                ) : (
                  <pre>{previewText(activeDoc)}</pre>
                )}

                <footer>
                  <span>{activeDoc.uploaded ? 'Synced from Neon' : 'Local fallback'}</span>
                  <span>{activeDoc.sha256 ? `sha ${activeDoc.sha256.slice(0, 10)}` : 'No hash'}</span>
                </footer>
              </article>
            )}
          </section>
        </aside>
      </section>
    </main>
  );
}
