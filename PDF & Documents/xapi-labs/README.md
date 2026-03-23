# xAPI

> xAPI 学习数据标准工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | xAPI |
| **作者** | glacier-luo |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/glacier-luo-xapi-labs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/glacier-luo/xapi-labs |
| **安全评级** | 🔴 High |

## 功能概述
- xAPI 语句生成和管理
- 学习活动数据追踪
- LRS 数据交互
- 学习分析报告

## 使用场景
- 为在线学习平台生成 xAPI 标准的学习记录
- 分析学员学习行为数据

## 依赖和前提条件
- API 密钥
- OAuth 认证
- Google API
- Stripe

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23