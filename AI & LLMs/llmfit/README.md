# llmfit

> 使用 LLM 优化健身计划和营养方案的智能助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | llmfit |
| **作者** | alexsjones |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/alexsjones-llmfit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alexsjones/llmfit |
| **安全评级** | 🟢 Low |

## 功能概述
- 基于个人身体数据生成定制化健身计划
- 提供 AI 驱动的营养建议和饮食方案
- 跟踪和分析健身进展并调整计划
- 支持多种健身目标：增肌、减脂、体能提升等
- 提供运动动作指导和注意事项
- 支持与健身数据源的集成
- 基于科学研究的训练方法推荐

## 使用场景
- 根据个人体质和目标生成专属健身训练计划
- AI 营养师根据饮食记录提供膳食优化建议
- 健身过程中实时调整训练强度和恢复策略

## 依赖和前提条件
- LLM API 密钥
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
