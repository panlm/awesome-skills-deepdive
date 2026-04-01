# Postavel

> 通过 MCP 协议连接 Postavel 社交媒体管理平台，创建、排期和管理跨平台社交内容

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Postavel |
| **作者** | nezaboravi |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/nezaboravi-postavel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nezaboravi/postavel |
| **安全评级** | 🔴 High |

## 功能概述
- 通过自然语言创建和管理社交媒体帖子
- 支持 Facebook、Instagram 和 LinkedIn 多平台发布
- 内容排期和日历管理功能
- 通过 MCP（Model Context Protocol）协议通信
- 支持查看和管理内容日历
- 在 OpenClaw 中通过对话界面直接操作社交媒体

## 使用场景
- 通过 AI 智能体自然语言排期一周的社交媒体内容
- 跨 Facebook、Instagram、LinkedIn 同步发布营销内容
- 查看和调整内容发布日历

## 依赖和前提条件
- Postavel 账户
- MCP 协议支持
- Postavel API 访问凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
