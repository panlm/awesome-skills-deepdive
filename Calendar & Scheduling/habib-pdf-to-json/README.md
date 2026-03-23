# habib-pdf-to-json

> "Extract structured data from construction PDFs. Convert specifications, BOMs, schedules, and reports from PDF to Excel/CSV/JSON. Use OCR for scanned documents and pdfplumber for native PDFs."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | habib-pdf-to-json |
| **作者** | dbmoradi60 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/dbmoradi60-habib-pdf-to-json |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dbmoradi60/habib-pdf-to-json |
| **安全评级** | 🟢 Low |

## 功能概述
- Book: "Data-Driven Construction" by Artem Boiko, Chapter 2.4
- Website: https://datadrivenconstruction.io
- pdfplumber Docs: https://github.com/jsvine/pdfplumber
- Tesseract OCR: https://github.com/tesseract-ocr/tesseract
- See `image-to-data` for image processing
- See `cad-to-data` for CAD/BIM data extraction

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23