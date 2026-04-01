# icloud-findmy

> 通过 iCloud 查找我的设备

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | icloud-findmy |
| **作者** | liamnichols |
| **ClawHub** | https://clawskills.sh/skills/liamnichols-icloud-findmy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liamnichols/icloud-findmy |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Devices are separated by `------------------------------`
- Location is a Python dict (use `eval()` or parse with regex)
- Battery Level is 0.0-1.0 (multiply by 100 for percentage)
- Battery Status: "Charging" or "NotCharging"
- Location fields: `latitude`, `longitude`, `timeStamp` (milliseconds), `horizontalAccuracy`
- Fancy Unicode apostrophes (U+2019 ') instead of ASCII '
- No apostrophes at all (e.g., "Lindas iPhone")
- Sessions last **1-2 months**

## 使用场景

Queries Apple iCloud Find My to retrieve device locations and battery status for personal and family devices. Uses pyicloud CLI under the hood. Requires one-time 2FA authentication, after which sessions persist for 1-2 months.

## 依赖和前提条件

- macOS 系统
- Python 3

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 使用 eval/exec 动态命令执行 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: pipx, pipx |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟡 警告 | 包含自动执行指令，但在合理范围内 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟡 警告 | 有限系统信息采集: 系统用户/内核信息 |
| SEC-10 混淆/反分析 | 🟡 警告 | 使用编码但非命令执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 1 项危险和 5 项警告。主要风险: 使用 eval/exec 动态命令执行

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
