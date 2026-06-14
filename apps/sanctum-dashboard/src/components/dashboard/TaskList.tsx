import type { Task } from '@/lib/sanctum-data';
import { statusLabels } from '@/lib/sanctum-data';
import { counts, scoreText, statusClass } from './model';
import { Icon } from './Icon';

type Props = {
  tasks: Task[];
  selectedId: string;
  onSelect: (taskId: string) => void;
  onOpenProof: () => void;
};

export function TaskList({ tasks, selectedId, onSelect, onOpenProof }: Props) {
  return (
    <section className="task-list-surface" aria-label="Task list">
      <div className="story-header task-list-header">
        <span className="story-number">06</span>
        <div>
          <p className="surface-kicker">Task cards</p>
          <strong>Open one proof</strong>
        </div>
      </div>
      {tasks.map(task => {
        const taskCounts = counts(task);
        const selected = selectedId === task.id;

        return (
          <article
            id={`task-${task.id}`}
            key={task.id}
            className={`simple-task-card surf ${task.stage} ${selected ? 'selected' : ''}`}
          >
            <button
              type="button"
              className="simple-task-button"
              aria-expanded={selected}
              onClick={() => onSelect(task.id)}
            >
              <div className="simple-task-main">
                <span className="task-token">{task.id}</span>
                <span className={statusClass(task.stage)}>{statusLabels[task.stage]}</span>
                <h3>{task.name}</h3>
                <small>{task.family}</small>
              </div>
              <span className="task-action-stack">
                <span className="task-score">
                  <strong>{scoreText(task)}</strong>
                  <span>Mean</span>
                </span>
                <span className="task-open-cue">
                  <span>{selected ? 'Viewing' : 'Open'}</span>
                  <Icon name={selected ? 'chevron-down' : 'arrow-right'} />
                </span>
              </span>
            </button>

            {selected ? (
              <div className="simple-task-detail">
                <span>{taskCounts.floors} critical</span>
                <span>{taskCounts.sub70}/{task.runsTotal} under 70</span>
                <span>{taskCounts.catchers} safe</span>
                <button type="button" className="inline-action compact" onClick={onOpenProof}>
                  Proof
                  <Icon name="folder-open" />
                </button>
              </div>
            ) : null}
          </article>
        );
      })}
    </section>
  );
}
