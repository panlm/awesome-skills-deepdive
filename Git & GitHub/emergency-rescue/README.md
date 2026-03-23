# Emergency Rescue Kit

> Recover from developer disasters. Use when someone force-pushed to main, leaked credentials in git, ran out of disk space, killed the wrong process, corrupted a database, broke a deploy, locked themselves out of SSH, lost commits after a bad rebase, or hit any other "oh no" moment that needs immediate, calm, step-by-step recovery.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Emergency Rescue Kit |
| **作者** | gitgoodordietrying |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/gitgoodordietrying-emergency-rescue |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/emergency-rescue |
| **安全评级** | 🔴 High |

## 功能概述
- Someone force-pushed to main and overwrote history
- Credentials were committed to a public repository
- A rebase or reset destroyed commits you need
- Disk is full and nothing works
- A process is consuming all memory or won't die
- A database migration failed halfway through

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- Docker
- macOS
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 8 项高风险，0 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23