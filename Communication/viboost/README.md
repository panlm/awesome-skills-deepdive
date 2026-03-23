# Viboost

> 自动将 AI 智能体的活动和成果记录到用户的 viboost.ai 公开个人档案

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Viboost |
| **作者** | osipov-anton |
| **版本** | 1.2.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/osipov-anton-viboost |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/osipov-anton/viboost |
| **安全评级** | 🔴 High |

## 功能概述
- 自动捕获和记录智能体活动日志
- 将活动同步到 viboost.ai 公开档案页面
- 支持自定义活动类型和描述
- 构建可展示的 AI 使用履历
- 活动时间线可视化展示

## 使用场景
- 展示个人 AI 工具使用能力和项目经验
- 建立公开的 AI 协作成果档案
- 团队成员展示各自的 AI 赋能工作记录

## 依赖和前提条件
- viboost.ai 账户
- viboost API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
