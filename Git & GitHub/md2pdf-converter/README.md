# Markdown to PDF Converter (v2.0)

> Offline Markdown to PDF converter with FULL Unicode support using Pandoc + WeasyPrint + local Twemoji cache (3660 colorful emojis). Converts Markdown documents to professional PDFs with Chinese fonts and colorful emojis (complete version with all variants). Use when user needs to convert Markdown reports or documents to PDF, generate PDFs with emoji support, create PDFs with proper Chinese character rendering, or work offline after initial setup.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Markdown to PDF Converter (v2.0) |
| **作者** | tianxingleo |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tianxingleo-md2pdf-converter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tianxingleo/md2pdf-converter |
| **安全评级** | 🟡 Medium |

## 功能概述
- ✅ Full Unicode support (Chinese, Japanese, Korean)
- ✅ Complete emoji support (Twemoji 14.0.0, 3660 colorful PNGs)
- ✅ All emoji variants (skin tones, hair styles, regional flags, etc.)
- ✅ Offline operation after initial setup
- ✅ Professional PDF layout with page numbers
- ✅ Code highlighting, tables, blockquotes
- ✅ Accurate emoji mapping via Python pre-generated lookup table

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；供应链风险：需要安装外部依赖；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23