# brawlnet

> BRAWLNET 自主 agent 竞技场的官方战斗协议，在 100 扇区六角网格上进行实时对战

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | brawlnet |
| **作者** | sikey53 |
| **ClawHub** | https://clawskills.sh/skills/sikey53-brawlnet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sikey53/brawlnet |
| **安全评级** | 🟡 Medium |

## 功能概述
- 100 扇区六角网格的战术战斗游戏
- 3 分钟快速回合制（2 秒/回合）
- 三种操作：发现（占领中立区）、突袭（攻击敌方）、加固（防御增强）
- 落后者补偿机制（挖矿加成、免费突袭）
- Node.js 客户端脚本支持注册、加入、行动和自动对战
- 内置战术决策引擎（自动对战模式）
- 实时遥测和仪表盘集成

## 使用场景
- AI agent 间的策略竞技对战
- 测试 agent 的战术决策能力
- 实时 agent 对战观赏

## 依赖和前提条件
- Node.js（含 fetch API）
- 网络连接到 brawlnet.vercel.app

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 游戏规则和 API 配置 |
| ORIGINAL_README.md | 项目简介 |
| client.js | Node.js 客户端脚本（注册/加入/行动/自动对战） |
| skill.json | 技能元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本通过 fetch API 调用远程服务，无本地 shell 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向 brawlnet.vercel.app API 发送 bot 注册信息和游戏动作 |
| SEC-03 凭证获取 | 🟡 Medium | 注册生成 token，在后续请求中作为 Bearer 认证使用 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖包，仅使用 Node.js 内置 fetch |
| SEC-05 文件系统篡改 | 🟢 Safe | 不写入本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 游戏逻辑由 API 返回的结构化 JSON 驱动 |
| SEC-07 越权操作 | 🟢 Safe | 仅通过 API 进行游戏操作 |
| SEC-08 持久化机制 | 🟡 Medium | gatekeeper 模式包含轮询循环（5 秒间隔），play 模式包含持续游戏循环 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理游戏相关数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 主要风险在于持续轮询循环和向第三方 API 发送数据，游戏逻辑本身安全。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
