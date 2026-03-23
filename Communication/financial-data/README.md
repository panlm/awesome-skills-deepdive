# Financial Data

> 实时和历史金融数据查询工具，覆盖股票和加密货币的价格、交易量、技术指标等

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Financial Data |
| **作者** | aisapay |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/aisapay-financial-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aisapay/financial-data |
| **安全评级** | 🔴 High |

## 功能概述
- 查询股票实时价格和行情数据
- 获取加密货币实时价格和市值
- 历史价格数据查询和导出
- 交易量和流动性数据分析
- 技术指标计算（MA、RSI 等）
- 多交易所数据源支持
- 自定义时间范围的数据检索

## 使用场景
- 投资研究时查询股票和加密货币数据
- 技术分析所需的历史价格和指标数据
- 构建投资组合时的资产数据获取

## 依赖和前提条件
- 金融数据 API 密钥
- OpenClaw 环境已配置

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
