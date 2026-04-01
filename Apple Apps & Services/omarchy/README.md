# omarchy

> 全面的 macOS 开发环境设置和管理

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | omarchy |
| **作者** | achals-iglu |
| **ClawHub** | https://clawskills.sh/skills/achals-iglu-omarchy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/achals-iglu/omarchy |
| **安全评级** | 🔴 High (高风险) |

## 功能概述

- Bad (generic shortcut):
- Good (Omarchy-native):
- Why: Omarchy wrappers usually handle environment/session assumptions better than raw kill-and-relaunch one-liners.
- restarting random processes manually until things look fixed
- use targeted refresh script first, e.g. `omarchy-refresh-waybar`, `omarchy-refresh-hyprland`, `omarchy-refresh-config` (pick by component)
- Why: refresh scripts are explicit and reversible; manual shotgun restarts are noisy and risky.
- using raw `pacman`/`yay` first without checking Omarchy wrappers
- inspect and prefer `omarchy-pkg-*` flow (`...-present`, `...-missing`, then `...-install`/`...-remove`)

## 使用场景

Omarchy is a Linux desktop environment built around Hyprland with 161 wrapper scripts for system management. The skill sets operating rules that favor omarchy-* commands over generic Linux one-liners to preserve expected state behavior. It covers package management, theme switching, service restarts, system updates, and hardware configuration.

## 依赖和前提条件

- macOS Shortcuts

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
| SEC-02 数据外泄 | 🔴 危险 | 存在向外部发送数据的行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟡 警告 | 涉及后台进程或 Git hooks |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🔴 High (高风险)**

**风险摘要:** 发现 2 项危险和 2 项警告。主要风险: 使用 sudo 提权操作; 存在向外部发送数据的行为

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
