# netlify

> 使用 Netlify CLI 创建/关联站点并配置 GitHub CI/CD 部署

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | netlify |
| **作者** | ajmwagar |
| **ClawHub** | https://clawskills.sh/skills/ajmwagar-netlify |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ajmwagar/netlify |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建和关联 Netlify 站点
- 配置 GitHub CI/CD 持续部署
- Monorepo 多站点部署模式
- Hugo 站点 netlify.toml 自动生成
- 环境变量和 Secrets 管理
- Deploy Preview 配置

## 使用场景
- 新项目快速部署到 Netlify
- Monorepo 多站点配置
- Hugo 静态站点 CI/CD 搭建

## 依赖和前提条件
- Netlify CLI（`netlify` 命令）
- 已登录 Netlify 或 `NETLIFY_AUTH_TOKEN`

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，部署指南 |
| scripts/hugo_netlify_toml.sh | 生成 Hugo netlify.toml 配置 |
| scripts/netlify_monorepo_site.sh | Monorepo 站点创建辅助脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 执行 netlify CLI 命令，参数处理安全 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Netlify 官方服务通信 |
| SEC-03 凭证获取 | 🟢 Safe | 使用 Netlify 已有登录或 token |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Netlify 官方 CLI |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅创建 netlify.toml 配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 Netlify 账户权限内 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 标准 Netlify 部署工具，脚本安全可靠

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
