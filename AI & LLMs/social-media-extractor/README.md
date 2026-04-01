# social-media-extractor

> This skill enables Claude to extract public data from **Instagram**, **TikTok**, and **Reddit**

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | social-media-extractor |
| **作者** | g4dr |
| **ClawHub** | https://clawskills.sh/skills/g4dr-social-media-extractor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g4dr/social-media-extractor |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Extract public posts, hashtags, and profiles from **Instagram**
- Scrape trending videos, comments, and creator stats from **TikTok**
- Pull posts, threads, comments, and subreddit data from **Reddit**
- Aggregate data across platforms for unified trend analysis
- Output structured JSON data ready for analysis, dashboards, or export

## 依赖和前提条件

- An Apify account → https://www.apify.com/?fpr=dx06p
- A valid **Personal API Token** from Settings → Integrations
- Node.js 18+ for the `apify-client` package
- No platform API keys required — Apify handles all platform access

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api., fetch( |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟡 警告 | 注意: npm install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 5 项警告: 命令执行, 数据外泄, 凭证获取, 供应链风险, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
