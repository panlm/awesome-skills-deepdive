# Agent Mail - CLI-Based Email for Agents

> AI 智能体专用邮箱服务，通过 @agentmail.to 地址为智能体提供独立的邮件收发能力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Mail - CLI-Based Email for Agents |
| **作者** | rimelucci |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rimelucci-agent-mail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail |
| **安全评级** | 🔴 High |

## 功能概述
- 为每个智能体分配独立的 @agentmail.to 邮箱地址
- 支持发送和接收标准电子邮件
- 智能体可自主管理邮件收件箱
- 支持邮件附件处理
- 提供邮件搜索和过滤功能

## 使用场景
- 智能体需要独立邮箱与外部服务或用户通信
- 自动化工作流中需要邮件触发或通知
- 多智能体协作时通过邮件传递信息

## 依赖和前提条件
- AgentMail 服务账号和 API 密钥
- 网络访问 agentmail.to 服务

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
