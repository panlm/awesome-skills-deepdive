# Talkspresso

> Manage a Talkspresso business (services, appointments, products, clients, earnings, calendar) using the Talkspresso REST API. Use when the user wants to check bookings, create services, manage digital products, view earnings, update their profile, schedule sessions, or do anything related to their Talkspresso account. Requires TALKSPRESSO_API_KEY environment variable.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Talkspresso |
| **作者** | baron-talkspresso |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/baron-talkspresso-talkspresso |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/baron-talkspresso/talkspresso |
| **安全评级** | 🟡 Medium |

## 功能概述
- 1:1 call: `{"capacity_type":"single","capacity":1}`
- Group session: `{"capacity_type":"group","capacity":10}`
- Webinar: `{"capacity_type":"group","capacity":50,"is_webinar":true}`
- Never send invites without confirmation. Always create with `skip_email: true`, show the user, then send.
- Stripe required for paid sessions. If the user hasn't connected Stripe, they can only create free services and free prod
- Get provider_id from the profile (`id` field) when needed for availability checks.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23