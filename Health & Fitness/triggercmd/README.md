# TRIGGERcmd - Run commands on your computers remotely

> Control TRIGGERcmd computers remotely by listing and running commands via the TRIGGERcmd REST API.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TRIGGERcmd - Run commands on your computers remotely |
| **作者** | rvmey |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/rvmey-triggercmd |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rvmey/triggercmd |
| **安全评级** | 🔴 High |

## 功能概述
- Export it in your shell: `export TRIGGERCMD_TOKEN='your-token-here'`
- Or prefix individual commands: `TRIGGERCMD_TOKEN='your-token-here' <command>`
- The file should contain only the raw token text (no quotes, spaces, or trailing newline)
- Must be permission-restricted: `chmod 600 ~/.TRIGGERcmdData/token.tkn`
- To create: `mkdir -p ~/.TRIGGERcmdData && read -s TOKEN && printf "%s" "$TOKEN" > ~/.TRIGGERcmdData/token.tkn && chmod 6
- For quick human output, pipe through `jq -r '.records[] | "\(.computer.name): \(.name) (voice: \(.voice // "-"))"'`.

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

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
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23