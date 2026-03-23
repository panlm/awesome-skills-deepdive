# paperless

> 通过 ppls CLI 与 Paperless-NGX 文档管理系统交互

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | paperless |
| **作者** | nickchristensen |
| **ClawHub** | https://clawskills.sh/skills/nickchristensen-paperless |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickchristensen/paperless |
| **安全评级** | 🟡 Medium |

## 功能概述
- 搜索文档（按名称、日期、标签、通讯录、文档类型等）
- 查看和下载文档（包括原始和 OCR 版本）
- 上传文档（支持元数据）
- 管理标签、通讯录、文档类型
- 更新文档元数据
- 丰富的过滤组合

## 使用场景
- 在 Paperless-NGX 中搜索和检索文档
- 批量上传和分类文档
- 管理文档元数据和标签

## 依赖和前提条件
- `ppls` CLI（npm 全局安装）
- PPLS_HOSTNAME、PPLS_TOKEN 环境变量

## 包含文件
- `SKILL.md` — 技能定义和完整命令参考
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 ppls CLI 操作 |
| SEC-02 数据外泄 | 🟡 Medium | 可上传本地文件到 Paperless-NGX 实例 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 PPLS_TOKEN API 令牌 |
| SEC-04 供应链风险 | 🟡 Medium | npm 包依赖（@nickchristensen/ppls） |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅下载文件到指定路径 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可创建/更新/删除文档和元数据 |
| SEC-08 持久化机制 | 🟢 Safe | 数据持久化在 Paperless-NGX 实例 |
| SEC-09 信息采集 | 🟡 Medium | 可搜索和获取所有文档内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 CLI 操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 对文档管理系统进行 CRUD 操作，可访问和上传文档

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
