# Conversational Ai Assistant

> 希腊会计数据的自然语言查询接口，用英语提问，从所有系统 Skill 中获取答案

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Conversational Ai Assistant |
| **作者** | satoshistackalotto |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-conversational-ai-assistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/conversational-ai-assistant |
| **安全评级** | 🔴 High |

## 功能概述
- 提供英语自然语言界面查询希腊会计系统数据
- 将英语问题翻译为 Skill 命令，将输出转换回易懂的英语回答
- 支持上下文感知，在会话中记住已讨论的客户信息
- 采用「先读后写」原则，查询操作自由，数据修改需确认
- 对不确定的结果诚实表达，不进行猜测
- 通过 Skill 编排而非重复实现来协调多个会计功能模块
- 保持专业、简洁的沟通语调

## 使用场景
- 会计助理通过自然语言查询客户税务信息和财务状态
- 无需了解 CLI 命令即可查询和管理希腊会计合规数据
- 跨多个会计 Skill 综合查询并生成统一报告

## 依赖和前提条件
- jq（JSON 处理）
- OpenClaw CLI
- OPENCLAW_DATA_DIR 环境变量
- 需配合其他希腊会计系统 Skill 使用

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
