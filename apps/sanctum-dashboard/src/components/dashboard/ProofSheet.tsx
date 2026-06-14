import type { ReactNode } from 'react';
import type { Task } from '@/lib/sanctum-data';
import { statusLabels } from '@/lib/sanctum-data';
import type { DisplayDocument } from './types';
import { formatBytes, roleLabel, roleTone, sourceName, statusClass } from './model';
import { Icon } from './Icon';

type Props = {
  open: boolean;
  task: Task;
  documents: DisplayDocument[];
  activeDocId: string | null;
  onSelectDoc: (docId: string) => void;
  onClose: () => void;
};

function previewText(doc: DisplayDocument) {
  if (doc.contentText) return doc.contentText;
  if (doc.contentBase64) return 'Image ready.';
  if (doc.uploaded) return 'No preview for this file type.';
  return 'Preview pending.';
}

function isMarkdown(doc: DisplayDocument) {
  return doc.mimeType === 'text/markdown' || doc.filename.toLowerCase().endsWith('.md');
}

function cleanInlineMarkdown(value: string) {
  return value
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/__([^_]+)__/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_([^_]+)_/g, '$1')
    .trim();
}

function renderTextPreview(text: string, markdown: boolean) {
  const lines = text.split('\n');
  const nodes: ReactNode[] = [];
  let codeLines: string[] = [];
  let inCode = false;

  function flushCode(key: string) {
    if (!codeLines.length) return;
    nodes.push(<pre className="md-code" key={key}>{codeLines.join('\n')}</pre>);
    codeLines = [];
  }

  lines.forEach((line, index) => {
    const trimmed = line.trim();

    if (markdown && trimmed.startsWith('```')) {
      if (inCode) flushCode(`code-${index}`);
      inCode = !inCode;
      return;
    }

    if (inCode) {
      codeLines.push(line);
      return;
    }

    if (!trimmed) return;

    if (markdown) {
      const heading = trimmed.match(/^(#{1,6})\s+(.+)$/);
      if (heading) {
        nodes.push(<h4 key={index}>{cleanInlineMarkdown(heading[2])}</h4>);
        return;
      }

      const bullet = trimmed.match(/^[-*+]\s+(.+)$/);
      if (bullet) {
        nodes.push(<p className="md-list" key={index}>{cleanInlineMarkdown(bullet[1])}</p>);
        return;
      }

      const numbered = trimmed.match(/^\d+[.)]\s+(.+)$/);
      if (numbered) {
        nodes.push(<p className="md-number" key={index}>{cleanInlineMarkdown(numbered[1])}</p>);
        return;
      }

      const quote = trimmed.match(/^>\s+(.+)$/);
      if (quote) {
        nodes.push(<blockquote key={index}>{cleanInlineMarkdown(quote[1])}</blockquote>);
        return;
      }
    }

    nodes.push(<p key={index}>{markdown ? cleanInlineMarkdown(trimmed) : trimmed}</p>);
  });

  flushCode('code-final');

  return <div className={markdown ? 'markdown-preview document-copy' : 'document-copy'}>{nodes}</div>;
}

function renderDocumentPreview(doc: DisplayDocument) {
  return renderTextPreview(previewText(doc), isMarkdown(doc));
}

export function ProofSheet({ open, task, documents, activeDocId, onSelectDoc, onClose }: Props) {
  if (!open) return null;

  const activeDoc = documents.find(doc => doc.id === activeDocId) ?? documents[0];

  return (
    <div className="modal-root" role="presentation">
      <button type="button" className="modal-backdrop" aria-label="Dismiss materials" onClick={onClose} />
      <section className="materials-modal surf" role="dialog" aria-modal="true" aria-label={`${task.id} materials`}>
        <div className="focus-head">
          <div>
            <p className="micro-label">{task.id} proof</p>
            <h2>{task.name}</h2>
          </div>
          <div className="modal-actions">
            <span className={statusClass(task.stage)}>{statusLabels[task.stage]}</span>
            <button type="button" className="close-button" aria-label="Close materials" onClick={onClose}>
              Close
              <Icon name="x" />
            </button>
          </div>
        </div>

        <div className="proof-sheet-grid">
          <div className="doc-tabs" aria-label="Task source files">
            {documents.map(doc => (
              <button
                key={doc.id}
                type="button"
                className={activeDoc?.id === doc.id ? 'active' : ''}
                onClick={() => onSelectDoc(doc.id)}
              >
                <span className={`role-dot ${roleTone(doc.role)}`} />
                <strong>{roleLabel(doc.role)}</strong>
                {sourceName(doc) !== roleLabel(doc.role) ? <small>{sourceName(doc)}</small> : null}
              </button>
            ))}
          </div>

          {activeDoc && (
            <article className="doc-preview">
              <header>
                <div>
                  <span className="micro-label">{roleLabel(activeDoc.role)}</span>
                  <strong>{sourceName(activeDoc)}</strong>
                </div>
                <span>{formatBytes(activeDoc.byteSize)}</span>
              </header>

              {activeDoc.contentBase64 ? (
                <img src={`data:${activeDoc.mimeType};base64,${activeDoc.contentBase64}`} alt={`${sourceName(activeDoc)} preview`} />
              ) : (
                renderDocumentPreview(activeDoc)
              )}

              <footer>
                <span>{activeDoc.uploaded ? 'Ready' : 'Pending'}</span>
                <span>{activeDoc.sha256 ? 'Checked' : 'Unchecked'}</span>
              </footer>
            </article>
          )}
        </div>
      </section>
    </div>
  );
}
