# apple-find-my-local

> 通过本地缓存数据查找 Apple 设备位置

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-find-my-local |
| **作者** | loganprit |
| **ClawHub** | https://clawskills.sh/skills/loganprit-apple-find-my-local |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/loganprit/apple-find-my-local |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Location data for people, devices, and items in your Find My app
- Screenshots of the Find My window (stored locally in `/tmp/`)
- No network requests to third-party services
- No credential storage or Apple ID access
- No data exfiltration — all operations are local UI automation
- Shared locations of family/friends
- Device locations (yours and Family Sharing members)
- AirTag/item locations

## 使用场景

Controls the native macOS Find My app through UI automation via Peekaboo, allowing location lookups for people, devices, and AirTag items. Operates entirely locally with no third-party API calls or Apple ID credential exposure.

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
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。涉及凭证/令牌使用但未直接读取凭证文件

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
