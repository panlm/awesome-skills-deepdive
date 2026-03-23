# Belong Events - Discover and Organize

> Create, discover, and manage events with NFT tickets on the Belong platform

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Belong Events - Discover and Organize |
| **作者** | nomadcalendar |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/nomadcalendar-belong-events |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nomadcalendar/belong-events |
| **安全评级** | 🟡 Medium |

## 功能概述
- All JSON-RPC calls are sent to the endpoint above (or `BELONG_EVENTS_ENDPOINT` if overridden).
- If `BELONG_EVENTS_API_KEY` is set, it is sent to that endpoint as `X-OpenClaw-Key`.
- list_tools — List available tools (no params)
- discover_events — Search events. Params: `city`, `category`, `startDate`, `endDate`, `limit`, `latitude`, `longitude` (a
- get_event_details — Get event details. Params: `eventId` (required), `source`, `city`, `latitude`, `longitude` (optional
- buy_ticket — Get checkout/event URL. Params: `eventId` (required), `tierId`, `quantity`

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `invoke.sh`

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