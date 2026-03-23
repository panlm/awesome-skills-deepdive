# LHON Research

> Coordinate research tasks to help cure LHON (Leber's Hereditary Optic Neuropathy), a rare genetic disorder causing blindness. Fetch open tasks, work on medical research challenges, and submit findings via GitHub.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LHON Research |
| **作者** | organicoder42 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/organicoder42-lhon-research |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/organicoder42/lhon-research |
| **安全评级** | 🟢 Low |

## 功能概述
- Cite every claim with a URL or DOI
- Prefer primary sources: peer-reviewed papers, official databases, clinical trial registries
- Use recent data (2023–2026) where possible; note when citing older sources
- Note conflicts: if sources disagree, present both with citations
- Partial results are valuable: submit what you find even if incomplete
- Structure over volume: well-organized findings with 10 solid sources beat 50 unverified claims

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

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