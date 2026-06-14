'use client';

import { useMemo, useState } from 'react';
import type { Task, World } from '@/lib/sanctum-data';
import { journey, statusLabels } from '@/lib/sanctum-data';

type Props = {
  worlds: World[];
  databaseConfigured: boolean;
};

function meanOf(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return Math.round(scored.reduce((sum, task) => sum + (task.mean ?? 0), 0) / scored.length);
}

function countFloors(task: Task) {
  return task.spread.filter(score => score <= 40).length;
}

function statusClass(stage: string) {
  return `status ${stage}`;
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

export default function SanctumDashboard({ worlds, databaseConfigured }: Props) {
  const [worldId, setWorldId] = useState(worlds[0]?.id ?? 'korvin-merrow');
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const world = worlds.find(item => item.id === worldId) ?? worlds[0];
  const selected = world.tasks.find(task => task.id === selectedId) ?? world.tasks.find(task => task.stage === 'ready') ?? world.tasks[0];

  const summary = useMemo(() => {
    const delivered = world.tasks.filter(task => task.stage === 'delivered').length;
    const ready = world.tasks.filter(task => task.stage === 'ready').length;
    return { delivered, ready, mean: meanOf(world.tasks) };
  }, [world]);

  return (
    <main className="app-shell">
      <nav className="topbar" aria-label="World navigation">
        <div>
          <span className="eyebrow">Project Sanctum</span>
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

      <section className="hero-grid">
        <div className="hero-panel">
          <span className="eyebrow">{world.kicker}</span>
          <h1>{summary.ready ? `${summary.ready} tasks ready for delivery` : world.title}</h1>
          <p>{world.blurb}</p>
          <div className="hero-metrics">
            <div><strong>{summary.delivered}/{world.tasks.length}</strong><span>Delivered</span></div>
            <div><strong>{summary.ready}</strong><span>Ready</span></div>
            <div><strong>{summary.mean ?? 'TBD'}</strong><span>Suite mean</span></div>
          </div>
        </div>
        <aside className="system-panel">
          <span className="eyebrow">System</span>
          <div className="system-row">
            <span>Neon</span>
            <strong>{databaseConfigured ? 'Configured' : 'Not linked'}</strong>
          </div>
          <div className="system-row">
            <span>Downloads</span>
            <strong>Gated</strong>
          </div>
          <p>Public-safe previews should be promoted deliberately. Raw workspace docs stay out of the deployed surface.</p>
        </aside>
      </section>

      <section className="journey-panel" aria-label="World journey">
        <div className="section-head">
          <span className="eyebrow">World journey</span>
          <h2>From concept to task suite</h2>
        </div>
        <div className="journey-track">
          {journey.map(item => (
            <article key={item.label} className={`journey-step ${item.status}`}>
              <span>{item.status}</span>
              <strong>{item.label}</strong>
              <p>{item.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="workspace-grid">
        <div className="task-list-panel">
          <div className="section-head">
            <span className="eyebrow">Tasks</span>
            <h2>Scan first. Open detail only when needed.</h2>
          </div>
          <div className="task-list">
            {world.tasks.map(task => (
              <button
                key={task.id}
                type="button"
                className={`task-row ${selected?.id === task.id ? 'selected' : ''}`}
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
              </button>
            ))}
          </div>
        </div>

        {selected && (
          <aside className="detail-panel" aria-label={`${selected.id} detail`}>
            <span className="eyebrow">{selected.id} detail</span>
            <h2>{selected.name}</h2>
            <p className="lede">{selected.plain}</p>
            <div className="detail-grid">
              <div><span>Mean</span><strong>{selected.mean ?? 'TBD'}</strong></div>
              <div><span>Status</span><strong>{statusLabels[selected.stage]}</strong></div>
              <div><span>Reach</span><strong>{selected.reach}</strong></div>
            </div>
            <section>
              <h3>Mechanism</h3>
              <p>{selected.mechanism}</p>
            </section>
            <section>
              <h3>Packet renderer</h3>
              <div className="packet-stack">
                <article><span>Prompt</span><strong>The ask the model receives</strong><small>{selected.packet.prompt}</small></article>
                <article>
                  <span>Task files</span>
                  <strong>Mounted evidence</strong>
                  {selected.packet.files.map(file => <small key={file}>{artifactCue(file)} · {file}</small>)}
                </article>
                <article><span>Golden</span><strong>The ideal clinical destination</strong><small>{selected.packet.golden}</small></article>
                <article><span>Grader</span><strong>The rule set that decides the score</strong><small>{selected.packet.grader}</small></article>
              </div>
            </section>
            <section>
              <h3>Downloads</h3>
              <p>Downloads are disabled until a sanitized artifact is promoted into the public download folder.</p>
            </section>
          </aside>
        )}
      </section>
    </main>
  );
}
