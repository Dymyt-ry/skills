---
name: video-processing-editing
description: "FFmpeg automation for cutting, trimming, concatenating, and exporting videos with audio mixing and platform optimization. Use when: trimming/cutting video segments, concatenating clips, resizing for platforms, extracting/replacing audio, compressing, converting formats, batch processing, audio sync, color space handling."
origin: erichowens/some_claude_skills
---

# Video Processing & Editing

Expert in FFmpeg-based video editing, processing automation, and export optimization for modern content creation workflows.

## When to Use

- Color grading and correction
- Batch video processing
- Export optimization for platforms
- Subtitle/caption handling
- Audio mixing and normalization
- Adding transitions, effects, overlays
- Cutting, trimming, concatenating clips
- Automated video editing pipelines (script-to-video)

## Technology Selection

| Tool | Speed | Features | Use Case |
|------|-------|----------|----------|
| FFmpeg | Very Fast | CLI automation | Production pipelines |
| MoviePy | Medium | Python API | Programmatic editing |
| PyAV | Fast | Low-level control | Custom processing |
| DaVinci Resolve | Slow | Full NLE | Manual editing |

## Keyframe-Aligned Cuts

### Re-encode for precise cuts
```bash
ffmpeg -i input.mp4 -ss 00:01:23.456 -to 00:02:45.678 \
  -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 192k \
  output.mp4
```

### Two-pass for best of both worlds
```bash
ffmpeg -ss 00:01:20.000 -i input.mp4 \
  -ss 00:00:03.456 -to 00:01:25.678 \
  -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 192k \
  output.mp4
```

### Find keyframes
```bash
ffprobe -select_streams v -show_frames -show_entries frame=pkt_pts_time,key_frame \
  -of csv input.mp4 | grep ",1$" | awk -F',' '{print $2}'
```

## Chain Operations (Avoid Multiple Re-encodes)

```bash
ffmpeg -ss 00:01:00 -i input.mp4 -i audio.mp3 \
  -to 00:04:00 \
  -vf "subtitles=subs.srt" \
  -map 0:v -map 1:a \
  -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 192k \
  output.mp4
```

## Color Space Normalization

```bash
# Analyze color space
ffprobe -v error -select_streams v:0 \
  -show_entries stream=color_space,color_transfer,color_primaries,pix_fmt \
  -of default=noprint_wrappers=1 clip.mp4

# Normalize BT.601 SD to BT.709 HD
ffmpeg -i clip.mp4 \
  -vf "scale=in_range=full:out_range=limited,colorspace=bt709:iall=bt601:fast=1" \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -c:v libx264 -crf 18 -preset medium -c:a copy \
  clip_normalized.mp4
```

## Audio Sync

### Stretch audio to match video
```bash
VIDEO_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 video.mp4)
AUDIO_DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio.mp3)
RATIO=$(echo "$VIDEO_DUR / $AUDIO_DUR" | bc -l)

ffmpeg -i video.mp4 -i audio.mp3 \
  -filter_complex "[1:a]atempo=${RATIO}[a]" \
  -map 0:v -map "[a]" \
  -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

### Mix multiple audio tracks
```bash
ffmpeg -i video.mp4 -i dialogue.wav -i music.mp3 -i sfx.wav \
  -filter_complex "
    [1:a]adelay=0|0[dlg];
    [2:a]volume=0.3,adelay=500|500[mus];
    [3:a]adelay=1200|1200[sfx];
    [dlg][mus][sfx]amix=inputs=3:duration=first[a]
  " \
  -map 0:v -map "[a]" \
  -c:v copy -c:a aac -b:a 256k \
  output.mp4
```

## Platform Export Presets

| Platform | Max Size | Max Duration | Resolution | FPS | Codec |
|----------|----------|-------------|------------|-----|-------|
| YouTube | Unlimited | Unlimited | 8K | 60 | H.264/VP9 |
| Instagram Story | 100 MB | 15s | 1080x1920 | 30 | H.264 |
| Instagram Reel | 1 GB | 90s | 1080x1920 | 30 | H.264 |
| Twitter | 512 MB | 2:20 | 1920x1080 | 60 | H.264 |
| TikTok | 287 MB | 10min | 1080x1920 | 30 | H.264 |
| LinkedIn | 5 GB | 10min | 1920x1080 | 30 | H.264 |

### TikTok Export
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset medium -crf 23 \
  -s 1080x1920 -r 30 -t 600 \
  -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac -b:a 128k \
  tiktok.mp4
```

### Instagram Reel Export
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset medium -crf 23 \
  -s 1080x1920 -r 30 -t 90 \
  -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac -b:a 128k \
  instagram_reel.mp4
```

### YouTube Export
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -s 1920x1080 -r 30 \
  -pix_fmt yuv420p \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -movflags +faststart \
  -c:a aac -b:a 192k -ar 48000 \
  youtube_1080p.mp4
```

## Batch Processing

```bash
#!/bin/bash
while IFS=, read -r start end label; do
  ffmpeg -i raw.mp4 -ss "$start" -to "$end" -c copy "segments/${label}.mp4"
done < cuts.txt
```

## Concatenation

```bash
for f in segments/*.mp4; do echo "file '$f'"; done > concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy assembled.mp4
```

## Scene & Silence Detection

```bash
# Scene changes
ffmpeg -i input.mp4 -vf "select='gt(scene,0.3)',showinfo" -vsync vfr -f null - 2>&1 | grep showinfo

# Silent segments
ffmpeg -i input.mp4 -af silencedetect=noise=-30dB:d=2 -f null - 2>&1 | grep silence
```

## Production Checklist

- Align cuts to keyframes (or two-pass seek)
- Chain operations in single FFmpeg command
- Normalize color spaces before concatenating
- Verify audio/video sync (test at multiple points)
- Use platform-specific export presets
- Apply `-movflags +faststart` for web delivery
- Set proper color metadata (bt709 for HD)
- Use hardware acceleration for batch jobs (NVENC, VideoToolbox)
