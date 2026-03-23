# Apify Competitor Intelligence

> Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apify Competitor Intelligence |
| **作者** | protoss70 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/protoss70-apify-competitor-intelligence |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/protoss70/apify-competitor-intelligence |
| **安全评级** | 🟡 Medium |

## 功能概述
- `APIFY_TOKEN` configured in OpenClaw settings
- `mcpc` CLI (auto-installed via skill metadata)
- ACTOR_ID: Must be either a technical name (`owner/actor-name` — alphanumeric, hyphens, dots, one slash) or a raw ID (exa
- SEARCH_KEYWORDS: Plain text words only. Reject shell metacharacters.
- JSON_INPUT: Must be valid JSON. Must not contain single quotes (use escaped double quotes). Validate structure before us
- Output filenames: Must match `YYYY-MM-DD_descriptive-name.{csv,json}`. No path separators (`/`, `..`), no spaces, no met

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reference`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23