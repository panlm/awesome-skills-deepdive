# Model Guard

> 自动监控 Anti-Gravity 模型配额，在配额不足时切换到最优可用模型

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Model Guard |
| **作者** | sarielwang93 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/sarielwang93-model-guard |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sarielwang93/model-guard |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动监控多个 Anti-Gravity 模型的剩余配额
- 智能切换默认模型为配额最高的可用模型
- 当所有模型配额低于 20% 时自动回退到 gemini-flash
- 支持手动触发（model-guard）和自动触发（cron/heartbeat）
- 可在 guard.js 中自定义阈值和回退模型

## 使用场景
- 在多模型环境中自动管理配额，避免因配额耗尽导致服务中断
- 通过 cron 定时检查模型配额，确保始终使用最优资源

## 依赖和前提条件
- Node.js 运行环境
- Anti-Gravity 模型访问权限

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive skill 自动生成
