# mantis-manager

> Manage Mantis Bug Tracker (issues, projects, users, filters, configs) via the official Mantis REST API. Supports full CRUD operations on issues, projects, users, attachments, notes, tags, relationships, and configuration management. Features dynamic instance switching with context-aware base URL and token resolution.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mantis-manager |
| **作者** | willykinfoussia |
| **ClawHub** | https://clawskills.sh/skills/willykinfoussia-mantis-manager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/willykinfoussia/mantis-manager |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- Switch between multiple Mantis instances dynamically
- Test against staging/production environments
- Work with different client instances without changing config
- `{{MANTIS_BASE_URL}}` refers to the **resolved base URL** (could be temporary_base_url, user_base_url, or env MANTIS_BASE_URL)
- `{{resolved_token}}` refers to the **resolved token** (could be temporary_token, user_token, or env MANTIS_API_TOKEN)
- All endpoints use the pattern: `{{MANTIS_BASE_URL}}/resource/path`

## 依赖和前提条件

- {"openclaw":{"emoji":"🐞","requires":{"env":["MANTIS_BASE_URL","MANTIS_API_TOKEN"]},"primaryEnv":"MANTIS_API_TOKEN
- `temporary_token
- `user_token

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
