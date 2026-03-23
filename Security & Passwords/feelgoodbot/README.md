# feelgoodbot

> 情绪支持机器人 — 正能量对话和鼓励

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feelgoodbot |
| **作者** | kris-hansen |
| **ClawHub** | https://clawskills.sh/skills/kris-hansen-feelgoodbot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kris-hansen/feelgoodbot |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Pronounced "Feel good, bot"
- GitHub: https://github.com/kris-hansen/feelgoodbot
- Go 1.21+ — Install with `brew install go`
- macOS — Uses launchd for daemon
- System binaries (`/usr/bin`, `/usr/sbin`)
- Launch daemons/agents (persistence mechanisms)

## 依赖和前提条件
- macOS** — Uses launchd for daemon

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🔴 High | 包含代码混淆或动态执行 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23