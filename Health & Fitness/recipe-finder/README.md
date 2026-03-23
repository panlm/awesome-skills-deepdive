# recipe-finder

> Find recipes by ingredients, cuisine, or dietary preferences using TheMealDB free API.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | recipe-finder |
| **作者** | harshasic |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/harshasic-recipe-finder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/harshasic/recipe-finder |
| **安全评级** | 🟢 Low |

## 功能概述
- Asks "what can I make with [ingredient]"
- Requests "recipes for dinner" or "Italian recipes"
- Says "vegetarian options" or "vegan meals"
- Asks for meal ideas based on ingredients they have
- `web_fetch` - Fetch recipe data from TheMealDB API
- Main ingredient (e.g., chicken, eggs, pasta)

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23