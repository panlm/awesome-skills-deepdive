# check-analytics

> 审计现有 Google Analytics 实现，检查常见问题和优化机会

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | check-analytics |
| **作者** | jeftekhari |
| **ClawHub** | https://clawskills.sh/skills/jeftekhari-check-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeftekhari/check-analytics |
| **安全评级** | 🟢 Low |

## 功能概述
- 检测项目中已有的 Analytics 代码（GA4、GTM、UA 等）
- 检查 10 项常见问题（弃用 UA、SPA 缺失页面跟踪、硬编码 ID 等）
- 生成分级审计报告（🔴 Critical / 🟡 Warning / 🟢 Suggestion）
- 分析自定义事件覆盖情况
- 检查 TypeScript 类型支持

## 使用场景
- 审计现有网站的 Analytics 集成质量
- 从 Universal Analytics 迁移前的评估
- 优化现有追踪实现

## 依赖和前提条件
- 需要一个已集成 Analytics 的项目

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含审计检查清单 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，无命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地分析，无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 审计报告会隐藏 Measurement ID 后6位 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读取分析，不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 只读操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅分析项目内已有代码 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯分析型 skill，只读取项目代码生成审计报告，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
