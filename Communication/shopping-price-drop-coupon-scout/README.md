# Shopping Price Drop Coupon Scout

> 追踪产品价格变动并自动发现官方优惠券或折扣码，无需实际购买即可获取优惠信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Shopping Price Drop Coupon Scout |
| **作者** | codedao12 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/codedao12-shopping-price-drop-coupon-scout |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/codedao12/shopping-price-drop-coupon-scout |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时监控指定产品的价格波动
- 自动搜索并匹配官方优惠券和折扣码
- 价格降至目标时主动推送通知
- 支持多平台多商品同时追踪
- 生成价格历史趋势报告
- 智能判断最佳购买时机

## 使用场景
- 等待心仪商品降价时设置价格监控自动提醒
- 大促前提前收集优惠券以获取最优价格
- 比较多平台价格找到最低购买渠道

## 依赖和前提条件
- 提供需要追踪的产品链接或名称
- 网络访问权限

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
