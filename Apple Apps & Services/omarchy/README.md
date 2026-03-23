# omarchy

> macOS 系统配置和开发环境管理框架

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | omarchy |
| **作者** | achals-iglu |
| **ClawHub** | https://clawskills.sh/skills/achals-iglu-omarchy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/achals-iglu/omarchy |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Bad (generic shortcut):
- Good (Omarchy-native):
- Why: Omarchy wrappers usually handle environment/session assumptions better than raw kill-and-relaunch one-liners.
- restarting random processes manually until things look fixed
- use targeted refresh script first, e.g. `omarchy-refresh-waybar`, `omarchy-refresh-hyprland`, `omarchy-refresh-config` (pick by component)
- Why: refresh scripts are explicit and reversible; manual shotgun restarts are noisy and risky.

## 依赖和前提条件
- Bad:
- using raw `pacman`/`yay` first without checking Omarchy wrappers
- Good:
- Why: wrapper flow keeps behavior consistent with Omarchy expectations.
- `omarchy-pkg-drop`

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟡 Medium | 包含网络探测功能 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23