# pipedream-connect

> 通过 Pipedream Connect 连接 2000+ 应用，支持每代理 OAuth 隔离和 MCP 工具暴露

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pipedream-connect |
| **作者** | maverick-software |
| **ClawHub** | https://clawskills.sh/skills/maverick-software-pipedream-connect |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maverick-software/pipedream-connect |
| **安全评级** | 🟡 Medium |

## 功能概述
- 2000+ 应用连接
- 每代理 OAuth 隔离
- MCP 工具自动注册为代理工具
- 实时连接账户发现
- 动态应用目录浏览
- OAuth 令牌自动刷新

## 使用场景
- 连接多个 SaaS 应用到 OpenClaw 代理
- 为不同代理配置独立的应用连接
- 自动刷新 OAuth 令牌

## 依赖和前提条件
Pipedream 账户, Python 3, OpenClaw

## 包含文件
- `.metadata.json`
- `CHANGELOG.md`
- `INSTALL.md`
- `SKILL.md`
- `_meta.json`
- `reference/README.md`
- `reference/agent-pipedream-controller.ts`
- `reference/agent-pipedream-views.ts`
- `reference/control-ui-csp.ts`
- `reference/pipedream-backend.ts`
- `reference/pipedream-controller.ts`
- `reference/pipedream-views.ts`
- `scripts/pipedream-token-refresh.py`
- `scripts/setup-cron.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 令牌刷新脚本和 Bash 安装脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Pipedream API 通信，OAuth 令牌交换 |
| SEC-03 凭证获取 | 🔴 High | 处理 OAuth client_id/secret，存储在 secrets.json 中 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Pipedream 云服务 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 mcporter.json 和代理配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | OAuth 连接可访问用户 2000+ 应用数据 |
| SEC-08 持久化机制 | 🟡 Medium | cron 定时刷新令牌（每 45 分钟） |
| SEC-09 信息采集 | 🟡 Medium | 可发现和访问所有已连接应用数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** OAuth 令牌管理涉及高权限凭证，连接后可访问大量第三方应用数据

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
