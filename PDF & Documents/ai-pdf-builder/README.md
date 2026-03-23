# Ai Pdf Builder

> AI 驱动的 PDF 文档智能生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Pdf Builder |
| **作者** | nextfrontierbuilds |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-ai-pdf-builder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/ai-pdf-builder |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 AI 自动生成 PDF 文档
- 支持多种文档模板和布局
- 智能排版和格式化处理
- 内容自动组织和结构化

## 使用场景
- 根据文本内容自动生成排版精美的 PDF 报告
- AI 辅助创建演示文档和手册

## 依赖和前提条件
- Pandoc
- LaTeX
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23