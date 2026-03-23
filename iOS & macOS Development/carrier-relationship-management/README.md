# carrier-relationship-management

> 运输承运商关系管理专家知识库，涵盖费率谈判、绩效追踪和投资组合策略

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | carrier-relationship-management |
| **作者** | nocodemf |
| **ClawHub** | https://clawskills.sh/skills/nocodemf-carrier-relationship-management |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nocodemf/carrier-relationship-management |
| **安全评级** | 🟢 Low |

## 功能概述
- 承运商费率谈判框架和策略
- 绩效记分卡系统（OTD、投标接受率等）
- RFP 流程管理（8-12 周完整周期）
- 市场情报分析（DAT、Greenscreens）
- FMCSA 合规审查
- 承运商组合策略优化
- 边缘案例决策框架

## 使用场景
- 新航线承运商选择与评估
- 年度费率谈判准备
- 承运商绩效问题的纠正行动

## 依赖和前提条件
- 无（纯知识型 Skill）

## 包含文件
SKILL.md（核心知识库）, references/（决策框架、沟通模板、边缘案例）, evals/（评估脚本和场景）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯知识库，eval 脚本仅调用标准框架 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外传 |
| SEC-03 凭证获取 | 🟡 Medium | eval 脚本需要 ANTHROPIC_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | eval 依赖上层 shared 模块 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 纯知识内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 内容完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯知识型 Skill，无代码执行风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
