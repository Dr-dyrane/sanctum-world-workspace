import type { Task } from '@/lib/sanctum-data';
import { statusLabels } from '@/lib/sanctum-data';

type Props = {
  tasks: Task[];
  selectedId: string;
  onSelect: (taskId: string) => void;
};

export function TaskRail({ tasks, selectedId, onSelect }: Props) {
  return (
    <nav className="task-rail" aria-label="Task picker">
      {tasks.map(task => (
        <button
          key={task.id}
          type="button"
          className={`rail-item ${task.stage} ${selectedId === task.id ? 'active' : ''}`}
          aria-label={`${task.id}. ${task.name}. ${statusLabels[task.stage]}.`}
          aria-current={selectedId === task.id ? 'true' : undefined}
          onClick={() => onSelect(task.id)}
        >
          <span>{task.id}</span>
        </button>
      ))}
    </nav>
  );
}
