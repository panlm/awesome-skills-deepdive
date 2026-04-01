# acestep-lyrics-transcription

> Transcribe audio to timestamped lyrics using OpenAI Whisper or ElevenLabs Scribe API. Outputs LRC, SRT, or JSON with word-level timestamps. Use when users want to transcribe songs, generate LRC files, or extract lyrics with timestamps from audio.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | acestep-lyrics-transcription |
| **作者** | dumoedss |
| **ClawHub** | https://clawskills.sh/skills/dumoedss-acestep-lyrics-transcription |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep-lyrics-transcription |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Replace misrecognized words with their correct original versions
- Keep all `[MM:SS.cc]` timestamps exactly as-is (timestamps from transcription are accurate)
- Do NOT add structure tags like `[Verse]` or `[Chorus]` — the LRC should only have timestamped text lines

## 依赖和前提条件

- curl, jq, python3 (or python)
- An API key for OpenAI or ElevenLabs

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api. |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: without asking, automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: platform. |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 5 项警告: 命令执行, 数据外泄, 凭证获取, Prompt 注入, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
