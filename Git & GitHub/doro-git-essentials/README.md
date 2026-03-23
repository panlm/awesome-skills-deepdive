# Doro Git Essentials

> Git 版本控制必备命令和工作流速查手册，涵盖分支管理、远程操作和团队协作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Doro Git Essentials |
| **作者** | a2mus |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/a2mus-doro-git-essentials |

## 功能概述
- 完整的 Git 初始化和配置命令参考（用户配置、仓库初始化、克隆）
- 暂存、提交、查看变更的基本工作流命令
- 分支创建、切换、合并、删除和冲突处理
- 远程仓库管理（添加/修改/删除远程源、fetch/pull/push）
- 历史查看和搜索（log、blame、bisect）
- 撤销操作（工作区、暂存区、提交的回退方式）
- Stash、Rebase、Tag、Cherry-pick、Submodule 等高级操作

## 使用场景
- AI Agent 在执行 Git 操作时查阅标准命令和最佳实践
- 开发者快速查找不常用的 Git 命令语法

## 依赖和前提条件
- `git`

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
