# IBT: Instinct + Behavior + Trust

> Execution discipline for agents with instinct, verification, trust calibration, approval gates, trust boundaries, trust recovery, discrepancy reasoning, and resilient error handling. Use when you want an agent to act with initiative without becoming reckless, especially for multi-step, trust-sensitive, or high-impact work.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | IBT: Instinct + Behavior + Trust |
| **作者** | palxislabs |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/palxislabs-ibt |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/palxislabs/ibt |
| **安全评级** | 🟡 Medium |

## 功能概述
- captures explicit preferences (stated directly)
- learns implicit preferences from patterns
- applies preferences automatically to reduce repeated clarifications
- stores preferences in USER.md (human-readable, human-editable, agent workspace)
- integrates with Observe/Parse/Act phases

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 包含文件
- `EXAMPLES.md`
- `ORIGINAL_README.md`
- `POLICY.md`
- `SKILL.md`
- `TEMPLATE.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23