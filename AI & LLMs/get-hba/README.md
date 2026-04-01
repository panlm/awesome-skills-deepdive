# get-hba

> Agent-first service to register and manage Human Bitcoin Addresses (BIP-353) on clank.money with L402 bitcoin payments.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | get-hba |
| **作者** | matbalez |
| **ClawHub** | https://clawskills.sh/skills/matbalez-get-hba |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matbalez/get-hba |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- `managementToken` is returned after successful paid registration (`201` or `202`).
- You must save `managementToken` immediately and securely.
- CRITICAL: If the token is lost, future updates to that address cannot be authenticated.
- `POST https://clank.money/api/v1/registrations`
- `GET https://clank.money/api/v1/registrations/{username}`
- `PATCH https://clank.money/api/v1/registrations/{username}`

## 依赖和前提条件

- TOKEN_FILE="$HOME/.clank/${USERNAME}.management_token

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
