# Clawemail

> 通过 ClawEmail.com 接入 Google Workspace 全套服务，包括 Gmail、Drive、Docs、Sheets 和 Slides

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Clawemail |
| **作者** | cto1 |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/cto1-clawemail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cto1/clawemail |
| **安全评级** | 🔴 High |

## 功能概述
- Gmail 邮件收发和管理
- Google Drive 文件存储和共享
- Google Docs 文档创建和编辑
- Google Sheets 电子表格操作
- Google Slides 演示文稿制作
- 统一的 Google Workspace 访问入口

## 使用场景
- 智能体通过 Google Workspace 完成日常办公文档处理
- 自动化邮件处理、文件归档和报告生成流程
- 团队协作中智能体代为创建和分享文档

## 依赖和前提条件
- 注册 ClawEmail.com 账户
- 完成 Google Workspace 授权
- 配置 ClawEmail API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

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
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
