# managing-apple-notes

> 管理和组织 Apple Notes 笔记

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | managing-apple-notes |
| **作者** | wangwalk |
| **ClawHub** | https://clawskills.sh/skills/wangwalk-managing-apple-notes |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wangwalk/managing-apple-notes |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- "brew install wangwalk/tap/inotes"
- ✅ **Open source**: Full source code at https://github.com/wangwalk/inotes
- ✅ **Local-only**: All operations run locally via AppleScript; no data leaves your machine
- ✅ **No network calls**: `inotes` does not connect to any remote servers
- ✅ **Auditable install**: Binary installed via Homebrew from signed release or GitHub Releases
- ✅ **MIT Licensed**: Free and open for inspection and contributions
- ⚠️ **Requires macOS Automation permission** for Notes.app (user grants via System Settings)
- 📦 **Universal binary**: Supports both Apple Silicon (arm64) and Intel (x86_64)

## 使用场景

inotes is a macOS CLI that manages Apple Notes from the terminal via AppleScript. It supports listing, reading, creating, editing, deleting, and searching notes across folders and accounts. All operations run locally with no network calls.

## 依赖和前提条件

- macOS 系统
- jq
- curl

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 使用 sudo 提权操作 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: wangwalk/tap/inotes", wangwalk/tap/inotes |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟡 警告 | 包含自动执行指令，但在合理范围内 |
| SEC-07 越权操作 | 🟡 警告 | 笔记工具访问网络/服务器功能 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 1 项危险和 3 项警告。主要风险: 使用 sudo 提权操作

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
