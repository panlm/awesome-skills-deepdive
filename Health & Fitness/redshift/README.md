# Redshift

> Redshift 数据仓库查询工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Redshift |
| **作者** | accolver |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/accolver-redshift |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/accolver/redshift |
| **安全评级** | 🔴 High |

## 功能概述
- Project (`-p`): a project slug (e.g. `backend`, `myapp`)
- Config/Environment (`-c`): an environment slug (e.g. `dev`, `staging`, `production`)
- redshift.yaml: per-directory project config created by `redshift setup`
- When `-p`/`-c` are omitted, Redshift reads from `redshift.yaml` in the current directory
- Never pass secret values directly on the command line in shared/logged environments — prefer `redshift secrets set` interactively or pipe from stdin
- Use `REDSHIFT_NSEC` / `REDSHIFT_BUNKER` env vars for CI/CD rather than CLI flags
- Avoid `redshift serve --host 0.0.0.0` unless you intend to expose the web UI to the network — default `127.0.0.1` is localhost-only
- All encryption is client-side; secrets never leave the device unencrypted

## 使用场景
- 执行 Amazon Redshift 数据查询
- 管理数据仓库的表和视图
- 优化数据查询的性能

## 依赖和前提条件
- Python / pip
- Docker
- API Key
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
