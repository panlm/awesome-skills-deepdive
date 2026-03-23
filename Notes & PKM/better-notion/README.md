# Better Notion

> Full CRUD for Notion pages, databases, and blocks. Create, read, update, delete, search, and query.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Better Notion |
| **作者** | tyler6204 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-better-notion |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/better-notion |
| **安全评级** | 🟡 Medium |

## 功能概述
- Databases = "data sources" in API
- Use `data_source_id` for both creating pages and querying
- Get `data_source_id` from search results (the `id` field)
- Rate limit: ~3 req/sec

## 使用场景
- 管理 Notion 数据库和页面
- 自动化笔记整理
- 构建个人知识库

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23