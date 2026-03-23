# Islamic Companion

> 伊斯兰日历和祈祷时间 — 伊斯兰历法和礼拜提醒

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Islamic Companion |
| **作者** | ilmimris |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/ilmimris-islamic-skills |
| **安全评级** | 🟡 Medium |

## 功能概述
- 伊斯兰历法日期转换
- 每日祈祷时间计算
- 斋月和节日提醒
- 朝向（Qibla）计算

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Python 3.x 及相关依赖
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23