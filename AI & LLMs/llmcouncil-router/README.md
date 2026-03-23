# LLM Council Router

> 智能 LLM 路由器，将请求分发到最适合的大语言模型

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LLM Council Router |
| **作者** | ashtiwariasu |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ashtiwariasu-llmcouncil-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ashtiwariasu/llmcouncil-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- 根据任务类型智能路由到最合适的 LLM
- 支持多个 LLM 提供商的统一接口
- 基于成本、延迟和质量的智能路由决策
- 提供 LLM 评议会机制，多模型协同决策
- 支持自定义路由规则和优先级配置
- 提供请求统计和模型性能对比分析

## 使用场景
- 根据任务复杂度自动选择最经济高效的 LLM
- 多个 LLM 协同工作，通过评议提升回答质量
- 企业 AI 应用中统一管理多个 LLM 服务的调用

## 依赖和前提条件
- 多个 LLM API 密钥
- OpenClaw 运行环境

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
