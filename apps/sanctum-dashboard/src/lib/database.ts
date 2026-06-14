import 'server-only';
import { neon } from '@neondatabase/serverless';

export type TaskDocumentRow = {
  id: string;
  worldId: string;
  taskId: string;
  role: string;
  filename: string;
  relativePath: string;
  mimeType: string;
  sha256: string;
  byteSize: number;
  contentText: string | null;
  contentBase64: string | null;
  updatedAt: string;
};

export function databaseIsConfigured() {
  return Boolean(process.env.DATABASE_URL);
}

export function getSql() {
  const url = process.env.DATABASE_URL;
  if (!url) return null;
  return neon(url);
}

export async function getTaskDocuments(): Promise<TaskDocumentRow[]> {
  const sql = getSql();
  if (!sql) return [];

  try {
    const rows = await sql`
      select
        id,
        world_id,
        task_id,
        role,
        filename,
        relative_path,
        mime_type,
        sha256,
        byte_size,
        content_text,
        content_base64,
        updated_at
      from sanctum_documents
      order by
        world_id,
        task_id,
        case role
          when 'prompt' then 1
          when 'task_file' then 2
          when 'golden' then 3
          when 'grader' then 4
          else 5
        end,
        filename
    `;

    return rows.map((row) => ({
      id: String(row.id),
      worldId: String(row.world_id),
      taskId: String(row.task_id),
      role: String(row.role),
      filename: String(row.filename),
      relativePath: String(row.relative_path),
      mimeType: String(row.mime_type),
      sha256: String(row.sha256),
      byteSize: Number(row.byte_size),
      contentText: row.content_text ? String(row.content_text) : null,
      contentBase64: row.content_base64 ? String(row.content_base64) : null,
      updatedAt: row.updated_at instanceof Date ? row.updated_at.toISOString() : String(row.updated_at),
    }));
  } catch {
    return [];
  }
}
