# Connect Apps

> 将 Claude 连接到 Gmail、Slack、GitHub 等 1000+ 外部应用，实现真正的发送邮件、创建 Issue、发布消息等操作。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Connect Apps |
| **作者** | sohamganatra |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/sohamganatra-connect-apps |

## 功能概述
- 通过 Composio Tool Router 插件连接 1000+ 外部应用
- 支持发送邮件（Gmail、Outlook、SendGrid）
- 支持聊天消息（Slack、Discord、Teams、Telegram）
- 支持开发工具（GitHub、GitLab、Jira、Linear）
- 支持文档协作（Notion、Google Docs、Confluence）
- 支持数据操作（Sheets、Airtable、PostgreSQL）
- 首次使用通过 OAuth 一次性授权，后续自动执行

## 使用场景
- 让 AI Agent 直接发送邮件、创建 GitHub Issue 或在 Slack 发消息，而不仅仅是生成文本
- 通过自然语言指令操作多个 SaaS 工具，实现跨应用自动化
- 快速集成新的外部服务，无需编写 API 集成代码

## 依赖和前提条件
- Composio 平台 API Key（免费注册：platform.composio.dev）
- 安装 Composio Tool Router 插件（`/plugin install composio-toolrouter`）
- 各外部应用的 OAuth 授权

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
