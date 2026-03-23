# Auto Skill Hunter

> 技能自动发现和推荐工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Auto Skill Hunter |
| **作者** | wanng-ide |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/wanng-ide-auto-skill-hunter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wanng-ide/auto-skill-hunter |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动搜索和发现新技能
- 技能匹配和推荐
- 技能评估和评分
- 安装建议和指导

## 使用场景
- 根据工作需求自动推荐合适的 Agent 技能
- 持续发现和评估新的可用技能

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `claw.json`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；持久化机制：涉及定时或后台任务；信息采集：读取环境变量或系统信息




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23