# Expanso email-triage

> AI 驱动的邮件分诊系统，自动分类邮件优先级，支持日历同步和回复草稿生成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expanso email-triage |
| **作者** | aronchick |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/aronchick-expanso-email-triage |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-email-triage |
| **安全评级** | 🟢 Low |

## 功能概述
- 邮件自动分类和优先级排序
- AI 生成回复草稿供审核
- 日历事件自动同步和提醒
- 垃圾邮件和低优先级邮件过滤
- 重要邮件摘要和行动要点提取
- 支持多邮箱账号统一管理

## 使用场景
- 邮件量大时的智能分诊和优先处理
- 自动从邮件中提取会议邀请同步到日历
- 快速处理积压邮件并生成回复草稿

## 依赖和前提条件
- 邮箱账号访问权限（IMAP/API）
- 日历服务集成（可选）
- OpenClaw 环境已配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `examples`
- `pipeline-cli.yaml`
- `pipeline-mcp.yaml`
- `skill.yaml`
- `test`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
