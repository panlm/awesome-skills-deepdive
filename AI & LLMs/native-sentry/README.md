# Native Sentry

> 通过 Sentry REST API 读取生产环境错误和问题，支持查看堆栈追踪和 PII 脱敏

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Native Sentry |
| **作者** | codeninja23 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/codeninja23-native-sentry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/codeninja23/native-sentry |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出最近未解决的 Sentry 问题
- 获取问题详情和关联事件
- 查看事件详情及可选堆栈追踪信息
- 解析短 ID（如 MYAPP-123）到内部 ID
- 默认自动脱敏 PII 信息（邮箱、IP 等）
- 纯 Python 标准库实现，无需 pip 安装

## 使用场景
- 快速检查生产环境中最近出现的错误和异常
- 通过 AI 智能体自然语言查询 Sentry 问题并获取堆栈追踪
- 生成生产健康状况摘要报告

## 依赖和前提条件
- Python 3（仅标准库）
- SENTRY_AUTH_TOKEN（需 project:read、event:read、org:read 权限）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
