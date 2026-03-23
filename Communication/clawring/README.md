# clawr.ing

> 真实电话拨打工具，使用托管服务替代本地语音通话插件，实现智能体拨打真实电话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawr.ing |
| **作者** | marcospgp |
| **版本** | 1.0.3 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/marcospgp-clawring |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marcospgp/clawring |
| **安全评级** | 🔴 High |

## 功能概述
- 拨打真实电话号码进行语音通话
- 托管云服务，无需本地语音硬件
- 文字转语音（TTS）自动通话内容播报
- 通话记录和日志管理
- 支持国际电话和多种语言

## 使用场景
- 智能体自动拨打电话提醒用户重要事项或日程
- 客服智能体通过电话回访客户和处理售后问题
- 紧急情况下智能体通过电话通知相关人员

## 依赖和前提条件
- 配置电话服务提供商 API（如 Twilio）
- 充值通话费用余额
- 遵守当地电话通信法规

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
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
