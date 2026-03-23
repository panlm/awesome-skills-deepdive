# Scalekit Agent Auth

> 通过 Scalekit Connect 连接任意第三方服务并执行工具操作的通用 Skill

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Scalekit Agent Auth |
| **作者** | avinash-kamath |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/avinash-kamath-scalekit-agent-auth |

## 功能概述
- 自动发现用户在 Scalekit 中配置的第三方服务连接
- 检查用户授权状态，未授权时生成认证链接（Magic Link）
- 自动发现并执行目标服务的可用工具（如获取 Notion 页面、列出 HubSpot 联系人等）
- 无匹配工具时，回退到直接代理 API 请求
- 支持任意 Scalekit Connect 提供商：Notion、Gmail、Slack、HubSpot、Google Drive、Todoist 等
- 提供连接列表查看、按提供商筛选、工具列表获取等管理功能

## 使用场景
- AI Agent 需要访问用户的 Notion、Gmail、Slack 等第三方服务时，统一通过此 Skill 发现连接并执行操作
- 需要为 AI Agent 快速接入多个 SaaS 应用的 API，无需逐个编写集成代码
- 用户希望用自然语言指挥 Agent 操作外部服务（如"获取我的 Notion 页面"、"列出 HubSpot 联系人"）

## 依赖和前提条件
- `uv` 包管理器（用于安装依赖和运行脚本）
- 环境变量 `TOOL_ENV_URL`：Scalekit 环境 URL
- 环境变量 `TOOL_CLIENT_ID`：Scalekit 客户端 ID
- 环境变量 `TOOL_CLIENT_SECRET`：Scalekit 客户端密钥
- 环境变量 `TOOL_IDENTIFIER`：Agent 标识名称
- Scalekit 账号及已配置的第三方服务连接

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，0 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
