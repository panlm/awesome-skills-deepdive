# clawstrike

> CrowdStrike 安全测试技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawstrike |
| **作者** | misirov |
| **ClawHub** | https://clawskills.sh/skills/misirov-clawdstrike-test |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/misirov/clawdstrike-test |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- CrowdStrike 安全测试技能

## 依赖和前提条件
- Every row must cite a `verified-bundle.json` key and include a short, redacted excerpt.
- If any required evidence key is missing, mark `VULNERABLE (UNVERIFIED)` and request a re-run.
- Firewall status must be confirmed from `fw.*` output. If only `fw.none` exists, mark `VULNERABLE (UNVERIFIED)` and request verification.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23