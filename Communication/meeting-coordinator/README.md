# Meeting Coordinator - In Person + Virtual (Google Meet)

> 高管级日程协调助手，自动处理会议安排中的邮件沟通、日历冲突和场地预订

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Meeting Coordinator - In Person + Virtual (Google Meet) |
| **作者** | voshawn |
| **版本** | 1.0.3 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/voshawn-meeting-coordinator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/voshawn/meeting-coordinator |
| **安全评级** | 🔴 High |

## 功能概述
- 智能解析会议邀请邮件
- 自动检测日历时间冲突
- 会议场地/会议室预订
- 参会者可用时间协调
- 会议确认和提醒邮件发送
- 多时区会议时间转换
- 会议议程自动生成

## 使用场景
- CEO 助理自动协调多方参会者的会议时间
- 跨时区团队会议的智能排期和场地预订
- 处理会议变更请求并自动通知所有参会者

## 依赖和前提条件
- 邮箱账户接入（IMAP/SMTP 或 API）
- 日历服务接入（Google Calendar/Outlook）
- 会议室/场地预订系统权限

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
