# Scan Skill

> Deep security analysis of an individual skill before installation

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Scan Skill |
| **作者** | itsnishi |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/itsnishi-scan-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/itsnishi/scan-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- SKILL.md frontmatter analysis (dangerous field combinations, hidden skills, pre-approved tools)
- Hidden HTML comments with imperative instructions
- Shell command patterns (remote-code-pipe-to-shell, encoded payloads)
- Description persistence triggers (forced repeated execution keywords)
- Supporting files analysis (scripts/ directory contents, executable permissions)
- Dynamic context injection (preprocessor command execution)
- Encoding and obfuscation (base64, hex, zero-width characters)
- Instruction override attempts (context manipulation, role impersonation)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。Prompt 注入：存在可疑 Prompt 模式；混淆/反分析：使用编码/解码操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23