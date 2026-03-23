# Nas Movie Download

> Search and download movies via Jackett and qBittorrent. Use when user wants to download movies or videos from torrent sources, search for specific movie titles, or manage movie downloads. Now includes automatic subtitle download support with SMB integration.

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
- `JACKETT_URL`: Jackett service URL (default: http://192.168.1.246:9117)
- `JACKETT_API_KEY`: Jackett API key (default: o5gp976vq8cm084cqkcv30av9v3e5jpy)
- `QB_URL`: qBittorrent Web UI URL (default: http://192.168.1.246:8888)
- `QB_USERNAME`: qBittorrent username (default: admin)
- `QB_PASSWORD`: qBittorrent password (default: adminadmin)
- `SMB_USERNAME`: SMB username (default: 13917908083)

## 使用场景
- 视频内容管理和下载
- 影视信息查询
- 视频平台自动化操作

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config`
- `scripts`

## 详细安全审计
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