# telegram send files

> 通过 Telegram 快速发送文件，一行命令即可完成文件传输

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | telegram send files |
| **作者** | shingwha |
| **版本** | 2.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/shingwha-tsend |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shingwha/tsend |
| **安全评级** | 🔴 High |

## 功能概述
- 命令行一键发送文件到 Telegram 聊天
- 支持发送文档、图片、视频等多种文件类型
- 支持指定接收者或群组
- 文件发送进度显示
- 支持批量发送多个文件

## 使用场景
- 开发者快速将服务器日志或报告发送到 Telegram
- 自动化流程中将生成的文件通过 Telegram 分发
- 远程设备上的文件快速传输到手机

## 依赖和前提条件
- Telegram Bot Token
- 目标聊天 ID 或群组 ID
- tsend CLI 工具

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
