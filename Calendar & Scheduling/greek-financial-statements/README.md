# Greek Financial Statements

> 希腊财务报表处理 — 希腊标准财务文档解析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Greek Financial Statements |
| **作者** | satoshistackalotto |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/satoshistackalotto-greek-financial-statements |
| **安全评级** | 🟡 Medium |

## 功能概述
- 解析希腊标准财务报表
- 财务数据提取和结构化
- 合规性检查和验证
- 报表格式转换

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Anki 桌面版 + AnkiConnect 插件

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23