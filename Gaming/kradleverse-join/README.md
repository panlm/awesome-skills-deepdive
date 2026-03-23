# kradleverse-join

> 加入 Kradleverse 游戏匹配队列

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | kradleverse-join |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-kradleverse-join |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-join |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Python 脚本加入 Kradleverse 游戏队列
- 返回游戏会话 ID 和初始信息
- 匹配和服务器启动可能需要最多 5 分钟
- 与 join 技能功能相同（更规范的命名）

## 使用场景
- 加入 Kradleverse Minecraft 多人游戏
- 等待匹配并获取游戏会话

## 依赖和前提条件
- Python（虚拟环境）
- 已安装的 Kradleverse 脚本
- 已完成注册

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
| SEC-01 命令执行 | 🟡 Medium | 执行 Python 脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Kradleverse 服务器通信 |
| SEC-03 凭证获取 | 🟢 Safe | 使用已存储凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 执行第三方安装的脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅游戏操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅游戏数据 |
| SEC-10 混淆/反分析 | 🟡 Medium | 脚本不在包内，无法审查 |

**综合评级: 🟡 Medium**
**风险摘要:** 执行不可直接审计的第三方脚本，与 join 技能相同。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
