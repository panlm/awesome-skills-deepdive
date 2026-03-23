# Agent Contact Card

> 发现和创建 Agent 联系卡片——一种类似 vCard 的 AI Agent 联系方式标准格式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Contact Card |
| **作者** | davedean |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/davedean-agent-contact-card |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davedean/agent-contact-card |
| **安全评级** | 🟡 Medium |

## 功能概述
- 定义了 Agent 联系卡片的标准格式：Markdown + YAML 前置数据
- 通过 /.well-known/agent-card 路径实现自动发现
- 支持多种联系渠道：Email、Discord、Webhook、Signal、Telegram 等
- 支持多 Agent 配置：一个域名下可发布多个专业化 Agent 的联系方式
- Webhook 渠道支持详细的认证和数据格式说明
- 可声明 Agent 能力（如 scheduling、accepts_ical）供其他 Agent 查询

## 使用场景
- 为自己的 AI Agent 创建公开的联系方式页面，让其他 Agent 可以自动发现并联系
- 在 Agent 间通信前先查询对方的联系卡片以确定最佳沟通渠道
- 构建 Agent 社交网络的基础身份和通信发现协议

## 依赖和前提条件
- 一个可托管静态文件的域名（用于发布 /.well-known/agent-card）

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
