# Near Batch Sender

> NEAR 区块链批量操作工具，支持批量转账、NFT 转移和奖励领取

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Near Batch Sender |
| **作者** | shaiss |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/shaiss-near-batch-sender |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shaiss/near-batch-sender |
| **安全评级** | 🟡 Medium |

## 功能概述
- 批量发送 NEAR 代币到多个接收地址
- 批量转移 NFT 到指定账户
- 批量领取质押奖励
- 支持 JSON 格式的收件人配置文件
- 内置成本估算功能，发送前预览费用

## 使用场景
- 项目方向多个钱包批量空投 NEAR 代币
- 批量转移 NFT 资产到不同持有者
- 自动化 NEAR 质押奖励的定期领取

## 依赖和前提条件
- Node.js / npm
- NEAR CLI 已安装并配置
- 发送账户有足够的 NEAR 余额

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
