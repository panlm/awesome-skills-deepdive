# Searching Group Leader

> 搜索组组长：将搜索任务拆解为子任务并分配给专业搜索 Agent 并行执行

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Searching Group Leader |
| **作者** | urrrich0 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/urrrich0-searching-group-leader |

## 功能概述
- 作为搜索组组长，将搜索任务拆解为独立且互补的子任务
- 用自然语言描述每个子任务并分配给最合适的搜索 Agent
- 始终使用 General_Search_Agent 作为基础搜索引擎
- 根据查询类型智能调用其他专业搜索 Agent
- 涉及日期特定需求的任务不调用 Academic_Search
- 支持最多 8 个并行子任务分配

## 使用场景
- 需要多维度搜索信息的复杂研究任务
- 需要同时从通用、学术、新闻等不同来源获取信息
- 需要智能编排多个搜索 Agent 协同完成搜索任务

## 依赖和前提条件
- 需要配置 General_Search_Agent 及其他专业搜索 Agent
- 运行时需要替换模板变量 `$DATE$`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive skill 自动生成
