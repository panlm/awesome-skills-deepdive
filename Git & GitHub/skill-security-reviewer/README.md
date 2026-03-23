# Skill Security Reviewer 3.0

> **Enhanced Malicious Skill Detection Tool** - With anti-obfuscation and anti-evasion detection capabilities

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Security Reviewer 3.0 |
| **作者** | ninjagpt |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ninjagpt-skill-security-reviewer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ninjagpt/skill-security-reviewer |
| **安全评级** | 🔴 High |

## 功能概述
- Code obfuscation detection and de-obfuscation analysis
- Encoding/encryption evasion detection (Base64, Hex, ROT13, XOR, AES, etc.)
- String splitting/concatenation detection
- Dynamic code generation detection
- Multi-layer nested obfuscation detection
- Entropy analysis to identify encrypted content

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 7 项高风险，3 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23