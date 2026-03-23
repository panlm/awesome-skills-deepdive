# MUKI Asset Fingerprinting

> MUKI asset fingerprinting tool for red team reconnaissance. Use when performing authorized penetration testing, asset discovery, service fingerprinting, vulnerability scanning, and attack surface mapping. Supports active/passive fingerprinting with 30,000+ signatures, sensitive path detection, and sensitive information extraction. Requires explicit authorization for target systems.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MUKI Asset Fingerprinting |
| **作者** | admin4giter |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/admin4giter-muki-fingerprint |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/admin4giter/muki-fingerprint |
| **安全评级** | 🟡 Medium |

## 功能概述
- Linux amd64 environment
- Network access to target
- Explicit authorization for targets
- Linux amd64 system
- Network access to target systems
- Explicit written authorization for all target systems

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Docker
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23