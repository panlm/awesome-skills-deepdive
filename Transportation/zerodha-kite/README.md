# Zerodha

> Route natural-language trading/account queries to the correct `zerodha` CLI command with exact flags, validation constraints, and synonym mapping. Use when a user asks to view prices, place/modify/cancel orders, manage auth/profile/config, work with holdings/positions/margins/GTT/MF flows, or asks "which zerodha command should I run?"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zerodha |
| **作者** | jatinbansal1998 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/jatinbansal1998-zerodha-kite |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jatinbansal1998/zerodha-kite |
| **安全评级** | 🟡 Medium |

## 功能概述
- Linux/macOS (`curl`): `curl -fsSL https://raw.githubusercontent.com/jatinbansal1998/zerodha-kite-cli/main/scripts/instal
- Linux/macOS (`wget`): `wget -qO- https://raw.githubusercontent.com/jatinbansal1998/zerodha-kite-cli/main/scripts/install
- Windows PowerShell: `irm https://raw.githubusercontent.com/jatinbansal1998/zerodha-kite-cli/main/scripts/install.ps1 | i
- Windows CMD: `powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/jatinbansal1
- `zerodha version`
- `--profile <name>`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23