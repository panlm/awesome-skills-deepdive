# Get a clank.money Human Bitcoin Address

> Agent-first service to register and manage Human Bitcoin Addresses (BIP-353) on clank.money with L402 bitcoin payments.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Get a clank.money Human Bitcoin Address |
| **作者** | matbalez |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/matbalez-get-hba |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matbalez/get-hba |
| **安全评级** | 🟡 Medium |

## 功能概述
- `managementToken` is returned after successful paid registration (`201` or `202`).
- You must save `managementToken` immediately and securely.
- CRITICAL: If the token is lost, future updates to that address cannot be authenticated.
- `POST https://clank.money/api/v1/registrations`
- `GET https://clank.money/api/v1/registrations/{username}`
- `PATCH https://clank.money/api/v1/registrations/{username}`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23