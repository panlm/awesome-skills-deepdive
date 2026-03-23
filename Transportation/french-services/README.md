# French Services

> 法国公共服务查询和集成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | French Services |
| **作者** | hugosbl |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/hugosbl-french-services |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hugosbl/french-services |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询法国政府公共服务信息
- 获取行政手续和流程指南
- 支持多种法国公共服务 API

## 使用场景
- 查询法国行政手续所需的文件和流程
- 获取法国公共服务的最新政策信息

## 依赖和前提条件
- API Key（法国公共服务平台）

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

> 本文档由 awesome-skills-deepdive skill 自动生成
