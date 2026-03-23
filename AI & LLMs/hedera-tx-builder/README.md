# Hedera Transaction Builder

> 构建和执行 Hedera 区块链交易的智能助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hedera Transaction Builder |
| **作者** | harleyscodes |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/harleyscodes-hedera-tx-builder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/harleyscodes/hedera-tx-builder |
| **安全评级** | 🟡 Medium |

## 功能概述
- 支持在 Hedera 网络上构建多种类型的交易
- 提供 HBAR 代币转账功能
- 支持 HCS（Hedera 共识服务）消息提交
- 支持 HTS（Hedera 代币服务）代币操作
- 提供交易预览和确认机制
- 自动处理交易签名和提交流程

## 使用场景
- 通过 AI 代理在 Hedera 网络上执行代币转账
- 向 Hedera 共识服务提交消息用于去中心化应用
- 自动化 Hedera 区块链上的代币管理操作

## 依赖和前提条件
- Hedera 账户 ID 和私钥
- Hedera 网络访问
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
