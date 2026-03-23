# Publora Threads

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Publora Threads |
| **作者** | sergebulaev |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/sergebulaev-publora-threads |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sergebulaev/publora-threads |
| **安全评级** | 🟡 Medium |

## 功能概述
- Single posts (text, images, videos, carousels)
- Standalone posts under 500 characters
- Connected via Meta OAuth — same account as Instagram
- 5 links per post max — Threads enforces this at the API level
- PNG supported — unlike Instagram, Threads accepts PNG images
- Threading restriction — see the notice at the top of this skill

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23