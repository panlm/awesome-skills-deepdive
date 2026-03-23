# OpenTangl

> Not a code generator — an entire dev team. You write the vision, it ships the code. Autonomous builds, PRs, reviews, and merges across multiple repos. Point it at any JS/TS project and a product vision. It plans features, writes code, verifies builds, creates PRs, reviews diffs, and merges — autonomously. Manages multiple repos as one product. Use when you want to ship code without writing it. AI code generation, autonomous development, workflow automation, multi-repo orchestration, TypeScript, JavaScript, GitHub, OpenAI, Anthropic, Claude, GPT, LLM, devtools, CI/CD, pull requests, code review.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenTangl |
| **作者** | 8co |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/8co-opentangl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/8co/opentangl |
| **安全评级** | 🔴 High |

## 功能概述
- Node.js ≥ 18 — run `node --version` and show the output
- git — run `git --version` and show the output
- GitHub CLI — run `gh auth status` and show the output (needed for PR creation and merging)
- Type: `tsconfig.json` → TypeScript, `vite.config.ts` → Vite, `next.config.*` → Next.js, `serverless.yml` → Serverless
- Package manager: `package-lock.json` → npm, `yarn.lock` → yarn, `pnpm-lock.yaml` → pnpm
- Build/test commands: Read `package.json` scripts for `build`, `test`, `lint`, `typecheck`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23