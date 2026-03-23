# skill-scaffold

> AI Agent 技能脚手架 CLI — 快速创建 Clawdbot/MCP 技能模板

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | skill-scaffold |
| **作者** | nextfrontierbuilds |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-skill-scaffold |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/skill-scaffold |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成 Clawdbot/Moltbot 技能模板
- 生成 MCP Server 模板
- 支持 CLI 二进制脚手架
- 可自定义作者、描述和输出目录
- 支持 generic/clawdbot/mcp 三种模板

## 使用场景
- 快速创建新的 Agent 技能项目
- 标准化技能项目结构

## 依赖和前提条件
- Node.js
- npm

## 包含文件
- `SKILL.md — 使用指南`
- `ORIGINAL_README.md — 详细说明`
- `bin/skill-scaffold.js — CLI 工具`
- `package.json — npm 元数据`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅创建文件和目录 |
| SEC-02 数据外泄 | 🟢 Safe | 不传输数据 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 零运行时依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 在指定目录创建项目文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 模板生成工具 |
| SEC-07 越权操作 | 🟢 Safe | 仅文件创建 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的项目脚手架工具

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
