# clawdbot-security-check

> Clawdbot 自身安全审计框架，覆盖 12 个安全域的知识驱动检测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-security-check |
| **作者** | thesethrose |
| **ClawHub** | https://clawskills.sh/skills/thesethrose-clawdbot-security-check |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thesethrose/clawdbot-security-check |
| **安全评级** | 🟡 Medium |

## 功能概述
- 12 个安全域系统检查
- 动态检测而非硬编码脚本
- 网关暴露/DM 策略/凭证安全等关键检查
- 支持 --fix 自动修复
- 只读审计模式
- 可扩展的安全框架

## 使用场景
- 全面审计 Clawdbot 安全配置
- 检测和修复安全漏洞
- 定期安全健康检查

## 依赖和前提条件
Clawdbot, bash, 文件读取权限

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `skill.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 shell 命令读取配置文件（cat/grep/env） |
| SEC-02 数据外泄 | 🟢 Safe | 无外部网络通信 |
| SEC-03 凭证获取 | 🟡 Medium | 读取凭证文件和环境变量进行审计 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | --fix 模式会修改配置文件和权限 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | --fix 可修改 groupPolicy 和文件权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 全面扫描凭证存储和配置 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，框架透明 |

**综合评级: 🟡 Medium**
**风险摘要:** 安全审计工具本身需要读取敏感配置，--fix 模式会修改系统设置

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
