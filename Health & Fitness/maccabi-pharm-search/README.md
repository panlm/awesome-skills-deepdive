# maccabi-pharm-search

> Search for medications and check real-time stock availability at Maccabi pharmacies in Israel. Use when searching for drugs like "nurofen", "acamol/אקמול", "advil", or finding nearby pharmacy branches with stock. Supports Hebrew and English drug names. מכבי פארם, תרופות, מלאי, בית מרקחת.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | maccabi-pharm-search |
| **作者** | alexpolonsky |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/alexpolonsky-maccabi-pharm-search |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/maccabi-pharm-search |
| **安全评级** | 🟡 Medium |

## 功能概述
- "Which Maccabi pharmacies in Haifa have Nurofen in stock right now?"
- "I need Nurofen - where can I find it in Ramat Gan?"
- "Check if Acamol is available at any branch near me"

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23