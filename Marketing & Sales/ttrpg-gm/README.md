# TTRPG Game Master

> TTRPG Game Master for mature dark-themed campaigns. Use for Cyberpunk, Dark Fantasy, Horror, character-driven narratives with consequence tracking. Features dual-consequence system (World + Relationships), autonomous NPCs, hidden D20 rolls, psychological gauges. Optional adult content module.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TTRPG Game Master |
| **作者** | rogerkink6 |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/rogerkink6-ttrpg-gm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rogerkink6/ttrpg-gm |
| **安全评级** | 🟡 Medium |

## 功能概述
- Auto-trigger patterns for seamless skill activation
- Full combat system with cinematic flow and status-based damage
- Death & failure handling with death spiral, last stand, and alternative failures
- Safety tools (Lines & Veils, X-card, tone checks)
- Location & quest tracking in campaign files
- Inventory & resources tracking
- NPC voice templates for distinctive dialogue
- Encounter generation tables and guidelines

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `test-prompts.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23