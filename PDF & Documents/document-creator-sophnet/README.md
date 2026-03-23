# document-creator-sophnet

> An integrated document creation skill that supports creating Word documents (DOCX) and PowerPoint presentations (PPTX), with automatic upload to OSS and URL return.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | document-creator-sophnet |
| **作者** | yi-sir |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/yi-sir-document-creator-sophnet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yi-sir/document-creator-sophnet |
| **安全评级** | 🟡 Medium |

## 功能概述
- ✅ Dual Format Support: DOCX and PPTX document creation
- ✅ Auto Upload: Automatically uploads to OSS and returns URL
- ✅ Smart Key Management: Environment variable first, config file backup
- ✅ Professional Formatting: Supports titles, lists, tables, etc.
- ✅ Error Handling: Complete exception capture and user-friendly prompts
- `type`: Document type (docx/pptx, required)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `document_creator.py`
- `document_creator_skill.py`
- `install.sh`
- `package.json`
- `test_integration.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23