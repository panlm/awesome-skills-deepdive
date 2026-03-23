# Agentic Governance

> AI Agent 治理与约束管理工具，自动检测约束过期并管理生命周期

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agentic Governance |
| **作者** | leegitw |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/leegitw-agentic-governance |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/agentic-governance |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动检测和管理 Agent 行为约束的生命周期
- 约束过期检测和自动更新提醒
- 支持自定义治理规则和策略
- 监控 Agent 行为是否符合预定义约束
- 生成合规性报告和审计日志

## 使用场景
- 定期检查 Agent 的安全约束是否过期需要更新
- 自动监控多个 Agent 的行为合规性
- 生成 Agent 治理审计报告用于合规审查

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。Prompt 注入：发现 Prompt 注入特征

> 本文档由 awesome-skills-deepdive skill 自动生成
