# Daily Business Report

> OpenClaw 每日业务报告生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Daily Business Report |
| **作者** | mariusfit |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/mariusfit-oc-daily-business-report |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mariusfit/oc-daily-business-report |
| **安全评级** | 🟢 Low |

## 功能概述
- Multi-Source Aggregation — Weather, crypto, news, system stats, inspirational quotes
- Free APIs — No API keys required for core functionality
- Configurable — Set your city, preferred cryptocurrencies, news country
- Multiple Formats — Text, JSON, Markdown output
- Cron-Ready — Designed for scheduled OpenClaw execution
- No Dependencies — Pure Python, uses stdlib urllib

## 使用场景
- 自动生成每日业务数据报告
- 汇总关键业务指标和趋势
- 发送报告到指定渠道

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
