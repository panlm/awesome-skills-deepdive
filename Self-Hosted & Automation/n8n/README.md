# n8n

> 通过 API 管理 n8n 工作流和自动化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | n8n |
| **作者** | thomasansems |
| **ClawHub** | https://clawskills.sh/skills/thomasansems-n8n |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thomasansems/n8n |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出/创建/激活/停用 n8n 工作流
- 从模板库创建 SaaS 自动化工作流
- 工作流结构验证和 Dry-Run 测试
- 执行监控和错误分析
- 性能优化分析（瓶颈检测、0-100 健康评分）
- 严格的工作流创建规则（禁止占位符节点）

## 使用场景
- 通过 API 管理 n8n 工作流生命周期
- 自动化创建和测试 n8n 工作流
- 监控执行状态和优化性能

## 依赖和前提条件
- Python 3、requests 库
- N8N_API_KEY、N8N_BASE_URL 环境变量

## 包含文件
- `SKILL.md` — 技能定义和使用指南
- `scripts/n8n_api.py` — n8n API 客户端
- `scripts/n8n_tester.py` — 工作流测试工具
- `scripts/n8n_optimizer.py` — 性能优化器
- `references/api.md` — API 参考文档

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Python HTTP 请求，无 shell 执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向 n8n 实例发送工作流数据和触发执行 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 N8N_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 requests Python 包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可激活/创建工作流，执行自动化任务 |
| SEC-08 持久化机制 | 🟢 Safe | 工作流持久化在 n8n 实例中 |
| SEC-09 信息采集 | 🟢 Safe | 按需访问工作流信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 可对 n8n 实例进行管理操作（创建/激活工作流），需注意 API 权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
