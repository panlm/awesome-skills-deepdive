# WhereCanIWatch

> Find where to stream any movie or TV show in the US using the WhereCanIWatch.tv API. Use when a user asks "where can I watch [title]?", wants streaming availability, needs to compare prices across services, or wants to know if something is on Netflix/Hulu/Disney+/etc. Supports filtering by user's subscriptions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | WhereCanIWatch |
| **作者** | samthewise2855 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/samthewise2855-wherecaniwatch |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/samthewise2855/wherecaniwatch |
| **安全评级** | 🟢 Low |

## 功能概述
- Lead with the best option and include the deep link URL
- Mention 1-2 alternatives (e.g., free option, cheapest rent)
- Link to the full page: `https://www.wherecaniwatch.tv/watch/{slug}`
- Search: 10 requests/minute per IP
- Watch API: 60 requests/minute per IP
- US region only

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

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