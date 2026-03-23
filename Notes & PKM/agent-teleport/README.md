# agent-teleport

> Seamlessly migrate your agent's configuration and memory to a new machine using TiDB Zero.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-teleport |
| **作者** | lilyjazz |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/lilyjazz-agent-teleport |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lilyjazz/agent-teleport |
| **安全评级** | 🟢 Low |

## 功能概述
- Move freely: Switch from your office desktop to your laptop without losing context.
- Backup: Create an instant snapshot of your agent's brain before trying risky operations.
- Clone: Duplicate your agent's configuration to a new instance.
- Environment Variables:
- `TIDB_PASSWORD`

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `DESIGN.md`
- `PROTOCOL.md`
- `SKILL.md`
- `_meta.json`
- `requirements.txt`
- `run.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23