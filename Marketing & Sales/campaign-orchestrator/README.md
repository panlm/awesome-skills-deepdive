# Campaign Orchestrator

> Multi-channel follow-up campaign orchestrator for ShapeScale sales. Schedules and executes SMS + Email sequences with CRM logging and auto-termination on replies. Use when following up with demo leads or managing outreach campaigns.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Campaign Orchestrator |
| **作者** | kesslerio |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-campaign-orchestrator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/campaign-orchestrator |
| **安全评级** | 🔴 High |

## 功能概述
- Multi-channel: SMS (Dialpad) + Email (Gmail)
- Scheduled: Cron-based execution with configurable delays
- Personalized: Templates filled from Attio CRM data
- Auto-terminating: Replies stop all future scheduled steps
- Logged: All activities recorded in Attio
- Dialpad webhook is configured to hit this server

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `campaign.py`
- `post-demo.md`
- `primary.md`
- `re-engagement.md`
- `secondary.md`
- `webhook_handler.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23