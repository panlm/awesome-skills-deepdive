# voice-email

> 通过自然语音命令撰写和发送邮件，专为无障碍使用场景设计

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | voice-email |
| **作者** | sundiver1 |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sundiver1-voice-email |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sundiver1/voice-email |
| **安全评级** | 🔴 High |

## 功能概述
- 语音输入自动转换为邮件内容
- 自然语言指定收件人、主题和正文
- 语音确认后自动发送邮件
- 支持语音朗读收到的邮件
- 为视障或行动不便用户优化的无障碍体验
- 支持语音纠错和内容修改

## 使用场景
- 视障用户通过语音完成日常邮件收发
- 驾驶或运动中需要免手操作发送邮件
- 行动不便人士的无障碍邮件通信

## 依赖和前提条件
- 邮件服务器凭据（SMTP）
- 语音输入设备（麦克风）
- 语音识别服务支持

## 包含文件
- `README.md`
- `SETUP.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
