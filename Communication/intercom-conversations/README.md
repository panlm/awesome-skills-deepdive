# intercom-conversations

> Intercom 客服对话管理工具，通过 Node 模块读取和管理客户对话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | intercom-conversations |
| **作者** | duyeng |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/duyeng-intercom-conversations |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/duyeng/intercom-conversations |
| **安全评级** | 🟢 Low |

## 功能概述
- 获取和浏览 Intercom 客服对话列表
- 查看对话详情和消息历史
- 通过 Node.js 模块调用 Intercom API
- 支持对话筛选和搜索
- 管理客服工单状态

## 使用场景
- AI 助手自动监控和分类客服对话
- 快速检索特定客户的历史沟通记录
- 将 Intercom 对话数据集成到工作流中

## 依赖和前提条件
- Intercom 账户和工作区
- Intercom API Access Token
- Node.js 运行环境
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `clawhub.skill.json`
- `index.js`
- `openapi.yaml`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
