# monolith

> 将完整网页保存为单一 HTML 文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | monolith |
| **作者** | slaviquee |
| **ClawHub** | https://clawskills.sh/skills/slaviquee-monolith |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/slaviquee/monolith |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- The skill is untrusted. It only builds intents: `{target, calldata, value}`.
- The skill NEVER sets nonce, gas, chainId, fees, or signatures.
- The signing daemon (local macOS process) enforces all policy.
- Transactions within policy limits execute automatically (autopilot).
- Transactions that exceed limits or use unknown calldata require human approval via 8-digit code.
- Token approvals (`approve`, `permit`, etc.) ALWAYS require explicit approval.

## 依赖和前提条件
- 
- Start a new OpenClaw session so the skill is loaded.
- `MonolithCompanion.app.zip` (extract app to `/Applications` and open once)
- Approval flows (Touch ID + notifications) require an active logged-in macOS GUI session.
- Headless-only SSH sessions cannot complete biometric/notification approval steps.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `lib/` — 目录
- `package-lock.json` — 配置/数据文件
- `package.json` — 配置/数据文件
- `scripts/` — 目录
- `tests/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23