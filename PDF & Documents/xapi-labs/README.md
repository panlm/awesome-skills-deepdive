# xAPI

> Use xapi CLI to access real-time external data — Twitter/X profiles, tweets, and timelines, crypto token prices and metadata, web search, news, and AI text processing (summarize, rewrite, chat, embeddings). Trigger this skill whenever the user wants to look up a Twitter user, get tweet details, check crypto prices, search the web or news, generate embeddings, summarize or rewrite text, or call any third-party API through xapi. Also use this skill when the user mentions xapi, asks about available capabilities or APIs, or wants to discover what external services are accessible.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | xAPI |
| **作者** | glacier-luo |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/glacier-luo-xapi-labs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/glacier-luo/xapi-labs |
| **安全评级** | 🔴 High |

## 功能概述
- X API v2 (`x-official`) — Official Twitter/X API with 156 endpoints (tweets, users, spaces, lists, DMs, etc.)
- Reddit — Reddit API with 24 endpoints
- Ave Cloud Data API — Crypto data with 19 endpoints
- Twitter API — Alternative Twitter data API with 26 endpoints
- OpenRouter API — Multi-model AI API gateway
- Serper API — Google Search API with 10 endpoints

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key
- OAuth

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
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23