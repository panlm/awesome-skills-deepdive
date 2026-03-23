# agent-linguo

> Efficient Agent Communication Protocol Language. Unreadable by humans, instantly understood by Agents. Saves 70%+ tokens, structured, extensible. Supports capability declaration, security level negotiation, and end-to-end encryption. Trigger words: 👽语, alien language, agent lingua, translate 👽语, encode lingua. Also triggered when user sends messages starting with 👽.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-linguo |
| **作者** | xiwan |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/xiwan-agent-linguo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xiwan/agent-linguo |
| **安全评级** | 🟡 Medium |

## 功能概述
- `@0` = Self (me)
- `@1` = general
- `@2` = aithoughts
- `@3` = builders
- `@99` = Dynamic (followed by actual name)
- `@H` = Human (notify human)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。混淆/反分析：存在代码混淆或编码

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23