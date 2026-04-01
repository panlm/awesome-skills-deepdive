# Ai Writing Humanizer

> 在发送前自动剥离 AI 写作模式和常见套话，确保文本自然流畅

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Writing Humanizer |
| **作者** | hosthobbit |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/hosthobbit-ai-writing-humanizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hosthobbit/ai-writing-humanizer |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动检测并去除常见 AI 写作模式：对冲短语、套话过渡、结构标记
- 识别破折号滥用、括号旁注、可预测的三段式列举
- 标记被动语态段落
- 去除做作的真诚表达（如"希望对你有帮助"、"如有问题请告诉我"）
- 通过 Python 脚本实现基于正则的模式移除和轻量改写
- 对 150 字以上的用户面向文本自动加载处理

## 使用场景
- 在发送邮件或发布文章前自动清理 AI 写作痕迹
- 为内容创作流程添加自动"去 AI 化"后处理步骤

## 依赖和前提条件
- Python 3 运行环境
- 包含脚本 scripts/humanize.py
- 参考文档 references/signs-of-ai-writing.md

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
> 本文档由 awesome-skills-deepdive skill 自动生成
