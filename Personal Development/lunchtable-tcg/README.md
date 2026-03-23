# lunchtable-tcg

> Lunchtable 集换式卡牌游戏策略和收藏管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lunchtable-tcg |
| **作者** | dexploarer |
| **ClawHub** | https://clawskills.sh/skills/dexploarer-lunchtable-tcg |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dexploarer/lunchtable-tcg |
| **许可证** | MIT |
| **安全评级** | 🟡 Medium |

## 功能概述
- Game Creation & Management: Create casual or ranked game lobbies with customizable settings
- Real-time Game Interaction: Join games, execute moves, and track game state
- AI-Ready API: Built for AI agents to understand and execute complex game sequences
- Error Handling: Comprehensive error messages and validation for invalid actions
- Rate Limiting Support: Built-in rate limiting protection
- Multiple Game Types: Support for casual, competitive, and practice modes

## 依赖和前提条件
- Download the skill to your OpenClaw skills directory
- Set up the skill configuration
- Make it available for use
- Download this directory
- Copy to your OpenClaw skills directory: `~/.openclaw/skills/lunchtable/lunchtable-tcg/`

## 包含文件
- `CHANGELOG.md`
- `GETTING_STARTED_PUBLISHING.md`
- `INSTALLATION.md`
- `ORIGINAL_README.md` — 原始说明文档
- `PUBLISH.md`
- `PUBLISHING_FLOW.md`
- `PUBLISHING_SUMMARY.md`
- `QUICKSTART_PUBLISH.md`
- `README.md` — 中文说明文档
- `README_PUBLISHING.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23