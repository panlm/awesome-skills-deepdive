# Send SMS text and bulk messages via TelTel.io API

> Send SMS text messages via TelTel (teltel.io) using the REST API (api.teltel.io). Includes bulk send, delivery report, and bulk sms.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Send SMS text and bulk messages via TelTel.io API |
| **作者** | teltel-call-center |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/teltel-call-center-teltel-send-sms-text-message |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teltel-call-center/teltel-send-sms-text-message |
| **安全评级** | 🟡 Medium |

## 功能概述
- `skills.entries.teltel-send-sms-text-message.apiKey` → `TELTEL_API_KEY`
- `skills.entries.teltel-send-sms-text-message.env.TELTEL_SMS_FROM`
- `TELTEL_API_KEY` (required)
- `TELTEL_SMS_FROM` (optional) — default sender name/number
- `TELTEL_BASE_URL` (optional) — defaults to `https://api.teltel.io/v2`
- Base URL: `https://api.teltel.io/v2`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
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