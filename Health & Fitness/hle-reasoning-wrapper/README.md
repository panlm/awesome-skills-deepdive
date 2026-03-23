# Hle Reasoning Wrapper

> HLE 推理能力增强包装工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hle Reasoning Wrapper |
| **作者** | wanng-ide |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/wanng-ide-hle-reasoning-wrapper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wanng-ide/hle-reasoning-wrapper |
| **安全评级** | 🟢 Low |

## 功能概述
- Wraps HLE benchmark questions in a structured Chain-of-Thought (CoT) reasoning process
- Use when answering HLE questions to ensure strict step-by-step logic and format compliance
- 支持数据跟踪和记录

## 使用场景
- 增强 AI 模型的推理能力
- 封装复杂的推理链流程
- 优化推理任务的执行效果

## 依赖和前提条件
- 参见 SKILL.md 获取详细依赖信息

## 包含文件
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`
- `test.js`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
