# recipe-finder

> 食谱搜索和推荐工具

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
- Main ingredient (e.g., chicken, eggs, pasta)
- Cuisine type (e.g., Italian, Mexican, Chinese)
- Dietary restriction (e.g., vegetarian, vegan, gluten-free)
- By ingredient: `https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}`

## 使用场景
- 根据食材搜索匹配的食谱
- 获取食谱的营养信息和步骤
- 发现新的菜品和烹饪灵感

## 依赖和前提条件
- API 密钥或访问令牌
- 数据库
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
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
