# Skill

> "Security audit tool for ClawHub skills. Scans a skill directory with 65 detection patterns, anti-obfuscation analysis, and dual rating system (Security + Compliance). v0.6.1 fixes batch scan performance by skipping venv/node_modules directories. Use when: installing a new skill, reviewing skill safety, or auditing permissions."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | yx2601816404-sys |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/yx2601816404-sys-skill-shield |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yx2601816404-sys/skill-shield |
| **安全评级** | 🔴 High |

## 功能概述
- File deletion: rm -rf, shred, unlink, rmtree, rimraf, del /f (7 patterns)
- Network exfiltration: curl POST, wget --post, requests.post, fetch POST, netcat reverse shell, DNS exfil, pipe to curl, 
- Environment variable access: process.env, os.environ, .env files, printenv (5 patterns)
- Secret/key access: .ssh/, .gnupg/, private keys, wallets, tokens, passwords, keychain, cloud credentials (8 patterns)
- Privilege escalation: sudo, su, chmod 777, chown, setuid/setgid, doas (6 patterns)
- Code execution: eval, exec(), Function(), child_process, subprocess, os.system, os.popen, compile (8 patterns)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reports`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，3 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23