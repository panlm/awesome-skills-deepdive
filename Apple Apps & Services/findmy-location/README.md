# findmy-location

> 通过 FindMy 网络查找设备位置

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | findmy-location |
| **作者** | poiley |
| **ClawHub** | https://clawskills.sh/skills/poiley-findmy-location |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/poiley/findmy-location |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **macOS** 13+ with Find My app
- **Python** 3.9+
- **iCloud account** signed in on your Mac (for Find My access)
- **Location sharing** enabled from the contact you want to track
- **peekaboo** - screen reading CLI ([GitHub](https://github.com/steipete/peekaboo))
- **Hammerspoon** (optional) - for reliable UI clicking ([hammerspoon.org](https://www.hammerspoon.org/))
- System Settings → Apple ID → iCloud → Find My Mac (enabled)
- The person you want to track must share their location with this iCloud account via Find My

## 使用场景

Reads a shared contact's location from Apple Find My and returns a structured result with street address, city, and a context label (home, work, or out). It works by opening the Find My app, capturing the map, and matching visible landmarks against a user-defined list of known locations. A vision fallback flag is set when the location is unrecognized.

## 依赖和前提条件

- macOS 系统
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
| SEC-01 命令执行 | 🟢 通过 | 无 shell 命令，或仅使用明确命名的 CLI 工具 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: steipete/tap/peekaboo, hammerspoon |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。安装软件包: steipete/tap/peekaboo, hammerspoon

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
