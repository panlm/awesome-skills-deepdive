# llmfit

> Detect local hardware (RAM, CPU, GPU/VRAM) and recommend the best-fit local LLM models with optimal quantization, speed estimates, and fit scoring.

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
- "what local models can I run?"
- "which LLMs fit my hardware?"
- "recommend a local model"
- "what's the best model for my GPU?"
- "can I run Llama 70B locally?"
- "configure local models"

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Homebrew

## 包含文件
- `SKILL.md`
- `_meta.json`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23