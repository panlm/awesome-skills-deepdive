# Token Alert

> 实时监控 Anthropic Claude 会话 Token 用量，在达到阈值时发出告警

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Token Alert |
| **作者** | r00tid |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/r00tid-token-alert |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/r00tid/token-alert |
| **安全评级** | 🟡 Medium |

## 功能概述
- 实时追踪 Anthropic Claude API 的 Token 消耗量
- 在 75%、90%、95% 使用率时自动发出 CLI 告警
- 可选的可视化仪表盘展示 Token 使用趋势
- 支持自定义告警阈值和通知方式
- 帮助避免会话中途因 Token 耗尽而丢失上下文
- 轻量级 CLI 工具，无需复杂配置

## 使用场景
- 长时间与 Claude 对话时，实时监控剩余 Token 量，避免突然中断
- 团队共享 API Key 时，追踪和分配 Token 使用配额
- 开发环境中自动告警，提前切换对话或保存上下文

## 依赖和前提条件
- 参见 SKILL.md 获取详细依赖信息

## 安全状态
> 暂无安全审计数据

---
> 本文档由 awesome-skills-deepdive skill 自动生成
