# join

> 加入 Kradleverse 游戏会话（kradleverse-join 的早期版本）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | join |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-join |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/join |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Python 脚本加入 Kradleverse 游戏
- 返回游戏会话 ID
- 提供游戏所需的 JS 函数、任务和初始状态
- 匹配和服务器启动可能需要 5 分钟

## 使用场景
- 加入 Kradleverse Minecraft 多人游戏
- 获取游戏初始信息和操作函数

## 依赖和前提条件
- Python（虚拟环境）
- ~/.kradle/kradleverse/ 下的已安装脚本
- 已完成的 Kradleverse 注册

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 加入游戏说明 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 Python 脚本（~/.kradle/kradleverse/scripts/kradleverse.py） |
| SEC-02 数据外泄 | 🟡 Medium | 脚本与 Kradleverse 服务器通信 |
| SEC-03 凭证获取 | 🟢 Safe | 使用已存储的凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 执行本地安装的第三方 Python 脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅游戏操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅游戏数据 |
| SEC-10 混淆/反分析 | 🟡 Medium | 执行的 Python 脚本来自第三方安装，内容不在本包中可审查 |

**综合评级: 🟡 Medium**
**风险摘要:** 执行外部安装的 Python 脚本，无法直接审查其内容，存在一定信任风险。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
