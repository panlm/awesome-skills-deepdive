# Claude Usage Checker

> 检查 Claude Code / Claude Max 使用额度和配额信息，通过交互式 CLI 读取用量数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Claude Usage Checker |
| **作者** | aligurelli |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/aligurelli-claude-usage-checker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aligurelli/claude-usage-checker |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过 PTY 启动 Claude CLI 并交互式读取 /usage 输出
- 报告当前会话、每周（全模型）、每周（仅 Sonnet）的使用百分比
- 显示额度重置时间，转换为标准 HH:MM 格式
- 支持额外用量（Extra usage）的费用追踪
- 自动处理 Claude CLI 的启动和退出流程
- 检测 API Key 缺失并提示用户手动登录

## 使用场景
- 快速查看 Claude Code 订阅的剩余额度和重置时间
- 在高频使用期间监控配额消耗速率
- 诊断 Claude CLI 连接和认证问题

## 依赖和前提条件
- Claude CLI（通过 `npm i -g @anthropic-ai/claude-code` 安装）
- 需要交互式 PTY 支持
- 用户需先完成 Claude CLI 的浏览器登录流程

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
