import type { SelectedTaskState } from './types';
import type { CSSProperties } from 'react';
import { Icon } from './Icon';
import { runState } from './model';
import type { IconName } from './types';

type Props = {
  selected: SelectedTaskState;
};

export function TrajectorySurface({ selected }: Props) {
  const task = selected.task;
  const proofScore = selected.proofRunIndex >= 0 ? task.spread[selected.proofRunIndex] : null;

  const stateLabel = (state: string) => {
    if (state === 'critical') return 'Clinical miss';
    if (state === 'weak') return 'Under 70';
    if (state === 'safe') return 'Safe run';
    if (state === 'middle') return 'Borderline';
    return 'Pending';
  };

  const stateIcon = (state: string): IconName => {
    if (state === 'critical') return 'alert-triangle';
    if (state === 'safe') return 'shield';
    if (state === 'middle') return 'eye';
    if (state === 'weak') return 'activity';
    return 'x';
  };

  return (
    <section className="story-surface trajectory-surface surf" aria-label="Trajectory score shape">
      <div className="story-header">
        <span className="story-number">03</span>
        <div>
          <p className="surface-kicker">Score shape</p>
          <strong>Where the miss appears</strong>
        </div>
      </div>
      <div className="trajectory-hero">
        <div>
          <h2>{selected.counts.floors} miss{selected.counts.floors === 1 ? '' : 'es'}</h2>
          <p>{selected.counts.sub70}/{task.runsTotal} runs under 70</p>
        </div>
        <div className="proof-run-callout">
          <span>Proof run</span>
          <strong>{proofScore ?? '-'}</strong>
        </div>
      </div>

      <div className="score-skyline" role="list" aria-label={`${task.id} trajectory scores`}>
        <span className="score-threshold" aria-hidden="true">70</span>
        {Array.from({ length: task.runsTotal }).map((_, index) => {
          const value = task.spread[index];
          const state = runState(task, index);
          const proof = index === selected.proofRunIndex;
          const height = typeof value === 'number' ? `${Math.max(6, Math.min(100, value))}%` : '6%';

          return (
            <span
              key={`${task.id}-${index}`}
              role="listitem"
              tabIndex={0}
              className={`score-bar ${state} ${proof ? 'proof' : ''}`}
              style={{ '--i': index, '--score': height } as CSSProperties}
              aria-label={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
              title={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
            >
              <span className="bar-track" aria-hidden="true">
                <i />
              </span>
              <span className="run-state-icon" aria-hidden="true">
                <Icon name={stateIcon(state)} />
              </span>
              <span className="bar-caption" aria-hidden="true">
                <small>Run {index + 1}</small>
                <strong>{typeof value === 'number' ? value : '-'}</strong>
                <span>{stateLabel(state)}</span>
              </span>
            </span>
          );
        })}
      </div>
    </section>
  );
}
