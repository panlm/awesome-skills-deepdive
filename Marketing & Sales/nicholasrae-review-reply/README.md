# App Store ReviewReply

> "Automatically monitors your App Store reviews and drafts warm, on-brand replies for 1–3 star reviews — so unhappy users hear back fast. Connects to App Store Connect API, detects repeat complaint patterns as bug signals, and delivers a daily approval queue to Telegram at 8am. You approve, it sends. Supports multiple apps simultaneously."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | App Store ReviewReply |
| **作者** | nicholasrae |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/nicholasrae-nicholasrae-review-reply |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicholasrae/nicholasrae-review-reply |
| **安全评级** | 🔴 High |

## 功能概述
- 🔍 Monitors reviews — polls App Store Connect every 4h across all your apps
- ✏️ Drafts replies — Claude writes warm, on-brand responses for 1–3★ reviews
- 🚨 Pattern alerts — same complaint 3+ times in 7 days → instant Telegram bug alert
- 📲 Daily queue — 8am Telegram digest with pending replies; approve/edit/reject inline
- 📤 Auto-posts — approved replies posted directly to App Store Connect
- 📊 Metrics — response rate, avg response time, rating trend per app

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip
- macOS
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23