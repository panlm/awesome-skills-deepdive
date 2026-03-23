# Deslop

> Remove AI-style code slop from a branch by reviewing diffs, deleting inconsistent defensive noise, and preserving behavior and local style.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deslop |
| **作者** | brennerspear |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/brennerspear-deslop |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brennerspear/deslop |
| **安全评级** | 🟢 Low |

## 功能概述
- "remove AI slop"
- "clean up generated code style"
- "review branch diff for weird comments/defensive checks/casts"
- Do not remove protections at trust boundaries (user input, auth, network, db, file I/O).
- Do not replace real typing with weaker typing.
- Prefer minimal edits over broad rewrites.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23