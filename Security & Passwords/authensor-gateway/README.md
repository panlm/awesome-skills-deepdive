# Authensor Gateway

> Authensor 认证网关 — 安全身份验证服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Authensor Gateway |
| **作者** | authensor |
| **ClawHub** | https://clawskills.sh/skills/authensor-authensor-gateway |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/authensor/authensor-gateway |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- CONTROL_PLANE_URL
- AUTHENSOR_API_KEY
- CONTROL_PLANE_URL
- AUTHENSOR_API_KEY
- Low-risk actions (read files, search, grep) — run automatically
- High-risk actions (write files, run commands, network requests) — require your approval

## 依赖和前提条件
- Run marketplace skills you didn't write.** Third-party skills can execute Bash, write files, and make network requests. [ClawHavoc](https://snyk.io/blog/clawhavoc) found 341 malicious skills on ClawHub — Authensor gates every tool call before it runs.
- Want approval before destructive actions.** Instead of blanket-allowing or blanket-denying, you choose which actions need your sign-off.
- Need an audit trail.** Every action (allowed, denied, or pending) is logged with a receipt ID and timestamp.
- Work in regulated environments.** Authensor provides evidence of human-in-the-loop oversight for compliance.
- If the control plane is unreachable, the agent is instructed to deny all actions (fail-closed).**

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 包含高危系统命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件删除操作 |
| SEC-06 Prompt 注入 | 🔴 High | 检测到 Prompt 注入模式 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23