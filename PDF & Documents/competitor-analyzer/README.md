# Competitor Analyzer

> Analyze any company's competitive position in minutes. Takes a company name or URL and produces a structured report covering what they do, pricing, social presence, and recent news.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Competitor Analyzer |
| **作者** | claudiodrusus |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/claudiodrusus-competitor-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/claudiodrusus/competitor-analyzer |
| **安全评级** | 🟢 Low |

## 功能概述
- Company Overview — What they do, market position
- Pricing Analysis — Plans, tiers, free tier details
- Social Presence — Twitter, LinkedIn, GitHub activity
- Recent News — Latest announcements, funding, launches
- Strengths & Weaknesses — Quick SWOT-lite summary
- `curl` (standard)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `analyze.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23