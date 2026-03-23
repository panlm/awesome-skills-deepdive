# Email Tool

> 邮件发送和管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Email Tool |
| **作者** | chowardcode |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/chowardcode-email-tool |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chowardcode/email-tool |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 API 发送和接收邮件
- 支持邮件模板和批量发送
- 邮件内容格式化和附件处理

## 使用场景
- 自动发送通知邮件给指定收件人
- 处理和转发收到的重要邮件

## 依赖和前提条件
- 邮件服务 API 凭证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
