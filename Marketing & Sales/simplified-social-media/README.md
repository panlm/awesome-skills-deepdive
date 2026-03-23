# Simplified Social Media

> 简化版社交媒体管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Simplified Social Media |
| **作者** | jacksimplified |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/jacksimplified-simplified-social-media |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jacksimplified/simplified-social-media |
| **安全评级** | 🟡 Medium |

## 功能概述
- 社交媒体内容简单管理
- 快速发布功能
- 基础数据追踪
- 多平台支持

## 使用场景
- 简化社交媒体内容的创建和发布流程
- 快速管理多个社交媒体平台的基础操作

## 依赖和前提条件
- API 密钥
- Google API
- Facebook API
- Instagram API
- TikTok API
- Bluesky API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
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