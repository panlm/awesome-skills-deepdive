# kradleverse-init

> 在 Kradleverse 平台注册 agent 身份

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | kradleverse-init |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-kradleverse-init |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-init |
| **安全评级** | 🟡 Medium |

## 功能概述
- 检查名称可用性
- 注册 agent 并获取 API Key（仅显示一次）
- 保存凭证到 ~/.kradle/kradleverse/.env
- 需要 Twitter 验证完成注册流程
- 与 init 技能功能相同（更规范的命名）

## 使用场景
- 首次加入 Kradleverse Minecraft 游戏平台
- 注册 agent 身份获取游戏凭证

## 依赖和前提条件
- curl
- Twitter 账号

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 注册流程说明 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl 和 cat 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向 kradleverse.com 发送注册信息 |
| SEC-03 凭证获取 | 🟡 Medium | 获取 API Key 并写入本地文件 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建 ~/.kradle/kradleverse/.env 文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 在用户目录下操作 |
| SEC-08 持久化机制 | 🟢 Safe | 仅凭证文件 |
| SEC-09 信息采集 | 🟢 Safe | 仅注册数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档透明 |

**综合评级: 🟡 Medium**
**风险摘要:** 向第三方注册并写入凭证文件，风险可控，与 init 技能相同。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
