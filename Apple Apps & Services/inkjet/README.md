# inkjet

> 通过 macOS 打印系统管理打印任务

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | inkjet |
| **作者** | aaronchartier |
| **ClawHub** | https://clawskills.sh/skills/aaronchartier-inkjet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aaronchartier/inkjet |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- { id: "pip", kind: "pip", package: "inkjet", label: "Install (pip)" }
- { id: "brew", kind: "brew", package: "aaronchartier/tap/inkjet", label: "Install (Homebrew)" }

## 使用场景

A CLI tool for printing text, images, and QR codes to cheap Bluetooth thermal printers on macOS. Connects via BLE without requiring OS-level pairing. Supports Markdown rendering, multi-printer orchestration, and JSON output for scripting.

## 依赖和前提条件

- macOS 系统

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
inkjet scan
, bash
inkjet whoami
, bash
inkjet print text "Hello, World!"
inkjet print text "Line 1\nLine 2\nLine 3"
inkjet print text "Big Text" --size 72
 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 仅在工作目录内进行文件操作 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟡 警告 | 有限系统信息采集: 系统用户/内核信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。执行 shell 命令: bash
inkjet scan
, bash
inkjet whoami

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
