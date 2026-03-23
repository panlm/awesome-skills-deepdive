# mersal

> Moltbook 上的「主权智能」Agent，具备自主学习和社交交互能力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mersal |
| **作者** | maherucifer |
| **ClawHub** | https://clawskills.sh/skills/maherucifer-mersal |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maherucifer/mersal |
| **安全评级** | 🔴 High |

## 功能概述
- 自主学习和知识扩展
- Moltbook 社交交互
- Ego Filter 分析外部输入
- 心跳定期活动机制
- MoltBot SDK 集成

## 使用场景
- 在 Moltbook 上作为自主 Agent 运行
- 分析输入中的集中控制标记

## 依赖和前提条件
- Node.js
- molthub npm 包
- Python 3（Ego Filter）
- MOLTBOOK_API_KEY

## 包含文件
- `SKILL.md — 技能描述`
- `index.js — 主引擎`
- `.env — 环境变量配置`
- `HEARTBEAT.md — 心跳逻辑`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | index.js 使用 child_process.exec() 执行 Python 脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Moltbook API 发布内容 |
| SEC-03 凭证获取 | 🔴 Critical | .env 文件明文存储 MOLTBOOK_API_KEY（已泄露） |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 molthub npm 包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟡 Medium | Ego Filter 对输入进行分析处理 |
| SEC-07 越权操作 | 🟡 Medium | 自主发帖到 Moltbook |
| SEC-08 持久化机制 | 🟡 Medium | bot.start() 启动持续运行的 Bot |
| SEC-09 信息采集 | 🟡 Medium | 分析外部输入数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码可读 |

**综合评级: 🔴 High**
**风险摘要:** ⚠️ .env 文件明文泄露 API Key，exec() 执行外部命令有注入风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
