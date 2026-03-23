# jellyseerr

> 通过 Jellyseerr 管理影视请求和 Plex/Jellyfin 媒体库

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | jellyseerr |
| **作者** | ericrosenberg |
| **ClawHub** | https://clawskills.sh/skills/ericrosenberg-jellyseerr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ericrosenberg/jellyseerr |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Jellyseerr server URL
- API key (from Jellyseerr Settings > General)

## 依赖和前提条件
- Jellyseerr server URL
- API key (from Jellyseerr Settings > General)

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
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23