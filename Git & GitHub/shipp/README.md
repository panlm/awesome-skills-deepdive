# Shipp

> 教会 AI Agent 集成 Shipp 实时数据连接器，获取体育赛事等实时事件流

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Shipp |
| **作者** | kclonts |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/kclonts-shipp |

## 功能概述
- 支持多种认证方式（Bearer Token、查询参数、自定义 Header）连接 Shipp API
- 通过自然语言 `filter_instructions` 创建可重用的实时数据查询连接
- 基于游标的分页轮询机制（`since_event_id`）高效获取增量实时事件
- 通过赛程端点发现即将开始和最近结束的比赛
- 灵活的数据结构处理，防御性处理可选字段
- 完整的错误处理策略，包括状态码、提示信息和重试机制
- 附带开源示例项目 Alph Bot：结合 Shipp + Claude AI + Kalshi 的自动交易机器人

## 使用场景
- 构建实时体育赛事数据看板、比分追踪或赛事播报系统
- AI Agent 需要接入实时事件流作为决策上下文（如体育博彩概率评估）
- 构建实时告警系统，监控特定赛事状态变化

## 依赖和前提条件
- 环境变量 `SHIPP_API_KEY`：从 [platform.shipp.ai](https://platform.shipp.ai/signup) 获取
- Shipp 账号和 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
