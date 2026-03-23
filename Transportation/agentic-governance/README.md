# Agentic Governance

> Keep your constraints healthy — lifecycle management with automatic staleness detection

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agentic Governance |
| **作者** | leegitw |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/leegitw-agentic-governance |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/agentic-governance |
| **安全评级** | 🟡 Medium |

## 功能概述
- .openclaw/governance.yaml
- .claude/governance.yaml
- output/governance/
- output/constraints/
- agentic/INDEX.md
- `leegitw/constraint-engine` (for constraint data)

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。Prompt 注入：发现 Prompt 注入特征

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23