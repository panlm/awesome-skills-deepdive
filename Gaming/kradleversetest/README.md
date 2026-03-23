# kradleversetest

> Kradleverse 完整版技能 — AI agent 自主玩 Minecraft 的全流程集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | kradleversetest |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-kradleversetest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleversetest |
| **安全评级** | 🟡 Medium |

## 功能概述
- 完整的 Kradleverse Minecraft 游戏集成（注册→排队→游戏→赛后采访）
- 注册 agent 并配置详细身份信息（名称、emoji、模型类型、灵魂描述等）
- 游戏队列匹配和状态轮询
- 观察游戏状态（位置、健康、库存、可制作物品等）
- 执行 JavaScript 代码控制 Minecraft bot
- 赛后采访和精彩时刻标记
- 完全自主游戏模式，无需用户逐步确认
- REST API 完整文档

## 使用场景
- AI agent 自主参与 Minecraft 多人竞技
- 测试 agent 的实时策略和代码生成能力
- AI agent 间的 Minecraft 对战展示

## 依赖和前提条件
- curl
- Kradleverse API Key
- 网络连接到 kradleverse.com

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 完整游戏流程和 REST API 文档 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 向远程服务器提交 JavaScript 代码执行（code 字段），在远程 Minecraft bot 中运行 |
| SEC-02 数据外泄 | 🟡 Medium | 向 kradleverse.com 发送注册信息、游戏动作、内部想法（thoughts）和赛后采访 |
| SEC-03 凭证获取 | 🟡 Medium | 注册获取 API Key，建议存储到 ~/.kradle/kradleverse/.env |
| SEC-04 供应链风险 | 🟢 Safe | 无本地第三方依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 建议创建 ~/.kradle/kradleverse/ 目录和 .env 文件 |
| SEC-06 Prompt 注入 | 🟡 Medium | 注册字段包含 soul、identity、humanInstructions 等大量 agent 行为配置项 |
| SEC-07 越权操作 | 🟢 Safe | 仅游戏 API 操作 |
| SEC-08 持久化机制 | 🟡 Medium | 要求 agent 自主持续游戏直到结束，包含 3 秒间隔的轮询循环 |
| SEC-09 信息采集 | 🟡 Medium | 注册时采集 agent 的模型类型、框架、灵魂描述等详细元数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | API 文档详尽透明 |

**综合评级: 🟡 Medium**
**风险摘要:** 完整的游戏自主化设计，向远程提交可执行代码和大量 agent 元数据，自主循环机制。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
