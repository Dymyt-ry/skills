# Remotion Templates

Ready-to-use Remotion compositions for each reel type. Copy into your project's `src/` folder.

## Shared: Theme & Utilities

### src/theme.ts
```tsx
export const theme = {
  bg: '#0F1729',
  bgAlt: '#1a2332',
  accent: '#00D4AA',
  accentDim: 'rgba(0, 212, 170, 0.12)',
  text: '#F8F9FC',
  textMuted: '#8395a7',
  textSubtle: '#c8d6e5',
  warning: '#F5A623',
  danger: '#FF4757',
  success: '#2ED573',
} as const;

export const fonts = {
  heading: "'Inter', -apple-system, sans-serif",
  mono: "'JetBrains Mono', 'SF Mono', monospace",
  body: "'Inter', -apple-system, sans-serif",
} as const;

export const canvas = {
  width: 1080,
  height: 1920,
  fps: 30,
} as const;

export const safeZone = {
  top: 90,
  bottom: 290,
  left: 90,
  right: 90,
} as const;
```

### src/components/Background.tsx
```tsx
import { AbsoluteFill } from 'remotion';
import { theme } from '../theme';

export const Background: React.FC<{ variant?: 'solid' | 'glow' | 'dots' }> = ({ variant = 'solid' }) => {
  const styles: React.CSSProperties = {
    backgroundColor: theme.bg,
  };

  if (variant === 'glow') {
    styles.backgroundImage = `radial-gradient(ellipse at 50% 40%, rgba(0, 212, 170, 0.06) 0%, transparent 50%)`;
  }

  if (variant === 'dots') {
    styles.backgroundImage = `radial-gradient(rgba(200, 214, 229, 0.04) 1px, transparent 1px)`;
    styles.backgroundSize = '24px 24px';
  }

  return <AbsoluteFill style={styles} />;
};
```

### src/components/SafeArea.tsx
```tsx
import { safeZone } from '../theme';

export const SafeArea: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={{
    position: 'absolute',
    top: safeZone.top,
    left: safeZone.left,
    right: safeZone.right,
    bottom: safeZone.bottom,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
  }}>
    {children}
  </div>
);
```

---

## Template 1: Stat Reveal

```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { Background } from './components/Background';
import { SafeArea } from './components/SafeArea';
import { theme, fonts } from './theme';

interface StatRevealProps {
  label: string;      // e.g. "BURN RATE"
  value: string;      // e.g. "82%"
  context: string;    // e.g. "of SMBs fail due to cash flow"
}

export const StatReveal: React.FC<StatRevealProps> = ({ label, value, context }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const labelOpacity = interpolate(frame, [15, 30], [0, 1], { extrapolateRight: 'clamp' });
  const labelY = interpolate(frame, [15, 30], [20, 0], { extrapolateRight: 'clamp' });

  const numberScale = spring({ frame: frame - 30, fps, config: { damping: 12, stiffness: 100 } });
  const numberOpacity = interpolate(frame, [30, 35], [0, 1], { extrapolateRight: 'clamp' });

  const contextOpacity = interpolate(frame, [60, 80], [0, 1], { extrapolateRight: 'clamp' });
  const contextY = interpolate(frame, [60, 80], [30, 0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill>
      <Background variant="glow" />
      <SafeArea>
        <div style={{ textAlign: 'center' }}>
          <div style={{
            fontFamily: fonts.heading,
            fontSize: 20,
            fontWeight: 600,
            color: theme.textMuted,
            textTransform: 'uppercase',
            letterSpacing: '0.08em',
            opacity: labelOpacity,
            transform: `translateY(${labelY}px)`,
            marginBottom: 24,
          }}>
            {label}
          </div>

          <div style={{
            fontFamily: fonts.mono,
            fontSize: 160,
            fontWeight: 800,
            color: theme.accent,
            opacity: numberOpacity,
            transform: `scale(${numberScale})`,
            lineHeight: 1,
            marginBottom: 32,
          }}>
            {value}
          </div>

          <div style={{
            fontFamily: fonts.body,
            fontSize: 28,
            fontWeight: 400,
            color: theme.textSubtle,
            opacity: contextOpacity,
            transform: `translateY(${contextY}px)`,
            lineHeight: 1.5,
            maxWidth: 700,
            margin: '0 auto',
          }}>
            {context}
          </div>
        </div>
      </SafeArea>
    </AbsoluteFill>
  );
};
```

