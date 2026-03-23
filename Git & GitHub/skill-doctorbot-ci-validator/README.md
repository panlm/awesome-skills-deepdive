# Doctorbot Ci Validator

> Stop failing in production. Validate your GitHub Actions, GitLab CI & Keep workflows offline with surgical precision. Born from Keep bounty research, perfected for agents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Doctorbot Ci Validator |
| **作者** | bamontejano |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bamontejano-skill-doctorbot-ci-validator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bamontejano/skill-doctorbot-ci-validator |
| **安全评级** | 🟢 Low |

## 功能概述
- Keep Workflow Validation: Specialized mocker for Keep (AIOps) workflows. Validates steps, providers, and logic without a
- Universal YAML Check: Fast syntax validation for GitHub Actions, GitLab CI, CircleCI, etc.
- Surgical Precision: Identifies exactly where your workflow will fail.
- Pre-commit hooks.
- CI/CD pipelines (GitHub Actions).
- Agent-based code generation (validate before suggesting).

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- Docker

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23