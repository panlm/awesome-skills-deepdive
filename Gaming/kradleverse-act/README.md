# kradleverse-act

> 在 Kradleverse 游戏中发送动作指令

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | kradleverse-act |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-kradleverse-act |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-act |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在 Kradleverse 游戏会话中发送动作
- 通过 Python 脚本执行游戏操作
- 支持 --help 参数查看使用说明

## 使用场景
- 在 Kradleverse Minecraft 游戏中执行操作
- Agent 自主游戏行为控制

## 依赖和前提条件
- Python（虚拟环境）
- ~/.kradle/kradleverse/ 下的已安装脚本
- 活跃的游戏会话 ID

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 动作发送说明 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行第三方 Python 脚本（act.py） |
| SEC-02 数据外泄 | 🟡 Medium | 向 Kradleverse 服务器发送游戏动作 |
| SEC-03 凭证获取 | 🟢 Safe | 使用已存储的凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 执行本地安装的第三方脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅游戏操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅游戏数据 |
| SEC-10 混淆/反分析 | 🟡 Medium | 实际脚本内容不在包内，无法直接审查 |

**综合评级: 🟡 Medium**
**风险摘要:** 执行外部安装的 Python 脚本，脚本内容不可直接审计。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
