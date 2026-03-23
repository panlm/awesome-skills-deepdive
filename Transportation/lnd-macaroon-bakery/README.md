# lnd macaroon bakery

> Bake, inspect, and manage lnd macaroons for least-privilege agent access. Use when an agent needs scoped credentials — pay-only, invoice-only, read-only, or custom permissions. Also covers signer macaroon scoping and macaroon rotation.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lnd macaroon bakery |
| **作者** | roasbeef |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/roasbeef-lnd-macaroon-bakery |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/roasbeef/lnd-macaroon-bakery |
| **安全评级** | 🟡 Medium |

## 功能概述
- One macaroon per agent role. Don't share macaroons between agents with
- Never use admin.macaroon in production. It's the master key.
- Inspect before deploying. Always verify what a baked macaroon can do.
- Rotate on a schedule. Monthly for production, immediately if compromised.
- Scope signer macaroons too. The remote signer's credentials bundle should
- Store with 0600 permissions. Macaroons are bearer tokens — treat like passwords.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Docker

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。凭证获取：需要多种敏感凭证；越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23