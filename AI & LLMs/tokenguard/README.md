# TokenGuard

> API cost guardian for AI agents. Track spending, enforce limits, prevent runaway costs. Essential for any agent making paid API calls.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TokenGuard |
| **作者** | g0head |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/g0head-tokenguard |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g0head/tokenguard |
| **安全评级** | 🟡 Medium |

## 功能概述
- Session-based tracking — Costs reset daily (or on demand)
- Hard limits — Actions blocked when budget exceeded
- Pre-flight checks — Verify budget BEFORE expensive calls
- Override controls — Extend limits or bypass when needed
- Full audit trail — Every cost logged with timestamps
- `0` — Success / within budget

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。凭证获取：需要多种敏感凭证；Prompt 注入：发现 Prompt 注入特征

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23