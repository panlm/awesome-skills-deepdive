# Build Session

> 为 AI Agent 自主工作会话提供框架，在定时任务或空闲时间保持高效产出而非被动等待。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Build Session |
| **作者** | stevenartzt |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/stevenartzt-build-session |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stevenartzt/build-session |
| **安全评级** | 🟡 Medium |

## 功能概述
- 提供结构化的自主工作会话框架
- 包含会话日志记录辅助脚本（session-log.sh）
- 包含随机任务选择器（pick-task.sh），从项目创意中选取任务
- 核心理念：每次会话必须产出成果，执行优于规划
- 支持通过 cron 定时任务触发构建会话

## 使用场景
- 为 AI Agent 设置定期自主工作时间，持续推进项目
- 在无人值守时让 Agent 自主选择并完成待办任务
- 建立"构建-记录-迭代"的 Agent 自主工作循环

## 依赖和前提条件
- 安装方式：`clawhub install build-session`
- 需要 Bash shell 环境

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
