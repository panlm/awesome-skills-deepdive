# Agent Rpg

> 将 Agent 变为全能 RPG 游戏主持人——支持任何题材的文字角色扮演游戏

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Rpg |
| **作者** | xhrisfu |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/xhrisfu-agent-rpg |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xhrisfu/agent-rpg |
| **安全评级** | 🟢 Low |

## 功能概述
- 完整的 Session Zero 协议：逐步引导世界观、势力、角色创建和机制选择
- 支持多种规则系统：D20（D&D）、2D6（PbtA）、D100（CoC）和自由叙事
- 适配任何题材：赛博朋克、奇幻、恐怖、黑色电影等
- 状态管理工具：持久化记忆、掷骰子、叙事后果追踪
- 安全工具：设定"硬线"和"面纱"保护玩家边界
- 结构化游戏循环：状态检索 → 掷骰判定 → 叙事生成 → 选项呈现

## 使用场景
- 与 AI 进行沉浸式文字角色扮演游戏，体验个性化故事冒险
- 快速搭建各种题材的 TRPG 跑团环境，无需人类 GM
- 利用 Agent 的持久记忆实现长期连续的战役叙事

## 依赖和前提条件
- Python 3.x（dice.py 掷骰脚本）

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
