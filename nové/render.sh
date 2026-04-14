#!/bin/bash
DIR="/Users/timi/Desktop/Pronea/social-posts"
SRC="$DIR/src"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

for html_file in "$SRC"/*.html; do
  [ "$(basename "$html_file")" = "render.sh" ] && continue
  base=$(basename "$html_file" .html)
  png_file="$DIR/${base}.png"
  if [ -f "$png_file" ]; then
    echo "SKIP: $base.png"
    continue
  fi
  "$CHROME" --headless=new --disable-gpu --no-sandbox \
    --screenshot="$png_file" \
    --window-size=1080,1350 \
    --hide-scrollbars \
    --force-device-scale-factor=2 \
    "file://$html_file" 2>/dev/null
  
  # Crop to exact 2160x2700 to remove any edge artifacts
  sips --cropToHeightWidth 2700 2160 "$png_file" >/dev/null 2>&1
  
  echo "OK: $base.png"
done
echo "DONE"
