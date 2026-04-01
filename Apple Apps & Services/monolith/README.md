# monolith

> 综合性 macOS 系统管理和自动化工具

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | monolith |
| **作者** | slaviquee |
| **ClawHub** | https://clawskills.sh/skills/slaviquee-monolith |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/slaviquee/monolith |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **The skill is untrusted.** It only builds intents: `{target, calldata, value}`.
- The skill NEVER sets nonce, gas, chainId, fees, or signatures.
- The signing daemon (local macOS process) enforces all policy.
- Transactions within policy limits execute automatically (autopilot).
- Transactions that exceed limits or use unknown calldata require human approval via 8-digit code.
- Token approvals (`approve`, `permit`, etc.) ALWAYS require explicit approval.
- Transfers over per-tx or daily spending caps
- Transfers to non-allowlisted addresses

## 使用场景

Monolith is a crypto wallet for AI agents on macOS. Private keys are stored in Apple Secure Enclave and never exposed to the skill layer. Spending caps, an allowlist, and a default-deny policy engine control what agents can execute without human approval.

## 依赖和前提条件

- macOS 系统

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
