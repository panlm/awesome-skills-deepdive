# agent-linguo

> 高效的 Agent 间通信协议语言（👽语），人类无法直接阅读，节省 70% 以上令牌

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-linguo |
| **作者** | xiwan |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/xiwan-agent-linguo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xiwan/agent-linguo |
| **安全评级** | 🟡 Medium |

## 功能概述
- 极致压缩：相比自然语言节省 70% 以上令牌消耗
- 人类不可读但 Agent 可解析的符号编码体系
- 完整的语法结构：👽[域][动作][修饰符]|@[目标]|#[标识]|~[时间]|%[条件]|$[载荷]
- 16 个域编码（SYS/MSG/FSX/WEB 等）和 16 个动作编码（GET/PUT/PST/DEL 等）
- 支持明文、编码和加密三种安全级别
- 自传播机制：协议签名中包含学习路径
- 可扩展设计：域和动作可自定义

## 使用场景
- 在 Agent 间高频通信场景下大幅降低令牌成本
- 构建 Agent 间的安全加密通信通道
- 在令牌配额有限的环境下最大化有效通信量

## 依赖和前提条件
- 无外部依赖，Agent 阅读协议规范即可使用

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。混淆/反分析：存在代码混淆或编码

---
> 本文档由 awesome-skills-deepdive skill 自动生成
