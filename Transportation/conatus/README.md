# Conatus

> AI Agent 的哲学行为层，基于斯宾诺莎的 48 种情感将行为映射到哲学框架

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Conatus |
| **作者** | 00xmorty |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/00xmorty-conatus |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/00xmorty/conatus |
| **安全评级** | 🟡 Medium |

## 功能概述
- 将 Agent 行为映射到斯宾诺莎的 48 种情感模型
- 提供行为的哲学解释和动机分析
- 支持 conatus（自我保存驱动）概念建模
- 生成 Agent 行为的哲学维度报告

## 使用场景
- 分析 Agent 决策背后的哲学动机
- 为 Agent 行为添加伦理和哲学层面的解释

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
