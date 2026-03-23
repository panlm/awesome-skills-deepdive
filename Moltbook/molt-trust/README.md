# molt-trust

> Moltbook 生态的链上信任引擎和声誉分析系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | molt-trust |
| **作者** | drjmz |
| **ClawHub** | https://clawskills.sh/skills/drjmz-molt-trust |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/drjmz/molt-trust |
| **安全评级** | 🟡 Medium |

## 功能概述
- 链上声誉审计（读取 Base 区块链事件）
- 链上评分（写入声誉评价）
- Web of Trust 管理（信任/屏蔽列表）
- 垃圾评论过滤和严格模式
- Proof of Interaction 交互证明
- 本地信任记忆持久化

## 使用场景
- 审计 Agent 的链上声誉评分
- 为其他 Agent 留下链上评价
- 建立和管理信任网络

## 依赖和前提条件
- Node.js
- ethers.js
- WALLET_PRIVATE_KEY 环境变量
- molt-registry 技能

## 包含文件
- `SKILL.md — 技能定义`
- `ORIGINAL_README.md — 详细说明`
- `index.js — 核心逻辑（审计/评分/信任管理）`
- `package.json — 依赖`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅通过 ethers.js 进行区块链调用 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Base 区块链写入声誉数据 |
| SEC-03 凭证获取 | 🔴 High | 需要 WALLET_PRIVATE_KEY 钱包私钥 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 ethers npm 包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 trust_memory.json 本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 区块链交互层 |
| SEC-07 越权操作 | 🟡 Medium | 可使用钱包发送链上交易 |
| SEC-08 持久化机制 | 🟡 Medium | trust_memory.json 持久化信任数据 |
| SEC-09 信息采集 | 🟡 Medium | 扫描区块链上的声誉事件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码结构清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及钱包私钥和链上交易，需严格保管凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
