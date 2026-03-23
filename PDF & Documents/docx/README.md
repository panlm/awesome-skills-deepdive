# Docx

> "Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. When Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Docx |
| **作者** | seanphan |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/seanphan-docx |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seanphan/docx |
| **安全评级** | 🟡 Medium |

## 功能概述
- Your own document + simple changes
- Someone else's document
- Legal, academic, business, or government docs
- `word/document.xml` - Main document contents
- `word/comments.xml` - Comments referenced in document.xml
- `word/media/` - Embedded images and media files

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `LICENSE.txt`
- `SKILL.md`
- `_meta.json`
- `docx-js.md`
- `ooxml`
- `ooxml.md`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23