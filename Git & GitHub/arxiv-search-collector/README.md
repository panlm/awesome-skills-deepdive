# Arxiv Search Collector

> "Model-driven arXiv retrieval workflow for building a paper set with a manual language parameter: initialize a run, fetch metadata for each model-designed query, let the model filter irrelevant items per query by keep indexes, then merge and dedupe into per-paper metadata directories. Use when query planning and relevance filtering should be done by the model, not rule-based heuristics."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arxiv Search Collector |
| **作者** | xukp20 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/xukp20-arxiv-search-collector |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xukp20/arxiv-search-collector |
| **安全评级** | 🟡 Medium |

## 功能概述
- `--language` must be set manually for each collection run.
- Use the same language value across all collector scripts for consistency.
- If `--language` is non-English (for example `Chinese`), generated markdown files are written in that language:
- `task_meta.md`
- `query_results/<label>.md`
- `<arxiv_id>/metadata.md`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `agents`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23