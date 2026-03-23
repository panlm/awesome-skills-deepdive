# gh

> 使用 GitHub CLI (gh) 执行核心 GitHub 操作：认证状态、仓库创建/克隆/Fork、Issues、Pull Requests、Releases 及基础仓库管理。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gh |
| **作者** | trumppo |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/trumppo-gh |

## 功能概述
- 通过 `gh auth status` 检查 GitHub 认证状态
- 创建仓库（支持私有仓库，`--private` 标志）
- 克隆和 Fork 远程仓库
- Issue 管理：列出、创建、评论
- Pull Request 管理：创建、列出、查看、合并
- Release 发布：创建带版本号和说明的 Release
- 查看当前仓库上下文信息

## 使用场景
- 在终端中快速管理 GitHub 仓库、Issue 和 PR，无需切换到浏览器
- 自动化 CI/CD 流程中的 GitHub 操作（如自动创建 Release）
- 在脚本中集成 GitHub 操作用于批量处理

## 依赖和前提条件
- 安装 `gh`（GitHub CLI）
- 已通过 `gh auth login` 完成 GitHub 认证

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
