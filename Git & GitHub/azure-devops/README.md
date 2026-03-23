# Azure DevOps

> 管理 Azure DevOps 项目、仓库和分支，创建 PR，管理工作项，查看构建状态

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Azure DevOps |
| **作者** | pals-software |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/pals-software-azure-devops |

## 功能概述
- 列出 Azure DevOps 组织下的所有项目及其描述
- 查看项目中的仓库列表和仓库中的分支
- 创建 Pull Request，指定源分支、目标分支和描述
- 列出和查看仓库的 Pull Request 详情
- 获取仓库 ID 用于后续 API 操作
- 使用 Azure DevOps REST API v7.1，Basic Auth 认证

## 使用场景
- 在 AI 代理工作流中集成 Azure DevOps 操作，如自动创建 PR
- 查询项目结构和 PR 状态，辅助代码审查决策
- 自动化 DevOps 工作流，减少手动 Azure 门户操作

## 依赖和前提条件
- 环境变量 `AZURE_DEVOPS_PAT`（个人访问令牌）
- 环境变量 `AZURE_DEVOPS_ORG`（组织名称）
- `curl` 和 `jq` 命令行工具

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
