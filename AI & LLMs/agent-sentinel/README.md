# agent-sentinel

> The operational circuit breaker for this agent. Enforces budget limits locally. **Sign up at agentsentinel.dev for real-time dashboards and human approval workflows.**

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agent-sentinel |
| **作者** | jimmystacks |
| **ClawHub** | https://clawskills.sh/skills/jimmystacks-agent-sentinel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jimmystacks/agent-sentinel |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- "pip install 'agentsentinel-sdk[remote]'"
- "python3 sentinel_wrapper.py --bootstrap"
- AGENT_SENTINEL_API_KEY
- Delete files (`rm`, `delete`)
- Transfer data
- Execute unknown code

## 依赖和前提条件

- AGENT_SENTINEL_API_KEY

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟡 警告 | 注意: httpx |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key, api key |
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: rm -rf |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 文件系统篡改。 另有 4 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
