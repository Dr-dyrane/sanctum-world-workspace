import type { Stage, Task } from '@/lib/sanctum-data';
import { statusLabels } from '@/lib/sanctum-data';
import { counts, scoreText } from './model';
import { Icon } from './Icon';
import type { IconName } from './types';

type Props = {
  tasks: Task[];
  selectedId: string | null;
  onSelect: (taskId: string) => void;
  onOpenProof: () => void;
};

const stageIcons: Record<Stage, IconName> = {
  delivered: 'file-check',
  ready: 'shield',
  built: 'folder-open',
  review: 'alert-triangle',
  planned: 'activity',
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
              aria-label={`${selected ? 'Close' : 'Inspect'} ${task.id}. ${task.name}. ${statusLabels[task.stage]}.`}
              onClick={() => onSelect(task.id)}
            >
              <div className="simple-task-main">
                <span className="task-token">{task.id}</span>
                <span className={`state-badge ${task.stage}`}>
                  <Icon name={stageIcons[task.stage]} />
                  {statusLabels[task.stage]}
                </span>
                <h3>{task.name}</h3>
                <small>{task.family}</small>
              </div>
              <span className="task-action-stack">
                <span className="task-score">
                  <strong>{scoreText(task)}</strong>
                  <span>Mean</span>
                </span>
                <span className="task-open-cue">
                  <span>{selected ? 'Close' : 'Inspect'}</span>
                  <Icon name={selected ? 'chevron-down' : 'arrow-right'} />
                </span>
              </span>
            </button>

            {selected ? (
              <div className="simple-task-detail">
                <span className="detail-metric critical">
                  <Icon name="alert-triangle" />
                  <span>
                    <strong>{taskCounts.floors}</strong>
                    <small>critical</small>
                  </span>
                </span>
                <span className="detail-metric weak">
                  <Icon name="activity" />
                  <span>
                    <strong>{taskCounts.sub70}/{task.runsTotal}</strong>
                    <small>under 70</small>
                  </span>
                </span>
                <span className="detail-metric safe">
                  <Icon name="shield" />
                  <span>
                    <strong>{taskCounts.catchers}</strong>
                    <small>safe</small>
                  </span>
                </span>
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
