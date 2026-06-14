import type { CSSProperties } from 'react';
import type { journey } from '@/lib/sanctum-data';
import { Icon } from './Icon';
import type { IconName } from './types';

type JourneyItem = (typeof journey)[number];

type Props = {
  items: JourneyItem[];
};

const icons: IconName[] = [
  'activity',
  'shield',
  'eye',
  'folder-open',
  'file-check',
  'alert-triangle',
  'download',
];

export function JourneyTimeline({ items }: Props) {
  return (
    <ol className="journey-timeline" aria-label="World build timeline">
      {items.map((item, index) => (
        <li
          key={item.label}
          className={`journey-step ${item.status} ${index % 2 === 0 ? 'rise' : 'dip'}`}
          style={{ '--step-index': index } as CSSProperties}
        >
          <span className="journey-node">
            <Icon name={icons[index % icons.length]} />
          </span>
          <span className="journey-copy">
            <small>{String(index + 1).padStart(2, '0')}</small>
            <strong>{item.label}</strong>
            <span>{item.detail}</span>
          </span>
        </li>
      ))}
    </ol>
  );
}
