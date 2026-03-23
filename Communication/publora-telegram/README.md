# Publora Telegram

> Publora 社交媒体管理工具的 Telegram 集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Publora Telegram |
| **作者** | sergebulaev |
| **版本** | 1.2.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sergebulaev-publora-telegram |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sergebulaev/publora-telegram |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 Telegram 管理 Publora 社交媒体内容
- 在 Telegram 中发布和调度社交帖子
- 接收 Publora 平台通知和更新
- 跨平台社交媒体内容分发

## 使用场景
- 通过 Telegram 机器人管理社交媒体发布
- 在移动端快速调度和发布内容

## 依赖和前提条件
- Publora 平台账号
- Telegram Bot Token
- 配置 Publora API 集成

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
