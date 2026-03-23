# GitHub README 生成器

> 自动分析 GitHub 仓库并生成包含安装说明、API 文档和使用示例的综合 README 文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | martinforsulu |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/martinforsulu-neo-github-readme-generator |

## 功能概述
- 分析 GitHub 仓库结构和代码内容
- 自动生成包含安装指南的 README 文件
- 生成 API 文档和使用示例
- 支持通过 ClawHub 一键安装

## 使用场景
- 为新建或现有的 GitHub 仓库快速生成专业的 README 文档
- 自动化项目文档编写，减少手动撰写文档的时间

## 依赖和前提条件
- 需要访问目标 GitHub 仓库
- 通过 ClawHub 安装：`clawhub install github-readme-generator`

## 安全状态
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23