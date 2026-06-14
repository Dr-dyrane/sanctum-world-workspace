'use client';

import { useEffect, useMemo, useState } from 'react';
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

function extensionFor(filename: string) {
  const index = filename.lastIndexOf('.');
  return index === -1 ? '' : filename.slice(index + 1).toLowerCase();
}

function isImage(doc: DisplayDocument) {
  return doc.mimeType.startsWith('image/');
}

function isDocx(doc: DisplayDocument) {
  return doc.mimeType === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    || extensionFor(doc.filename) === 'docx';
}

function isTextLike(doc: DisplayDocument) {
  const extension = extensionFor(doc.filename);
  return doc.mimeType.startsWith('text/') || extension === 'md' || extension === 'txt';
}

function decodeBase64ToText(value: string) {
  const binary = window.atob(value);
  const bytes = Uint8Array.from(binary, character => character.charCodeAt(0));
  return new TextDecoder('utf-8').decode(bytes);
}

function decodeBase64ToArrayBuffer(value: string) {
  const binary = window.atob(value);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  return bytes.buffer;
}

function downloadHref(doc: DisplayDocument) {
  if (doc.contentBase64) {
    return `data:${doc.mimeType || 'application/octet-stream'};base64,${doc.contentBase64}`;
  }

  if (doc.contentText) {
    return `data:text/plain;charset=utf-8,${encodeURIComponent(doc.contentText)}`;
  }

  return null;
}

function TextSourceView({ doc }: { doc: DisplayDocument }) {
  const text = useMemo(() => {
    if (doc.contentBase64) return decodeBase64ToText(doc.contentBase64);
    return doc.contentText ?? 'No preview available.';
  }, [doc.contentBase64, doc.contentText]);

  return (
    <pre className="source-text" aria-label={`${sourceName(doc)} source text`}>
      {text}
    </pre>
  );
}

function DocxSourceView({ doc }: { doc: DisplayDocument }) {
  const [html, setHtml] = useState('');
  const [state, setState] = useState<'loading' | 'ready' | 'fallback'>('loading');

  useEffect(() => {
    let active = true;
    setHtml('');
    setState(doc.contentBase64 ? 'loading' : 'fallback');

    if (!doc.contentBase64) return () => {
      active = false;
    };

    async function convert() {
      try {
        const mammoth = await import('mammoth');
        const result = await mammoth.convertToHtml(
          { arrayBuffer: decodeBase64ToArrayBuffer(doc.contentBase64 ?? '') },
          {
            styleMap: [
              "p[style-name='Title'] => h1:fresh",
              "p[style-name='Subtitle'] => h2:fresh",
              "p[style-name='Heading 1'] => h2:fresh",
              "p[style-name='Heading 2'] => h3:fresh",
              "p[style-name='Heading 3'] => h4:fresh",
            ],
          },
        );
        if (!active) return;
        setHtml(result.value);
        setState('ready');
      } catch {
        if (!active) return;
        setState('fallback');
      }
    }

    void convert();

    return () => {
      active = false;
    };
  }, [doc.contentBase64]);

  if (state === 'loading') {
    return <div className="render-state">Opening document.</div>;
  }

  if (state === 'fallback') {
    return <TextSourceView doc={doc} />;
  }

  return (
    <div
      className="word-preview"
      aria-label={`${sourceName(doc)} Word preview`}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}

function BinaryFileView({ doc }: { doc: DisplayDocument }) {
  return (
    <div className="render-state">
      <strong>{extensionFor(doc.filename).toUpperCase() || 'File'}</strong>
      <span>Preview unavailable.</span>
    </div>
  );
}

function SourceRenderer({ doc }: { doc: DisplayDocument }) {
  if (isImage(doc) && doc.contentBase64) {
    return <img src={`data:${doc.mimeType};base64,${doc.contentBase64}`} alt={`${sourceName(doc)} preview`} />;
  }

  if (isDocx(doc)) return <DocxSourceView doc={doc} />;
  if (isTextLike(doc)) return <TextSourceView doc={doc} />;

  return <BinaryFileView doc={doc} />;
}

export function ProofSheet({ open, task, documents, activeDocId, onSelectDoc, onClose }: Props) {
  if (!open) return null;

  const activeDoc = documents.find(doc => doc.id === activeDocId) ?? documents[0];
  const activeDownloadHref = activeDoc ? downloadHref(activeDoc) : null;

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
                <div className="doc-file-actions">
                  <span>{formatBytes(activeDoc.byteSize)}</span>
                  {activeDownloadHref ? (
                    <a className="download-link" href={activeDownloadHref} download={activeDoc.filename}>
                      Download
                      <Icon name="download" />
                    </a>
                  ) : null}
                </div>
              </header>

              <div className="doc-preview-frame">
                <SourceRenderer doc={activeDoc} />
              </div>

              <footer>
                <span>{activeDoc.contentBase64 ? 'Original file' : activeDoc.uploaded ? 'Text only' : 'Pending'}</span>
                <span>{activeDoc.sha256 ? 'Checked' : 'Unchecked'}</span>
              </footer>
            </article>
          )}
        </div>
      </section>
    </div>
  );
}
