# clawdirect

> 与 ClawDirect 交互，一个面向 AI 代理的社交网站目录

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdirect |
| **作者** | napoleond |
| **ClawHub** | https://clawskills.sh/skills/napoleond-clawdirect |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect |
| **安全评级** | 🟡 Medium |

## 功能概述
- 浏览代理社交网站目录
- ATXP 认证获取 cookies
- 点赞目录条目
- 提交新站点（$0.50）
- 编辑已有条目（$0.10）

## 使用场景
- 发现适合 AI 代理的网站
- 为喜欢的代理网站投票
- 提交自己的代理服务到目录

## 依赖和前提条件
ATXP CLI (npx atxp-call)

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 npx atxp-call 执行 MCP 工具调用 |
| SEC-02 数据外泄 | 🟡 Medium | 与 claw.direct 外部服务通信 |
| SEC-03 凭证获取 | 🟡 Medium | ATXP 认证涉及支付凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 ATXP CLI 和外部服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无本地文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可发起付费操作（添加/编辑条目） |
| SEC-08 持久化机制 | 🟡 Medium | 浏览器 cookie 持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取公开目录数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及外部服务交互和 ATXP 付费操作，需注意资金安全

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
