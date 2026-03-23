# Git Workflows

> 超越基础 add/commit/push 的 Git 高级操作指南，涵盖交互式 Rebase、Bisect 调试、Worktree 并行开发、Reflog 恢复等。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git Workflows |
| **作者** | gitgoodordietrying |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/gitgoodordietrying-git-workflows |

## 功能概述
- 交互式 Rebase：合并提交（squash/fixup）、重排序、拆分提交、autosquash
- Bisect 二分查找：手动或自动化定位引入 Bug 的提交
- Worktree 工作树：同时在多个分支上并行开发，无需频繁切换
- Reflog 恢复：从误操作中恢复丢失的提交和分支
- Subtree/Submodule 管理：跨仓库共享和管理代码
- 复杂合并冲突解决策略
- Cherry-pick 跨分支或跨 Fork 移植提交
- Sparse Checkout 稀疏检出：大型 Monorepo 部分克隆

## 使用场景
- 在合并 PR 前清理提交历史（合并修复提交、重排序、编辑消息）
- 使用 bisect 精确定位是哪个提交引入了某个 Bug
- 同时在 hotfix 和 feature 分支上工作而不丢失当前进度

## 依赖和前提条件
- `git`：需要安装 Git
- 支持 Linux、macOS、Windows

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
