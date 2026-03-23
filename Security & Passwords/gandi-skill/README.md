# gandi

> 通过 Gandi API 管理域名和 DNS 记录

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gandi |
| **作者** | chrisagiddings |
| **ClawHub** | https://clawskills.sh/skills/chrisagiddings-gandi-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chrisagiddings/gandi-skill |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Status: ✅ Phase 2 Complete - DNS modification & snapshots functional
- This skill can perform DESTRUCTIVE operations on your Gandi account:
- DNS Modification: Add, update, or delete DNS records (can break websites/email)
- Email Management: Create, modify, or delete email forwards (can intercept emails)
- Domain Registration: Register domains (creates financial transactions)
- Bulk Operations: Replace all DNS records at once (cannot be undone except via snapshots)

## 依赖和前提条件
- Required:** Node.js >= 18.0.0
- Expected packages:**
- axios (HTTP client for Gandi API)
- Troubleshooting:**
- If permission errors: Don't use `sudo` - fix npm permissions or use nvm

## 包含文件
- `CHANGELOG.md`
- `README.md` — 中文说明文档
- `SCRIPTS.md`
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `config/` — 目录
- `config.schema.json` — 配置/数据文件
- `references/` — 目录
- `scripts/` — 目录
- `test-underscore.js` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23