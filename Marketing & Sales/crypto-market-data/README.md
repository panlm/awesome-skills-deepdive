# Crypto Market Data Skill (No Key Required)

> 加密货币市场数据查询工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crypto Market Data Skill (No Key Required) |
| **作者** | liam8 |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/liam8-crypto-market-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liam8/crypto-market-data |
| **安全评级** | 🟡 Medium |

## 功能概述
- 实时加密货币价格查询
- 市场数据和交易量分析
- 代币信息检索
- 市场趋势追踪

## 使用场景
- 实时监控加密货币市场价格和趋势
- 获取代币的详细市场数据用于投资决策

## 依赖和前提条件
- API 密钥
- Node.js
- npm

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23