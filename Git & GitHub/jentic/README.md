# Jentic

> "Call external APIs through Jentic — AI agent API middleware. Use whenever you need to interact with external APIs (Gmail, Google Calendar, GitHub, Stripe, Twilio, and many more). Jentic handles authentication centrally so no per-API credentials are needed in the agent. The flow is: search by intent, load the schema, then execute. Use this in preference to direct curl/API calls for any API in the Jentic catalog."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Jentic |
| **作者** | seanblanchfield |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/seanblanchfield-jentic |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seanblanchfield/jentic |
| **安全评级** | 🟡 Medium |

## 功能概述
- [Jentic](https://jentic.com)
- [Jentic Docs](https://docs.jentic.com)
- [Jentic SDK](https://github.com/jentic/jentic-sdks)
- [OpenClaw](https://openclaw.ai)
- [ClawHub](https://clawhub.ai)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23