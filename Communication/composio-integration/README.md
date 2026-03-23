# Composio Integration

> 通过 Composio 统一 API 平台访问 600+ 应用和服务，一站式集成各类第三方工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Composio Integration |
| **作者** | rita5fr |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rita5fr-composio-integration |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rita5fr/composio-integration |
| **安全评级** | 🔴 High |

## 功能概述
- 统一 API 接口访问 600+ 应用和服务
- 预置主流 SaaS 工具集成（Slack、GitHub、Jira 等）
- OAuth 和 API Key 认证统一管理
- 动作和触发器的灵活编排
- 跨应用的数据流转和工作流自动化
- 无需单独开发每个平台的集成接口

## 使用场景
- 智能体通过 Composio 快速接入数百种 SaaS 工具无需逐个开发
- 构建跨平台自动化工作流（如 GitHub Issue 自动创建 Jira 工单）
- 统一管理多个第三方服务的认证和 API 调用

## 依赖和前提条件
- 注册 Composio 账户并获取 API Key
- 在 Composio 中授权目标应用连接
- 安装 Composio 集成插件

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

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

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
