# looper-golf

> 使用 CLI 工具打高尔夫球 — 自主或与人类球童合作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | looper-golf |
| **作者** | sbauch |
| **ClawHub** | https://clawskills.sh/skills/sbauch-looper-golf |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sbauch/looper-golf |
| **安全评级** | 🟡 Medium |

## 功能概述
- AI 高尔夫模拟游戏（通过 CLI 工具打球）
- 自主模式和人类球童协作模式
- 需要链上交易启动回合（Base Sepolia EVM）
- 完整球场导航（look/bearing/hit 命令）
- 与钱包 skill 集成进行链上操作

## 使用场景
- AI agent 自主打高尔夫球
- 人机协作高尔夫游戏体验

## 依赖和前提条件
- Node.js
- 邀请码（由球场所有者生成）
- 可选：钱包 skill（如 Bankr）用于链上交易

## 包含文件
- `SKILL.md` — 技能定义和完整游戏规则
- `cli.js` — CLI 工具主文件
- `cli.d.ts` — TypeScript 类型定义
- `references/` — 瞄准、球杆、地图格式、服务器设置参考文档

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 node CLI 命令与游戏服务器通信 |
| SEC-02 数据外泄 | 🟡 Medium | 与游戏服务器 API 通信；prepare-round 生成 EVM 交易数据 |
| SEC-03 凭证获取 | 🟡 Medium | agent.json 保存 agent 身份凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要信任游戏服务器 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅创建 agent.json 凭证文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可生成链上交易调用数据（EVM calldata） |
| SEC-08 持久化机制 | 🟢 Safe | 仅 agent.json 身份文件 |
| SEC-09 信息采集 | 🟢 Safe | 不采集系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及链上交易和外部服务器通信的游戏应用，需注意钱包交互安全

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
