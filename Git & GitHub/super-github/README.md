# Sg

> 终极 GitHub 自动化框架：集 Issue、PR、Release 和仓库管理于一体

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sg |
| **作者** | heldinhow |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/heldinhow-super-github |

## 功能概述
- Issue 自动化：创建（含标签、指派人）、列表（按状态/标签筛选）、更新、自动分类和标签建议
- PR 审查助手：PR 摘要分析、文件变更统计、审查清单生成、冲突检测
- Release 自动化：创建发布、自动生成变更日志、标签管理
- 仓库管理：列出仓库、获取/设置 Secrets、管理 Workflows
- 整合了 openclaw-github-assistant、github-automation-pro、github-mcp 三个 Skill 的最佳功能

## 使用场景
- 需要一站式管理 GitHub 仓库的 Issue、PR、Release 和工作流
- AI Agent 需要完整的 GitHub 操作能力，而不是分散安装多个 Skill
- 团队需要自动化 PR 审查流程和 Release 发布管理

## 依赖和前提条件
- `gh` CLI 已安装并完成认证

## 安全状态
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
