# Arc Budget Tracker

> 智能体开支追踪器，设置预算上限和告警阈值，防止 API 调用产生意外高额账单

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arc Budget Tracker |
| **作者** | trypto1019 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-budget-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-budget-tracker |
| **安全评级** | 🟢 Low |

## 功能概述
- 追踪智能体的 API 调用开支
- 设置预算上限和消费告警
- 实时费用监控和统计
- 超支自动告警或暂停执行
- 支持多维度费用分析（按时间/服务/智能体）

## 使用场景
- 控制 AI 智能体运行成本避免账单失控
- 团队环境下各智能体的费用分配和管理
- 长时间运行任务的成本监控和预算控制

## 依赖和前提条件
- ARC 服务账号配置
- 预算参数和告警阈值设定

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
