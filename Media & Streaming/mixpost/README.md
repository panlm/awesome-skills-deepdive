# Mixpost

> Mixpost 多平台社交媒体管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mixpost |
| **作者** | lao9s |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/lao9s-mixpost |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lao9s/mixpost |
| **安全评级** | 🟡 Medium |

## 功能概述
- Mixpost is a self-hosted social media management software that helps you schedule and manage your social media content across multiple platforms including Facebook, Twitter/X, Instagram, LinkedIn, Pinterest, TikTok, YouTube, Mastodon, Google Business Profile, Threads, Bluesky, and more
- 支持通过命令行进行操作控制
- 提供自动化工作流集成

## 使用场景
- 管理多个社交媒体平台的发布
- 统一排期和管理内容
- 分析跨平台社交媒体数据

## 依赖和前提条件
- API 密钥或访问令牌
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
