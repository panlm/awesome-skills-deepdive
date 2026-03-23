# OpenCal

> Log meals, check nutrition progress, and manage calorie goals in the OpenCal app — hands-free via your AI agent. Use when the user mentions eating, food, calories, macros, or nutrition.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenCal |
| **作者** | neikfu |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/neikfu-opencal |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/neikfu/opencal |
| **安全评级** | 🟡 Medium |

## 功能概述
- Search results are per 100g — always scale before logging
- If the user doesn't mention an amount, ask — don't guess
- If search returns nothing, try shorter/simpler terms (e.g. "rice" instead of "steamed jasmine rice")
- Always confirm what you logged so the user can correct mistakes
- Rate limit: 100 requests/min

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23