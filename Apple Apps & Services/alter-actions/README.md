# alter-actions

> 通过 Shortcuts 在 macOS/iOS 上创建和管理自动化操作

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | alter-actions |
| **作者** | olivieralter |
| **ClawHub** | https://clawskills.sh/skills/olivieralter-alter-actions |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/olivieralter/alter-actions |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- 见 SKILL.md 原始文件

## 使用场景

Trigger any of 84+ Alter macOS app actions via x-callback-urls from the command line or Clawdbot. Actions span writing, translation, summarization, code, git, social media, email, and more. Works by constructing and opening alter:// URLs with encoded parameters.

## 依赖和前提条件

- macOS 系统
- Node.js

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
# Trigger an action directly
node index.js trigger ask-anything --input "What is AI?"

# Find actions with natural language
node index.js find "summarize video"

# List all actions in a category
node index.js list --category writing
,  | Rewrite | Rewrites text with fresh perspectives | None |
| , : Arabic, Chinese, Dutch, English, Filipino, French, German, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Vietnamese |
|  |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。执行 shell 命令: bash
# Trigger an action directly
nod

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
