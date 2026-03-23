# Deepseek Reasoner Lite Agent

> 基于 DeepSeek-R1 模型的轻量级内容创作 Agent

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deepseek Reasoner Lite Agent |
| **作者** | teamolab |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/teamolab-deepseek-reasoner-lite-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamolab/deepseek-reasoner-lite-agent |
| **安全评级** | 🟢 Low |

## 功能概述
- 使用 DeepSeek-R1 模型进行内容创作
- 轻量级 Agent 配置，快速部署
- 支持模板变量替换（如 $DATE$ 用于当前日期）

## 使用场景
- 使用 DeepSeek-R1 模型进行高质量内容生成
- 在 OpenClaw 中快速切换到 DeepSeek 推理模型

## 依赖和前提条件
- 无外部依赖，纯指令型 Skill
- 需要 DeepSeek API 访问权限

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
