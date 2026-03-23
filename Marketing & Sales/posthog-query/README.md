# PostHog Query

> Run SQL queries against PostHog product analytics data using the PostHog CLI. Use when checking pageviews, event counts, trends, or any analytics data from PostHog.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | PostHog Query |
| **作者** | quinlanjager |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/quinlanjager-posthog-query |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/quinlanjager/posthog-query |
| **安全评级** | 🟡 Medium |

## 功能概述
- `posthog-cli exp query editor` — interactive query editor
- `posthog-cli exp query check "<SQL>"` — syntax/type check without running
- Append `--debug` to `run` to get the full JSON response (columns, types, cache info)
- HogQL is ClickHouse-compatible SQL — standard ClickHouse functions apply
- Shell-escape `$` in event names: `'\$pageview'` or use double quotes carefully
- The `--debug` flag returns full metadata including column types and cache status

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23