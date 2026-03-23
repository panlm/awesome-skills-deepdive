# OpenRA-RL

> Play Command & Conquer Red Alert RTS — build bases, train armies, and defeat AI opponents using 48 MCP tools.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenRA-RL |
| **作者** | yxc20089 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/yxc20089-openra-rl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yxc20089/openra-rl |
| **安全评级** | 🟡 Medium |

## 功能概述
- Real-time: The game runs continuously at ~25 ticks/second. Call `advance(ticks)` to let time pass.
- Fog of war: You can only see areas near your units/buildings. Scout to find the enemy.
- Resources: Harvest ore to earn credits. Credits buy buildings and units.
- Power: Buildings need power. Build Power Plants (`powr`) to stay powered. Low power slows production.
- Tech tree: Advanced buildings require prerequisites (e.g., War Factory needs Ore Refinery).
- Keep power positive (build Power Plants when needed)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- Docker
- macOS

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23