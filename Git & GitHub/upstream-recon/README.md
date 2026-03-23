# Upstream Recon

> 在提交 Issue、PR 或评论之前先调研开源项目，避免重复劳动和无效贡献

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Upstream Recon |
| **作者** | semmyt |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/semmyt-upstream-recon |

## 功能概述
- 在提交 Issue 前检查是否已存在相同或相似的 Issue
- 在发起 PR 前评估维护者的合并偏好和代码风格
- 分析项目的现有讨论线程，了解社区态度
- 防止提交重复 Issue、浪费 PR 精力或发表无根据的评论
- 自动激活于准备与开源项目交互的场景

## 使用场景
- 准备为开源项目提交 Bug Report 或 Feature Request 时先做调研
- 贡献代码前了解项目的合并文化和维护者偏好
- 参与开源讨论前检查已有的相关讨论和结论

## 依赖和前提条件
- 通过 `npx skills add oss-skills/upstream-recon` 安装
- 或手动复制到 `~/.claude/skills/upstream-recon/`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
