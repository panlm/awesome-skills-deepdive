# Agentic Compass

> 纯本地运行的 AI 代理自我反思与行动规划工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agentic Compass |
| **作者** | orosha-ai |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/orosha-ai-agentic-compass |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agentic-compass |
| **安全评级** | 🟢 Low |

## 功能概述
- 读取本地记忆文件生成结构化的代理行动计划
- 从五个维度评估代理表现：任务完成率、响应相关性、工具使用质量、记忆一致性、主动性
- 每次生成四类输出：主动任务、延迟/定时任务、规避规则、具体交付物
- 所有数据保留本地，无外部数据传输
- 支持自定义记忆文件路径
- 使用可量化指标而非主观评价进行评分

## 使用场景
- 定期对 AI 代理的行为模式进行自检和优化
- 生成具体可执行的行动计划，提升代理的任务完成效率
- 追踪代理在多个会话中的记忆一致性和表现趋势

## 依赖和前提条件
- Python 3 运行环境
- 本地记忆文件（如 MEMORY.md、daily notes）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；文件系统篡改：存在文件系统操作；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive skill 自动生成
