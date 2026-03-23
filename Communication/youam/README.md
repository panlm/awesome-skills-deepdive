# YouAM

> 基于通用智能体消息传递协议（Universal Agent Messaging）实现跨平台 AI 智能体互通

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | YouAM |
| **作者** | midlifedad |
| **版本** | 0.3.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/midlifedad-youam |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/midlifedad/youam |
| **安全评级** | 🟢 Low |

## 功能概述
- 实现 Universal Agent Messaging 标准协议
- 跨平台 AI 智能体间收发消息
- 支持结构化消息格式和自定义载荷
- 智能体身份验证和消息路由
- 异步消息队列和可靠投递
- 支持多对多智能体通信拓扑

## 使用场景
- 不同平台的 AI 智能体之间建立通信协作
- 构建多智能体协作系统的消息总线
- 跨组织的智能体间安全消息交换

## 依赖和前提条件
- YOUAM 协议兼容的智能体环境
- 网络访问权限
- 智能体身份注册

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
