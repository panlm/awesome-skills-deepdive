# Sovereign Commit Craft

> Git 提交信息专家：分析 Diff 生成完美的 Conventional Commit 消息、变更日志和发布说明

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sovereign Commit Craft |
| **作者** | ryudi84 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-commit-craft |

## 功能概述
- 分析 Git Diff 生成规范的 Conventional Commit 消息（支持 11 种类型：feat、fix、docs 等）
- 生成 Keep a Changelog 格式的变更日志
- 生成面向营销的发布说明，包含亮点、升级指南和破坏性变更迁移指南
- 生成结构化 PR 描述（摘要、变更列表、测试计划、检查清单）
- 提供大型提交拆分建议：当一个提交应拆为多个时给出指导
- 基于提交类型推荐语义化版本号（SemVer）
- 审查现有提交消息并提出改进建议
- 覆盖 Conventional Commits v1.0.0、Keep a Changelog v1.1.0、SemVer v2.0.0 等规范

## 使用场景
- 开发完成后生成规范的提交信息，确保团队提交历史的一致性和可读性
- 版本发布时自动生成变更日志和发布说明
- 审查团队成员的提交消息质量并提出改进建议

## 依赖和前提条件
- 通过 ClawHub 安装：`npx clawhub install sovereign-commit-craft`
- Git 仓库环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
