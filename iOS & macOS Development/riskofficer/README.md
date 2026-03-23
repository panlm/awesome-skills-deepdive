# riskofficer

> 投资组合管理与风险分析工具，支持 VaR、蒙特卡洛、Black-Litterman 优化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | riskofficer |
| **作者** | mib424242 |
| **ClawHub** | https://clawskills.sh/skills/mib424242-riskofficer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mib424242/riskofficer |
| **安全评级** | 🟡 Medium |

## 功能概述
- 股票搜索（MOEX、NYSE、NASDAQ、Crypto）
- 投资组合管理（创建、编辑、删除）
- 风险计算（VaR、蒙特卡洛模拟、压力测试）
- 组合优化（Risk Parity、Calmar、Black-Litterman）
- 跨组合相关性分析
- 券商集成（Tinkoff/T-Bank）
- 多币种支持（RUB/USD）

## 使用场景
- 管理虚拟投资组合
- 计算投资组合风险指标
- 使用 Black-Litterman 模型优化持仓

## 依赖和前提条件
- RiskOfficer iOS 应用
- API Token（RISK_OFFICER_TOKEN）

## 包含文件
SKILL.md, references/（13 个方法论文档）, clawhub.json

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 Markdown 和 API 文档，无可执行代码 |
| SEC-02 数据外泄 | 🟡 Medium | 向 RiskOfficer API 发送投资组合数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 RISK_OFFICER_TOKEN API 密钥 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖第三方 RiskOfficer 服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 通过 API 限制操作范围 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 处理金融投资数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 需要 API Token 和第三方服务，处理金融数据需注意隐私

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
