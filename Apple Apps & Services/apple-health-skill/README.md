# apple-health-skill

> 访问和分析 Apple Health 健康数据

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-health-skill |
| **作者** | nftechie |
| **ClawHub** | https://clawskills.sh/skills/nftechie-apple-health-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nftechie/apple-health-skill |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- "How many workouts did I do this week?"
- "What's my VO2 Max trend?"
- "How has my sleep been trending this week?"
- "Compare my running pace this month vs last month"
- "Should I take a rest day based on my recent training?"
- Maximum range between `start` and `end` is 90 days.

## 使用场景

Connects AI agents to Apple Health data via the Transition app. Enables natural language queries about workouts, heart rate trends, VO2 Max, sleep, and training load. Also provides a free workout generator that requires no account.

## 依赖和前提条件

- macOS 系统
- curl

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 无 shell 命令，或仅使用明确命名的 CLI 工具 |
| SEC-02 数据外泄 | 🟡 警告 | 调用已知服务 API 发送数据 |
| SEC-03 凭证获取 | 🟡 警告 | 要求用户提供 API 密钥/令牌 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。调用已知服务 API 发送数据

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
