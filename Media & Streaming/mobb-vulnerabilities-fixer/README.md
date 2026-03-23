# Mobb Vulnerabilities Fixer

> Scan, fix, and remediate security vulnerabilities in a local code repository using Mobb MCP/CLI. Use when the user asks to scan for vulnerabilities, run a security check, auto-fix issues, remediate findings, or apply Mobb fixes (e.g., \"scan this repo\", \"fix security issues\", \"remediate vulnerabilities\", \"run Mobb on my changes\").

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mobb Vulnerabilities Fixer |
| **作者** | jonathansantilli |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/jonathansantilli-mobb-vulnerabilities-fixer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jonathansantilli/mobb-vulnerabilities-fixer |
| **安全评级** | 🟡 Medium |

## 功能概述
- `path`: absolute path to the repository root
- `offset`: pagination offset for additional fixes
- `limit`: maximum number of fixes to return (default is 3)
- `maxFiles`: scan up to N recently changed files (default is 10); setting this triggers a fresh scan
- `rescan`: force a full rescan; only when user explicitly asks
- `scanRecentlyChangedFiles`: when true and no git changes are found, scan recently changed files from history

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `agents`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23