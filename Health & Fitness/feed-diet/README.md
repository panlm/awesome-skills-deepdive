# feed-diet

> Audit your information diet across HN and RSS feeds — beautiful reports with category breakdowns, ASCII charts, and personalized recommendations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feed-diet |
| **作者** | tkuehnl |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/tkuehnl-feed-diet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tkuehnl/feed-diet |
| **安全评级** | 🟡 Medium |

## 功能概述
- Compact first summary (top category + recommendations), full report on demand
- Component-style quick actions when available (`Show Full Diet Report`, `Generate Weekly Digest`, `Show Recommendations`)
- Numbered-list fallback when components are unavailable
- Total items: 50
- Categories used: 7/7
- Diversity score: 100%

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23