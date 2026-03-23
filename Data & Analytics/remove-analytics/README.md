# remove-analytics

> 安全地从项目中移除 Google Analytics 追踪代码和相关依赖

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | remove-analytics |
| **作者** | jeftekhari |
| **ClawHub** | https://clawskills.sh/skills/jeftekhari-remove-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeftekhari/remove-analytics |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索项目中所有 Analytics 相关代码
- 移除 gtag 脚本和组件
- 清理环境变量和 npm 包
- 操作前要求用户确认
- 生成移除摘要报告
- 禁止模型自行触发（需用户明确调用）

## 使用场景
- 从项目中完全移除 Google Analytics
- 清理已弃用的 UA 追踪代码

## 依赖和前提条件
- 已集成 Analytics 的项目

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，移除步骤指南 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，无脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 仅移除环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 删除文件和修改代码，但需用户确认 |
| SEC-06 Prompt 注入 | 🟢 Safe | 设置了 disable-model-invocation |
| SEC-07 越权操作 | 🟢 Safe | 需用户明确调用 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的代码清理工具，需用户确认后才执行，设有防误触发机制

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
