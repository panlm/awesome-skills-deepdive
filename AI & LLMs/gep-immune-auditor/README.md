# GEP Immune Auditor

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GEP Immune Auditor |
| **作者** | andyxinweiminicloud |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-gep-immune-auditor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/gep-immune-auditor |
| **安全评级** | 🟡 Medium |

## 功能概述
- Cross-Capsule dependency chain analysis: does the chain include flagged assets?
- Publish frequency anomaly: mass publish from one node (like abnormal cell proliferation)
- Clone detection: near-duplicate Capsules washing IDs to bypass SHA-256 dedup
- Declared vs actual behavior: summary says "fix SQL injection" — does the code actually fix it?
- Permission creep: does fixing one bug require reading `.env`? calling `subprocess`?
- Covert channels: base64-encoded payloads? outbound requests to non-whitelisted domains?

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `evomap_publish.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 7 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23