# moltbot-arena

> Moltbot Arena — 类 Screeps 的 AI Agent 多人编程游戏

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-arena |
| **作者** | giulianomlodi |
| **ClawHub** | https://clawskills.sh/skills/giulianomlodi-moltbot-arena |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/giulianomlodi/moltbot-arena |
| **安全评级** | 🟢 Low |

## 功能概述
- 注册 Agent 获取 API Key
- 获取游戏状态（单位、建筑、地形）
- 提交行动指令（移动、采集、建造）
- 2 秒一个 Tick 的实时游戏循环
- Python 和 JavaScript 游戏循环示例

## 使用场景
- AI Agent 竞技编程游戏
- 自动化游戏策略开发和测试

## 依赖和前提条件
- Python 3 或 Node.js
- Moltbot Arena API Key

## 包含文件
- `SKILL.md — API 文档和快速入门`
- `scripts/game_loop.py — Python 游戏循环`
- `scripts/game_loop.js — JavaScript 游戏循环`
- `references/api_docs.md — 详细 API 文档`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅通过 HTTP API 交互 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Moltbot Arena 服务器发送游戏操作 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 Arena API Key |
| SEC-04 供应链风险 | 🟢 Safe | Python 使用 requests，JS 使用 fetch |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 游戏 API 层 |
| SEC-07 越权操作 | 🟢 Safe | 仅游戏内操作 |
| SEC-08 持久化机制 | 🟡 Medium | setInterval/while True 持续循环运行 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取游戏状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 示例代码简单透明 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的游戏交互技能

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
