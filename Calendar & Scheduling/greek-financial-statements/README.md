# Greek Financial Statements

> Greek financial statement generation — P&L, balance sheets, VAT summaries with EGLS integration. Completeness gates prevent partial outputs.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Greek Financial Statements |
| **作者** | satoshistackalotto |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-greek-financial-statements |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/greek-financial-statements |
| **安全评级** | 🟡 Medium |

## 功能概述
- Completeness First: Never generate a statement with incomplete source data — halt and report blockers
- ΕΓΛΣ Native: All accounts classified per Greek Chart of Accounts standards
- Versioned & Immutable: Once issued, a statement is never overwritten — amendments create new versions
- Bilingual Output: Greek labels for client-facing documents, English for internal use
- Balance Sheet Must Balance: Assets must equal equity plus liabilities — halt on any mismatch
- Human Oversight: All generated statements are drafts until a senior accountant reviews and issues them

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 包含文件
- `EVALS.json`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23