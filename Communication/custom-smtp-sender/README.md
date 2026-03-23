# Custom Smtp Sender

> A skill to send emails with support for markdown, HTML text, and attachments, leveraging existing SMTP configuration in `/home/bb/.openclaw/smtp-config.json`. Includes retry logic and logging.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Custom Smtp Sender |
| **作者** | scccmsd |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/scccmsd-custom-smtp-sender |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/scccmsd/custom-smtp-sender |
| **安全评级** | 🟢 Low |

## 功能概述
- HTML/Markdown support: Compose emails using markdown converted to HTML.
- Attachments: Include one or more files easily.
- Retries: Attempts to resend in case of temporary failures.
- Logging: Maintains a log of sent emails and errors for auditing.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `email_sender.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23