# Context Gatekeeper

> Keeps the conversation token-friendly by summarizing recent exchanges, surfacing pending actions, and delivering a compact briefing for each turn before calling the model. Trigger this skill whenever you need to prune a bloated thread or keep the next prompt lean.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Context Gatekeeper |
| **作者** | davienzomq |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/davienzomq-context-gatekeeper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davienzomq/context-gatekeeper |
| **安全评级** | 🟡 Medium |

## 功能概述
- Checks for an existing `auto_monitor.py` process (`pgrep -f auto_monitor.py`). If none exists, it launches the monitor w
- Designed to be called at startup (`STARTUP.md`) so the monitor automatically restarts after `/reset`, `/new`, or any reb
- Published as `context-gatekeeper@0.1.1` (latest release). The version bundle includes this README plus all scripts and c
- Author: Davi Marques. Repository slug: `context-gatekeeper`.
- Limit the history file to the essential RECENT exchanges that drive the next turn.
- Watch `/tmp/context-gatekeeper-monitor.log` for monitor errors or long pauses.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `context`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23