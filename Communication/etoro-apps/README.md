# eToro Apps

> 通过自然语言与 eToro API 交互，访问市场数据、管理投资组合和执行交易操作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | eToro Apps |
| **作者** | marian2js |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/marian2js-etoro-apps |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marian2js/etoro-apps |
| **安全评级** | 🔴 High |

## 功能概述
- 查询实时市场行情和资产价格
- 查看和管理投资组合持仓
- 执行买入/卖出交易操作
- 跟踪投资收益和损益情况
- 获取热门交易者和跟单信息
- 市场新闻和分析数据查询

## 使用场景
- 通过对话方式查看 eToro 投资组合状态
- 快速获取股票和加密货币的实时行情
- 管理和调整 eToro 交易策略

## 依赖和前提条件
- eToro 账号及 API 访问凭据
- OpenClaw 环境已配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
