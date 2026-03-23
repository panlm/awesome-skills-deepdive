# Zillow × Airbnb Matcher

> Zillow 与 Airbnb 房产匹配分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zillow × Airbnb Matcher |
| **作者** | freemountaindeer |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/freemountaindeer-zillow-airbnb-matcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/freemountaindeer/zillow-airbnb-matcher |
| **安全评级** | 🟡 Medium |

## 功能概述
- Revenue estimates are based on nightly rate × 70% occupancy. For precise data, use AirDNA ($100+/mo)
- Geo-matching means the Airbnb may be a neighbor's property, not the exact same house — always verify
- Free tier gives 100 Airbnb + 600 Zillow searches per month (RapidAPI free plan)
- Cost per search: $0 on free plan
- Airbnb: https://rapidapi.com/3b-data-3b-data-default/api/airbnb13
- Zillow: https://rapidapi.com/SwongF/api/us-property-market1
- Cap Rate — annual return on full purchase price
- Cash-on-Cash — return on your actual cash invested

## 使用场景
- 匹配 Zillow 房源和 Airbnb 租赁数据
- 估算短租投资回报率
- 分析区域性房产投资机会

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `GUIDE.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`
- `src`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
