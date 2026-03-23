# Context Scope Tags

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Context Scope Tags |
| **作者** | phenomenoner |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/phenomenoner-context-scope-tags |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/phenomenoner/context-scope-tags |
| **安全评级** | 🟢 Low |

## 功能概述
- `[ISO: <topic>]` fresh slate for this message (no prior project/topic context)
- `[SCOPE: <topic>]` restrict to one named scope
- `[GLOBAL]` cross-topic reuse allowed (call out what was reused)
- `[NOMEM]` do not store long-term memory from this exchange
- `[REM]` persist preferences/decisions (requires a memory backend; otherwise advisory)
- `[ISO: marketing][NOMEM] Draft 5 ad angles for OpenClaw; don't store memory.`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23