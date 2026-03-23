# Budget

> 智能体开支追踪和预算管理工具，设置预算上限和告警机制，防止意外高额账单

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Budget |
| **作者** | rogerscristo |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rogerscristo-budget |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rogerscristo/budget |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时追踪智能体的 API 调用和服务开支
- 设置预算上限和阶梯告警阈值
- 超支自动告警和可选自动暂停
- 按时间段生成开支报告和趋势分析
- 支持多智能体和多服务的统一预算管理
- 成本归因分析，定位高消耗环节

## 使用场景
- 运维人员为 AI 智能体设置月度预算上限，防止费用失控
- 团队管理者监控多个智能体的总体开支并优化成本
- 开发者在测试阶段限制 API 调用费用

## 依赖和前提条件
- 配置需要追踪的服务和 API 账户
- 设定预算金额和告警规则
- 配置通知渠道（邮件、消息等）

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
