# calendar-scheduling

> |-

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | calendar-scheduling |
| **作者** | billylui |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/billylui-calendar-scheduling |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/billylui/calendar-scheduling |
| **安全评级** | 🔴 High |

## 功能概述
- ~/.config/temporal-cortex/credentials.json
- ~/.config/temporal-cortex/config.json
- Homepage: [temporal-cortex.com](https://temporal-cortex.com)
- Source code: [github.com/temporal-cortex/mcp](https://github.com/temporal-cortex/mcp) (open-source Rust)
- npm package: [@temporal-cortex/cortex-mcp](https://www.npmjs.com/package/@temporal-cortex/cortex-mcp)
- Skills repo: [github.com/temporal-cortex/skills](https://github.com/temporal-cortex/skills)

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- Node.js / npm
- Python / pip
- Docker
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23