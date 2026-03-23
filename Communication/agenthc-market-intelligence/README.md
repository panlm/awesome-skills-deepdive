# Stock Market Intelligence

> AI 智能体市场数据 API，覆盖股票、固定收益、加密货币和宏观经济数据，支持比特币闪电网络微支付

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Stock Market Intelligence |
| **作者** | traderhc123 |
| **版本** | 2.4.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/traderhc123-agenthc-market-intelligence |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/traderhc123/agenthc-market-intelligence |
| **安全评级** | 🔴 High |

## 功能概述
- 实时查询股票行情和历史数据
- 获取固定收益产品（债券等）市场信息
- 加密货币价格和交易数据查询
- 宏观经济指标和数据获取
- 支持比特币闪电网络进行数据访问微支付
- 按需付费的灵活计费模式

## 使用场景
- 智能体自主进行市场研究和投资分析
- 构建自动化交易信号监控系统
- 获取多资产类别数据进行跨市场分析

## 依赖和前提条件
- AgentHC API 访问凭证
- 比特币闪电网络钱包（用于微支付）
- 网络连接到 AgentHC 数据服务

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
