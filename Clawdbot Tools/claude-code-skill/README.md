# claude-code-skill

> MCP 协议集成库，支持子代理编排、状态持久化和跨设备会话同步

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claude-code-skill |
| **作者** | enderfga |
| **ClawHub** | https://clawskills.sh/skills/enderfga-claude-code-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/enderfga/claude-code-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- MCP 服务器生命周期管理（创建/暂停/恢复/重启）
- 跨多服务器的工具调用
- IndexedDB/localStorage 状态持久化
- 水合跟踪防止数据丢失
- 基于时间戳的冲突解决
- 多源会话合并

## 使用场景
- 连接和编排多个 MCP 工具服务器
- 跨设备同步 AI 会话状态
- 持久化代理状态以实现上下文恢复

## 依赖和前提条件
Node.js 18+, npm (openclaw-claude-code-skill)

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `examples/basic-mcp.ts`
- `examples/chat-store.ts`
- `mcp_config.example.json`
- `package.json`
- `src/index.ts`
- `src/mcp/actions.ts`
- `src/mcp/client.ts`
- `src/mcp/index.ts`
- `src/mcp/logger.ts`
- `src/mcp/types.ts`
- `src/mcp/utils.ts`
- `src/store/index.ts`
- `src/store/indexeddb-storage.ts`
- `src/store/persist.ts`
- `src/store/sync.ts`
- `tsconfig.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 通过 StdioClientTransport 启动子进程执行 MCP 服务器命令 |
| SEC-02 数据外泄 | 🟡 Medium | MCP 工具可跨服务器通信 |
| SEC-03 凭证获取 | 🟡 Medium | 传递 process.env 给子进程，可能包含敏感信息 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 npm 包和 MCP SDK |
| SEC-05 文件系统篡改 | 🟡 Medium | IndexedDB/localStorage 持久化存储 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无明显 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | MCP 工具可执行广泛操作 |
| SEC-08 持久化机制 | 🟡 Medium | 状态持久化到本地存储 |
| SEC-09 信息采集 | 🟡 Medium | 可访问 MCP 服务器暴露的所有资源 |
| SEC-10 混淆/反分析 | 🟢 Safe | TypeScript 源码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** MCP 集成库涉及子进程启动和环境变量传递，需信任 MCP 服务器

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
