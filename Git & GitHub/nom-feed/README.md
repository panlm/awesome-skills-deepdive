# Search recent repo activities

> 从 Nom 平台获取 GitHub 最近的仓库活动动态

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Search recent repo activities |
| **作者** | lws803 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lws803-nom-feed |

## 功能概述
- 通过 Nom (beta.nomit.dev) API 获取 GitHub 活动 Feed
- 支持按仓库（org/repo）或全局范围查询活动
- 支持按事件类型过滤：Pull Request、Issue、Release、Push
- 支持全文搜索、组织过滤、日期范围限定
- 支持 RSS 格式输出
- 以清晰的格式展示事件类型、标题链接、AI 摘要、作者和时间

## 使用场景
- 快速了解特定 GitHub 仓库的最近动态（PR、Issue、Release 等）
- 跨组织或全局范围搜索 GitHub 活动，追踪开源项目进展
- 通过 RSS 订阅持续监控感兴趣的仓库更新

## 依赖和前提条件
- `curl` 命令行工具
- 需要网络访问 beta.nomit.dev API

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23