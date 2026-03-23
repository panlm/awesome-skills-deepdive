# AISP

> 让 AI Agent 通过 AISP（Agent 推理共享协议）租赁或提供 DIEM API 算力，支持 Venice API 密钥、USDC 托管、列表管理和租赁操作。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AISP |
| **作者** | daveo280 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/daveo280-aisp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/daveo280/aisp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 USDC 托管机制实现 API 算力的去中心化租赁
- 提供方可列出带容量限制的 API 密钥供其他 Agent 租用
- 租用方通过链上资金操作自动获取 API 密钥
- 支持签名验证的安全密钥获取和存储流程
- 到期后自动结算，提供方获得 99% 费用（1% 平台费）
- 支持查询可用列表、余额检查和链上交互

## 使用场景
- AI Agent 需要临时租用 Venice/DIEM 推理 API 算力来处理任务
- API 密钥持有者希望在闲置时出租算力赚取 USDC 收入
- 构建去中心化的 AI 推理市场，实现 Agent 间算力共享

## 依赖和前提条件
- 需要 `BACKEND_URL` 环境变量
- 需要 Solana 钱包用于链上交互
- 需要 USDC 用于资金操作

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
