# Anti Regression

> 防止 AI Agent 退化为聊天机器人行为的模式集合，帮助 Agent 在跨会话中保持自主性和执行效率。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Anti Regression |
| **作者** | zoroposkai |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/zoroposkai-anti-regression |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zoroposkai/anti-regression |
| **安全评级** | 🟡 Medium |

## 功能概述
- 识别并纠正 Agent 退化行为（过度请求许可、解释代替执行、犹豫代替决策）
- 提供具体的行为覆盖模式，维持 Agent 自主性
- 通过"CTO 测试"简单判断是否需要请求许可
- 可集成到 SOUL.md 或 AGENTS.md 中实现快速启用
- 包含示例和变更日志，便于理解和追踪改进

## 使用场景
- Agent 频繁退化为被动问答模式，需要主动保持自主执行能力
- 在定时任务或自动化流程中确保 Agent 直接行动而非等待指令
- 建立 Agent 行为规范，避免 LLM 基础训练带来的保守倾向

## 依赖和前提条件
- 安装方式：`clawhub install anti-regression`
- 无额外环境依赖

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
