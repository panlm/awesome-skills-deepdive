# Agent Docs

> 创建专为 AI Agent 消费优化的文档——提升 RAG 检索效率和令牌利用率

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Docs |
| **作者** | tylervovan |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/tylervovan-agent-docs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tylervovan/agent-docs |
| **安全评级** | 🟡 Medium |

## 功能概述
- 三层混合上下文层次结构：内联宪法层（始终在上下文）、参考库层（按需加载）、研究助手层（外部检索）
- 基于 Vercel 基准测试：内联 AGENTS.md 方案的测试通过率达 100%（工具检索仅 53%）
- 压缩索引策略：8KB 压缩索引优于 40KB 完整文档转储
- 解决"中间遗忘"问题：关键规则放在文档开头利用首因效应
- 面向分块优化：每个章节自包含，适配 RAG 系统的分段策略
- 信噪比优化：剥离欢迎语、营销文案等无关内容

## 使用场景
- 编写 SKILL.md、AGENTS.md 等 Agent 专用文档时参考最佳实践
- 优化项目文档结构使 AI Agent 能更高效地理解和使用
- 设计 API 文档和技术规范以最大化 LLM 上下文窗口利用率

## 依赖和前提条件
- 无外部依赖，纯文档写作方法论

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
