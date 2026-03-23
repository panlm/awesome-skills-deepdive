# Ecommerce Price Watcher

> Track product prices across ecommerce sites and alert on offers or target-price hits. Use when a user wants to monitor one or many product URLs or item queries, compare current vs previous prices, detect discounts, and generate alert-ready summaries with product name, old/new price, percent drop, and direct link.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ecommerce Price Watcher |
| **作者** | pbalajiips |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/pbalajiips-ecommerce-price-watcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pbalajiips/ecommerce-price-watcher |
| **安全评级** | 🟢 Low |

## 功能概述
- `add`: add a single product URL
- `add-item`: discover product URLs from an item query, then add watches
- `list`: list watched products
- `check --id <id>`: check one product now
- `check --all`: check all products now
- `remove --id <id>`: delete watcher

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

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23