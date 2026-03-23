# Ecommerce Price Watcher

> 跨电商平台商品价格监控工具，在降价促销或达到目标价格时自动发出警报通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ecommerce Price Watcher |
| **作者** | pbalajiips |
| **版本** | 1.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/pbalajiips-ecommerce-price-watcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pbalajiips/ecommerce-price-watcher |
| **安全评级** | 🟢 Low |

## 功能概述
- 跨多个电商平台追踪商品价格
- 设定目标价格触发警报
- 价格历史曲线记录与分析
- 促销活动和优惠券自动检测
- 支持多商品同时监控
- 价格变动实时通知推送

## 使用场景
- 等待心仪商品降价时的自动价格监控
- 比较不同电商平台的同款商品价格
- 追踪电子产品或大件商品的价格走势

## 依赖和前提条件
- OpenClaw 环境已配置
- 目标商品的电商页面链接

## 包含文件
- `README.md`
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
