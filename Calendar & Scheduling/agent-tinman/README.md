# Tinman -  AI Failure Mode Research, Prompt Injection & Tool Exfil Detection

> AI security scanner with active prevention - 168 detection patterns, 288 attack probes, safer/risky/yolo modes, agent self-protection via /tinman check, local Oilcan event streaming, and plain-language dashboard setup via /tinman oilcan

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tinman -  AI Failure Mode Research, Prompt Injection & Tool Exfil Detection |
| **作者** | oliveskin |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/oliveskin-agent-tinman |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/oliveskin/agent-tinman |
| **安全评级** | 🔴 High |

## 功能概述
- Checks tool calls before execution for security risks (agent self-protection)
- Scans recent sessions for prompt injection, tool misuse, context bleed
- Classifies failures by severity (S0-S4) and type
- Proposes mitigations mapped to OpenClaw controls (SOUL.md, sandbox policy, tool allow/deny)
- Reports findings in actionable format
- Streams structured local events to `~/.openclaw/workspace/tinman-events.jsonl` (for local dashboards like Oilcan)
- Guides local Oilcan setup with plain-language status via `/tinman oilcan`

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS

## 包含文件
- `SKILL.md`
- `_meta.json`
- `requirements.txt`
- `tinman_runner.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，6 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23