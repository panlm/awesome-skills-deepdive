# provider-sync

> 同步上游 provider 模型列表到 OpenClaw 配置，支持预览和自动备份

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | provider-sync |
| **作者** | c-joey |
| **ClawHub** | https://clawskills.sh/skills/c-joey-provider-sync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/c-joey/provider-sync |
| **安全评级** | 🟡 Medium |

## 功能概述
- 拉取上游 /v1/models 模型列表
- 规范化模型字段
- dry-run 预览差异
- 自动备份后再写入
- 裁剪不可用的 agent 模型别名
- 交互式文本命令选择

## 使用场景
- 同步 OpenAI/Claude 等 provider 最新模型
- 预览模型配置变更
- 新增 provider 配置

## 依赖和前提条件
Python 3, OpenClaw 配置文件

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references/examples.md`
- `references/field-normalization.md`
- `references/gemini.md`
- `references/mapping.example.json`
- `references/mapping.openai-models.json`
- `references/provider-patterns.md`
- `references/safety-rules.md`
- `scripts/provider_sync.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 脚本读写 OpenClaw 配置文件 |
| SEC-02 数据外泄 | 🟡 Medium | 从 provider API 拉取模型列表 |
| SEC-03 凭证获取 | 🟡 Medium | 读取配置中的 API Key 用于认证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Python 标准库 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 openclaw.json 配置文件（有备份） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 修改 provider 模型配置和 agent 默认模型 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取 provider 配置中的认证信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，缓存会剔除敏感字段 |

**综合评级: 🟡 Medium**
**风险摘要:** 修改核心配置文件，虽有备份机制但需确保 provider 源可信

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
