# Jentic

> AI 代理 API 中间件，通过统一接口发现和调用真实世界 API，无需在代理中存储凭证。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Jentic |
| **作者** | seanblanchfield |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/seanblanchfield-jentic |

## 功能概述
- 通过统一接口发现和执行多种 API（Gmail、GitHub、Stripe、Twilio 等）
- API 凭证服务端注入，代理本身不存储敏感密钥
- 按意图搜索 API 功能（如"发送邮件"）
- 浏览公开 API 目录，无需认证
- 查看 API 操作的详细 Schema
- 支持通过 `clawhub install` 或手动安装

## 使用场景
- 让 AI Agent 安全调用外部 API（如发邮件、查股票、管理日历）而无需暴露凭证
- 快速集成多种第三方服务到 OpenClaw 工作流中
- 降低 Prompt 注入攻击导致凭证泄露的风险

## 依赖和前提条件
- Jentic 账号（从 [jentic.com](https://jentic.com) 注册）
- Jentic Agent Key（`ak_...` 格式）
- `uv` 或 Python 环境运行 `jentic.py` 脚本

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
