# Analytics And Advisory Intelligence

> 智能分析和咨询建议工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Analytics And Advisory Intelligence |
| **作者** | satoshistackalotto |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-analytics-and-advisory-intelligence |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/analytics-and-advisory-intelligence |
| **安全评级** | 🟡 Medium |

## 功能概述
- 业务数据智能分析
- AI 驱动的策略建议
- 市场趋势分析
- 数据可视化报告

## 使用场景
- 利用 AI 分析业务数据并获取策略建议
- 生成市场趋势分析报告辅助决策

## 依赖和前提条件
- GitHub API

## 包含文件
- `EVALS.json`
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23