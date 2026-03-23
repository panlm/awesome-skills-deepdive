# health-sync

> Analyze synced health data across Oura, Withings, Hevy, Strava, WHOOP, and Eight Sleep.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | health-sync |
| **作者** | filipe-m-almeida |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/filipe-m-almeida-health-sync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/filipe-m-almeida/health-sync |
| **安全评级** | 🟡 Medium |

## 功能概述
- workspace/health-sync/health-sync.toml
- workspace/health-sync/.health-sync.creds
- workspace/health-sync/health.sqlite
- User asks for health-sync setup, auth, sync, provider status, or remote bootstrap onboarding
- User asks about sleep, recovery, training, activity, your health, or cross-provider trends
- How did I sleep last night?

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `agents`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。凭证获取：需要多种敏感凭证；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23