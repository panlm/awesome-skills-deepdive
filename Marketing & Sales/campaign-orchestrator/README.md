# Campaign Orchestrator

> 营销活动编排和管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Campaign Orchestrator |
| **作者** | kesslerio |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-campaign-orchestrator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/campaign-orchestrator |
| **安全评级** | 🔴 High |

## 功能概述
- 多渠道营销活动编排
- 活动流程自动化
- 效果实时监控
- 活动数据分析

## 使用场景
- 编排和管理跨渠道的整合营销活动
- 自动化营销活动的执行和效果追踪

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Google API
- GitHub API
- Webhook 配置
- Attio CRM

## 包含文件
- `README.md`
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