# Dr. Frankenstein

> "Give your agents soul."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Dr. Frankenstein |
| **作者** | brancante |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/brancante-dr-frankenstein |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brancante/dr-frankenstein |
| **安全评级** | 🟡 Medium |

## 功能概述
- Parent/child metadata (`parent`, lineage, stage)
- Stage-based tool presets and autonomy growth
- Child score model (`hunger`, `anger`, `fear`, `learning`, `protection`, `bonding`)
- Threshold engine + cron/event triggers
- Escalation and audit trail
- Cross-workspace visibility with safety boundaries

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `docs`
- `interview`
- `schema`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。越权操作：需要提权或管理员权限；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23