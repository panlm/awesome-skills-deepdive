# Self-Integration

> Connect to any external app and perform actions on it. Use when the user wants to interact with external services like Slack, Linear, HubSpot, Salesforce, Jira, GitHub, Google Sheets, or any other app — send messages, create tasks, sync data, manage contacts, or perform any API operation.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Self-Integration |
| **作者** | bratchenko |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bratchenko-self-integration |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bratchenko/self-integration |
| **安全评级** | 🟡 Medium |

## 功能概述
- MEMBRANE_TOKEN
- MEMBRANE_API_URL
- `status: "pending"` — user hasn't completed yet, poll again.
- `status: "success"` — done. Use `resultConnectionId` as the connection ID going forward.
- `status: "error"` — failed. Check `resultError` for details.
- All data is sent to the Membrane API over HTTPS.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23