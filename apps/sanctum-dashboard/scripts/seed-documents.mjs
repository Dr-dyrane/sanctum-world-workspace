import { neon } from '@neondatabase/serverless';
import crypto from 'node:crypto';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import mammoth from 'mammoth';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(scriptDir, '..');
const repoRoot = path.resolve(appRoot, '../..');
const envPath = path.join(appRoot, '.env.local');
const platformRoot = path.join(repoRoot, 'worlds/korvin-merrow/task-setup/platform');

async function loadLocalEnv() {
  const raw = await fs.readFile(envPath, 'utf8');
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const separator = trimmed.indexOf('=');
    if (separator === -1) continue;
    const key = trimmed.slice(0, separator);
    const value = trimmed.slice(separator + 1);
    if (!process.env[key]) process.env[key] = value;
  }
}

function roleFor(filename) {
  const lower = filename.toLowerCase();
  if (lower.startsWith('prompt')) return 'prompt';
  if (lower.startsWith('golden')) return 'golden';
  if (lower.startsWith('grader')) return 'grader';
  if (lower.startsWith('run-instructions')) return 'run_instructions';
  return 'task_file';
}

function mimeFor(filename) {
  const lower = filename.toLowerCase();
  if (lower.endsWith('.docx')) return 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
  if (lower.endsWith('.txt')) return 'text/plain';
  if (lower.endsWith('.md')) return 'text/markdown';
  if (lower.endsWith('.png')) return 'image/png';
  if (lower.endsWith('.jpg') || lower.endsWith('.jpeg')) return 'image/jpeg';
  return 'application/octet-stream';
}

async function textFor(filename, buffer) {
  const lower = filename.toLowerCase();
  if (lower.endsWith('.txt') || lower.endsWith('.md')) return cleanText(buffer.toString('utf8'));
  if (lower.endsWith('.docx')) {
    const result = await mammoth.extractRawText({ buffer });
    return cleanText(result.value);
  }
  return null;
}

function base64For(filename, buffer) {
  const lower = filename.toLowerCase();
  if (!lower.endsWith('.png') && !lower.endsWith('.jpg') && !lower.endsWith('.jpeg')) return null;
  if (buffer.length > 3_000_000) return null;
  return buffer.toString('base64');
}

function cleanText(value) {
  return value
    .replace(/\u0000/g, '')
    .replace(/\r\n/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

async function currentTaskDirs() {
  const entries = await fs.readdir(platformRoot, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isDirectory() && /^task\d+$/.test(entry.name))
    .map((entry) => path.join(platformRoot, entry.name, 'current'))
    .sort((a, b) => {
      const numberA = Number(path.basename(path.dirname(a)).replace('task', ''));
      const numberB = Number(path.basename(path.dirname(b)).replace('task', ''));
      return numberA - numberB;
    });
}

async function collectDocuments() {
  const documents = [];
  for (const currentDir of await currentTaskDirs()) {
    const taskNumber = Number(path.basename(path.dirname(currentDir)).replace('task', ''));
    const taskId = `KM${String(taskNumber).padStart(2, '0')}`;
    const files = await fs.readdir(currentDir, { withFileTypes: true });

    for (const file of files) {
      if (!file.isFile()) continue;
      const absolutePath = path.join(currentDir, file.name);
      const relativePath = path.relative(repoRoot, absolutePath);
      const buffer = await fs.readFile(absolutePath);
      const sha256 = crypto.createHash('sha256').update(buffer).digest('hex');
      const role = roleFor(file.name);

      documents.push({
        id: `korvin-merrow:${taskId}:${role}:${file.name}`,
        worldId: 'korvin-merrow',
        taskId,
        role,
        filename: file.name,
        relativePath,
        mimeType: mimeFor(file.name),
        sha256,
        byteSize: buffer.length,
        contentText: await textFor(file.name, buffer),
        contentBase64: base64For(file.name, buffer),
      });
    }
  }
  return documents;
}

async function main() {
  await loadLocalEnv();
  const databaseUrl = process.env.DATABASE_URL;
  if (!databaseUrl) throw new Error('DATABASE_URL is not configured.');

  const sql = neon(databaseUrl);
  await sql`
    create table if not exists sanctum_documents (
      id text primary key,
      world_id text not null,
      task_id text not null,
      role text not null,
      filename text not null,
      relative_path text not null,
      mime_type text not null,
      sha256 text not null,
      byte_size integer not null,
      content_text text,
      content_base64 text,
      seeded_at timestamptz not null default now(),
      updated_at timestamptz not null default now()
    )
  `;
  await sql`alter table sanctum_documents add column if not exists content_base64 text`;
  await sql`create index if not exists sanctum_documents_world_task_idx on sanctum_documents (world_id, task_id, role)`;

  const documents = await collectDocuments();
  for (const doc of documents) {
    await sql`
      insert into sanctum_documents (
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
      )
      values (
        ${doc.id},
        ${doc.worldId},
        ${doc.taskId},
        ${doc.role},
        ${doc.filename},
        ${doc.relativePath},
        ${doc.mimeType},
        ${doc.sha256},
        ${doc.byteSize},
        ${doc.contentText},
        ${doc.contentBase64},
        now()
      )
      on conflict (id) do update set
        relative_path = excluded.relative_path,
        mime_type = excluded.mime_type,
        sha256 = excluded.sha256,
        byte_size = excluded.byte_size,
        content_text = excluded.content_text,
        content_base64 = excluded.content_base64,
        updated_at = now()
    `;
  }

  const [count] = await sql`select count(*)::int as total from sanctum_documents where world_id = 'korvin-merrow'`;
  console.log(`Seeded ${documents.length} current packet files. Neon now holds ${count.total} Korvin packet documents.`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
