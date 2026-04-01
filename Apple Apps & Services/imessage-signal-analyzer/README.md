# imessage-signal-analyzer

> 分析 iMessage 和 Signal 聊天记录模式

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | imessage-signal-analyzer |
| **作者** | terellison |
| **ClawHub** | https://clawskills.sh/skills/terellison-imessage-signal-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/terellison/imessage-signal-analyzer |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Open **System Settings → Privacy & Security → Full Disk Access**
- Click **+** and add Python or your terminal app
- iMessage is not available on Linux/Windows
- Signal analysis works via exported JSON
- Install signal-cli: `brew install signal-cli` (macOS) or see https://github.com/AsamK/signal-cli
- Link your device: `signal-cli link` and scan QR code
- Export messages: `signal-cli export --output ~/signal_export.json`
- **Your sent messages** may only exist from the current device's setup date — older sent messages are lost when switching devices. This skews initiation stats.

## 使用场景

Reads iMessage (macOS) and Signal conversation history to produce relationship reports covering message volume, initiation patterns, silence gaps, tone samples, and recent exchanges. Works on macOS for both platforms; Linux and Windows support Signal only via exported JSON.

## 依赖和前提条件

- macOS 系统
- Homebrew: signal-cli
- Python 3

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 无 shell 命令，或仅使用明确命名的 CLI 工具 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: signal-cli |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟡 警告 | 包含自动执行指令，但在合理范围内 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。安装软件包: signal-cli

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
