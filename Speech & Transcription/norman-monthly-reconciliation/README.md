# monthly-reconciliation

> AI 辅助月度财务对账

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | monthly-reconciliation |
| **作者** | stanlee000 |
| **ClawHub** | https://clawskills.sh/skills/stanlee000-norman-monthly-reconciliation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stanlee000/norman-monthly-reconciliation |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- norman-finance
- Call `search_transactions` for the specified month (or last month if not specified)
- Identify uncategorized transactions
- For each batch, suggest categories and let the user confirm
- Use `categorize_transaction` to assign the correct bookkeeping category
- After all transactions are categorized, verify each one using `change_transaction_verification`

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23