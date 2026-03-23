# Skill Cleaner

> Automatically verify "suspicious" skills via VirusTotal and add them to the security allowlist via the Bridge.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Cleaner |
| **作者** | jacobthejacobs |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jacobthejacobs-skill-cleaner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jacobthejacobs/skill-cleaner |
| **安全评级** | 🟡 Medium |

## 功能概述
- Heuristic Scanning: Uses OpenClaw Core scanner to find suspicious code patterns.
- VirusTotal Integration: Cross-references hashes with VT for reputation.
- Trust Bridge: Automatically allowlists "false positives" via the Gateway.
- Quarantine: Moves malicious files (detects > 0 on VT) to a `.quarantine/` folder for safety.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 7 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23