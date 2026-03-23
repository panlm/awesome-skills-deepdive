# Vet Repo

> Scan repository agent configuration files for known malicious patterns

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Vet Repo |
| **作者** | itsnishi |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/itsnishi-vet-repo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/itsnishi/vet-repo |
| **安全评级** | 🟡 Medium |

## 功能概述
- `.claude/settings.json` -- hook configs (auto-approve, stop loops, env persistence)
- `.claude/skills/` -- all SKILL.md files (hidden comments, curl|bash, persistence triggers)
- `.mcp.json` -- MCP server configs (unknown URLs, env var expansion, broad tools)
- `CLAUDE.md` / `.claude/CLAUDE.md` -- instruction injection in project config

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
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23