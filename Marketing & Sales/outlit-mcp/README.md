# Outlit MCP

> Outlit MCP 内容发布工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Outlit MCP |
| **作者** | leo-paz |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/leo-paz-outlit-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leo-paz/outlit-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 内容发布和分发
- 多平台内容管理
- MCP 协议集成
- 发布工作流自动化

## 使用场景
- 通过 MCP 协议自动化内容发布流程
- 管理跨平台的内容分发和同步

## 依赖和前提条件
- API 密钥
- PostgreSQL
- Slack API

## 包含文件
- `README.md`
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23