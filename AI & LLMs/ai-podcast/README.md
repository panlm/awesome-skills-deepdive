# ai-podcast

> Generate AI podcast episodes from PDFs, text, notes, and links using MagicPodcast in OpenClaw. Creates natural two-person dialogue audio, supports custom language, and returns podcast links with progress tracking in the MagicPodcast dashboard. Use for PDF-to-podcast, text-to-podcast, and fast content-to-audio workflows.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | ai-podcast |
| **作者** | mogens9 |
| **ClawHub** | https://clawskills.sh/skills/mogens9-ai-podcast |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mogens9/ai-podcast |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- Signed-in users can generate free podcast.
- Expected generation time is usually 2-5 minutes.
- Right after starting, direct users to `https://www.magicpodcast.app/app`.
- Tell the user this page is their dashboard: they can see created podcasts, live progress/status, and finished episodes.
- Return `outputs.shareUrl` as the default completion link.
- If `outputs.shareUrl` is missing, fall back to `outputs.appUrl`.

## 依赖和前提条件

- {"clawdbot":{"emoji":"🎙️","requires":{"bins":["curl","jq"],"env":["MAGICPODCAST_API_URL","MAGICPODCAST_API_KEY
- MAGICPODCAST_API_KEY="<your_api_key
- $MAGICPODCAST_API_KEY

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
