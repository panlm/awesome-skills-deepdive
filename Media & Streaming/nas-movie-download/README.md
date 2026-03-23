# Nas Movie Download

> NAS 电影下载和管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Nas Movie Download |
| **作者** | roger0808 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/roger0808-nas-movie-download |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/roger0808/nas-movie-download |
| **安全评级** | 🔴 High |

## 功能概述
- The Pirate Bay
- Connects to NAS via SMB
- Uses subliminal for subtitle search
- Downloads Chinese and English subtitles
- Uploads subtitles to corresponding video folders
- Skips existing subtitle files
- Use English movie names for better search results
- Check Jackett indexer status if searches return no results

## 使用场景
- 自动搜索和下载电影到 NAS
- 管理 NAS 上的电影库分类
- 获取电影元数据和字幕

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