Register in `src/Root.tsx`:
```tsx
import { Composition } from 'remotion';
import { StatReveal } from './StatReveal';
import { canvas } from './theme';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="StatReveal"
      component={StatReveal}
      durationInFrames={canvas.fps * 6}
      fps={canvas.fps}
      width={canvas.width}
      height={canvas.height}
      defaultProps={{
        label: 'CASH FLOW',
        value: '82%',
        context: 'of small businesses in EU fail\ndue to poor cash flow management',
      }}
    />
  </>
);
```

---

## Template 2: Tips Reel (Multi-Step)

```tsx
import { AbsoluteFill, Sequence, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { Background } from './components/Background';
import { SafeArea } from './components/SafeArea';
import { theme, fonts } from './theme';

interface TipsReelProps {
  hook: string;
  steps: Array<{ title: string; description: string }>;
  cta: string;
}

const StepSlide: React.FC<{ index: number; title: string; description: string }> = ({ index, title, description }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const numberScale = spring({ frame, fps, config: { damping: 10, stiffness: 120 } });
  const textOpacity = interpolate(frame, [8, 20], [0, 1], { extrapolateRight: 'clamp' });
  const textY = interpolate(frame, [8, 20], [24, 0], { extrapolateRight: 'clamp' });

  return (
    <SafeArea>
      <div style={{ padding: '0 20px' }}>
        <div style={{
          fontFamily: fonts.mono,
          fontSize: 80,
          fontWeight: 800,
          color: theme.accent,
          transform: `scale(${numberScale})`,
          marginBottom: 16,
        }}>
          {String(index + 1).padStart(2, '0')}
        </div>
        <div style={{
          fontFamily: fonts.heading,
          fontSize: 44,
          fontWeight: 700,
          color: theme.text,
          opacity: textOpacity,
          transform: `translateY(${textY}px)`,
          marginBottom: 16,
          lineHeight: 1.2,
        }}>
          {title}
        </div>
        <div style={{
          fontFamily: fonts.body,
          fontSize: 24,
          fontWeight: 400,
          color: theme.textMuted,
          opacity: textOpacity,
          transform: `translateY(${textY}px)`,
          lineHeight: 1.6,
          maxWidth: 800,
        }}>
          {description}
        </div>
      </div>
    </SafeArea>
  );
};

export const TipsReel: React.FC<TipsReelProps> = ({ hook, steps, cta }) => {
  const { fps } = useVideoConfig();
  const beatDuration = fps * 4; // 4 seconds per beat

  return (
    <AbsoluteFill>
      <Background variant="dots" />

      {/* Hook */}
      <Sequence durationInFrames={beatDuration}>
        <HookSlide text={hook} />
      </Sequence>

      {/* Steps */}
      {steps.map((step, i) => (
        <Sequence key={i} from={beatDuration * (i + 1)} durationInFrames={beatDuration}>
          <StepSlide index={i} title={step.title} description={step.description} />
        </Sequence>
      ))}

      {/* CTA */}
      <Sequence from={beatDuration * (steps.length + 1)} durationInFrames={beatDuration}>
        <CTASlide text={cta} />
      </Sequence>
    </AbsoluteFill>
  );
};

const HookSlide: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const scale = spring({ frame, fps, config: { damping: 12 } });
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <SafeArea>
      <div style={{
        textAlign: 'center',
        fontFamily: fonts.heading,
        fontSize: 56,
        fontWeight: 800,
        color: theme.text,
        opacity,
        transform: `scale(${scale})`,
        lineHeight: 1.15,
        letterSpacing: '-0.03em',
        padding: '0 20px',
      }}>
        {text}
      </div>
    </SafeArea>
  );
};

const CTASlide: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <SafeArea>
      <div style={{ textAlign: 'center', opacity }}>
        <div style={{
          fontFamily: fonts.heading,
          fontSize: 44,
          fontWeight: 800,
          color: theme.text,
          marginBottom: 24,
        }}>
          {text}
        </div>
        <div style={{
          display: 'inline-block',
          background: theme.accent,
          color: theme.bg,
          fontFamily: fonts.heading,
          fontSize: 22,
          fontWeight: 700,
          padding: '16px 40px',
          borderRadius: 12,
        }}>
          Follow for more
        </div>
      </div>
    </SafeArea>
  );
};
```

---

## Template 3: Quote Reel

