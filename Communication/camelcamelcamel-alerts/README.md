# CamelCamelCamel Alerts

> 监控 CamelCamelCamel 亚马逊商品价格下降提醒，通过 RSS 推送 Telegram 实时通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CamelCamelCamel Alerts |
| **作者** | jgramajo4 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jgramajo4-camelcamelcamel-alerts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jgramajo4/camelcamelcamel-alerts |
| **安全评级** | 🔴 High |

## 功能概述
- 监控 CamelCamelCamel 价格追踪 RSS 源
- 价格下降时自动推送 Telegram 通知
- 支持多商品同时监控
- 自定义价格阈值触发提醒
- 历史价格趋势数据展示

## 使用场景
- 购物达人自动追踪心愿单商品降价并即时收到通知
- 电商运营监控竞品价格变动及时调整策略
- 节俭用户设置目标价格等待最佳购买时机

## 依赖和前提条件
- 拥有 CamelCamelCamel 账户并配置价格追踪
- 配置 Telegram Bot Token
- 设置目标 Telegram 聊天频道

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
