'use client';

import { useEffect, useMemo, useState } from 'react';
import type { Stage } from '@/lib/sanctum-data';
import { journey, statusLabels } from '@/lib/sanctum-data';
import { GateSurface } from './dashboard/GateSurface';
import { JourneyTimeline } from './dashboard/JourneyTimeline';
import { ProofSheet } from './dashboard/ProofSheet';
import { SignalGroups } from './dashboard/SignalGroups';
import { TaskList } from './dashboard/TaskList';
import { TaskRail } from './dashboard/TaskRail';
import { TopChrome } from './dashboard/TopChrome';
import { TrajectorySurface } from './dashboard/TrajectorySurface';
import { VerdictHero } from './dashboard/VerdictHero';
import type { DashboardProps, Filter } from './dashboard/types';
import {
  defaultTaskFor,
  fallbackDocuments,
  meanOf,
  selectedTaskState,
  uploadedDocuments,
} from './dashboard/model';

const filterLabels: Array<{ id: Filter; label: string }> = [
  { id: 'all', label: 'All' },
  { id: 'delivered', label: 'Delivered' },
  { id: 'ready', label: 'Ready' },
  { id: 'built', label: 'Built' },
  { id: 'planned', label: 'Planned' },
  { id: 'review', label: 'Review' },
];

export default function SanctumDashboard({ worlds, databaseConfigured, documents }: DashboardProps) {
  const [worldId, setWorldId] = useState(worlds[0]?.id ?? 'korvin-merrow');
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [expandedTaskId, setExpandedTaskId] = useState<string | null>(null);
  const [activeDocId, setActiveDocId] = useState<string | null>(null);
  const [proofOpen, setProofOpen] = useState(false);
  const [worldMenuOpen, setWorldMenuOpen] = useState(false);
  const [activeFamily, setActiveFamily] = useState<string | null>(null);
  const [filter, setFilter] = useState<Filter>('all');
  const [darkMode, setDarkMode] = useState(false);
  const [themeReady, setThemeReady] = useState(false);
  const [scrollProgress, setScrollProgress] = useState(0);

  const world = worlds.find(item => item.id === worldId) ?? worlds[0];
  const defaultTask = world ? defaultTaskFor(world) : null;
  const selectedTask = world?.tasks.find(task => task.id === selectedId) ?? defaultTask;
  const selected = selectedTask ? selectedTaskState(selectedTask) : null;

  useEffect(() => {
    setActiveDocId(null);
  }, [selectedTask?.id, world?.id]);

  useEffect(() => {
    setActiveFamily(null);
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
    if (!proofOpen) return;

    function onKeyDown(event: KeyboardEvent) {
      if (event.key === 'Escape') setProofOpen(false);
    }

    document.body.style.overflow = 'hidden';
    window.addEventListener('keydown', onKeyDown);

    return () => {
      document.body.style.overflow = '';
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [proofOpen]);

  const summary = useMemo(() => {
    if (!world) return { delivered: 0, ready: 0, review: 0, built: 0, planned: 0, mean: null, sourceFiles: 0 };
    return {
      delivered: world.tasks.filter(task => task.stage === 'delivered').length,
      ready: world.tasks.filter(task => task.stage === 'ready').length,
      review: world.tasks.filter(task => task.stage === 'review').length,
      built: world.tasks.filter(task => task.stage === 'built').length,
      planned: world.tasks.filter(task => task.stage === 'planned').length,
      mean: meanOf(world.tasks),
      sourceFiles: documents.filter(doc => doc.worldId === world.id).length,
    };
  }, [documents, world]);

  const taskDocuments = useMemo(() => {
    if (!world || !selectedTask) return [];
    const uploaded = uploadedDocuments(documents, world.id, selectedTask.id);
    return uploaded.length ? uploaded : fallbackDocuments(world.id, selectedTask);
  }, [documents, selectedTask, world]);

  const visibleTasks = useMemo(() => {
    if (!world) return [];
    return world.tasks.filter(task => filter === 'all' || task.stage === filter);
  }, [filter, world]);

  if (!world || !selected || !selectedTask) return null;

  const sourceStatus = summary.sourceFiles ? `${summary.sourceFiles} files` : databaseConfigured ? 'Sources ready' : 'Sources pending';
  const lensCounts: Record<Filter, number> = {
    all: world.tasks.length,
    delivered: summary.delivered,
    ready: summary.ready,
    built: summary.built,
    planned: summary.planned,
    review: summary.review,
  };

  function chooseWorld(nextWorldId: string) {
    setWorldId(nextWorldId);
    setSelectedId(null);
    setExpandedTaskId(null);
    setFilter('all');
    setProofOpen(false);
    setActiveFamily(null);
    setWorldMenuOpen(false);
  }

  function selectTask(taskId: string) {
    if (!taskId) return;
    setSelectedId(taskId);
    setExpandedTaskId(taskId);
  }

  function toggleTaskCard(taskId: string) {
    if (!taskId) return;
    setSelectedId(taskId);
    setExpandedTaskId(current => current === taskId ? null : taskId);
  }

  return (
    <>
      <div className="scroll-progress" style={{ width: `${scrollProgress}%` }} />
      <TopChrome
        world={world}
        worlds={worlds}
        sourceStatus={sourceStatus}
        darkMode={darkMode}
        worldMenuOpen={worldMenuOpen}
        onToggleWorldMenu={() => setWorldMenuOpen(open => !open)}
        onToggleTheme={() => setDarkMode(value => !value)}
        onSelectWorld={chooseWorld}
      />

      <main className="product-shell">
        <VerdictHero world={world} selected={selected} onOpenProof={() => setProofOpen(true)} />
        <section className="story-nav-surface surf-2" aria-label="Choose task scene">
          <div className="story-header compact">
            <span className="story-number">02</span>
            <div>
              <p className="surface-kicker">Task rail</p>
              <strong>Choose the scene</strong>
            </div>
          </div>
          <TaskRail tasks={world.tasks} selectedId={selectedTask.id} onSelect={selectTask} />
        </section>

        <div className="story-grid">
          <TrajectorySurface selected={selected} />
          <GateSurface selected={selected} />
        </div>

        <section className="lens-surface surf-2" aria-label="Task view">
          <div className="story-header compact">
            <span className="story-number">05</span>
            <div>
              <p className="surface-kicker">Task index</p>
              <strong>{filter === 'all' ? 'All tasks' : statusLabels[filter as Stage]}</strong>
            </div>
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

        <TaskList
          tasks={visibleTasks}
          selectedId={expandedTaskId}
          onSelect={toggleTaskCard}
          onOpenProof={() => setProofOpen(true)}
        />

        <SignalGroups
          tasks={world.tasks}
          activeFamily={activeFamily}
          onToggleFamily={family => setActiveFamily(value => value === family ? null : family)}
          onSelectTask={selectTask}
        />

        <section className="journey-surface surf" aria-label="World path">
          <div className="story-header">
            <span className="story-number">08</span>
            <div>
              <p className="surface-kicker">Build path</p>
              <strong>From idea to files</strong>
            </div>
          </div>
          <JourneyTimeline items={journey} />
        </section>
      </main>

      <ProofSheet
        open={proofOpen}
        task={selectedTask}
        documents={taskDocuments}
        activeDocId={activeDocId}
        onSelectDoc={setActiveDocId}
        onClose={() => setProofOpen(false)}
      />
    </>
  );
}
