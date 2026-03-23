# Chaos pivot

> Prevents LLMs from sunk-cost pushing broken solutions. Triggers when an agent is stuck, looping, or failing repeatedly. Forces a Popperian falsification moment, then generates 3 constrained-chaotic alternative approaches and picks the best one. Loops like design thinking until solved or escalated.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Chaos pivot |
| **作者** | manecharo |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/manecharo-chaos-pivot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manecharo/chaos-pivot |
| **安全评级** | 🟢 Low |

## 功能概述
- Cosmetic pivots: Changing variable names, retrying with slightly different parameters, or adding a retry loop around a b
- Narrating success on failure: Do not describe a failed output as "a good first step" or "progress" if it did not actuall
- Skipping the Falsification Moment: You must name what failed and why before generating alternatives. Pivoting without di
- Carrying forward the broken assumption: Each alternative must violate at least one core assumption of the previous appro

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

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