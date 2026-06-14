import type { SelectedTaskState } from './types';
import type { CSSProperties } from 'react';
import { runState } from './model';

type Props = {
  selected: SelectedTaskState;
};

export function TrajectorySurface({ selected }: Props) {
  const task = selected.task;
  const proofScore = selected.proofRunIndex >= 0 ? task.spread[selected.proofRunIndex] : null;

  return (
    <section className="story-surface trajectory-surface surf" aria-label="Trajectory score shape">
      <div className="surface-kicker">Score shape</div>
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
              className={`score-bar ${state} ${proof ? 'proof' : ''}`}
              style={{ '--i': index, '--score': height } as CSSProperties}
              aria-label={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
              title={typeof value === 'number' ? `Run ${index + 1}: ${value}` : `Run ${index + 1}: pending`}
            >
              <i aria-hidden="true" />
              <small>{index + 1}</small>
              <strong>{typeof value === 'number' ? value : '-'}</strong>
            </span>
          );
        })}
      </div>
    </section>
  );
}
