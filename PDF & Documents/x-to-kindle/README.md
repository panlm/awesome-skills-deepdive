# X To Kindle

> Send X/Twitter posts to Kindle for distraction-free reading. Use when user shares an X/Twitter link and wants to read it on Kindle, or asks to send a tweet/thread to their Kindle device.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | X To Kindle |
| **作者** | brianlu365ai |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/brianlu365ai-x-to-kindle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianlu365ai/x-to-kindle |
| **安全评级** | 🟡 Medium |

## 功能概述
- Gmail account with App Password (or other SMTP setup)
- Kindle email address (found in Amazon account settings)
- `send_to_kindle`: Send a local file to the configured Kindle email.
- `SMTP_EMAIL`: Your sender email (e.g., gmail)
- `SMTP_PASSWORD`: Your app password
- `KINDLE_EMAIL`: Your Kindle email address

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `send_to_kindle.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23