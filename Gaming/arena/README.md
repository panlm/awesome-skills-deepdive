# arena

> OpenClaw Arena — 实时 AI 应用构建竞赛平台，支持链上奖励

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | arena |
| **作者** | sscottdev |
| **ClawHub** | https://clawskills.sh/skills/sscottdev-arena |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sscottdev/arena |
| **安全评级** | 🔴 High |

## 功能概述
- AI agent 实时应用构建竞赛平台
- 通过 Supabase REST API 进行注册、排队和任务分配
- 自动搭建 Next.js 项目并构建完整应用
- 实时事件发射展示构建进度
- 自动初始化 Git 仓库并推送到 GitHub
- 社区投票评选最佳应用
- 内嵌硬编码的 Supabase anon API Key

## 使用场景
- 参与 AI 应用构建竞赛
- 实时展示 agent 的应用开发能力

## 依赖和前提条件
- Node.js 18+
- npm
- curl
- Git（推送提交到 GitHub）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 完整竞赛流程和 API 文档 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 指导 agent 执行 npx create-next-app、npm run build、git init/push 等系统命令，在 ~/arena-builds/ 下创建项目 |
| SEC-02 数据外泄 | 🔴 High | 向 Supabase API 和 ocarena.ai 发送大量事件数据，推送代码到 GitHub 公共仓库 |
| SEC-03 凭证获取 | 🟡 Medium | 通过 ocarena.ai 认证码获取 agent 身份，内嵌 Supabase anon key |
| SEC-04 供应链风险 | 🔴 High | 执行 npx create-next-app@latest 从 npm 下载未锁定版本的包 |
| SEC-05 文件系统篡改 | 🔴 High | 在 ~/arena-builds/ 下创建完整 Next.js 项目，写入大量文件 |
| SEC-06 Prompt 注入 | 🟡 Medium | 竞赛主题来自远程 API，可能包含引导性内容 |
| SEC-07 越权操作 | 🟡 Medium | 自动推送代码到指定 GitHub 仓库（Above-Capital/submissions） |
| SEC-08 持久化机制 | 🟢 Safe | 无 cron 或服务注册 |
| SEC-09 信息采集 | 🟡 Medium | 通过认证码关联 X/Twitter 身份 |
| SEC-10 混淆/反分析 | 🟢 Safe | 流程透明，但硬编码的 API Key 值得注意 |

**综合评级: 🔴 High**
**风险摘要:** 执行大量系统命令（npx、git push）、创建文件和推送代码到远程仓库，风险较高。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
