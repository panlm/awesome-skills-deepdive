# apple-mail-search

> 搜索 Apple Mail 邮件内容

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-mail-search |
| **作者** | mneves75 |
| **ClawHub** | https://clawskills.sh/skills/mneves75-apple-mail-search |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mneves75/apple-mail-search |
| **安全评级** | 🟢 Safe (安全) |

## 功能概述

- Read-only (cannot compose/send)
- Metadata only (bodies in .emlx files)
- Mail.app only (not Outlook, etc.)

## 使用场景

Searches Apple Mail emails by querying the local SQLite database directly. Returns results in ~50ms across large mailboxes. Read-only, macOS only, works with Mail.app metadata.

## 依赖和前提条件

- macOS 系统
- jq

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
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Safe (安全)**

**风险摘要:** 静态分析未发现明显安全问题，但 ClawHub 扫描标记需注意。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
