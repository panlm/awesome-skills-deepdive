# meeting-autopilot

> 会议自动驾驶系统，智能管理会议全流程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | meeting-autopilot |
| **作者** | tkuehnl |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/tkuehnl-meeting-autopilot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tkuehnl/meeting-autopilot |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动记录和转录会议内容
- 实时生成会议摘要和关键要点
- 智能提取行动项和任务分配
- 支持会议日程管理和提醒
- 提供会议效率分析和改进建议
- 支持多种会议平台集成
- 自动生成会议纪要并分发给参会者

## 使用场景
- 会议期间实时记录并生成结构化会议纪要
- 自动提取会议中的任务分配并创建跟踪项
- 分析团队会议效率并提供优化建议

## 依赖和前提条件
- 会议平台 API 集成
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
