# Twitter Post

> Twitter/X 自动发帖工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Twitter Post |
| **作者** | sit-in |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/sit-in-twitter-post |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sit-in/twitter-post |
| **安全评级** | 🟡 Medium |

## 功能概述
- Call `POST /oauth/request_token` with `oauth_callback=oob`
- User opens `https://api.twitter.com/oauth/authorize?oauth_token=<token>`
- User provides the PIN code
- Call `POST /oauth/access_token` with the PIN as `oauth_verifier`
- Max 280 weighted characters per tweet
- CJK characters (Chinese/Japanese/Korean) count as 2 each
- URLs count as 23 each regardless of length
- Script auto-validates before posting; rejects if over limit

## 使用场景
- 自动发布推文到 Twitter/X
- 管理帖子内容和发布时间
- 跟踪推文的互动数据

## 依赖和前提条件
- Node.js / npm
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
