# add-analytics

> 为任何项目添加 Google Analytics 4 (GA4) 追踪代码，支持多框架自动检测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | add-analytics |
| **作者** | jeftekhari |
| **ClawHub** | https://clawskills.sh/skills/jeftekhari-add-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeftekhari/add-analytics |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动检测项目框架类型（Next.js、Nuxt、Astro、SvelteKit 等 12 种）
- 验证 GA4 Measurement ID 格式（G-XXXXXXXXXX）
- 根据框架生成对应的追踪代码组件
- 支持自定义事件追踪辅助函数
- 支持 Cookie 同意集成
- 支持开发调试模式

## 使用场景
- 为新项目快速集成 Google Analytics 4
- 从 Universal Analytics 迁移到 GA4

## 依赖和前提条件
- Google Analytics 4 Measurement ID（G- 开头）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含各框架实现指南 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型 skill，无脚本文件，不执行命令 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输，仅生成本地代码 |
| SEC-03 凭证获取 | 🟢 Safe | 仅处理用户主动提供的 Measurement ID |
| SEC-04 供应链风险 | 🟢 Safe | 引入 Google gtag.js 外部脚本，属预期行为 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅修改项目内文件，属预期行为 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态内容注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化行为 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯指令型 skill，仅生成 GA4 追踪代码，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
