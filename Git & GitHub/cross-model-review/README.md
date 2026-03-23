# Cross Model Review

> Adversarial plan review using two different AI models. Supports static mode (fixed roles) and alternating mode (models swap writer/reviewer each round, fully autonomous). Use when building features touching auth/payments/data models, or plans >1hr to implement. NOT for simple fixes, research tasks, or quick scripts.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cross Model Review |
| **作者** | don-gbot |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/don-gbot-cross-model-review |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/don-gbot/cross-model-review |
| **安全评级** | 🔴 High |

## 功能概述
- Simple one-file fixes or quick scripts
- Pure research or investigation tasks
- Changes you can fully reverse in under 5 minutes
- Plans already reviewed by a human engineer in the last hour
- Node.js >= 18.0.0 (uses `structuredClone`, `fs.readSync` on fd 0, etc.)
- OpenClaw — the skill is invoked by the OpenClaw agent and relies on `sessions_spawn` for the reviewer

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `SECURITY.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`
- `templates`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，4 项中风险。命令执行：发现直接命令执行指令；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23