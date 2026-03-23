# moltbot-best-practices

> AI Agent 最佳实践指南 — 来自真实失败案例的 15 条规则

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-best-practices |
| **作者** | nextfrontierbuilds |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-moltbot-best-practices |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-best-practices |
| **安全评级** | 🟢 Low |

## 功能概述
- 执行前确认任务
- 发布前需审批
- 简单路径优先
- 失败快速上报
- 匹配用户能量级别
- 操作完成后验证

## 使用场景
- 新 Agent 开发者学习避坑指南
- 改善 Agent 的用户体验和可靠性

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `SKILL.md — 15 条最佳实践规则`
- `ORIGINAL_README.md — 完整说明`
- `package.json — npm 元数据`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯文档指南 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无代码依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 指导 Agent 行为模式的规则集 |
| SEC-07 越权操作 | 🟢 Safe | 鼓励谨慎操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无数据采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 纯文档最佳实践指南，对 Agent 行为有积极指导

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
