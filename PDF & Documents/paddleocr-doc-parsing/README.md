# PaddleOCR Document Parsing

> Complex document parsing with PaddleOCR. Intelligently converts complex PDFs and document images into Markdown and JSON files that preserve the original structure.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | PaddleOCR Document Parsing |
| **作者** | bobholamovic |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/bobholamovic-paddleocr-doc-parsing |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bobholamovic/paddleocr-doc-parsing |
| **安全评级** | 🔴 High |

## 功能概述
- PADDLEOCR_DOC_PARSING_API_URL
- PADDLEOCR_ACCESS_TOKEN
- PADDLEOCR_DOC_PARSING_TIMEOUT
- Documents with tables (invoices, financial reports, spreadsheets)
- Documents with mathematical formulas (academic papers, scientific documents)
- Documents with charts and diagrams

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23