# ACC Error Memory

> "Error pattern tracking for AI agents. Detects corrections, escalates recurring mistakes, learns mitigations. The 'something's off' detector from the AI Brain series."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ACC Error Memory |
| **作者** | impkind |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/impkind-acc-error-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/impkind/acc-error-memory |
| **安全评级** | 🔴 High |

## 功能概述
- Detects when users correct or express frustration
- Logs error patterns with context and mitigations
- Escalates recurring patterns (normal → warning → critical)
- Resolves patterns that haven't recurred in 30+ days

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23