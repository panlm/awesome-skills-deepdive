# Price Monitor FR

> 监控法国电商网站产品价格，价格下降时发出警报（法语界面）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Price Monitor FR |
| **作者** | hugosbl |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/hugosbl-price-monitor-fr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hugosbl/price-monitor-fr |
| **安全评级** | 🟢 Low |

## 功能概述
- 监控法国主流电商网站产品价格
- 检测价格下降并发送警报通知
- 追踪商品价格历史变化趋势
- 支持多个法国电商平台
- 法语界面和通知内容
- 自定义价格监控规则

## 使用场景
- 等待心仪商品降价时自动提醒
- 比较法国电商平台间的价格差异
- 追踪促销季商品价格变化

## 依赖和前提条件
- 配置需监控的商品 URL
- 设置价格警报阈值和通知方式
- 法国电商网站可访问

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
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
