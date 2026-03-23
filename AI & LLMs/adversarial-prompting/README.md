# Adversarial Prompting

> 通过对抗性分析方法论，为复杂问题生成、批判、修复并整合多种解决方案

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Adversarial Prompting |
| **作者** | abe238 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/abe238-adversarial-prompting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/abe238/adversarial-prompting |
| **安全评级** | 🟢 Low |

## 功能概述
- 7 阶段结构化问题解决流程：方案生成 → 对抗批判 → 修复开发 → 验证 → 整合 → 排名 → 实施
- 为每个问题生成 3-7 个独立解决方案
- 深度对抗性批判：检查边缘案例、安全漏洞、性能瓶颈和隐藏假设
- 验证每个修复方案是否真正解决根本原因而非治标不治本
- 支持技术和非技术问题的全面分析
- 强制分析灾难性故障场景和意外后果

## 使用场景
- 架构设计决策前的全面方案评估和风险分析
- 复杂 bug 调试时生成多种修复策略并验证有效性
- 高风险业务决策前的多角度对抗性审查

## 依赖和前提条件
- 无外部依赖，纯 Prompt 驱动的方法论技能

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
