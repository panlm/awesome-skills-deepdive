# Git Essentials

> Git 版本控制的核心命令和工作流速查手册，涵盖分支管理、远程操作和团队协作。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git Essentials |
| **作者** | arnarsson |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/arnarsson-git-essentials |

## 功能概述
- 完整的 Git 基础工作流：暂存、提交、查看差异
- 分支管理：创建、切换、合并、删除、重命名
- 远程仓库操作：添加/修改 remote、fetch/pull/push
- 提交历史查看和搜索：日志、blame、bisect
- 撤销操作：工作区恢复、取消暂存、回退提交、revert
- Stash 暂存管理：保存、恢复、查看、清除
- 交互式 Rebase：合并提交、重排序、编辑
- Tag 管理和高级操作：Cherry-pick、Submodule

## 使用场景
- 作为 Git 命令速查手册，Agent 在执行版本控制操作时快速参考正确语法
- 帮助用户解决 Git 操作问题（合并冲突、提交回退、分支管理等）
- 为不熟悉 Git 的用户提供标准化工作流指导

## 依赖和前提条件
- `git`：需要安装 Git

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
