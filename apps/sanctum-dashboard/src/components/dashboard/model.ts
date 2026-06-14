import type { Task, World } from '@/lib/sanctum-data';
import type { TaskDocumentRow } from '@/lib/database';
import type { DisplayDocument, Readiness, ReadinessGate, SelectedTaskState } from './types';

export function meanOf(tasks: Task[]) {
  const scored = tasks.filter(task => typeof task.mean === 'number');
  if (!scored.length) return null;
  return Number((scored.reduce((sum, task) => sum + (task.mean ?? 0), 0) / scored.length).toFixed(1));
}

export function criticalRunIndexes(task: Task) {
  if (task.criticalRuns?.length) return task.criticalRuns;
  return (task.spread ?? [])
    .map((score, index) => score <= 40 ? index : -1)
    .filter(index => index >= 0);
}

export function counts(task: Task) {
  const spread = task.spread ?? [];
  const criticalRuns = criticalRunIndexes(task);
  return {
    catchers: spread.filter(score => score >= 85).length,
    floors: criticalRuns.length,
    sub70: spread.filter(score => score < 70).length,
  };
}

export function proofRunIndex(task: Task) {
  const criticalRuns = criticalRunIndexes(task);
  if (criticalRuns.length) return criticalRuns[0];
  if (!task.spread.length) return -1;
  return task.spread.reduce((lowestIndex, score, index) => score < task.spread[lowestIndex] ? index : lowestIndex, 0);
}

export function readinessFor(task: Task): Readiness {
  if (task.stage === 'planned') return { label: 'Not built', tone: 'planned' };
  if (task.stage === 'built') return { label: 'Built', tone: 'built' };
  if (task.stage === 'review') return { label: 'Needs review', tone: 'review' };
  if (task.stage === 'delivered') return { label: 'Delivered', tone: 'delivered' };
  if (task.reach === 'watch' || task.reach === 'open') return { label: 'Ready with watch', tone: 'watch' };
  return { label: 'Ready', tone: 'ready' };
}

export function reachLabel(task: Task) {
  if (task.reach === 'proven') return 'Proven';
  if (task.reach === 'watch') return 'Watch';
  if (task.reach === 'open') return 'Open';
  return 'Pending';
}

export function readinessGates(task: Task): ReadinessGate[] {
  const taskCounts = counts(task);
  const built = task.stage !== 'planned';
  const scored = task.spread.length > 0;
  const proofComplete = task.stage === 'delivered' || task.stage === 'ready';
  return [
    {
      icon: 'alert-triangle',
      label: 'Clinical miss',
      value: scored ? `${taskCounts.floors}/${task.runsTotal}` : 'Pending',
      state: taskCounts.floors > 0 ? 'pass' : scored ? 'watch' : 'pending',
    },
    {
      icon: 'shield',
      label: 'Fairness',
      value: built ? 'Clean' : 'Pending',
      state: built ? 'pass' : 'pending',
    },
    {
      icon: 'eye',
      label: 'Reach',
      value: reachLabel(task),
      state: task.reach === 'proven' ? 'pass' : task.reach === 'notstarted' ? 'pending' : 'watch',
    },
    {
      icon: 'file-check',
      label: 'Proof',
      value: proofComplete ? 'Complete' : 'Pending',
      state: proofComplete ? 'pass' : 'pending',
    },
  ];
}

export function selectedTaskState(task: Task): SelectedTaskState {
  return {
    task,
    readiness: readinessFor(task),
    gates: readinessGates(task),
    criticalRuns: criticalRunIndexes(task),
    proofRunIndex: proofRunIndex(task),
    counts: counts(task),
  };
}

export function defaultTaskFor(world: World) {
  const weakestReady = world.tasks.find(task => task.stage === 'ready' && (task.reach === 'watch' || task.reach === 'open'));
  if (weakestReady) return weakestReady;
  const ready = world.tasks.find(task => task.stage === 'ready');
  if (ready) return ready;
  const scored = world.tasks.filter(task => typeof task.mean === 'number');
  if (scored.length) {
    return scored.reduce((lowest, task) => (task.mean ?? 100) < (lowest.mean ?? 100) ? task : lowest, scored[0]);
  }
  return world.tasks[0];
}

export function scoreText(task: Task) {
  return typeof task.mean === 'number' ? String(task.mean) : 'TBD';
}

