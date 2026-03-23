# CMA Email

> 当消息以 'cma' 开头时通过 Gmail 发送邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CMA Email |
| **作者** | mtbf999 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/mtbf999-cma-email |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mtbf999/cma-email |
| **安全评级** | 🟢 Low |

## 功能概述
- 检测以 'cma' 或 'cmap' 开头的消息
- 通过 Gmail API 自动发送邮件
- 支持自定义收件人和邮件内容

## 使用场景
- 在聊天中快速发送邮件给指定联系人
- 通过简单前缀触发邮件发送流程

## 依赖和前提条件
- Gmail API 凭证

## 安全状态
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

> 本文档由 awesome-skills-deepdive skill 自动生成
