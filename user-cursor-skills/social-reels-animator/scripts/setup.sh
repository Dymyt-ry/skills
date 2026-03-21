#!/bin/bash
set -e

PROJECT_DIR="${1:-.}"

if [ "$PROJECT_DIR" = "." ]; then
  echo "Usage: bash setup.sh /path/to/project-name"
  echo "Creates a Remotion project configured for Pronea branded reels."
  exit 1
fi

echo "Setting up Remotion reels project at: $PROJECT_DIR"

npx create-video@latest "$PROJECT_DIR" --template blank

cd "$PROJECT_DIR"

npm install @remotion/cli @remotion/player

cat > src/theme.ts << 'THEME'
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
THEME

mkdir -p src/components

cat > src/components/Background.tsx << 'BG'
import React from 'react';
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
BG

cat > src/components/SafeArea.tsx << 'SA'
import React from 'react';
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
SA

echo ""
echo "Project ready at: $PROJECT_DIR"
echo ""
echo "Next steps:"
echo "  cd $PROJECT_DIR"
echo "  npx remotion preview"
echo ""
echo "Copy templates from:"
echo "  ~/.cursor/skills/social-reels-animator/references/remotion-templates.md"
