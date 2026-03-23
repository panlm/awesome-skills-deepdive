# Bring Recipes

> Use when user wants to browse recipe inspirations from Bring! shopping app. For discovering recipes, viewing recipe details (name, author, type, images), or filtering by tags. Note - cannot import ingredients (API limitation).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bring Recipes |
| **作者** | darkdevelopers |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/darkdevelopers-bring-recipes |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/darkdevelopers/bring-recipes |
| **安全评级** | 🟡 Medium |

## 功能概述
- User wants to discover Bring! recipes
- Browsing recipe inspirations
- Viewing recipe metadata (names, authors, types, images, links)
- Filtering recipes by tags (all, mine)
- Need JSON output of recipes for scripting
- User wants to add ingredients to shopping list (API limitation)

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23