# Ai Influencer Generation

> 使用 each::sense API 生成风格一致的 AI 虚拟网红形象和社交媒体内容

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Influencer Generation |
| **作者** | eftalyurtseven |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/eftalyurtseven-ai-influencer-generation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/ai-influencer-generation |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建外观跨内容保持一致的虚拟网红人设
- 生成 Instagram 帖子、Stories、Reels 缩略图、TikTok 内容等
- 支持品牌合作和产品推广的虚拟代言人
- 提供时尚、生活方式和商业内容的 AI 模特生成
- 通过 each::sense API 实现高质量图像输出
- 支持自定义外观特征、光线风格和拍摄美学

## 使用场景
- 为品牌快速创建具有统一形象的虚拟代言人
- 批量生成社交媒体多平台内容素材
- 无需真人模特即可完成产品拍摄和视觉内容制作

## 依赖和前提条件
- each::sense API Key（`EACHLABS_API_KEY` 环境变量）
- API 端点：https://sense.eachlabs.run/chat
- HTTP 客户端（curl 或类似工具）

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
