# Basecamp CLI

> Basecamp 项目管理命令行工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Basecamp CLI |
| **作者** | emredoganer |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/emredoganer-basecamp-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/emredoganer/basecamp-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- Basecamp 项目和任务管理
- 消息和讨论操作
- 文件和文档管理
- CLI 驱动的项目操作

## 使用场景
- 通过命令行管理 Basecamp 项目和任务
- 自动化 Basecamp 中的日常项目管理操作

## 依赖和前提条件
- OAuth 认证
- npm
- Basecamp

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23