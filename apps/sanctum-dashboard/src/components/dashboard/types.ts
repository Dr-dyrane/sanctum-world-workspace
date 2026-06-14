import type { TaskDocumentRow } from '@/lib/database';
import type { Stage, Task, World } from '@/lib/sanctum-data';

export type DashboardProps = {
  worlds: World[];
  databaseConfigured: boolean;
  documents: TaskDocumentRow[];
};

export type DisplayDocument = {
  id: string;
  worldId: string;
  taskId: string;
  role: string;
  filename: string;
  relativePath: string;
  mimeType: string;
  sha256: string | null;
  byteSize: number | null;
  contentText: string | null;
  contentBase64: string | null;
  uploaded: boolean;
};

export type Filter = 'all' | Stage;

export type ReadinessTone = 'planned' | 'review' | 'delivered' | 'ready' | 'watch';

export type Readiness = {
  label: string;
  tone: ReadinessTone;
};

export type GateState = 'pass' | 'watch' | 'pending';

export type ReadinessGate = {
  icon: IconName;
  label: string;
  value: string;
  state: GateState;
};

export type IconName =
  | 'activity'
  | 'alert-triangle'
  | 'arrow-right'
  | 'chevron-down'
  | 'eye'
  | 'file-check'
  | 'folder-open'
  | 'moon'
  | 'shield'
  | 'sun'
  | 'x';

export type SelectedTaskState = {
  task: Task;
  readiness: Readiness;
  gates: ReadinessGate[];
  criticalRuns: number[];
  proofRunIndex: number;
  counts: {
    catchers: number;
    floors: number;
    sub70: number;
  };
};
