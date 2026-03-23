# E-Commerce Price Monitor & Competitive Intel

> This skill enables Claude to monitor and track **product prices across major e-commerce platforms**

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | E-Commerce Price Monitor & Competitive Intel |
| **作者** | g4dr |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/g4dr-ecommerce-price-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g4dr/ecommerce-price-monitor |
| **安全评级** | 🔴 High |

## 功能概述
- Monitor product prices on Amazon, Zalando, eBay, AliExpress, and more
- Track price history and detect drops, spikes, and promotions
- Compare prices for the same product across multiple retailers
- Trigger repricing alerts when a competitor changes their price
- Build structured price datasets for dashboards and analytics
- Schedule recurring runs for continuous price surveillance

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23