export function runState(task: Task, index: number) {
  const value = task.spread[index];
  if (criticalRunIndexes(task).includes(index)) return 'critical';
  if (typeof value !== 'number') return 'pending';
  if (value >= 85) return 'safe';
  if (value < 70) return 'weak';
  return 'middle';
}

export function statusClass(stage: string) {
  return `status-pill ${stage}`;
}

export function families(tasks: Task[]) {
  const byFamily = new Map<string, Task[]>();
  for (const task of tasks) {
    const list = byFamily.get(task.family) ?? [];
    list.push(task);
    byFamily.set(task.family, list);
  }
  return Array.from(byFamily.entries()).map(([family, list]) => {
    const scored = list.filter(task => typeof task.mean === 'number');
    const mean = scored.length ? meanOf(scored) : null;
    const floorCount = list.reduce((sum, task) => sum + counts(task).floors, 0);
    return { family, tasks: list, mean, floorCount };
  });
}

export function roleLabel(role: string) {
  const labels: Record<string, string> = {
    prompt: 'Task ask',
    task_file: 'Source file',
    golden: 'Reference answer',
    grader: 'Review guide',
    run_instructions: 'Run note',
  };
  return labels[role] ?? 'Source file';
}

export function roleTone(role: string) {
  if (role === 'prompt') return 'blue';
  if (role === 'task_file') return 'green';
  if (role === 'golden') return 'amber';
  if (role === 'grader') return 'purple';
  return 'gray';
}

export function sourceCue(name: string) {
  const lower = name.toLowerCase();
  if (lower.includes('photo') || lower.endsWith('.png') || lower.endsWith('.jpg')) return 'Visual evidence';
  if (lower.includes('signout')) return 'Covering note';
  if (lower.includes('handoff')) return 'External handoff';
  if (lower.includes('query')) return 'Documentation query';
  if (lower.includes('coding') || lower.includes('him')) return 'Coding worksheet';
  if (lower.includes('draft') || lower.includes('started')) return 'Started document';
  return 'Supporting file';
}

export function sourceName(doc: DisplayDocument) {
  if (doc.role === 'prompt') return 'Task ask';
  if (doc.role === 'golden') return 'Reference answer';
  if (doc.role === 'grader') return 'Review guide';
  if (doc.role === 'run_instructions') return 'Run note';
  return sourceCue(doc.filename);
}

export function formatBytes(value: number | null) {
  if (!value) return 'No preview';
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${Math.round(value / 102.4) / 10} KB`;
  return `${Math.round(value / 1024 / 102.4) / 10} MB`;
}

export function fallbackDocuments(worldId: string, task: Task): DisplayDocument[] {
  return [
    {
      id: `${task.id}:prompt:fallback`,
      worldId,
      taskId: task.id,
      role: 'prompt',
      filename: task.packet.prompt,
      relativePath: '',
      mimeType: 'text/plain',
      sha256: null,
      byteSize: null,
      contentText: 'Task ask preview pending.',
      contentBase64: null,
      uploaded: false,
    },
    ...task.packet.files.map((file, index) => ({
      id: `${task.id}:task_file:${index}:fallback`,
      worldId,
      taskId: task.id,
      role: 'task_file',
      filename: file,
      relativePath: '',
      mimeType: 'application/octet-stream',
      sha256: null,
      byteSize: null,
      contentText: `${sourceCue(file)}. Preview pending.`,
      contentBase64: null,
      uploaded: false,
    })),
    {
      id: `${task.id}:golden:fallback`,
      worldId,
      taskId: task.id,
      role: 'golden',
      filename: task.packet.golden,
      relativePath: '',
      mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      sha256: null,
      byteSize: null,
      contentText: 'Reference answer preview pending.',
      contentBase64: null,
      uploaded: false,
    },
    {
      id: `${task.id}:grader:fallback`,
      worldId,
      taskId: task.id,
      role: 'grader',
      filename: task.packet.grader,
      relativePath: '',
      mimeType: 'text/plain',
      sha256: null,
      byteSize: null,
      contentText: 'Review guide preview pending.',
      contentBase64: null,
      uploaded: false,
    },
  ];
}

export function uploadedDocuments(documents: TaskDocumentRow[], worldId: string, taskId: string): DisplayDocument[] {
  return documents
    .filter(doc => doc.worldId === worldId && doc.taskId === taskId)
    .filter(doc => doc.role !== 'run_instructions')
    .map(doc => ({
      ...doc,
      sha256: doc.sha256,
      byteSize: doc.byteSize,
      uploaded: true,
    }));
}
