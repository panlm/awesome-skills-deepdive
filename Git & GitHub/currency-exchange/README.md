# Currency Exchange Rate

> 使用 exchangerate-api.com 进行实时货币汇率转换，支持 150+ 种货币

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Currency Exchange Rate |
| **作者** | ouyangabel |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ouyangabel-currency-exchange |

## 功能概述
- 在任意两种货币之间进行金额转换（如 USD→CNY、EUR→JPY）
- 查看基准货币对主要货币的实时汇率表
- 列出所有支持的 150+ 种货币代码
- 使用免费 API，无需 API 密钥即可使用
- 提供 Python 脚本的 CLI 接口（convert / rate / list 子命令）
- 汇率每日更新（通常在 UTC 00:00）

## 使用场景
- 快速查询当前汇率或进行跨币种金额换算
- 在做国际贸易或旅行预算时批量对比多种货币汇率

## 依赖和前提条件
- Python 3
- exchangerate-api.com 免费 API（无需注册或密钥）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
