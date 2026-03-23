# Switch Modes

> 快速切换 AI 对话模式，支持多种预设交互风格

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Switch Modes |
| **作者** | serudda |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/serudda-switch-modes |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/serudda/switch-modes |
| **安全评级** | 🟢 Low |

## 功能概述
- 在不同 AI 对话模式间快速切换
- 支持预设的多种交互模式
- 自定义模式参数和行为规则
- 通过简单命令切换系统提示词
- 适用于需要多角色或多场景的工作流
- 提高 AI 助手的灵活性和适应性

## 使用场景
- 工作中需要在编程助手、写作助手等模式间切换
- 构建多角色 AI 助手支持不同场景需求

## 依赖和前提条件
- Bash/Shell 环境
- API Key
- Anthropic API Key
- OpenAI API Key

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
