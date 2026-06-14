import type { Task } from '@/lib/sanctum-data';
import { families } from './model';

type Props = {
  tasks: Task[];
  activeFamily: string | null;
  onToggleFamily: (family: string) => void;
  onSelectTask: (taskId: string) => void;
};

export function SignalGroups({ tasks, activeFamily, onToggleFamily, onSelectTask }: Props) {
  const signals = families(tasks);
  const active = signals.find(signal => signal.family === activeFamily) ?? null;

  return (
    <section className="quiet-surface surf" aria-label="Challenge groups">
      <div className="surface-kicker">Challenge groups</div>
      <h2>Where tasks break</h2>
      <div className="signal-grid">
        {signals.map(signal => (
          <button
            key={signal.family}
            type="button"
            className={`signal-tile ${activeFamily === signal.family ? 'active' : ''}`}
            onClick={() => onToggleFamily(signal.family)}
          >
            <span>{signal.family}</span>
            <strong>{signal.mean ?? 'TBD'}</strong>
            <small>{signal.floorCount} misses</small>
          </button>
        ))}
      </div>

      {active ? (
        <div className="signal-drawer">
          <span>{active.tasks.map(task => task.id).join(', ')}</span>
          <button type="button" className="quiet-link" onClick={() => onSelectTask(active.tasks[0]?.id ?? '')}>
            View first task
          </button>
        </div>
      ) : null}
    </section>
  );
}
