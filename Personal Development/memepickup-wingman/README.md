# memepickup-wingman

> Meme 式搭讪助手 — AI 生成创意开场白

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | memepickup-wingman |
| **作者** | samcraw1 |
| **ClawHub** | https://clawskills.sh/skills/samcraw1-memepickup-wingman |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/samcraw1/memepickup-wingman |
| **许可证** | MIT |
| **安全评级** | 🟡 Medium |

## 功能概述
- Pickup Lines — Generate lines at different intensity levels (Sweet > Playful > Bold > Chaotic)
- Reply Help — Get 3 reply suggestions at different intensities for any dating conversation
- Screenshot Analysis — Share a conversation screenshot, get replies + wingman advice
- Profile Analysis — Score dating profiles against your preferences (Hinge, Tinder, Bumble, Instagram)
- Coaching — Timing advice, double-texting warnings, reading the room
- Date Planning — Personalized ideas based on your conversation context

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `examples/` — 目录
- `package.json` — 配置/数据文件
- `references/` — 目录
- `scripts/` — 目录

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