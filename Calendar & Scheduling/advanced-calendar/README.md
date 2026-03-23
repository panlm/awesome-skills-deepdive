# advanced-calendar

> Advanced calendar skill with natural language processing, automatic reminders, and multi-channel notifications

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | advanced-calendar |
| **作者** | toughworm |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/toughworm-advanced-calendar |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/toughworm/advanced-calendar |
| **安全评级** | 🟢 Low |

## 功能概述
- Natural Language Processing: Talk to your calendar in everyday language
- Smart Event Creation: Automatically extracts dates, times, durations, and reminders
- Interactive Assistance: Asks for missing information when needed
- Multi-Channel Notifications: Sends notifications via WhatsApp, Discord, Telegram, Signal, and other configured channels
- Persistent Reminders: If no acknowledgment is received, reminders repeat every 15 minutes like a snooze alarm
- Flexible Reminders: Set reminders minutes, hours, or days in advance

## 使用场景
- 设置和管理提醒事项
- 跟踪待办任务
- 通过自然语言创建提醒

## 依赖和前提条件
- Python / pip

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `PUBLISH.md`
- `SKILL.md`
- `UPDATES.md`
- `_meta.json`
- `docs`
- `intent_handler.py`
- `openclaw_integration.py`
- `package.json`
- `release-notes-v1.02.md`
- `scripts`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23