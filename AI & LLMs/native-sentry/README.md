# native-sentry

> Read Sentry issues, events, and production errors via the Sentry REST API. Use when the user wants to inspect errors, list recent issues, get stack traces, or summarize production health. Requires SENTRY_AUTH_TOKEN with read-only scopes.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | native-sentry |
| **作者** | codeninja23 |
| **ClawHub** | https://clawskills.sh/skills/codeninja23-native-sentry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/codeninja23/native-sentry |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- PII (emails, IPs) is redacted by default
- Stack traces are excluded from event detail by default — add `--include-entries` only when you need them and trust the environment
- `--no-redact` disables PII redaction — avoid in shared or logged environments
- For self-hosted Sentry, set `SENTRY_BASE_URL` or use `--base-url`

## 依赖和前提条件

- SENTRY_AUTH_TOKEN
- {"openclaw":{"emoji":"🐛","primaryEnv":"SENTRY_AUTH_TOKEN","requires":{"bins":["python3"],"env":["SENTRY_AUTH_TOKEN
- "$SENTRY_AUTH_TOKEN

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
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 命令执行, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
