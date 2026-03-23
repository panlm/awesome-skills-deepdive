# Skill Sandbox

> Test untrusted skills in an isolated environment before installing. Monitors network access, filesystem writes, environment variable reads, and subprocess calls. Run any skill safely without risking your agent's data or credentials.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Sandbox |
| **作者** | trypto1019 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-skill-sandbox |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-skill-sandbox |
| **安全评级** | 🟡 Medium |

## 功能概述
- Files opened (read/write)
- Directories created
- File deletions
- Permission changes
- Which env vars are read
- Whether sensitive keys are accessed (API keys, tokens, passwords)

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Python / pip
- Docker

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23