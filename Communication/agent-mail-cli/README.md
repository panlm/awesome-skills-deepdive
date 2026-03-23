# CLI-Based Email for Agents

> AI 智能体命令行邮箱客户端，通过 CLI 操作 @agentmail.to 邮箱收发邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CLI-Based Email for Agents |
| **作者** | rimelucci |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rimelucci-agent-mail-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail-cli |
| **安全评级** | 🔴 High |

## 功能概述
- 命令行界面管理 agentmail.to 邮箱
- 支持发送、接收、列出和搜索邮件
- 适合脚本和自动化流程集成
- 轻量级无需图形界面即可操作邮箱
- 支持管道和批处理邮件操作

## 使用场景
- 在终端环境中快速收发智能体邮件
- 将邮件操作集成到 Shell 脚本或 CI/CD 流程
- 服务器环境下无 GUI 的邮件管理

## 依赖和前提条件
- AgentMail 服务账号和 API 密钥
- agent-mail-cli 命令行工具已安装

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
