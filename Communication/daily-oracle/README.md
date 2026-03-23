# Sentiet ORB

> 后台智能体，通过分析本地数据（日历、邮件、习惯等）生成每日个性化生活预测与建议

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sentiet ORB |
| **作者** | invelene |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/invelene-daily-oracle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/invelene/daily-oracle |
| **安全评级** | 🔴 High |

## 功能概述
- 分析本地数据生成每日预测
- 结合日历和待办事项推断日程建议
- 基于历史模式的行为预测
- 个性化生活建议和提醒
- 运势风格的趣味化呈现
- 后台自动运行无需手动触发

## 使用场景
- 每天获取基于个人数据的生活洞察
- 趣味性的每日运势和建议
- 发现日常生活中的规律和模式

## 依赖和前提条件
- OpenClaw 环境已配置
- 本地数据源（日历、邮件等）已连接

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
