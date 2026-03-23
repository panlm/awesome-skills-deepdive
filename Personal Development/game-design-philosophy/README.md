# game-design-philosophy

> 游戏设计哲学 — 游戏机制和体验设计原则

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | game-design-philosophy |
| **作者** | nyxur42 |
| **ClawHub** | https://clawskills.sh/skills/nyxur42-game-design-philosophy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nyxur42/game-design-philosophy |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- game-development
- systems-design
- player-experience
- Every designer has instincts they can't articulate yet. This skill helps you find the words.*
- Design Preferences:
- Genre affinities (what they gravitate toward and what they avoid)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 包含网络探测功能 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23