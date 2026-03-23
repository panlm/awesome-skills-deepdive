# BotSee

> Bot 监控和可视化工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BotSee |
| **作者** | grahac |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/grahac-botsee |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/grahac/botsee |
| **安全评级** | 🟡 Medium |

## 功能概述
- Bot 运行状态监控
- 性能数据可视化
- 错误追踪和告警
- 运行日志分析

## 使用场景
- 实时监控 Bot 运行状态和性能指标
- 可视化分析 Bot 的运行数据和趋势

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Stripe
- GitHub API
- HubSpot API

## 包含文件
- `.claude-plugin`
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`
- `skills`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23