# Coordinate a Meeting

> 智能会议协调工具，为人类和智能体安排会议、创建调度投票并分发参会链接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Coordinate a Meeting |
| **作者** | mkelk |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/mkelk-coordinate-meeting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkelk/coordinate-meeting |
| **安全评级** | 🔴 High |

## 功能概述
- 创建调度投票让参会者选择可用时间
- 自动汇总投票结果确定最佳会议时间
- 生成并分发会议参会链接
- 支持人类和智能体混合参会的场景
- 多时区智能适配和展示
- 会议提醒和日程同步

## 使用场景
- 团队负责人为跨时区成员创建投票选出最佳会议时间
- 智能体自动协调多方日程并发送会议邀请
- 人机协作会议的统一调度和通知管理

## 依赖和前提条件
- 配置日历服务集成
- 配置参会者联系方式和通知渠道
- 设置会议平台（Zoom、Meet 等）API 凭证

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
