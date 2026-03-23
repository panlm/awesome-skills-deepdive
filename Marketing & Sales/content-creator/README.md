# Content Creator

> "Deprecated redirect skill that routes legacy 'content creator' requests to the correct specialist. Use when a user invokes 'content creator', asks to write a blog post, article, guide, or brand voice analysis (routes to content-production), or asks to plan content, build a topic cluster, or create a content calendar (routes to content-strategy). Does not handle requests directly — identifies user intent and redirects to content-production for writing/SEO/brand-voice tasks or content-strategy for planning tasks."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Content Creator |
| **作者** | alirezarezvani |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-content-creator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/content-creator |
| **安全评级** | 🟢 Low |

## 功能概述
- content-production — Full pipeline: research → brief → draft → optimize → publish. Includes all Python tools from the or
- content-strategy — Strategic planning: topic clusters, keyword research, content calendars, prioritization frameworks.
- User asks "content creator" → Route to content-production (most likely intent is writing).
- User asks "content plan" or "what should I write" → Route to content-strategy.
- content-production: Full content execution pipeline (successor).
- content-strategy: Content planning and topic selection (successor).

## 使用场景
- SEO 优化和内容创建
- 内容营销策略执行
- 搜索排名分析和优化

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `assets`
- `examples`
- `references`

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