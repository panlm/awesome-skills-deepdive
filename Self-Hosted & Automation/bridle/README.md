# bridle

> AI 编程助手的统一配置管理器

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bridle |
| **作者** | bjesuiter |
| **ClawHub** | https://clawskills.sh/skills/bjesuiter-bridle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bjesuiter/bridle |
| **安全评级** | 🟢 Low |

## 功能概述
- 统一管理 Claude Code、OpenCode、Goose、Amp 等 AI 编程助手配置
- Profile 管理：创建、切换、比较、编辑配置方案
- 从 GitHub 安装 skills、agents、commands 和 MCP
- 交互式 TUI 终端界面
- 支持 JSON 和文本两种输出格式

## 使用场景
- 在多个 AI 编程助手间快速切换配置方案
- 统一管理工作/个人/最小化等不同配置
- 批量安装和管理 GitHub 上的组件

## 依赖和前提条件
- `bridle` CLI（通过 Homebrew 或 Cargo 安装）
- macOS 或 Linux

## 包含文件
- `SKILL.md` — 技能定义和完整使用文档
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅通过 `bridle` CLI 操作，无直接 shell 执行 |
| SEC-02 数据外泄 | 🟢 Safe | 仅本地配置管理，无网络传输 |
| SEC-03 凭证获取 | 🟢 Safe | 不直接处理凭证，配置文件在 ~/.config/bridle/ |
| SEC-04 供应链风险 | 🟡 Medium | 通过 `bridle install owner/repo` 从 GitHub 安装组件 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅修改 AI 助手配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 相关操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅配置管理功能 |
| SEC-08 持久化机制 | 🟢 Safe | 正常配置文件持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 仅 SKILL.md 文本，无代码 |

**综合评级: 🟢 Low**
**风险摘要:** 纯配置管理工具，无脚本代码，仅依赖外部 CLI，风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
