# Adversarial Prompting

> Applies rigorous adversarial analysis to generate, critique, fix, and consolidate solutions for any problem (technical or non-technical). Use when facing complex problems requiring thorough analysis, multiple solution approaches, and validation of proposed fixes before implementation.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Adversarial Prompting |
| **作者** | abe238 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/abe238-adversarial-prompting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/abe238/adversarial-prompting |
| **安全评级** | 🟢 Low |

## 功能概述
- Facing complex technical problems requiring thorough analysis (architecture decisions, debugging, performance optimizati
- Solving strategic or business problems with multiple viable approaches
- Needing to identify weaknesses in proposed solutions before implementation
- Requiring validated fixes that address root causes, not symptoms
- Working on high-stakes decisions where failure modes must be understood
- Seeking comprehensive analysis with detailed reasoning visible throughout

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23