import type { World } from '@/lib/sanctum-data';
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

  return (
    <section className={`verdict-hero surf ${selected.readiness.tone}`} aria-label="Task readiness verdict">
      <div className="hero-meta-row">
        <div>
          <p className="micro-label">{world.title}</p>
          <span>Task readiness</span>
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

        <aside className="score-squircle" aria-label={`${task.id} mean score`}>
          <div className="score-meter" aria-hidden="true">
            <span style={{ transform: `scaleX(${typeof task.mean === 'number' ? task.mean / 100 : 0})` }} />
          </div>
          <span>Mean</span>
          <strong>{scoreText(task)}</strong>
          <p>{task.name}</p>
        </aside>
      </div>
    </section>
  );
}
