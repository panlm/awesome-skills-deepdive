# Email Auto Reply Generator

> 智能邮件自动回复系统，根据收件内容上下文生成个性化的回复草稿

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Email Auto Reply Generator |
| **作者** | user520512 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/user520512-email-autoreply |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/user520512/email-autoreply |
| **安全评级** | 🟢 Low |

## 功能概述
- 分析收件邮件内容和上下文
- 生成语气得体的自动回复
- 支持自定义回复模板和风格
- 根据发件人关系调整回复策略
- 紧急邮件优先处理标记
- 多语言回复支持

## 使用场景
- 休假或忙碌时的邮件自动应答
- 常规咨询邮件的快速回复
- 客户邮件的初步自动响应

## 依赖和前提条件
- 邮箱账号访问权限
- OpenClaw 环境已配置

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
