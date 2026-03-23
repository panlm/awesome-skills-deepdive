# Microsoft 365

> Microsoft 365 全面集成，连接 Outlook 邮箱、日历、联系人和 OneDrive 云存储

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Microsoft 365 |
| **作者** | robert-janssen |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/robert-janssen-microsoft365 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/robert-janssen/microsoft365 |
| **安全评级** | 🔴 High |

## 功能概述
- Outlook 邮件收发和管理
- 日历事件创建和查询
- 联系人信息访问和管理
- OneDrive 文件上传和下载
- 邮件搜索和过滤
- 日历提醒和冲突检测
- 共享日历和文件夹管理

## 使用场景
- AI 助手自动读取和回复 Outlook 邮件
- 通过语音指令创建日历事件和设置提醒
- 智能整理 OneDrive 文件并与团队共享

## 依赖和前提条件
- Microsoft 365 订阅账户
- Azure AD 应用注册和 OAuth 认证
- Microsoft Graph API 权限配置

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`
- `setup.js`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，5 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
