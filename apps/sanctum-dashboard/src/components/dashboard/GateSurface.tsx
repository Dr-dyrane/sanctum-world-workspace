import type { SelectedTaskState } from './types';
import { Icon } from './Icon';

type Props = {
  selected: SelectedTaskState;
};

export function GateSurface({ selected }: Props) {
  return (
    <section className="story-surface gate-surface surf" aria-label="Readiness gates">
      <div className="surface-kicker">Pass logic</div>
      <h2>Why it can move</h2>
      <div className="gate-list">
        {selected.gates.map(gate => (
          <div key={gate.label} className={`gate-row ${gate.state}`}>
            <span className="gate-icon">
              <Icon name={gate.icon} />
            </span>
            <span>{gate.label}</span>
            <strong>{gate.value}</strong>
          </div>
        ))}
      </div>
    </section>
  );
}
