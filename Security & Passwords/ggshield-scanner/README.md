# ggshield-scanner

> 使用 GitGuardian ggshield 扫描代码中的密钥泄露

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ggshield-scanner |
| **作者** | amascia-gg |
| **ClawHub** | https://clawskills.sh/skills/amascia-gg-ggshield-scanner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/amascia-gg/ggshield-scanner |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- This is NOT a CLI tool you run in the terminal. Instead, you ask your AI agent to use it:
- AWS Access Keys, GCP Service Accounts, Azure credentials
- API tokens (GitHub, Slack, Stripe, OpenAI, etc.)
- Database passwords and connection strings
- Private encryption keys and certificates
- OAuth tokens and refresh tokens

## 依赖和前提条件
- This is NOT a CLI tool you run in the terminal.** Instead, you ask your AI agent to use it:
- Example conversation:**
- Returns user-friendly messages** - With emoji indicators (✅ ❌ 🔍)

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `ggshield_skill.py` — 脚本文件
- `pyproject.toml` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23