# clawddocs

> Clawdbot 文档专家，支持决策树导航、搜索、文档获取和版本追踪

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawddocs |
| **作者** | nicholasspisak |
| **ClawHub** | https://clawskills.sh/skills/nicholasspisak-clawddocs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicholasspisak/clawddocs |
| **安全评级** | 🟢 Low |

## 功能概述
- 决策树式文档导航
- 关键词搜索和全文索引
- 文档获取和缓存
- 版本变更追踪
- 常用配置代码片段
- 12 个文档类目覆盖

## 使用场景
- 查找 Clawdbot 配置方法
- 排查 Clawdbot 故障
- 了解 Clawdbot 最新功能

## 依赖和前提条件
bash (脚本为 stub 实现)

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts/build-index.sh`
- `scripts/cache.sh`
- `scripts/fetch-doc.sh`
- `scripts/recent.sh`
- `scripts/search.sh`
- `scripts/sitemap.sh`
- `scripts/track-changes.sh`
- `snippets/common-configs.md`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Shell 脚本为占位符实现，仅 echo 输出 |
| SEC-02 数据外泄 | 🟡 Medium | 设计上会从 docs.clawd.bot 获取文档 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无实际外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅读取操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取公开文档 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本为简单 stub |

**综合评级: 🟢 Low**
**风险摘要:** 文档查询工具，当前脚本为占位符，实际功能安全

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
