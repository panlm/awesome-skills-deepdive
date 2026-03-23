# Content Repurposer

> 将一篇内容转化为 7+ 种平台格式的内容再利用工具，支持博客转推文、文章转 LinkedIn 帖子、播客笔记转社交媒体等，所有数据本地处理，不发送任何外部请求。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Content Repurposer |
| **作者** | mkpareek0315 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/mkpareek0315-content-repurpose-pro |

## 功能概述
- 15 项内容转化功能：将一篇内容自动转化为 7+ 种不同平台格式
- 支持 Twitter 推文/线程、LinkedIn 帖子、Instagram 配文、邮件 Newsletter、YouTube 描述等
- 平台感知：针对不同平台的特性和规范生成适配内容
- 完全本地化：不进行任何外部 API 调用、网络请求或数据上传
- 生成文本供用户复制粘贴，不直接发布到任何平台
- 内容历史记录和收藏功能

## 使用场景
- 将一篇博客文章快速转化为 Twitter 线程、LinkedIn 帖子和 Instagram 配文
- 将播客笔记或演讲稿转化为多平台社交媒体内容
- 从长文中提取 TL;DR 摘要和邮件 Newsletter 内容

## 依赖和前提条件
- 文件读写权限（数据存储在 `~/.openclaw/content-repurposer/`）
- 无外部依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
