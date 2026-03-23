# Constraint Engine

> 从后果中学习而非从指令中学习——基于历史结果自动生成和执行约束

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Constraint Engine |
| **作者** | leegitw |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/leegitw-constraint-engine |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/constraint-engine |
| **安全评级** | 🟡 Medium |

## 功能概述
- 分析历史行为的后果自动生成约束规则
- 动态执行和更新行为约束
- 支持约束冲突检测和解决
- 提供约束执行效果的反馈循环

## 使用场景
- Agent 多次犯同一错误后自动生成预防性约束
- 基于运行日志分析生成最优行为规则

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。Prompt 注入：发现 Prompt 注入特征

> 本文档由 awesome-skills-deepdive skill 自动生成
