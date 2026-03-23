# Git Pushing

> 一键暂存、提交并推送 Git 变更，自动生成约定式提交消息。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git Pushing |
| **作者** | tianyi-billy-ma |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tianyi-billy-ma-git-pushing |

## 功能概述
- 一键完成 Git 工作流：暂存所有变更 → 创建约定式提交 → 推送到远程分支
- 提供 `smart_commit.sh` 脚本自动化整个流程
- 支持自定义提交消息（如 `"feat: add feature"`）
- 自动使用 `-u` 标志推送并设置上游分支
- 在提交消息中自动添加 Claude 页脚标识

## 使用场景
- 完成功能开发后快速将代码推送到远程仓库，无需手动执行多步 Git 命令
- Agent 在代码修改完成后自动提交和推送，保持远程仓库同步

## 依赖和前提条件
- `git`：需要安装 Git
- `bash`：运行 smart_commit.sh 脚本
- 已配置 Git 远程仓库

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive skill 自动生成
