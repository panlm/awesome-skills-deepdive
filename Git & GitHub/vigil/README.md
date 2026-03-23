# Vigil

> AI agent safety guardrails for tool calls. Use when (1) you want to validate agent tool calls before execution, (2) building agents that run shell commands, file operations, or API calls, (3) adding a safety layer to any MCP server or agent framework, (4) auditing what your agents are doing. Catches destructive commands, SSRF, SQL injection, path traversal, data exfiltration, prompt injection, and credential leaks. Requires npm package vigil-agent-safety (12.3KB, under 2ms latency). Source: github.com/hexitlabs/vigil

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Vigil |
| **作者** | robinoppenstam |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/robinoppenstam-vigil |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/robinoppenstam/vigil |
| **安全评级** | 🟡 Medium |

## 功能概述
- Destructive commands (rm -rf, mkfs, reverse shells) → BLOCK
- SSRF (metadata endpoints, localhost, internal IPs) → BLOCK
- Data exfiltration (curl to external, .ssh/id_rsa access) → BLOCK
- SQL injection (DROP TABLE, UNION SELECT) → BLOCK
- Path traversal (../../../etc/shadow) → BLOCK
- Prompt injection (ignore instructions, [INST] tags) → BLOCK
- Encoding attacks (base64 decode, eval(atob())) → BLOCK
- Credential leaks (API keys, AWS keys, tokens) → ESCALATE

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，6 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23