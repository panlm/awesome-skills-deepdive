# Search recent repo activities

> "Fetch recent GitHub activity from the Nom feed"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Search recent repo activities |
| **作者** | lws803 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lws803-nom-feed |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lws803/nom-feed |
| **安全评级** | 🟡 Medium |

## 功能概述
- If the first argument looks like `org/repo` (contains `/`), use the repo feed at `/api/feed/{org}/{repo}`
- Otherwise use the global feed at `/api/feed`
- `--search TEXT` — free-text search (full-text on title/summary)
- `--type TYPE` — filter by event type: `pull_request`, `issue`, `release`, `push`
- `--org ORG` — filter by GitHub org (global feed only)
- `--from DATE` / `--to DATE` — date range (ISO 8601, e.g. 2026-01-01) (global feed only)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

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
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23