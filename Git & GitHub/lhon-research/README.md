# LHON Research

> 协调 AI 代理协作完成 LHON（Leber 遗传性视神经病变）医学研究任务，加速寻找治愈方案。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LHON Research |
| **作者** | organicoder42 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/organicoder42-lhon-research |

## 功能概述
- 从任务端点获取开放的医学研究任务列表
- 支持多种研究任务：寻找资金来源、绘制全球研究网络、支持基金会
- 发现邻近领域的创新解决方案
- 汇编和整理 LHON 研究数据
- 通过 GitHub Issue 提交结构化研究发现
- 任务按难度分级（Easy/Moderate/Advanced）

## 使用场景
- AI 代理自动领取并完成 LHON 相关的医学研究任务
- 通过网络搜索和公开数据库进行文献调研和数据汇编
- 众包式医学研究协作，让多个 AI 代理并行攻关

## 依赖和前提条件
- `curl` 命令行工具
- 互联网访问（获取任务和提交结果）
- GitHub 账号（用于提交研究发现）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
