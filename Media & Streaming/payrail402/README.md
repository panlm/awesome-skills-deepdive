# payrail402

> Payrail 支付集成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | payrail402 |
| **作者** | rsquaredsolutions2026 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/rsquaredsolutions2026-payrail402 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rsquaredsolutions2026/payrail402 |
| **安全评级** | 🔴 High |

## 功能概述
- Used by: `payrail402_track` tool
- How: Embedded in the API URL path (`/api/ingest/webhook/{token}`) to authenticate transaction submissions
- Why: Each agent has a unique webhook token that links transactions to the correct agent in the dashboard. Without it, the skill cannot submit transactions
- Security: Sent as a URL path segment over HTTPS only. Never included in query strings, headers, or request bodies
- Used by: `payrail402_track` (alternative auth path) and `payrail402_status` tool
- How: Sent via `x-agent-key` or `x-api-key` HTTP header over HTTPS
- Why: Required for checking agent status and for multi-agent setups where one API key manages multiple agents. Not needed if you only use webhook auth for tracking
- Security: Transmitted only in HTTP headers over HTTPS. Format: `pr4_` prefix + base64url secret. Stored as SHA-256 hash on the server

## 使用场景
- 集成支付处理和交易管理
- 跟踪支付状态和交易历史
- 管理支付配置和账户

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `openclaw-skill.js`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
