# testflight-monitor

> 监控 TestFlight 应用测试版本更新

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | testflight-monitor |
| **作者** | jon-xo |
| **ClawHub** | https://clawskills.sh/skills/jon-xo-testflight-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jon-xo/testflight-monitor |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **Lookup TestFlight codes** → app names using community data
- **Check single URLs** for immediate status
- **Batch monitoring** with state tracking (silent by default)
- **Only alerts on changes** (full → available)
- **Configurable intervals** (30min - 3hr recommended)
- Monitors multiple betas in one job
- Stays silent unless something changes
- Uses human-readable app names (not cryptic codes)

## 使用场景

Monitors TestFlight beta slots across multiple apps and alerts only when slots open up. Resolves cryptic TestFlight codes to human-readable app names using a community-maintained lookup table of 800+ apps. Tracks state between checks so you only get notified on transitions from full to available.

## 依赖和前提条件

- macOS 系统
- jq
- curl

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
