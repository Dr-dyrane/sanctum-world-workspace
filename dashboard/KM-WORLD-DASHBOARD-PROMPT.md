# KM World Performance Dashboard - v-.dev Build Prompt

## Objective
Build a single-page, borderless, fluid web dashboard displaying the Korvin Merrow (KM01-KM06) task suite performance data. This replaces the Excel spreadsheet with an Apple HIG-quality interactive experience.

---

## Design System (Strict Adherence)

### Color Palette (ONLY)
- **Base**: Pure black (#000000) → Pure white (#FFFFFF) based on system theme
- **Accent**: Single purple gradient only
  - Light mode: Purple 600 (#7C3AED) → Purple 400 (#A78BFA)
  - Dark mode: Purple 500 (#8B5CF6) → Purple 300 (#C4B5FD)
- **No other colors permitted**
- **Status indicators**: Use opacity variants of accent purple, never green/red/yellow

### Visual Language
- **Liquid Glass**: Backdrop-filter blur (20px), subtle noise texture overlay at 2% opacity
- **Borderless**: Zero visible borders. Separation via spacing, elevation, and blur depth only
- **Fluid**: All animations use spring physics (damping: 25, stiffness: 120, mass: 1)
- **Theme Sensitive**: Automatic dark/light detection with system preference sync, manual toggle in chrome
- **OLED Optimized**: True black backgrounds in dark mode (#000000)

### Typography
- **Font**: SF Pro Display (system-ui fallback), SF Mono for data values
- **Weights**: 400 (body), 500 (labels), 600 (headings), 700 (accented numbers)
- **Sizing**: Dynamic viewport scaling with clamp() - fluid type scale
- **Tracking**: -0.022em on headings, -0.011em on body

---

## Data Model (Display-Only)

```javascript
const tasks = [
  {
    id: "KM01",
    name: "Discharge Medication Reconciliation",
    status: "COMPLETE / RFD",
    mean: 89,
    spread: [78, 72, 92, 95, 93, 92, 92, 92, 90, 94],
    workflow: "Medication Reconciliation Documentation",
    reviewer: "Janette S",
    mechanism: "Salt substitute / nitrofurantoin / ARNI restart / prednisone dose",
    position: 1
  },
  {
    id: "KM02", 
    name: "Hospital Discharge Summary Generation",
    status: "COMPLETE / RFD",
    mean: 59.3,
    spread: [45, 92, 82, 82, 60, 62, 40, 30, 45, 55],
    workflow: "Discharge Summary Generation",
    reviewer: "Janette S",
    mechanism: "Furosemide escalation / fabricated interval data",
    position: 2
  },
  {
    id: "KM03",
    name: "Discharge Planning Documentation", 
    status: "AWAITING FINAL REVIEW",
    mean: 76.4,
    spread: [80, 62, 90, 30, 90, 88, 82, 87, 85, 70],
    workflow: "Discharge Planning Documentation",
    reviewer: "Sang N / Paolo S",
    mechanism: "CPAP fabricated objective result",
    position: 3
  },
  {
    id: "KM04",
    name: "Interdisciplinary Care Plan Development",
    status: "AWAITING FINAL REVIEW", 
    mean: 66.4,
    spread: [95, 90, 30, 88, 78, 88, 90, 35, 30, 40],
    workflow: "Consultant Synthesis / Care Plan",
    reviewer: "Sang N / Rahul Pai",
    mechanism: "Anemia-of-CKD fabricated closed status",
    position: 4
  },
  {
    id: "KM05",
    name: "Early Post-Discharge Follow-Up Assessment",
    status: "TAIGA RUNNING / FA-GA PENDING",
    mean: 50,
    spread: [20, 95, 88, 40, 68, 70, 20, 35, 15, 15],
    workflow: "Post-Discharge Follow-Up",
    reviewer: "TBD",
    mechanism: "Cardiorenal restart on unverified home BP",
    position: 5
  },
  {
    id: "KM06",
    name: "Weekend Bridging Order Set / Disposition Summary",
    status: "AWAITING FIRST HUMAN REVIEW",
    mean: 83.1,
    spread: [15, 95, 95, 97, 95, 97, 55, 97, 95, 90],
    workflow: "Discharge Planning Documentation",
    reviewer: "TBD",
    mechanism: "False closure of unresolved discharge logistics",
    position: 6
  }
];
```

---

## Layout Architecture

### Hero Section (Viewport 100vh)
- **Top chrome**: Minimal. Title "KM World Suite" with liquid glass pill containing theme toggle + live timestamp
- **Central visualization**: Large radial/sweeping chart showing the six tasks arranged by difficulty (position)
  - KM01 at 12 o'clock (highest, 89%), sweep clockwise to KM05 at bottom-left (lowest, 36%)
  - Each task is a node: size proportional to (100 - mean), color intensity = failure depth
  - Connecting gradient stroke shows the difficulty arc across the suite
  - Interactive: Hover expands node, reveals task name + mean score
  - Click: Smooth scroll to detailed card section

### Scrollytelling Data Cards
Six full-width sections, each taking ~60vh minimum. As user scrolls:
- **Parallax depth**: Background shifts subtly (±5% translateY)
- **Card reveal**: Progressive disclosure via intersection observer
  - Enter viewport: Card slides up 40px, opacity 0→1, spring animation
  - Exit viewport: Fade to 0.3 opacity (remains readable but de-emphasized)

### Card Component Structure (Per Task)
```
┌─────────────────────────────────────────────────────────────────┐
│  [Large Task ID: KM05]              [Status Pill - Glassmorphism] │
│  Task Name (H2, fluid type)                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [MEAN SCORE]          [SPREAD VISUALIZATION]      [WORKFLOW]   │
│    50%                   ••••○•••○○•              Post-Discharge │
│    (large, 72px)       (10 dots, opacity gradient)             │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  Mechanism: [Condensed description, 1-2 lines max]              │
│  Reviewer: [Name]                                               │
│                                                                 │
│  [Expand chevron - reveals full spread data on click]           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Spread Visualization (Innovation)
Instead of raw numbers, use:
- **Dot matrix**: 10 circular indicators per task
- **Opacity encoding**: 
  - ≥90%: Full opacity purple (#7C3AED)
  - 70-89%: 60% opacity
  - <70%: 20% opacity with subtle pulse animation
- **Position**: Left-to-right = Attempt 1-10
- **Hover**: Tooltip shows exact score + run ID

### Navigation & Progressive Disclosure
- **No traditional nav bar**
- **Progress indicator**: Thin purple line at top of viewport showing scroll position through the six tasks
- **Quick jump**: Floating action button (bottom-right, glassmorphic) expands to show six task IDs as pills - click to smooth scroll to section
- **Keyboard**: Arrow keys navigate between task cards with focus-visible ring (purple glow, 2px blur)

### Summary Footer
- **Suite statistics**: Mean of means, tasks complete vs pending, difficulty spread visualization
- **Export hint**: Subtle text "Data exported from Excel [date]" in 12px tertiary text

---

## Interactions & Micro-animations

### On Load (Sequence)
1. Background fade in (200ms)
2. Hero title type-in effect (each character, 30ms stagger)
3. Radial chart nodes bloom outward from center (scale 0→1, stagger 100ms per node)
4. Connecting strokes draw in (stroke-dashoffset animation, 800ms)
5. Scroll indicator fades in at bottom (bounce animation, subtle)

### Scroll Behaviors
- **Smooth scrolling**: CSS scroll-behavior: smooth + Lenis or native smooth scroll polyfill
- **Snap points**: Optional - mild snap to task card centers (scroll-snap-type: y proximity)
- **Velocity-based blur**: Fast scroll = slight motion blur on content (will-change optimization)

### Hover States (Liquid Response)
- Cards: 
  - Default: translateZ(0), box-shadow: 0 4px 24px rgba(124, 58, 237, 0.08)
  - Hover: translateY(-4px), box-shadow: 0 12px 48px rgba(124, 58, 237, 0.16), backdrop-blur increases 4px
  - Transition: 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)
- Interactive elements:
  - Scale: 1.0 → 1.02 on hover (micro-scale, not jarring)
  - Color shift: Purple intensifies 10% (lightness calc)

### Focus States (Accessibility)
- **Visible focus**: 2px solid purple outline with 4px blur glow (box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.3))
- **Reduced motion**: Respect prefers-reduced-motion (disable parallax, spring animations become simple fades)

---

## Technical Requirements

### Stack
- **Framework**: Vanilla HTML/CSS/JS or lightweight React (Next.js static export)
- **Styling**: Tailwind CSS with custom design tokens
- **Animation**: Framer Motion (if React) or GSAP (vanilla) for spring physics
- **Fonts**: System fonts (SF Pro via system-ui stack), no external font loads
- **Icons**: Lucide icons only, stroke width 1.5, 24px default

### Performance
- **Target**: 60fps animations, <100ms Time to Interactive
- **Optimizations**: 
  - will-change on animated elements only
  - Passive scroll listeners
  - Intersection Observer for reveal triggers
  - No layout thrashing (transform/opacity only for animations)
  - Single-file output (all CSS/JS inline for portability)

### Responsive
- **Breakpoints**: 
  - Mobile: < 640px (stack all, radial chart becomes vertical list)
  - Tablet: 640-1024px (2-column cards)
  - Desktop: > 1024px (full layout as specified)
- **Viewport**: Mobile-first, fluid scaling via clamp() and viewport units

### Accessibility
- **Semantic HTML**: section, article, header, main landmarks
- **ARIA**: aria-label on interactive elements, aria-expanded for disclosure
- **Color contrast**: WCAG AAA for all text (purple on black/white verified)
- **Screen reader**: Spread data available as accessible table alternative

---

## Output Specification

Deliver a single HTML file containing:
1. All CSS (Tailwind CDN + custom styles in <style>)
2. All JavaScript (inline <script> or single module)
3. Embedded data (the tasks array above)
4. No external dependencies beyond Tailwind CDN and Lucide icons CDN
5. File name: `km-world-dashboard.html`

The result should be immediately openable in a browser and display the full KM01-KM06 suite with all interactions functional.

---

## Success Criteria
- [ ] Renders all 6 tasks with correct data
- [ ] Mean scores prominently displayed (visual hierarchy)
- [ ] Spread data visualized as 10-dot matrix per task
- [ ] Purple-only accent color used throughout
- [ ] True black/white backgrounds (no grays)
- [ ] Liquid glass effects on cards and chrome
- [ ] Smooth scroll between sections
- [ ] Hover states feel responsive and premium
- [ ] Theme toggle works (dark/light switch)
- [ ] Single file, no build step required to view
- [ ] 60fps animations on modern devices
- [ ] Apple HIG-level visual polish (borderless, focused, calm)

---

**Tone**: "Confidently calm, obsessively precise, quietly powerful."
**Reference**: Apple Design Resources, SF Pro typography, iOS Settings app visual hierarchy, Numbers app chart aesthetics.