```tsx
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';
import { Background } from './components/Background';
import { SafeArea } from './components/SafeArea';
import { theme, fonts } from './theme';

interface QuoteReelProps {
  quote: string;
  author: string;
  role: string;
}

export const QuoteReel: React.FC<QuoteReelProps> = ({ quote, author, role }) => {
  const frame = useCurrentFrame();

  const quoteMarkOpacity = interpolate(frame, [10, 25], [0, 0.3], { extrapolateRight: 'clamp' });

  const charsToShow = Math.floor(interpolate(frame, [20, 20 + quote.length * 1.5], [0, quote.length], {
    extrapolateRight: 'clamp',
  }));
  const visibleQuote = quote.slice(0, charsToShow);

  const authorStart = 20 + quote.length * 1.5 + 15;
  const authorOpacity = interpolate(frame, [authorStart, authorStart + 15], [0, 1], { extrapolateRight: 'clamp' });
  const authorY = interpolate(frame, [authorStart, authorStart + 15], [20, 0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill>
      <Background variant="glow" />
      <SafeArea>
        <div style={{ padding: '0 20px', position: 'relative' }}>
          <div style={{
            fontFamily: 'Georgia, serif',
            fontSize: 200,
            color: theme.accent,
            opacity: quoteMarkOpacity,
            position: 'absolute',
            top: -80,
            left: 0,
            lineHeight: 1,
          }}>
            "
          </div>

          <div style={{
            fontFamily: fonts.heading,
            fontSize: 40,
            fontWeight: 600,
            color: theme.text,
            lineHeight: 1.5,
            marginTop: 60,
            minHeight: 300,
          }}>
            {visibleQuote}
            <span style={{ opacity: frame % 30 < 15 ? 1 : 0, color: theme.accent }}>|</span>
          </div>

          <div style={{
            marginTop: 48,
            opacity: authorOpacity,
            transform: `translateY(${authorY}px)`,
          }}>
            <div style={{
              width: 40,
              height: 2,
              background: theme.accent,
              marginBottom: 16,
            }} />
            <div style={{
              fontFamily: fonts.heading,
              fontSize: 24,
              fontWeight: 700,
              color: theme.text,
            }}>
              {author}
            </div>
            <div style={{
              fontFamily: fonts.body,
              fontSize: 18,
              fontWeight: 400,
              color: theme.textMuted,
              marginTop: 4,
            }}>
              {role}
            </div>
          </div>
        </div>
      </SafeArea>
    </AbsoluteFill>
  );
};
```

---

## Registering All Compositions

```tsx
// src/Root.tsx
import { Composition } from 'remotion';
import { StatReveal } from './StatReveal';
import { TipsReel } from './TipsReel';
import { QuoteReel } from './QuoteReel';
import { canvas } from './theme';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="StatReveal"
      component={StatReveal}
      durationInFrames={canvas.fps * 6}
      fps={canvas.fps}
      width={canvas.width}
      height={canvas.height}
      defaultProps={{
        label: 'CASH FLOW',
        value: '82%',
        context: 'of small businesses fail\ndue to poor cash flow management',
      }}
    />
    <Composition
      id="TipsReel"
      component={TipsReel}
      durationInFrames={canvas.fps * 24}
      fps={canvas.fps}
      width={canvas.width}
      height={canvas.height}
      defaultProps={{
        hook: 'Stop guessing your runway.\nDo this instead:',
        steps: [
          { title: 'Connect your bank', description: 'PSD2 open banking — 5,000+ banks supported. Takes 30 seconds.' },
          { title: 'Let AI categorize', description: 'Automatic transaction categorization. No manual tagging.' },
          { title: 'See your runway', description: 'Real-time burn rate, runway, and cash position in one dashboard.' },
          { title: 'Get alerts', description: 'AI detects anomalies and warns you before problems escalate.' },
        ],
        cta: 'Your finances, finally clear.',
      }}
    />
    <Composition
      id="QuoteReel"
      component={QuoteReel}
      durationInFrames={canvas.fps * 10}
      fps={canvas.fps}
      width={canvas.width}
      height={canvas.height}
      defaultProps={{
        quote: 'I used to spend 4 hours every month reconciling spreadsheets. Now I just ask Pronea.',
        author: 'Jana Novotná',
        role: 'CEO, NovaTech s.r.o.',
      }}
    />
  </>
);
```

## Render Commands

```bash
# Preview all compositions
npx remotion preview

# Render specific composition
npx remotion render src/index.ts StatReveal out/stat-reveal.mp4 --codec h264

# Render with custom props (via CLI)
npx remotion render src/index.ts StatReveal out/custom.mp4 --props '{"label":"RUNWAY","value":"3.3","context":"months of cash remaining"}'

# Batch render
for comp in StatReveal TipsReel QuoteReel; do
  npx remotion render src/index.ts $comp out/${comp}.mp4 --codec h264
done
```
