# aaaaa

> Gmail 自动回复工具，代表用户以其语气和模板自动应答收到的 Gmail 邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | aaaaa |
| **作者** | azvast |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/azvast-aa |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/azvast/aa |
| **安全评级** | 🔴 High |

## 功能概述
- 自动检测并回复新收到的 Gmail 邮件
- 学习用户写作风格，生成符合个人语气的回复
- 支持自定义回复模板和规则
- 智能判断邮件优先级，选择性自动回复
- 保留回复历史记录供用户审核

## 使用场景
- 出差或休假期间自动处理常规邮件回复
- 高频客服邮件的自动化应答
- 日常邮件分流，减少人工处理量

## 依赖和前提条件
- Gmail 账号及 OAuth 授权
- 配置回复模板或语气样本

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `manifest.json`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
