# MantisBT Manager

> MantisBT 缺陷跟踪系统的 AI 管理助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MantisBT Manager |
| **作者** | willykinfoussia |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/willykinfoussia-mantis-manager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/willykinfoussia/mantis-manager |
| **安全评级** | 🔴 High |

## 功能概述
- 与 MantisBT 缺陷跟踪系统深度集成
- 支持创建、更新和管理缺陷报告
- 提供智能缺陷分类和优先级建议
- 支持批量操作和自动化工作流
- 提供缺陷统计分析和趋势报告
- 支持自定义字段和工作流配置
- 可通过自然语言与缺陷管理系统交互

## 使用场景
- 通过 AI 助手自动创建和分类缺陷报告
- 智能分析缺陷趋势并生成项目质量报告
- 自动化缺陷管理流程，减少人工操作

## 依赖和前提条件
- MantisBT 服务器访问
- MantisBT API 凭证
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
