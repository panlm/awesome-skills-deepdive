# Word Automation

> Automate common Word/WPS document operations on Windows via COM (read text, replace, insert, headings, headers/footers, page breaks, merge, split, export to PDF/TXT, add/replace images). Use for single-document actions (no batch).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Word Automation |
| **作者** | fadeloo |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/fadeloo-tiangong-wps-word-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/fadeloo/tiangong-wps-word-automation |
| **安全评级** | 🟢 Low |

## 功能概述
- Windows with Microsoft Word or WPS Writer installed.
- Python + pywin32 (`python -m pip install pywin32`).
- If WPS is installed, try `--app wps`; otherwise default uses Word.
- Use `--visible true` if you need to watch the UI.
- Avoid batch usage; this skill is for single-document operations.

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
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23