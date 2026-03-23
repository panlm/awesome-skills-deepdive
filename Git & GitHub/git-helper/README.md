# Git Helper

> 将常用 Git 操作封装为便捷命令，包括状态查看、拉取、推送、分支管理和日志查看。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git Helper |
| **作者** | xejrax |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/xejrax-git-helper |

## 功能概述
- `git-helper status`：查看工作树状态
- `git-helper pull`：拉取最新变更
- `git-helper push`：推送本地提交
- `git-helper branch`：列出和管理分支
- `git-helper log`：查看提交日志（支持 `--limit` 参数限制数量）

## 使用场景
- 为 Agent 提供简化的 Git 操作接口，无需记忆完整 Git 命令语法
- 在日常开发中快速执行最常用的 Git 操作

## 依赖和前提条件
- `git`：系统上需已安装 Git（通常已预装）
- 无需额外安装

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
