# Decompose Mcp

> Decompose any text into classified semantic units — authority, risk, attention, entities. No LLM. Deterministic.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Decompose Mcp |
| **作者** | echology-io |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/echology-io-decompose-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/echology-io/decompose-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- Authority levels — RFC 2119 keywords: "shall" = mandatory, "should" = directive, "may" = permissive
- Risk categories — safety-critical, security, compliance, financial, contractual
- Attention scoring — authority weight x risk multiplier, 0-10 scale
- Standards references — ASTM, ASCE, IBC, OSHA, ACI, AISC, AWS, ISO, EN
- Financial values — dollar amounts, percentages, retainage, liquidated damages
- Dates — deadlines, milestones, notice periods
- Irreducibility — legal mandates, threshold values, formulas that cannot be paraphrased

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `claw.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23