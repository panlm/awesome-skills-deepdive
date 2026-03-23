# Bitbucket Automation

> 通过 Rube MCP (Composio) 自动化 Bitbucket 仓库、PR、分支、Issue 和工作空间管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bitbucket Automation |
| **作者** | sohamganatra |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/sohamganatra-bitbucket-automation |

## 功能概述
- 管理 Pull Request：创建、列出、查看详情、获取 diff 和 diffstat
- 管理仓库和工作空间：列出、创建、删除仓库，查看工作空间成员
- Issue 管理：创建、更新、列出和评论仓库 Issue
- 分支操作：列出分支、验证源和目标分支存在性
- 支持 BBQL 查询语法进行高级筛选
- 通过 Bitbucket OAuth 完成身份认证
- 详细的参数说明和常见陷阱提示（如 UUID 格式、分页默认值等）

## 使用场景
- 在 AI 代理工作流中自动化 Bitbucket 的日常操作
- 批量管理多个仓库的 PR 和 Issue
- 搭建基于 Bitbucket 的自动化 CI/CD 辅助工作流

## 依赖和前提条件
- Rube MCP 服务已连接（添加 `https://rube.app/mcp` 为 MCP 服务器）
- 通过 `RUBE_MANAGE_CONNECTIONS` 完成 Bitbucket OAuth 认证
- 认证状态需为 ACTIVE

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
