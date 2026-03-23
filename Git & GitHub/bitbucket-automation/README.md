# Bitbucket Automation

> Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bitbucket Automation |
| **作者** | sohamganatra |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/sohamganatra-bitbucket-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sohamganatra/bitbucket-automation |
| **安全评级** | 🟡 Medium |

## 功能概述
- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Bitbucket connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `bitbucket`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas
- `workspace`: Workspace slug or UUID (required for all operations)
- `repo_slug`: URL-friendly repository name
- `source_branch`: Branch with changes to merge

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
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23