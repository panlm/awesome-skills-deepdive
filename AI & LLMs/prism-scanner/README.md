# Prism Scanner

> 即时检测加密货币 Rug Pull 风险，扫描持有者集中度、流动性锁定和合约安全

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Prism Scanner |
| **作者** | nextfrontierbuilds |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-prism-scanner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/prism-scanner |
| **安全评级** | 🟡 Medium |

## 功能概述
- 即时检测加密货币代币的 Rug Pull 风险
- 分析代币持有者集中度和分布情况
- 检查流动性锁定状态和合约安全性
- 识别仿冒代币和山寨币诈骗
- 支持 Solana 和 EVM 链上代币扫描
- 提供 0-100 风险评分和分级评估
- 支持通过合约地址或代币符号查询
- 输出 JSON 格式结果，便于自动化集成

## 使用场景
- 在购买新代币前快速进行安全审查，避免 Rug Pull 损失
- 构建自动化交易机器人时集成风险检测模块
- 对加密货币投资组合中的代币进行批量安全扫描

## 依赖和前提条件
- Bash/Shell 环境
- API Key
- 环境变量 `PRISM_API_KEY`
- 环境变量 `PRISM_URL`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
