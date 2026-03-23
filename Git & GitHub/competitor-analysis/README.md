# Competitor Analysis

> 'This skill should be used when the user asks to "analyze competitors", "competitor SEO", "who ranks for", "competitive analysis", "what are my competitors doing", "what are they doing differently", "why do they rank higher", or "spy on competitor SEO". Analyzes competitor SEO and GEO strategies including their ranking keywords, content approaches, backlink profiles, and AI citation patterns. Reveals opportunities to outperform competition. For content-focused gap analysis, see content-gap-analysis. For link profile specifics, see backlink-analyzer.'

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Competitor Analysis |
| **作者** | aaron-he-zhu |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/aaron-he-zhu-competitor-analysis |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aaron-he-zhu/competitor-analysis |
| **安全评级** | 🟡 Medium |

## 功能概述
- competitor analysis
- competitive intelligence
- market analysis
- ranking analysis
- competitive-seo
- competitor-keywords

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23