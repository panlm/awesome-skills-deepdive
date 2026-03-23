# Skill Install Guardian

> "Security and due diligence layer for installing external skills from ClawHub. Performs DEEP content scanning for malicious patterns, security checks, integration analysis, and requires owner confirmation before installation."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Install Guardian |
| **作者** | zendenho7 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/zendenho7-skill-install-guardian |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zendenho7/skill-install-guardian |
| **安全评级** | 🔴 High |

## 功能概述
- Fetches SKILL.md and script files (.py, .js, .sh)
- Scans for dangerous patterns in file contents
- Detects: command injection, API keys, hardcoded secrets, obfuscated code

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，0 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23