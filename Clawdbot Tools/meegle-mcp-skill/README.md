# meegle-mcp-skill

> 通过 MCP 协议与 Meegle 项目管理系统交互

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | meegle-mcp-skill |
| **作者** | pkycy |
| **ClawHub** | https://clawskills.sh/skills/pkycy-meegle-mcp-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pkycy/meegle-mcp-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 项目管理（创建/列表/更新）
- 任务操作（创建/分配/追踪）
- 工作流自动化
- 团队协作和权限
- 时间追踪和分析
- MCP 代理服务器

## 使用场景
- 在 OpenClaw 中管理 Meegle 项目
- 通过自然语言创建和分配任务
- 自动化项目工作流

## 依赖和前提条件
Node.js 16+, MEEGLE_USER_KEY, MEEGLE_MCP_KEY

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `mcp-config.example.json`
- `package.json`
- `scripts/mcp-proxy.js`
- `scripts/setup.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | JS 代理服务器和 Bash 安装脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Larksuite MCP 服务器转发请求 |
| SEC-03 凭证获取 | 🟡 Medium | MEEGLE_USER_KEY 和 MCP_KEY 在 URL 中明文传递 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Meegle/Larksuite 服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无本地文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可创建/修改/删除项目和任务 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可访问所有项目和任务数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** API Key 在 URL 中明文传递，项目管理权限广泛

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
