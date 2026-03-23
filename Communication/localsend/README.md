# Localsend

> Send and receive files to/from nearby devices using the LocalSend protocol. Trigger with /localsend to get an interactive Telegram menu with real inline buttons — device discovery, file sending, text sending, and receiving.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Localsend |
| **作者** | chordlini |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/chordlini-localsend |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chordlini/localsend |
| **安全评级** | 🟡 Medium |

## 功能概述
- Outer array = rows of buttons
- Inner array = buttons per row (max 3 per row for readability)
- Prefix all callback_data with `ls:` to namespace this skill
- When user taps a button, you receive: `callback_data: ls:action`
- When in `awaiting_file` state and user sends an image/file/path → treat it as the file to send. Show confirmation button
- When in `awaiting_text` state and user types anything → treat it as the text to send.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- macOS

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23