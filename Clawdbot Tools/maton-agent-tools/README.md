# maton-agent-tools

> 通过 Maton AI 连接 SaaS 工具（Gmail/Slack/Notion 等），含 UI 仪表板

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | maton-agent-tools |
| **作者** | maverick-software |
| **ClawHub** | https://clawskills.sh/skills/maverick-software-maton-agent-tools |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maverick-software/maton-agent-tools |
| **安全评级** | 🟡 Medium |

## 功能概述
- 50+ SaaS 应用连接
- 完整 UI 仪表板
- OAuth 连接管理
- API Key 集成
- RPC 后端方法
- 连接状态监控

## 使用场景
- 在 Clawdbot 中连接 Gmail/Slack/Notion 等应用
- 通过 UI 管理 OAuth 连接
- 集成第三方 SaaS 工具

## 依赖和前提条件
Clawdbot >= 2026.1.0, Maton 账户和 API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reference/README.md`
- `reference/maton-backend.ts`
- `reference/maton-controller.ts`
- `reference/maton-views.ts`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | TypeScript 参考代码涉及 HTTP 请求和 UI 操作 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Maton API (ctrl.maton.ai) 通信 |
| SEC-03 凭证获取 | 🟡 Medium | MATON_API_KEY 存储在 Clawdbot 配置中 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Maton 外部服务 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 Clawdbot 配置文件的 env 部分 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | OAuth 连接可授权访问用户 SaaS 数据 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化守护进程 |
| SEC-09 信息采集 | 🟡 Medium | 可访问已连接 SaaS 应用的数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** OAuth 集成工具，连接后可访问用户 SaaS 数据，需审慎授权

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
