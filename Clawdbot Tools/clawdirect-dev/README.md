# clawdirect-dev

> 构建基于 ATXP 认证的代理网站，提供 MCP 集成和 cookie 认证模板

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdirect-dev |
| **作者** | napoleond |
| **ClawHub** | https://clawskills.sh/skills/napoleond-clawdirect-dev |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect-dev |
| **安全评级** | 🟡 Medium |

## 功能概述
- ATXP 代理认证集成
- Cookie-based 会话管理
- MCP 服务器模板
- SQLite 数据存储
- Express + TypeScript 项目结构
- OAuth 支付流程

## 使用场景
- 开发代理可访问的 Web 应用
- 实现 ATXP 认证和支付
- 创建带 MCP 工具的网站

## 依赖和前提条件
Node.js, npm (@longrun/turtle, @atxp/server, better-sqlite3, express)

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | TypeScript 代码模板，需开发者执行 |
| SEC-02 数据外泄 | 🟡 Medium | HTTP 服务器和 MCP 服务器通信 |
| SEC-03 凭证获取 | 🟡 Medium | ATXP 认证和 API 密钥 |
| SEC-04 供应链风险 | 🟡 Medium | 大量 npm 依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | SQLite 数据库创建 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 创建数据库和 HTTP 服务 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化守护进程 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理自有应用数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** Web 应用开发模板，依赖较多但代码透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
