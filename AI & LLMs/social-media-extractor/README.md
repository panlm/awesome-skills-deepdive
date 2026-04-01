# Social Media Data Extractor

> 从多个社交媒体平台批量提取和分析数据内容

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Social Media Data Extractor |
| **作者** | g4dr |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/g4dr-social-media-extractor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g4dr/social-media-extractor |
| **安全评级** | 🔴 High |

## 功能概述
- 从社交媒体平台提取数据和内容
- 支持多个主流社交平台
- 提取帖子、评论、用户信息等数据
- 支持批量数据采集和导出
- 提供数据清洗和格式化功能
- 适用于社交媒体分析和监控

## 使用场景
- 批量采集社交媒体数据进行市场调研
- 监控品牌在社交平台上的提及和口碑
- 提取社交媒体内容用于数据分析项目

## 依赖和前提条件
- Node.js 运行环境
- Bash/Shell 环境
- API Key
- API Token
- 环境变量 `APIFY_TOKEN`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
