# Garmin Cli

> Access Garmin Connect health, fitness, and activity data via a non-interactive CLI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Garmin Cli |
| **作者** | voydz |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/voydz-garmin-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/voydz/garmin-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- `today` — current date
- `yesterday` — previous date
- `week` — last 7 days (returns a date range)
- `month` — last 30 days (returns a date range)
- `YYYY-MM-DD` — specific date
- `--format json` for machine-readable output (default: `table`)

## 使用场景
- 同步和分析运动数据
- 追踪健康指标趋势
- 生成健身报告和洞察

## 依赖和前提条件
- Homebrew

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
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23