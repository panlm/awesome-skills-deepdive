# Context Gatekeeper

> 通过自动摘要、待办提取和近期对话日志保持会话 token 高效，为每次模型调用提供精简简报

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Context Gatekeeper |
| **作者** | davienzomq |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/davienzomq-context-gatekeeper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davienzomq/context-gatekeeper |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动压缩活跃对话历史，生成紧凑摘要
- 识别并提取待处理任务（todo、task、follow-up 等关键词）
- 保留最近几轮对话记录，确保上下文连贯
- 通过 auto_monitor.py 实时监控历史文件变更并自动更新摘要
- 使用 ensure_context_monitor.sh 确保监控进程在重启后自动恢复
- 输出包含时间戳、摘要、待办和近期对话的 current-summary.md
- 支持自定义摘要长度、待办数量和近期对话轮数参数

## 使用场景
- 长对话会话中自动精简上下文以节省 token 消耗
- 在 24/7 运行的 Agent 中持续维护对话状态摘要
- 会话重置或重启后快速恢复上下文状态

## 依赖和前提条件
- Python 3
- 无外部 pip 依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
