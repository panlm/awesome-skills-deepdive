# Vincent - Credentials

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Vincent - Credentials |
| **作者** | glitch003 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/glitch003-vincent-credentials |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/glitch003/vincent-credentials |
| **安全评级** | 🔴 High |

## 功能概述
- ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials
- Creation: The agent runs `secret create` with `--type CREDENTIALS` — the CLI stores the API key automatically and return
- Value set: The user sets the credential value via the dashboard after claiming, or the agent sets it via the CLI.
- Write to .env: The agent runs `secret env` to write the value to a `.env` file without exposing it.
- Claim: The human operator uses the claim URL to take ownership and manage the secret from the dashboard.
- Revocation: The secret owner can revoke the agent's API key at any time from `https://heyvincent.ai`.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23