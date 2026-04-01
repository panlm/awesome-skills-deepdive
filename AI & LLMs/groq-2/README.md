# Groq (2)

> 通过 Groq API 实现超快速 AI 推理（第二版）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Groq (2) |
| **作者** | samirjtv-ctrl |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/samirjtv-ctrl-groq-2 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/samirjtv-ctrl/groq-2 |
| **安全评级** | 🟢 Low |

## 功能概述
- 集成 Groq 的高速 AI 推理 API 第二版
- 支持通过简单指令触发 AI 推理
- 使用 "Groq: <提示词>" 格式快速调用
- 利用 Groq 的硬件加速实现低延迟响应

## 使用场景
- 需要快速 AI 推理响应的实时对话场景
- 对延迟敏感的 AI 应用中替代传统推理服务

## 依赖和前提条件
- Groq API Key
- OpenClaw 运行环境

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
