import 'server-only';
import { neon } from '@neondatabase/serverless';

export function databaseIsConfigured() {
  return Boolean(process.env.DATABASE_URL);
}

export function getSql() {
  const url = process.env.DATABASE_URL;
  if (!url) return null;
  return neon(url);
}
