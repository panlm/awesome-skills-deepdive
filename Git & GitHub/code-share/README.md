# Code Share

> Share code via GitHub Gist instead of inline chat blocks. Use when code output exceeds 10 lines, when the user asks for copy-friendly code sharing in Discord/chat, or when preserving formatting is important.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Code Share |
| **作者** | jeromestein |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jeromestein-code-share |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeromestein/code-share |
| **安全评级** | 🟡 Medium |

## 功能概述
- Verify GitHub CLI auth: `gh auth status`
- If not authenticated (or missing gist scope), ask user to run: `gh auth login`
- Keep behavior simple: do not auto-fallback to alternate sharing backends by default; prefer guiding user to configure Gi
- Never include API keys, tokens, passwords, private keys, cookies, session IDs, webhook secrets, phone/email PII, or abso
- If code requires secrets, replace with placeholders, for example:
- `API_KEY="<FILL_ME>"`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

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
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23