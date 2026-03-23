# Tweet Summarizer Lite

> 轻量级推文抓取与摘要工具，一条命令获取并总结 Twitter/X 上的单条推文

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tweet Summarizer Lite |
| **作者** | franciscobuiltdat |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/franciscobuiltdat-tweet-summarizer-lite |

## 功能概述
- 通过自然语言指令抓取单条 Twitter/X 推文内容
- 自动总结推文要点并生成摘要
- 将推文内容保存到本地文件夹归档
- 支持直接粘贴 x.com 链接即可处理
- 无需复杂配置，开箱即用

## 使用场景
- 快速了解某条推文的核心内容，无需打开 Twitter 客户端
- 收集和归档感兴趣的推文内容，便于后续回顾

## 依赖和前提条件
- Twitter/X 访问凭证
- MIT 许可证开源项目

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
