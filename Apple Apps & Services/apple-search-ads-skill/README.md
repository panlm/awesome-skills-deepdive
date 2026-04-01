# apple-search-ads-skill

> 管理 Apple Search Ads 广告投放

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-search-ads-skill |
| **作者** | trebuhs |
| **ClawHub** | https://clawskills.sh/skills/trebuhs-apple-search-ads-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trebuhs/apple-search-ads-skill |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Config stored at `~/.asa-cli/config.yaml`, token cache at `~/.asa-cli/token_cache.json`
- Profiles: `asa-cli configure -p production --client-id "..." ...`, then `asa-cli campaigns list -p production`
- Env var overrides: `ASA_CLIENT_ID`, `ASA_TEAM_ID`, `ASA_KEY_ID`, `ASA_ORG_ID`, `ASA_PRIVATE_KEY_PATH`
- Always use `-o json` and pipe through `jq` when extracting specific fields
- For multi-org accounts, always include `--org-id` — run `asa-cli whoami -o json` to discover org IDs
- Fetch campaign/adgroup IDs first before operating on child resources
- Use `--all` on find commands to auto-paginate large result sets
- Reports require `--start-date` and `--end-date` in YYYY-MM-DD format

## 使用场景

Manage Apple Search Ads campaigns, ad groups, keywords, and reports through the asa-cli command-line tool. Covers the full Campaign Management API v5, including keyword bidding, negative keywords, and performance reports broken down by date, country, and device.

## 依赖和前提条件

- macOS 系统
- --start-time
- jq

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
asa-cli whoami                          # List all orgs (no --org-id needed)
asa-cli configure --client-id "..." --team-id "..." --key-id "..." --private-key-path "..."
asa-cli configure                       # Interactive mode
, bash
asa-cli campaigns list [--org-id <orgid>] [--limit N] [--offset N]
asa-cli campaigns get <id> [--org-id <orgid>]
asa-cli campaigns find [--org-id <orgid>] [--filter "status=ENABLED"] [--sort "name:asc"] [--limit N] [--all]
asa-cli campaigns create [--org-id <orgid>] --name "..." --budget 1000 --daily-budget 50 --countries US,GB --app-id 123456
asa-cli campaigns update <id> [--org-id <orgid>] [--name ...] [--budget ...] [--daily-budget ...] [--status ENABLED|PAUSED]
asa-cli campaigns delete <id> [--org-id <orgid>]
, bash
asa-cli adgroups list --campaign-id <id> [--org-id <orgid>]
asa-cli adgroups get <id> --campaign-id <id> [--org-id <orgid>]
asa-cli adgroups find --campaign-id <id> [--org-id <orgid>] [--filter "status=ENABLED"]
asa-cli adgroups create --campaign-id <id> [--org-id <orgid>] --name "..." --default-bid 1.50 --start-time "2026-01-01T00:00:00.000" [--cpa-goal 5.00] [--auto-keywords true|false]
asa-cli adgroups update <id> --campaign-id <id> [--org-id <orgid>] [--name ...] [--default-bid ...] [--status ...]
asa-cli adgroups delete <id> --campaign-id <id> [--org-id <orgid>]
 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟡 警告 | 有限系统信息采集: 系统用户/内核信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 3 项警告，无严重风险。执行 shell 命令: bash
asa-cli whoami                  

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
