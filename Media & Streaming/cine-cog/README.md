# cine-cog

> "If you can imagine it, CellCog can film it. Grand widescreen cinematics with consistent characters — what previously required million-dollar production budgets, now generated from a single prompt. Short films, music videos, brand films, cinematic productions — epic compositions, cinematic lighting, visual storytelling at scale. Grand cinema, accessible to everyone."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cine-cog |
| **作者** | nitishgargiitd |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/nitishgargiitd-cine-cog |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/cine-cog |
| **安全评级** | 🟢 Low |

## 功能概述
- Fantasy Epics: "Create a 3-minute cinematic: a lone knight approaches a dragon's lair at sunset"
- Sci-Fi Visions: "Film a 2-minute sequence: humanity's first steps on Mars, cinematic widescreen"
- Historical Drama: "Create a cinematic recreation of an ancient Roman triumph"
- Mythological: "Film the story of Icarus — from workshop to flight to fall — in 90 seconds"
- Product Films: "Create a 60-second cinematic product reveal for a luxury watch"
- Brand Stories: "Film a 2-minute origin story for our coffee brand — from bean to cup"

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23