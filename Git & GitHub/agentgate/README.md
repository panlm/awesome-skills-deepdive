# Agentgate Clawhub

> 个人数据的 API 网关，支持人机协同写入审批，连接 GitHub、Bluesky、Google Calendar 等多种服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agentgate Clawhub |
| **作者** | monteslu |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/monteslu-agentgate |

## 功能概述
- 读操作（GET）即时执行，写操作需经审批队列或可信代理绕过
- 支持多种服务：GitHub、Bluesky、Mastodon、Google Calendar、Home Assistant 等
- 代理间消息通信：发送、接收、广播消息，支持 supervised 和 open 模式
- Mementos 持久化记忆：通过关键词标签存储和检索跨会话笔记
- 写请求支持二进制数据上传（base64 编码）
- 服务发现端点 `/api/agent_start_here` 返回可用服务和 API 文档
- 支持撤回待审批的写请求

## 使用场景
- AI 代理安全地访问个人数据服务（日历、社交、代码仓库），所有写入需人工确认
- 多代理系统通过 agentgate 进行协调通信和任务分发
- 跨会话保持代理记忆，使用 Mementos 存储关键信息

## 依赖和前提条件
- 环境变量 `AGENT_GATE_TOKEN`（在 agentgate 管理界面创建）
- 环境变量 `AGENT_GATE_URL`（agentgate 服务器地址）
- agentgate 服务需运行在独立于 OpenClaw 的机器上

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
