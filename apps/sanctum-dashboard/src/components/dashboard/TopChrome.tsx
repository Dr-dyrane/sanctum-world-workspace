import Image from 'next/image';
import logo from '@/app/logo.png';
import type { World } from '@/lib/sanctum-data';
import { Icon } from './Icon';

type Props = {
  world: World;
  worlds: World[];
  sourceStatus: string;
  darkMode: boolean;
  worldMenuOpen: boolean;
  onToggleWorldMenu: () => void;
  onToggleTheme: () => void;
  onSelectWorld: (worldId: string) => void;
};

export function TopChrome({
  world,
  worlds,
  sourceStatus,
  darkMode,
  worldMenuOpen,
  onToggleWorldMenu,
  onToggleTheme,
  onSelectWorld,
}: Props) {
  return (
    <header className="top-chrome" aria-label="World navigation">
      <div className="chrome-bar">
        <Image src={logo} alt="Sanctum" className="logo-mark" width={28} height={28} priority />
        <strong>Sanctum</strong>
        <span className="chrome-separator" />
        <div className="world-menu-wrap">
          <button
            type="button"
            className="world-menu-button"
            aria-haspopup="menu"
            aria-expanded={worldMenuOpen}
            onClick={onToggleWorldMenu}
          >
            <span>{world.title}</span>
            <Icon name="chevron-down" className="menu-chevron" />
          </button>
        </div>
        <span className="chrome-separator" />
        <span className="chrome-stat">{sourceStatus}</span>
        <button
          type="button"
          className="theme-toggle"
          aria-label={darkMode ? 'Use light appearance' : 'Use dark appearance'}
          aria-pressed={darkMode}
          onClick={onToggleTheme}
        >
          <Icon name={darkMode ? 'moon' : 'sun'} />
        </button>
      </div>

      {worldMenuOpen ? (
        <div className="world-menu world-menu-popover surf" role="menu" aria-label="Switch world">
          {worlds.map(item => (
            <button
              key={item.id}
              type="button"
              role="menuitem"
              className={item.id === world.id ? 'active' : ''}
              onClick={() => onSelectWorld(item.id)}
            >
              <span>{item.title}</span>
              <small>{item.kicker}</small>
            </button>
          ))}
        </div>
      ) : null}
    </header>
  );
}
