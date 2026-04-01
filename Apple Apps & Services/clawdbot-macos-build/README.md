# clawdbot-macos-build

> 在 macOS 上构建和部署 ClawdBot 应用

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-macos-build |
| **作者** | manish-basargekar |
| **ClawHub** | https://clawskills.sh/skills/manish-basargekar-clawdbot-macos-build |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manish-basargekar/clawdbot-macos-build |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- macOS (10.14+)
- Xcode 15+ with Command Line Tools
- Node.js >= 22
- pnpm package manager
- 30+ GB free disk space (Swift build artifacts)
- Internet connection (large dependencies)
- Fetches Swift package dependencies (SwiftUI libraries, etc.)
- Compiles the macOS app for your architecture (arm64 for M1+, x86_64 for Intel)

## 使用场景

Builds the Clawdbot macOS menu bar companion app from source, covering dependency installation, React/TypeScript UI compilation, Swift compilation, code signing, and app packaging. The resulting app manages Gateway health, native permissions (camera, screen recording, accessibility), and hardware access on Mac.

## 依赖和前提条件

- macOS 系统
- Node.js
- Swift/Xcode

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 使用 sudo 提权操作 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: pnpm |
| SEC-05 文件系统篡改 | 🟡 警告 | 存在文件删除或权限修改操作 |
| SEC-06 Prompt 注入 | 🟡 警告 | 包含自动执行指令，但在合理范围内 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 1 项危险和 4 项警告。主要风险: 使用 sudo 提权操作

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
