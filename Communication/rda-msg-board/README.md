# RDA MSG Board

> Send scrolling text messages to RDA MSG Board via HTTP/JSON. Use for notifications, alerts, or status updates on physical LED matrix.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RDA MSG Board |
| **作者** | rdeangel |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rdeangel-rda-msg-board |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rdeangel/rda-msg-board |
| **安全评级** | 🔴 High |

## 功能概述
- "Send [message] to [board name]" → Use the named profile
- "Send [message] to msg board" → Use the default/office profile
- "Send [message]" → Use the default/office profile
- "Send alert with [sound]" → Include the `--chirp` parameter
- "Send 'Meeting in 5 min' to office" → `send_message.py "Meeting in 5 min" --profile office`
- "Send alert 'System down'" → `send_message.py "System down" --profile office --buzzer 5`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，7 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23