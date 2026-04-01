# Smart Context

> 智能管理 AI 对话上下文，优化 Token 使用和对话质量

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Smart Context |
| **作者** | joe3112 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/joe3112-smart-context |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/joe3112/smart-context |
| **安全评级** | 🟡 Medium |

## 功能概述
- 智能管理和注入上下文信息
- 根据对话内容动态调整上下文窗口
- 优化 Token 使用效率
- 支持长文档的智能分段和检索
- 提供上下文相关性评分和排序
- 适用于复杂对话和多轮交互场景

## 使用场景
- 处理长文档对话时智能管理上下文窗口
- 多轮复杂对话中动态优化上下文内容
- 减少 Token 消耗同时保持对话质量

## 依赖和前提条件
- 无特殊依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
