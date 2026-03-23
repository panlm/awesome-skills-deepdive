# grepwrapper

> Search exact code matches across public GitHub repos using grep.app via the grepwrapper CLI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | grepwrapper |
| **作者** | riprsa |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/riprsa-grepwrapper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/riprsa/grepwrapper |
| **安全评级** | 🟢 Low |

## 功能概述
- find exact code matches on GitHub
- locate repo/file/path occurrences for a snippet
- run grep.app code search from CLI
- `--q <query>` required
- `--case` case-sensitive
- `--words` whole-word (mutually exclusive with `--regexp`)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23