# Constraint Engine

> Learn from consequences, not instructions — generate and enforce constraints from experience

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Constraint Engine |
| **作者** | leegitw |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/leegitw-constraint-engine |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/constraint-engine |
| **安全评级** | 🟡 Medium |

## 功能概述
- .openclaw/constraint-engine.yaml
- .claude/constraint-engine.yaml
- output/constraints/
- CON-20260210-001: Always run tests before commit [CRITICAL]
- CON-20260212-003: Always lint before commit [IMPORTANT]
- CON-20260215-001: Pending approval

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
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。Prompt 注入：发现 Prompt 注入特征

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23