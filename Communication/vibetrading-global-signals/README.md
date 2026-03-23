# vibetrading-global-signals

> Query AI-generated trading signals from vibetrading-datahub. Signals are produced by autonomous agents analyzing whale activity, news, funding rates, and technical indicators.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | vibetrading-global-signals |
| **作者** | liuhaonan00 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/liuhaonan00-vibetrading-global-signals |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liuhaonan00/vibetrading-global-signals |
| **安全评级** | 🟡 Medium |

## 功能概述
- 📡 Query latest signals for multiple symbols
- 🎯 Get signals by specific symbol
- 🔍 Filter by signal type (WHALE_ACTIVITY, NEWS_ANALYSIS, etc.)
- ⏰ Time-based filtering
- 📊 Beautiful console output with sentiment analysis

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23