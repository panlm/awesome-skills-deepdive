# apple-contacts

> 管理和搜索 Apple 通讯录联系人

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-contacts |
| **作者** | tyler6204 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-apple-contacts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-contacts |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Case-insensitive
- Partial match with `contains`
- Exact match: use `is` instead of `contains`

## 使用场景

Queries macOS Contacts.app via AppleScript to look up contacts by phone number or name. Returns names, phone numbers, and email addresses from the local address book.

## 依赖和前提条件

- macOS (AppleScript)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
# By phone (name only)
osascript -e 'tell application "Contacts" to get name of every person whose value of phones contains "+1XXXXXXXXXX"'

# By name
osascript -e 'tell application "Contacts" to get name of every person whose name contains "John"'

# List all
osascript -e 'tell application "Contacts" to get name of every person'
, bash
# By phone
osascript -e 'tell application "Contacts"
  set matches to every person whose value of phones contains "+1XXXXXXXXXX"
  if length of matches > 0 then
    set p to item 1 of matches
    return {name of p, value of phones of p, value of emails of p}
  end if
end tell'

# By name
osascript -e 'tell application "Contacts"
  set matches to every person whose name contains "John"
  if length of matches > 0 then
    set p to item 1 of matches
    return {name of p, value of phones of p, value of emails of p}
  end if
end tell'
 |
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
# By phone (name only)
osascript

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
