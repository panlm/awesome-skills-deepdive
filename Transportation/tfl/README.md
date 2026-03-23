# TfL London Transit

> London TfL transit — real-time Tube arrivals, bus predictions, line status, service disruptions, journey planning, and route info for the London Underground, DLR, Overground, Elizabeth line, and buses. Use when the user asks about London public transport, Tube times, bus arrivals, or TfL service status.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TfL London Transit |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-tfl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/tfl |
| **安全评级** | 🔴 High |

## 功能概述
- Real-time Tube arrivals — know exactly when the next train comes
- Bus predictions — see when your bus will arrive at your stop
- Line status at a glance — check all Tube lines in one command
- Disruption alerts — know about delays, closures, and planned work
- Journey planning — step-by-step directions with fare estimates
- Stop and route lookup — find the nearest stop or explore a route's path

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `CLAUDE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23