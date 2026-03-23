# freshrss-reader

> 从自托管的 FreshRSS 实例查询新闻和文章

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | freshrss-reader |
| **作者** | nickian |
| **ClawHub** | https://clawskills.sh/skills/nickian-freshrss-reader |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickian/freshrss-reader |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过 Google Reader 兼容 API 查询 FreshRSS 标题和文章
- 支持按分类、时间范围、数量过滤
- 获取未读/全部文章
- 列出分类和订阅源
- 格式化输出标题、链接、分类

## 使用场景
- 获取自托管 RSS 阅读器的最新新闻
- 按分类浏览技术/新闻文章

## 依赖和前提条件
- curl、jq
- FreshRSS 实例 URL、用户名、API 密码

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/freshrss.sh` — RSS 查询脚本

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl 标准 HTTP 请求 |
| SEC-02 数据外泄 | 🟢 Safe | 仅从自有 FreshRSS 读取数据 |
| SEC-03 凭证获取 | 🟡 Medium | 使用环境变量中的 API 密码登录 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 只读 API 操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取用户自有 RSS 源 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 只读 RSS 查询工具，访问用户自托管实例，风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
