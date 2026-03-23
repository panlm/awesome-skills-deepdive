# AgentMail

> 专为 AI 代理设计的 API 优先邮件平台，支持编程式创建收件箱、收发邮件及 Webhook 事件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentMail |
| **作者** | adboio |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/adboio-agentmail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/adboio/agentmail |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 API 创建和管理编程式邮箱地址
- 支持完整的邮件收发功能，包括富文本内容和附件
- 提供 Webhook 实时推送收件通知
- 内置 AI 原生功能：语义搜索、自动标签、结构化数据提取
- 无速率限制，专为高频代理使用场景构建
- 提供 Python SDK，可快速集成到现有工作流

## 使用场景
- 为 AI 代理创建独立邮箱身份，处理自动化邮件往来
- 替代传统 Gmail/Outlook 实现代理级邮件基础设施
- 通过 Webhook 触发基于邮件的自动化工作流

## 依赖和前提条件
- AgentMail 账号及 API Key（从 console.agentmail.to 获取）
- Python / pip（`pip install agentmail python-dotenv`）
- 环境变量 `AGENTMAIL_API_KEY`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
