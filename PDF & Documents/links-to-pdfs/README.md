# Links to PDFs

> 将网页链接批量转换为 PDF 文档

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Links to PDFs |
| **作者** | chrisling-dev |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/chrisling-dev-links-to-pdfs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chrisling-dev/links-to-pdfs |
| **安全评级** | 🔴 High |

## 功能概述
- 抓取网页内容并保存为 PDF
- 支持批量 URL 处理
- 保持网页排版和样式
- 自定义 PDF 输出选项

## 使用场景
- 将收藏的文章链接批量保存为 PDF 离线阅读
- 归档网页内容为 PDF 文档

## 依赖和前提条件
- API 密钥
- npm
- Anthropic API
- Notion API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23