# Security Checker

> 安全漏洞检查和扫描工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Security Checker |
| **作者** | johstracke |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/johstracke-security-checker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/johstracke/security-checker |
| **安全评级** | 🔴 High |

## 功能概述
- Auth tokens (including ClawHub tokens)
- Passwords
- Private keys
- JWT-like tokens
- Absolute file paths outside expected directories
- Parent directory traversal (`..`)
- Writing to system directories
- Is it legitimate? Document why in code comments or SKILL.md

## 使用场景
- 扫描系统和代码的安全漏洞
- 生成安全检查报告
- 提供漏洞修复建议和最佳实践

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
