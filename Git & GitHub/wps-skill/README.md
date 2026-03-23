# Wps Skill

> WPS Office automation skill supporting document creation, Markdown conversion, and image-text layout.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Wps Skill |
| **作者** | lilei0311 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lilei0311-wps-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lilei0311/wps-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 📄 创建文档 - 创建 Word、Excel、PPT 文档
- 📂 打开文档 - 打开已有文档
- 📋 文档列表 - 列出文档目录中的文件
- 🔄 格式转换 - 转换文档格式（PDF、Word、Excel 等）
- 📦 批量处理 - 批量转换目录中的文档

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- macOS
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config.json`
- `scripts`
- `skill.json`
- `test`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23