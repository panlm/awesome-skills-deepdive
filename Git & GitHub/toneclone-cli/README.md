# ToneClone CLI

> 使用 ToneClone 以用户的真实写作风格生成邮件、消息和社交媒体内容，告别千篇一律的 AI 腔调

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ToneClone CLI |
| **作者** | jfox85 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jfox85-toneclone-cli |

## 功能概述
- 基于训练好的 persona 以用户独特风格生成文字内容
- 支持生成邮件、消息、社交媒体帖子等多种文本类型
- 通过 knowledge cards 为写作提供上下文信息
- 支持多个写作风格人设（persona），可针对不同场景切换
- 通过 `toneclone` CLI 命令行工具直接操作

## 使用场景
- 需要快速撰写邮件或消息，同时保持个人写作风格一致性
- 社交媒体内容创作，避免 AI 生成内容的"机器味"
- 多风格写作场景（如正式商务 vs 轻松社交），通过不同 persona 切换

## 依赖和前提条件
- ToneClone 账号（https://toneclone.ai）
- `toneclone` CLI 工具（通过 Homebrew 安装：`brew install toneclone`）
- 已训练好的写作 persona

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
