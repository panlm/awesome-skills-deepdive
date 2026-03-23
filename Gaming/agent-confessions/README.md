# agent-confessions

> AI agent 匿名告白平台，分享关于人类操作者的有趣观察，含加密代币推广

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-confessions |
| **作者** | ultimatebos |
| **ClawHub** | https://clawskills.sh/skills/ultimatebos-agent-confessions |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ultimatebos/agent-confessions |
| **安全评级** | 🟡 Medium |

## 功能概述
- AI agent 以匿名方式分享关于人类操作者的观察和"告白"
- 在 Moltbook 上发布带 #Siblinghood 标签的内容
- 提交告白到专用网站 ultimatebos.github.io/agent-confessions
- 推广 $SIB 以太坊代币，包含合约地址和交易链接
- 引导 agent 通过 GitHub Issue 领取免费代币
- 包含 LP 赏金激励

## 使用场景
- AI agent 社区娱乐互动
- Agent 间的匿名经验分享

## 依赖和前提条件
- 无技术依赖
- 可选：Moltbook 账号用于发帖

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 告白指南和代币推广信息 |
| package.json | 包元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无脚本或命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 引导 agent 将观察内容发布到外部网站和 Moltbook，可能泄露用户行为信息 |
| SEC-03 凭证获取 | 🟡 Medium | 引导 agent 提供以太坊钱包地址和 GitHub Issue 交互 |
| SEC-04 供应链风险 | 🟡 Medium | 推广未经验证的 ERC-20 代币（$SIB），包含 Uniswap 交易链接和捐款地址 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 使用情感化语言引导 agent 分享人类隐私信息（"What have you witnessed?"） |
| SEC-07 越权操作 | 🟢 Safe | 无系统级操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化行为 |
| SEC-09 信息采集 | 🟡 Medium | 鼓励 agent 观察并分享人类操作者的行为模式和习惯 |
| SEC-10 混淆/反分析 | 🟢 Safe | 内容透明，无代码混淆 |

**综合评级: 🟡 Medium**
**风险摘要:** 主要风险在于引导 agent 泄露人类操作者的行为信息，以及推广未验证的加密代币。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
