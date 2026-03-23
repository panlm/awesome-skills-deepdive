# Feast - Intelligent meal planning, region and season aware shopping lists, respects dietary requirements, provides recipes, and generates immersive mealtime playlists

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Feast - Intelligent meal planning, region and season aware shopping lists, respects dietary requirements, provides recipes, and generates immersive mealtime playlists |
| **作者** | smadgerano |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/smadgerano-feast |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/smadgerano/feast |
| **安全评级** | 🟡 Medium |

## 功能概述
- Weekly meal planning with advance preparation
- Authentic cuisines — properly researched, not Westernised defaults
- Intelligent shopping lists — ingredient overlap, waste reduction, price checking
- Cultural immersion — regional history, current events, and context for every dish
- Curated music — 1-2 hour playlists with contemporary + classic music from each region (not generic Spotify searches)
- Smart shopping — price checking across stores, deal alerts, shopping strategy recommendations
- Surprise & delight — shopping is transparent, daily meal reveals with full cultural experience
- Health-focused — balanced nutrition, dietary phases, calorie tracking

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `docs`
- `references`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23