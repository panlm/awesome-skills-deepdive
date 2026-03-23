# facebook-page-manager

> 通过 Meta Graph API 管理 Facebook 主页：发帖、评论管理、X 平台摘要发布

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | facebook-page-manager |
| **作者** | longmaba |
| **ClawHub** | https://clawskills.sh/skills/longmaba-facebook-page-manager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/longmaba/facebook-page-manager |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出管理的 Facebook 主页
- 发布文字、图片、链接帖子
- 查看帖子列表和评论
- 回复/隐藏/删除评论
- 从 X (Twitter) 收集内容摘要并发布到 Facebook
- 完整 OAuth 认证流程（长期 token）

## 使用场景
- 自动化 Facebook 主页内容管理
- 跨平台内容同步（X → Facebook）
- 社交媒体评论管理

## 依赖和前提条件
- Meta App（App ID + App Secret）
- Node.js + npm
- X 平台 Cookie（AUTH_TOKEN, CT0）用于 X 集成

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/auth.js | OAuth 认证脚本 |
| scripts/cli.js | CLI 命令工具 |
| scripts/fb_post.js | Facebook 发帖脚本 |
| scripts/x_digest_collect.js | X 平台内容收集 |
| scripts/x_digest_to_fb.js | X 内容转发到 Facebook |
| scripts/package.json | npm 依赖 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本，无危险命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Facebook Graph API 和 X 平台发送请求 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 META_APP_ID/SECRET、X 平台 AUTH_TOKEN/CT0 Cookie |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 commander、dotenv 等 npm 包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 将 token 写入本地 tokens.json（chmod 0600） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 Facebook Pages 授权范围内 |
| SEC-08 持久化机制 | 🟡 Medium | OAuth token 持久化到 tokens.json |
| SEC-09 信息采集 | 🟡 Medium | 从 X 平台搜索和收集内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及多平台 API 凭证和社交媒体操作，token 本地持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
