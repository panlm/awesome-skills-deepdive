# Confidant

> Secure secret handoff and credential setup wizard for AI agents. Use when you need sensitive information from the user (API keys, passwords, tokens) or need to save credentials to config files. Never ask for secrets via chat — use Confidant instead.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Confidant |
| **作者** | ericsantos |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ericsantos-confidant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ericsantos/confidant |
| **安全评级** | 🔴 High |

## 功能概述
- ✅ Starts server if not running (or reuses existing one)
- ✅ Creates a secure request with web form
- ✅ Detects existing tunnels (ngrok or localtunnel)
- ✅ Returns the URL to share with the user
- ✅ Polls until the secret is submitted
- ✅ Saves to `~/.config/openai/api_key` (chmod 600) and exits

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23