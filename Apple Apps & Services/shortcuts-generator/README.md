# shortcuts-generator

> 生成和管理 Apple Shortcuts 快捷指令

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | shortcuts-generator |
| **作者** | erik-agens |
| **ClawHub** | https://clawskills.sh/skills/erik-agens-shortcuts-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/erik-agens/shortcuts-generator |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **Identifier**: `is.workflow.actions.<name>` (e.g., `is.workflow.actions.showresult`)
- **Parameters**: Action-specific configuration in `WFWorkflowActionParameters`
- **UUID**: Unique identifier for referencing this action's output
- [PLIST_FORMAT.md](PLIST_FORMAT.md) - Complete plist structure
- [ACTIONS.md](ACTIONS.md) - All 427 WF*Action identifiers and parameters
- [APPINTENTS.md](APPINTENTS.md) - All 728 AppIntent actions
- [PARAMETER_TYPES.md](PARAMETER_TYPES.md) - All parameter value types and serialization formats
- [VARIABLES.md](VARIABLES.md) - Variable reference system

## 使用场景

Generates valid `.shortcut` plist files for Apple's Shortcuts app on macOS and iOS. Covers 1,155 actions spanning WF*Actions and AppIntents, including control flow, variable references, and app integrations. Outputs signed files ready to import directly into Shortcuts.

## 依赖和前提条件

- macOS Shortcuts

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
