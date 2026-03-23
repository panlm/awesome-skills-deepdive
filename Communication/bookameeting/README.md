# Book a meeting

> 智能会议预约工具，帮助用户快速安排和管理会议日程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Book a meeting |
| **作者** | yzlee |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/yzlee-bookameeting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yzlee/bookameeting |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动查询参会者空闲时间并匹配最佳时段
- 创建会议邀请并发送通知
- 支持多种日历系统集成
- 自动生成会议链接（Zoom、Google Meet 等）
- 会议冲突检测和智能提醒

## 使用场景
- 助理智能体自动为用户安排多方会议
- 团队成员通过自然语言快速预约会议室和时间
- 跨时区团队协调最佳会议时间

## 依赖和前提条件
- 连接日历服务（Google Calendar、Outlook 等）
- 配置会议平台 API 密钥

## 包含文件
- `README.md`
- `_meta.json`
- `skill.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
