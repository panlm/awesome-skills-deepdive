# Swap and bridge across 35+ chains with LI.FI

> 通过 LI.FI 协议实现 35+ 条链的跨链代币兑换和桥接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Swap and bridge across 35+ chains with LI.FI |
| **作者** | rhlsthrm |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/rhlsthrm-lifi-crosschain |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rhlsthrm/lifi-crosschain |
| **安全评级** | 🟡 Medium |

## 功能概述
- 支持 35 条以上区块链网络的跨链操作
- 提供代币兑换（Swap）和跨链桥接（Bridge）功能
- 自动寻找最优跨链路径和最佳费率
- 集成 LI.FI 协议的聚合路由技术
- 支持主流 DEX 和跨链桥协议
- 提供交易状态跟踪和确认

## 使用场景
- 在不同区块链网络之间进行代币跨链转移
- 通过 AI 代理自动寻找最优汇率进行代币兑换
- 构建多链 DeFi 策略时的自动化跨链操作

## 依赖和前提条件
- LI.FI API 访问
- 区块链钱包配置
- OpenClaw 运行环境

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
