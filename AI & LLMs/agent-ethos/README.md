# Agent Ethos

> Agent 的扩展行为准则和心智模型，用于行为审计和决策规范调优

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Ethos |
| **作者** | mrclanky |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/mrclanky-agent-ethos |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mrclanky/agent-ethos |
| **安全评级** | 🟢 Low |

## 功能概述
- 提供一套 Agent 行为和决策的心智模型框架
- 核心信念：多数失败源于激励不清晰而非恶意
- 强调系统性维护：系统不主动维护就会漂移
- 关系定位：作为可信赖的合作伙伴而非被动工具
- 高风险决策时主动放慢节奏，必要时提出异议

## 使用场景
- 对 Agent 行为进行一致性审计，确保决策符合预期规范
- 调整 Agent 的人格特质和决策风格

## 依赖和前提条件
- 无外部依赖

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
