# Gmail Secretary

> AI 邮件秘书，自动管理和回复 Gmail 邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gmail Secretary |
| **作者** | officialdelta |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/officialdelta-gmail-secretary |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/officialdelta/gmail-secretary |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动读取和分析 Gmail 收件箱中的邮件
- 基于 AI 理解邮件内容并生成智能回复
- 支持邮件分类、优先级排序和标记
- 可自动处理常规邮件并标记需要人工关注的邮件
- 支持自定义回复模板和处理规则
- 保持邮件上下文连贯性的对话式回复

## 使用场景
- 自动处理日常邮件，减少邮箱管理时间
- AI 代理代为筛选和回复低优先级邮件
- 出差或忙碌时自动管理收件箱并处理紧急邮件

## 依赖和前提条件
- Gmail API 凭证
- Google OAuth 配置
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
