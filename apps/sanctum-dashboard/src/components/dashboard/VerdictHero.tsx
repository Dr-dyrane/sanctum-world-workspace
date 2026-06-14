import type { World } from '@/lib/sanctum-data';
import type { CSSProperties } from 'react';
import type { SelectedTaskState } from './types';
import { Icon } from './Icon';
import { scoreText, statusClass } from './model';

type Props = {
  world: World;
  selected: SelectedTaskState;
  onOpenProof: () => void;
};

export function VerdictHero({ world, selected, onOpenProof }: Props) {
  const task = selected.task;
  const scorePosition = typeof task.mean === 'number' ? `${Math.max(0, Math.min(100, task.mean))}%` : '0%';

  return (
    <section className={`verdict-hero surf ${selected.readiness.tone}`} aria-label="Task readiness verdict">
      <div className="hero-meta-row">
        <div className="story-header compact">
          <span className="story-number">01</span>
          <div>
            <p className="micro-label">{world.title}</p>
            <strong>Task readiness</strong>
          </div>
        </div>
        <span className={statusClass(selected.readiness.tone)}>{selected.readiness.label}</span>
      </div>

      <div className="hero-stage-grid">
        <div className="hero-verdict-copy">
          <span className="task-token">{task.id}</span>
          <h1>{selected.readiness.label}</h1>
          <p>{task.plain}</p>
          <div className="hero-actions">
            <button type="button" className="primary-cta" onClick={onOpenProof}>
              Open proof
              <Icon name="folder-open" />
            </button>
            <a className="quiet-link" href={`#task-${task.id}`}>View task</a>
          </div>
        </div>

        <aside className={`score-squircle ${selected.readiness.tone}`} aria-label={`${task.id} mean score`}>
          <div className="score-meter" style={{ '--score': scorePosition } as CSSProperties} aria-hidden="true">
            <span />
          </div>
          <div className="score-scale" aria-hidden="true">
            <span>0</span>
            <span>70</span>
            <span>100</span>
          </div>
          <span>Mean</span>
          <strong>{scoreText(task)}</strong>
          <p>{task.name}</p>
        </aside>
      </div>
    </section>
  );
}
