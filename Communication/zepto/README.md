# Zepto

> Order groceries from Zepto in seconds. Just say what you need, get a payment link on WhatsApp, pay on your phone, done. Remembers your usual items. Works across India where Zepto delivers.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zepto |
| **作者** | bewithgaurav |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/bewithgaurav-zepto |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bewithgaurav/zepto |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🏠 Address confirmation - Always checks before ordering
- 🧠 Remembers your usuals - Tracks what you order frequently
- 🛒 Smart cart - Adds all items, then shows summary
- 💳 Payment links - Pay securely via WhatsApp on your phone
- ✅ Order verification - Confirms when your order is on the way
- 🧹 Auto cleanup - Clears cart after each order

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `PARSER-USAGE.md`
- `PUBLISH_CHECKLIST.md`
- `SECURITY.md`
- `SKILL.md`
- `ZEPTO_AUTH.md`
- `_meta.json`
- `package.json`
- `test-ops.js`
- `zepto-agent.js`
- `zepto-ops.js`
- `zepto-parser.js`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23