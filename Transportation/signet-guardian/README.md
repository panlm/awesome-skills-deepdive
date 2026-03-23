# Signet Guardian

> "Payment guard middleware for AI agents. Use whenever any skill is about to initiate a payment. Runs a preflight check against the user's policy (payments enabled, per-transaction limit, monthly cap). Returns ALLOW, DENY, or CONFIRM_REQUIRED. Other payment-capable skills must call signet-preflight before proceeding and signet-record after a successful payment."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Signet Guardian |
| **作者** | rafalzacher1 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/rafalzacher1-signet-guardian |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rafalzacher1/signet-guardian |
| **安全评级** | 🟡 Medium |

## 功能概述
- Preflight — Check if a payment is allowed (ALLOW / DENY / CONFIRM_REQUIRED).
- Record — Append a completed payment to the ledger (enforces monthly cap under lock).
- Report — View spending for today or month.
- Policy — Show or edit limits and rules.
- `tsx` (used via `npx`, or install locally)
- `plugins.entries.signet-guardian.config.policy`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `docs`
- `openclaw-extension`
- `package.json`
- `pnpm-lock.yaml`
- `references`
- `scripts`
- `test-guardian.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23