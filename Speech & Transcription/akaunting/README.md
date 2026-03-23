# akaunting

> 通过 Akaunting REST API 进行开源会计管理，包括发票、收支和账目自动化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | akaunting |
| **作者** | liekzejaws |
| **ClawHub** | https://clawskills.sh/skills/liekzejaws-akaunting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liekzejaws/akaunting |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Critical: Akaunting has a bug where module event listeners don't auto-register. Run:
- "Payment method is invalid" error:
- 401 Unauthorized:
- 403 Forbidden on contacts/documents:

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `assets/` — 目录
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23