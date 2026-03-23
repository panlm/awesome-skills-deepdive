# RamaLama CLI

> Run and interact with AI agents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RamaLama CLI |
| **作者** | ieaves |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/ieaves-ramalama-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ieaves/ramalama-cli |
| **安全评级** | 🟢 Low |

## 功能概述
- flexible model sourcing (`hf://`, `oci://`, `rlcr://`, `url://`)
- containerized local inference with runtime/network/device controls
- RAG data packaging and serving
- benchmark/perplexity evaluation
- model conversion and registry push/pull flows
- One-shot inference: `ramalama run <model> "<prompt>"`

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Docker

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23