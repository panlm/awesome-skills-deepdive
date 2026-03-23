# Phone Caller

> AI 电话拨打工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Phone Caller |
| **作者** | omerflo |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/omerflo-phone-caller |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/omerflo/phone-caller |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动化电话拨打
- 通话脚本管理
- 通话记录追踪
- 语音 AI 对话

## 使用场景
- 使用 AI 自动拨打销售或客服电话
- 管理和追踪自动化外呼活动的效果

## 依赖和前提条件
- API 密钥
- Python 运行环境
- OpenAI API
- Twilio
- Webhook 配置

## 包含文件
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
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23