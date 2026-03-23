# C.R.A.B Deploy Agent

> 全栈应用多步骤部署代理，按 构建 → 测试 → GitHub → Cloudflare Pages 流程执行，每步需人工审批

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | C.R.A.B Deploy Agent |
| **作者** | sherajdev |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/sherajdev-deploy-agent |

## 功能概述
- 5 步部署流程：初始化 → 构建 → 本地测试 → 推送 GitHub → 部署到 Cloudflare Pages
- 每个关键步骤都需要人工审批确认后才继续
- 自动创建 GitHub 仓库并推送代码
- 自动部署到 Cloudflare Pages 并配置自定义域名
- 部署状态持久化存储，支持跨会话恢复
- 支持随时取消和清理部署
- 附带 Next.js + Cloudflare D1 部署指南和常见问题修复

## 使用场景
- 将全栈应用从本地开发一键式部署到 Cloudflare Pages，全程有人工把关
- 标准化团队的部署流程，避免跳过测试或审查步骤直接上线

## 依赖和前提条件
- `gh` CLI（GitHub 仓库管理）
- `wrangler`（Cloudflare Pages 部署）
- `git`（版本控制）
- `jq`（JSON 状态管理）
- Cloudflare API Token（配置在 `~/.wrangler.toml`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。供应链风险：需要安装外部包且含管道安装；信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive skill 自动生成
