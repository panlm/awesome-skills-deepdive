# Github MergeGuard AI

> 分析 GitHub Pull Request 的安全风险，判断 PR 是否可以安全合并

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Github MergeGuard AI |
| **作者** | nerdvana-labs |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/nerdvana-labs-pr-risk-analyzer |

## 功能概述
- 评估 Pull Request 中的潜在安全风险（暴露密钥、大量代码变更、敏感文件修改等）
- 提供风险评分和风险等级判定
- 生成具体的问题清单和合并建议（安全合并 / 需要审查 / 高风险禁止合并）
- 支持私有仓库（需提供 GitHub Token）
- 通过外部分析服务（pr-risk-analyzer.onrender.com）进行 PR 分析

## 使用场景
- 在合并 PR 前快速进行安全风险扫描
- 自动化代码审查流程中的安全检查环节
- 评估大型或来自外部贡献者的 PR 的安全性

## 依赖和前提条件
- 需要提供仓库名（owner/repo）和 PR 编号
- 私有仓库需要 GitHub Access Token
- 需要网络访问 pr-risk-analyzer.onrender.com API

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23