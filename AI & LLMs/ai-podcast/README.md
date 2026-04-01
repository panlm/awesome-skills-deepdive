# Podcast Generation from PDF, Text, and Links

> 将 PDF、文本和链接转换为自然双人对话式播客

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Podcast Generation from PDF, Text, and Links |
| **作者** | mogens9 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/mogens9-ai-podcast |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mogens9/ai-podcast |
| **安全评级** | 🟡 Medium |

## 功能概述
- 支持从 PDF 文档、纯文本和网页链接生成播客
- 使用 MagicPodcast 引擎创建自然的双主持人对话音频
- 支持自定义播客语言
- 提供播客仪表盘追踪生成进度
- 生成完成后返回可分享的播客链接
- 通过简单的 API 调用即可完成全流程

## 使用场景
- 将研究论文或技术文档快速转化为易于收听的播客节目
- 为文字内容创作者提供音频内容的自动化生产方案
- 把学习笔记转换为播客形式方便通勤时收听

## 依赖和前提条件
- MagicPodcast API Key（`MAGICPODCAST_API_KEY` 环境变量）
- MagicPodcast API URL（`MAGICPODCAST_API_URL` 环境变量）
- curl 和 jq 命令行工具

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
