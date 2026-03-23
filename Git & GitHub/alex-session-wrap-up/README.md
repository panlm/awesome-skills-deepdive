# Alex Session Wrap-Up

> 会话结束时的自动化流程：提交未推送的代码、提取学习要点、检测重复模式并持久化规则

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Alex Session Wrap-Up |
| **作者** | xbillwatsonx |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/xbillwatsonx-alex-session-wrap-up |

## 功能概述
- 自动检测并提交工作区中未暂存/未提交的文件，推送到远程仓库
- 扫描会话对话，提取关键决策和学习要点
- 使用 gpt-4o-mini 分析提取的经验，检测重复错误和自动化机会
- 将学习成果写入每日记忆文件 `memory/YYYY-MM-DD.md`
- 发现新模式时自动更新 `AGENTS.md` 和 `MEMORY.md`

## 使用场景
- 在结束一段较长的工作会话时，自动整理和保存工作成果
- 持续积累工作经验，通过模式检测发现可改进的重复行为
- 确保所有代码变更都被提交和推送，不遗漏未保存的工作

## 依赖和前提条件
- 需要 gpt-4o-mini 模型访问（通过 OpenRouter 或 OpenAI）
- Git 已配置且可推送到远程仓库
- 工作区中存在标准的 memory 目录结构

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
