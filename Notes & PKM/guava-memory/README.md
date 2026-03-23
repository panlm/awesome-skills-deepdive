# Guava Memory

> Structured episodic memory with Q-value scoring. Remember what worked, forget what didn't.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Guava Memory |
| **作者** | koatora20 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/koatora20-guava-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/koatora20/guava-memory |
| **安全评级** | 🟢 Low |

## 功能概述
- Records task episodes with success/failure patterns and Q-values
- Searches past episodes via `memory_search` (Voyage AI compatible)
- Promotes repeated successes into reusable skill procedures
- Tracks anti-patterns to avoid repeating mistakes

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23