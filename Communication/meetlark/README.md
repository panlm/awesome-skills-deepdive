# Meetlark - coordinate a meeting

> Scheduling polls for humans and their agents. Create polls, share participation links, collect votes, and find the best meeting time. A Doodle alternative built for the age of AI agents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Meetlark - coordinate a meeting |
| **作者** | mkelk |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/mkelk-meetlark |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkelk/meetlark |
| **安全评级** | 🟡 Medium |

## 功能概述
- Admin token (`adm_...`) — Private. View full results, see who voted, close the poll. Store it in your memory for the pol
- Participate token (`prt_...`) — Shareable. Anyone with the participate URL can vote — humans via the web UI, agents via 
- OpenAPI spec: https://meetlark.ai/api/v1/openapi.json
- Interactive docs: https://meetlark.ai/docs
- AI plugin manifest: https://meetlark.ai/.well-known/ai-plugin.json
- meetlark.ai: https://meetlark.ai

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

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