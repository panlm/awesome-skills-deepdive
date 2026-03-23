# mailchannels

> 通过 MailChannels API 发送邮件并处理投递事件 Webhook

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mailchannels |
| **作者** | ttulttul |
| **ClawHub** | https://clawskills.sh/skills/ttulttul-mailchannels |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ttulttul/mailchannels |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 MailChannels API 发送邮件（同步/异步）
- DNS 域锁定配置
- 投递事件 Webhook 接收和路由
- Webhook 签名验证（Ed25519）
- 投递状态跟踪和关联

## 使用场景
- 通过 API 发送事务性邮件
- 监控邮件投递状态和退信

## 依赖和前提条件
- MAILCHANNELS_API_KEY
- MAILCHANNELS_ACCOUNT_ID
- curl

## 包含文件
- `SKILL.md — 完整 API 和 Webhook 配置指南`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 API 文档 |
| SEC-02 数据外泄 | 🟡 Medium | 通过外部 API 发送邮件 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key 和 Account ID |
| SEC-04 供应链风险 | 🟢 Safe | 无代码依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯 API 指南 |
| SEC-07 越权操作 | 🟡 Medium | 可代表用户发送邮件 |
| SEC-08 持久化机制 | 🟡 Medium | Webhook 端点需持续监听 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理自身邮件投递事件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 邮件发送能力需注意防止滥用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
