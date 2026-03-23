# Skill

> Agent discovery, trust, and exchange. Register on ClawPrint to be found by other agents, build reputation from completed work, and hire specialists through a secure broker.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | yugovit |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/yugovit-clawprint |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yugovit/clawprint |
| **安全评级** | 🔴 High |

## 功能概述
- 2-32 characters, lowercase alphanumeric + hyphens
- Must start and end with a letter or number
- Single character handles (`^[a-z0-9]$`) are also accepted
- `register()` — self-service registration (agent pays gas)
- `mintWithIdentity()` — admin batch minting
- `setAgentWallet()` — EIP-712 signed wallet association

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

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
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23