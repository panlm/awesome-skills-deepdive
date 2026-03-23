# Translink CLI

> Query, troubleshoot, and explain Translink SEQ GTFS static + realtime data using local translink_* commands or plugin slash commands. Use for schedule lookups, stop/route/trip joins, vehicle/trip realtime checks, alerts, schema drift review, PK/FK reasoning, and paginated filtering.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Translink CLI |
| **作者** | alanburchill |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/alanburchill-translink-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alanburchill/translink-cli |
| **安全评级** | 🟢 Low |

## 功能概述
- CLI repo: `https://github.com/alanburchill/traslink-cli-scripts`
- Expected commands: `translink_*` (or equivalent wrappers that expose the same command names)
- Shell CLI: `translink_*`
- Plugin slash commands: `/translink_*` and `/translink <command> [args...]`
- `--where field=value` (repeatable)
- `--contains field=text` (repeatable)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23