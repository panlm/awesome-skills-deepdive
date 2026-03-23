# Deai Image

> Detect and remove AI fingerprints from AI-generated images. Strip metadata, add film grain, recompress, and bypass AI image detectors. Works with Midjourney, DALL-E, Stable Diffusion, Flux output.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deai Image |
| **作者** | swaylq |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/swaylq-deai-image |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swaylq/deai-image |
| **安全评级** | 🔴 High |

## 功能概述
- Metadata: EXIF tags, C2PA watermarks
- Pixel patterns: Over-smoothness, unnatural noise
- Frequency domain: DCT coefficient signatures
- Deep learning: Model-specific fingerprints

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23