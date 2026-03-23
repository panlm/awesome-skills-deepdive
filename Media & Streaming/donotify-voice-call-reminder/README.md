# Donotify Voice Call Reminder

> 语音电话提醒和通知工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Donotify Voice Call Reminder |
| **作者** | micahele |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/micahele-donotify-voice-call-reminder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/micahele/donotify-voice-call-reminder |
| **安全评级** | 🟡 Medium |

## 功能概述
- Header: `Authorization: Bearer $DONOTIFY_API_TOKEN`
- Header: `Accept: application/json`
- Base URL: `$DONOTIFY_URL` (default: `https://donotifys.com`)
- When the user says "call me now about X" or "remind me right now about X", use the Call Now endpoint
- When the user says "remind me at [time] about X" or "call me at [time] for X", use the Schedule Reminder endpoint. Convert the user's natural language time to ISO 8601 for `call_at`
- When the user asks "how many reminders do I have left" or "check my usage", use the Usage endpoint
- Always check usage first if you're unsure whether the user has remaining notifications
- If `phone_number_set` is `false`, tell the user to set their phone number at their DoNotify profile page before placing calls

## 使用场景
- 通过语音电话发送重要提醒
- 设置定时语音通知
- 管理语音提醒的联系人列表

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
