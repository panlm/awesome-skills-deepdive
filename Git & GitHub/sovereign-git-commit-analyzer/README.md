# Sovereign git-commit-analyzer

> 全面分析 Git 提交历史，生成开发活动、贡献者模式和提交消息质量的详细报告

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sovereign git-commit-analyzer |
| **作者** | ryudi84 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-git-commit-analyzer |

## 功能概述
- 统计可配置时间窗口内的提交频率（按天/周/月），生成文本柱状图
- 按提交数、修改行数和文件数排名贡献者
- 生成文件变更热力图，识别高频修改的文件（潜在复杂度热点）
- 基于行业最佳实践的提交消息质量评分（0-100）
- 开发活动趋势分析，展示开发速度变化
- 支持多种输出格式：Markdown、JSON、纯文本
- 灵活的过滤选项：按时间范围、分支、作者筛选
- 可配置质量阈值，作为团队提交规范的基线

## 使用场景
- 工程团队负责人定期分析代码库开发活动，识别贡献热点和改进方向
- 代码审查前分析提交模式，识别频繁修改的文件作为重构候选
- 在 CI/CD 中集成提交消息质量检查，强制执行团队规范

## 依赖和前提条件
- `git` (>= 2.0)
- `bash` (>= 4.0)
- `awk`（推荐 GNU awk）、`sort`、`uniq`、`wc` 等标准 Unix 工具
- 支持 Linux、macOS 和 Windows（通过 Git Bash/WSL/MSYS2）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
