# Humanizer

> 检测并消除 AI 生成文本的痕迹，使文本更自然、更像人类撰写

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Humanizer |
| **作者** | brandonwise |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/brandonwise-ai-humanizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brandonwise/ai-humanizer |
| **安全评级** | 🟡 Medium |

## 功能概述
- 识别 24 种 AI 写作模式，使用 500+ 词汇表进行检测
- 运用统计文本分析：突发性、类型-标记比率、可读性指标
- 提供三种模式：评分（score）、完整分析（analyze）、自动修正（humanize）
- 基于维基百科 AI 写作特征和 Copyleaks 风格指纹研究开发
- 可作为 OpenClaw Skill 或独立 CLI 工具使用
- 支持批量处理文件和管道输入

## 使用场景
- 在发布前检查文本是否存在明显的 AI 写作痕迹
- 自动修正 AI 生成内容中的模式化表达，提升文本自然度
- 为内容团队提供 AI 文本检测评分工具

## 依赖和前提条件
- Node.js >= 18
- npm（`npm install` 安装依赖）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
