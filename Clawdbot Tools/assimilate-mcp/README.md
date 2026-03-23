# assimilate-mcp

> 通过 MCP 协议控制 Assimilate Live FX/SCRATCH 专业调色和合成软件，88 个工具覆盖 14 个类别

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | assimilate-mcp |
| **作者** | ergopooka |
| **ClawHub** | https://clawskills.sh/skills/ergopooka-assimilate-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ergopooka/assimilate-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 系统管理（用户/项目/组）
- 素材管理（构建/插槽/版本/镜头）
- 专业调色（色彩分级/取景框）
- 播放器控制（时间线/播放模式）
- 渲染管理（启动/停止/状态）
- 文件操作（目录列表/媒体查找）

## 使用场景
- AI 辅助专业视频调色工作流
- 自动化 Assimilate Live FX 项目管理
- 远程控制渲染和输出设置

## 依赖和前提条件
Node.js v18+, npx, Assimilate Live FX/SCRATCH（需启用 REST API）

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
| SEC-01 命令执行 | 🟡 Medium | 通过 npx 启动 MCP 服务器，执行 HTTP 请求控制外部软件 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Assimilate REST API 发送和接收数据 |
| SEC-03 凭证获取 | 🟡 Medium | 支持 --key 授权密钥参数 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 npm 包 assimilate-mcp |
| SEC-05 文件系统篡改 | 🟢 Safe | 不直接写入本地文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可控制外部专业软件（创建项目/渲染等） |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可读取项目结构和文件目录 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** MCP 桥接外部专业软件，操作权限取决于 Assimilate REST API 配置

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
