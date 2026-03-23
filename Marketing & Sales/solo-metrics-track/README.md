# Metrics Track

> 个人/独立开发者指标追踪工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Metrics Track |
| **作者** | fortunto2 |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/fortunto2-solo-metrics-track |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/fortunto2/solo-metrics-track |
| **安全评级** | 🟢 Low |

## 功能概述
- 关键业务指标追踪
- 数据可视化仪表盘
- 趋势分析和报告
- 目标设定和追踪

## 使用场景
- 独立开发者追踪产品的关键增长指标
- 管理和可视化个人业务的核心数据

## 依赖和前提条件
- PostHog

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23