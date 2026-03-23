# Antigravity Model Usage

> Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar, or when you need a scriptable per-model summary from codexbar cost JSON.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Antigravity Model Usage |
| **作者** | ls18166407597-design |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ls18166407597-design-ag-model-usage |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ls18166407597-design/ag-model-usage |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时同步：直接从 Google 内部 API 获取最真实的账户配额数据。
- 状态监控：支持 Gemini、Claude 等核心模型的剩余额度展示。
- 时间预估：精准显示每个模型下次刷新的具体时间点（已转换为本地时区）。

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23