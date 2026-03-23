# Firefly III

> Firefly III 集成 — 开源个人财务管理系统操作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Firefly III |
| **作者** | pushp1997 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/pushp1997-firefly-iii |
| **安全评级** | 🟡 Medium |

## 功能概述
- Firefly III 个人财务系统操作
- 交易记录和分类管理
- 预算追踪和报告
- 银行账户自动同步

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Firefly III 实例和 API 凭证
- Bear 笔记应用 (macOS/iOS)

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