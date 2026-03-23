# Tiktok Live Commerce

> 对接 TikTok 直播带货主播，实现实时产品演示、限时抢购和互动式电商销售

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tiktok Live Commerce |
| **作者** | realroc |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/realroc-tiktok-live-commerce |

## 功能概述
- 连接有经验的 TikTok 直播带货主播进行实时销售
- 支持产品演示、限时折扣和闪购活动
- 实时互动功能：观众 Q&A、弹幕互动、信任建立
- 通过 PingHuman API 管理直播商务流程
- 提供仪表盘查看直播数据和销售转化率
- 支持多种直播形式：购物直播、产品展示、互动营销

## 使用场景
- 电商品牌需要通过 TikTok 直播渠道推广产品并驱动即时购买
- AI Agent 自动对接和管理直播带货主播资源
- 需要实时监控直播带货数据和转化效果

## 依赖和前提条件
- PingHuman 平台账号（https://www.pinghuman.ai）
- API 访问凭证（API Base URL: `https://www.pinghuman.ai/api/v1`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
