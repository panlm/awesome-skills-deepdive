# venice-characters

> 浏览 Venice AI 角色人格库 - 发现用于角色扮演和创意写作的 AI 角色

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | venice-characters |
| **作者** | sabrinaaquino |
| **ClawHub** | https://clawskills.sh/skills/sabrinaaquino-venice-characters |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sabrinaaquino/venice-characters |
| **安全评级** | 🟢 Low |

## 功能概述
- 浏览 Venice AI 角色人格库
- 按名称或描述搜索角色
- 按标签过滤角色
- 支持表格、JSON、列表三种输出格式
- 导出角色数据到文件
- 显示角色详情（名称、slug、模型、标签、统计）

## 使用场景
- 发现适合角色扮演或创意写作的 AI 角色
- 浏览和搜索 Venice AI 角色库

## 依赖和前提条件
- uv（Python 包管理器）
- VENICE_API_KEY 环境变量

## 包含文件
- `SKILL.md` — 技能定义和命令参考
- `scripts/characters.py` — 角色浏览 Python 脚本

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Python httpx HTTP 请求，无 shell 执行 |
| SEC-02 数据外泄 | 🟢 Safe | 从 Venice AI API 读取数据到本地 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 VENICE_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 httpx 库（通过 uv 内联安装） |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅可选导出到指定文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 只读 API 操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取公开角色数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | Python 脚本简洁可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的只读 API 客户端，浏览公开角色数据，风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
