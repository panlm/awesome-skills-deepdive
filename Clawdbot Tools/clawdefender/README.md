# clawdefender

> AI 代理安全扫描器和输入消毒器，检测 prompt 注入、命令注入和数据外泄

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdefender |
| **作者** | nukewire |
| **ClawHub** | https://clawskills.sh/skills/nukewire-clawdefender |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nukewire/clawdefender |
| **安全评级** | 🟢 Low |

## 功能概述
- 全面 Skill 审计扫描
- 90+ prompt 注入模式检测
- 命令注入和 SSRF 检查
- URL 验证（防 SSRF）
- 通用输入消毒器
- 安全 Skill 安装检查

## 使用场景
- 安装新 Skill 前进行安全扫描
- 处理外部输入（邮件/API）前消毒
- 定期工作空间安全审计

## 依赖和前提条件
bash, grep, sed, jq

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts/clawdefender.sh`
- `scripts/sanitize.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 2 个 Bash 脚本执行 grep/sed 文本分析 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入安全扫描日志 |
| SEC-06 Prompt 注入 | 🟢 Safe | 设计目的就是检测 prompt 注入 |
| SEC-07 越权操作 | 🟢 Safe | 仅只读扫描 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 扫描所有 skill 文件内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，检测模式透明 |

**综合评级: 🟢 Low**
**风险摘要:** 安全防护工具本身设计安全，仅执行只读扫描和模式匹配

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
