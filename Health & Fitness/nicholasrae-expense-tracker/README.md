# Expense Tracker

> 个人支出跟踪和预算管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expense Tracker |
| **作者** | nicholasrae |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/nicholasrae-nicholasrae-expense-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicholasrae/nicholasrae-expense-tracker |
| **安全评级** | 🟡 Medium |

## 功能概述
- Natural language logging — "spent $45 at Costco" just works
- Auto-categorization — matches vendors to 16 categories using keyword lists
- Budget tracking — set monthly limits, get warned when you're close
- Reports — weekly and monthly spending summaries with trends
- Refunds & corrections — handles negative amounts, edits, and deletions
- Smart parsing — understands "yesterday", split bills, approximate amounts

## 使用场景
- 记录和分类每日支出
- 设定和跟踪月度预算目标
- 分析消费模式和节省建议

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `templates`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。命令执行：发现直接命令执行指令

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
