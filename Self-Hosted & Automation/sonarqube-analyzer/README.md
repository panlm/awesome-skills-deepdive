# sonarqube-analyzer

> 分析 SonarQube 自托管项目，获取代码质量问题并建议自动化修复

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sonarqube-analyzer |
| **作者** | felipeoff |
| **ClawHub** | https://clawskills.sh/skills/felipeoff-sonarqube-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/felipeoff/sonarqube-analyzer |
| **安全评级** | 🟡 Medium |

## 功能概述
- 获取 SonarQube 项目/PR 的代码质量问题
- 基于规则智能建议修复方案
- 检查 Quality Gate 状态
- 区分可自动修复和需手动修复的问题
- 支持 CLI 和 OpenClaw 插件两种模式
- 生成 JSON 或 Markdown 报告

## 使用场景
- PR 代码质量检查和修复建议
- 项目 Quality Gate 状态监控
- CI/CD 流水线中的自动化代码分析

## 依赖和前提条件
- Node.js 18+
- SonarQube 实例
- SONAR_HOST_URL、SONAR_TOKEN 环境变量

## 包含文件
- `SKILL.md` — 技能定义和工具说明
- `src/index.js` — 主入口
- `src/api.js` — SonarQube API 客户端
- `src/analyzer.js` — 分析引擎
- `src/reporter.js` — 报告生成器
- `src/rules.js` — 规则定义
- `scripts/analyze.js` — CLI 分析脚本
- `openclaw.plugin.json` — OpenClaw 插件配置
- `package.json` — 依赖配置

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js HTTP 请求，无 shell 执行 |
| SEC-02 数据外泄 | 🟢 Safe | 从 SonarQube 读取数据到本地 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 SONAR_TOKEN 环境变量；默认 token 为 'admin' |
| SEC-04 供应链风险 | 🟡 Medium | npm 依赖包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 可选 autoFix 参数可能触发代码修改（但默认关闭） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 只读分析操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 获取项目代码质量数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 与 SonarQube 实例交互获取代码质量数据，默认 token 设置需注意

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
