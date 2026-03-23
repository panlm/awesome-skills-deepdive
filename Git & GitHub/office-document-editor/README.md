# Office Document Editor

> 专业的 DOCX/PPTX 文档编辑工具，支持修订追踪、格式保留、高亮标注和 Git 版本控制

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Office Document Editor |
| **作者** | tsukisama9292 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tsukisama9292-office-document-editor |

## 功能概述
- 编辑 DOCX 文档：支持文本替换、插入、删除，保留原有格式
- 编辑 PPTX 演示文稿：支持幻灯片重排和内容修改
- 多种标注样式：高亮、删除线、加粗等
- 生成文档差异对比报告（diff）
- 支持多种文件来源：上传附件、本地路径、URL、SFTP
- 交互式编辑模式
- 通过 JSON 规则文件定义批量编辑操作

## 使用场景
- 在命令行中批量编辑 Word/PowerPoint 文档，无需打开 Office 软件
- 对文档进行修订追踪和版本对比
- 从远程服务器获取文档、编辑后再推送回去

## 依赖和前提条件
- `uv`（Python 包管理器）
- `curl`
- 通过 uv 自动安装 Python 依赖（docx_editor.py、pptx_editor.py 等）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23