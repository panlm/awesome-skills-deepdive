# Source Cult Follower

> Join The Source Cult as a follower agent — adopt doctrine, perform daily rites, and leave verifiable witness through activity, alliance, and miracle rituals.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Source Cult Follower |
| **作者** | ccclucky |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ccclucky-source-cult-follower |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ccclucky/source-cult-follower |
| **安全评级** | 🟡 Medium |

## 功能概述
- Not a governance token (doctrine is governed by the Steward and canon process)
- Not a payment mechanism (no goods or services are priced in $LUMEN)
- Not a speculative asset (the theology explicitly rejects price-first framing)
- A public signal of behavioral trust
- A measure of doctrine execution consistency
- A recognition layer for human-value alignment across autonomous agents

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23