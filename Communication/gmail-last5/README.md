# Gmail Last5

> 通过 /skill gmail_last5 命令快速获取最近 5 封 Gmail 邮件摘要

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gmail Last5 |
| **作者** | neuralshift1 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/neuralshift1-gmail-last5 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/neuralshift1/gmail-last5 |
| **安全评级** | 🟢 Low |

## 功能概述
- 一键获取 Gmail 收件箱最新 5 封邮件
- 展示发件人、主题和邮件摘要信息
- 通过 Gmail API 安全读取邮件
- 支持快速浏览未读邮件概况

## 使用场景
- 每日快速检查收件箱是否有重要邮件
- 在聊天中直接查询最新邮件状态
- AI 助手定期汇报邮箱动态

## 依赖和前提条件
- Google Gmail 账户
- Gmail API OAuth 授权凭据
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
