# Commit Analyzer

> 分析 Git 提交模式以监控 AI Agent 自主运行的健康状态，通过提交频率、类别分布和时间模式作为诊断指标。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Commit Analyzer |
| **作者** | bobrenze-bot |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bobrenze-bot-commit-analyzer |

## 功能概述
- 健康检查：基于提交频率判断 Agent 运行状态（0-1次/小时=等待模式，3-6次/小时=健康运行）
- 完整报告：生成过去 7 天的运行分析报告
- 每小时细分：按小时统计提交分布
- 类别分析：区分学习提交和任务提交，理想比率约 1:1
- 空闲检测：发现超过 3 小时无提交的等待模式
- 支持人类可读和 JSON 两种输出格式

## 使用场景
- 监控 AI Agent 的自主运行健康状态，及时发现卡顿或空闲
- 分析 Agent 的学习与任务执行比例，评估元认知能力
- 定期生成 Agent 运行健康报告用于运维监控

## 依赖和前提条件
- Git（需在有提交历史的 Git 仓库中运行）
- Bash shell

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
