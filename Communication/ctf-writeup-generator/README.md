# CTF Writeup Generator

> Automatically generate professional CTF writeups from solving sessions with flag detection, challenge categorization, and proper markdown formatting

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CTF Writeup Generator |
| **作者** | akhmittra |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/akhmittra-ctf-writeup-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/akhmittra/ctf-writeup-generator |
| **安全评级** | 🔴 High |

## 功能概述
- 🎯 Automatic Flag Detection: Recognizes common CTF flag formats (CTF{}, HTB{}, SHAASTRA{}, etc.)
- 📂 Smart Categorization: Auto-categorizes challenges (Web, Binary, Crypto, Forensics, etc.)
- 📝 Professional Formatting: Generates markdown with proper syntax highlighting
- 🛠️ Tool Recognition: Identifies and documents tools used during the solve
- 🎨 Multiple Templates: Academic, speedrun, tutorial, and portfolio styles
- 📤 Export Options: Markdown, PDF, HTML formats

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `QUICKSTART.md`
- `SKILL.md`
- `_meta.json`
- `example_writeup.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23