# canva

> 通过 Canva Connect API 创建、导出和管理 Canva 设计作品

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | canva |
| **作者** | abgohel |
| **ClawHub** | https://clawskills.sh/skills/abgohel-canva |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/abgohel/canva |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出所有 Canva 设计作品
- 从品牌模板自动填充创建设计
- 导出设计为 PNG/JPG/PDF 格式
- 上传图片资源到 Canva 素材库
- 管理品牌模板
- 完整 OAuth 认证流程

## 使用场景
- 批量创建和导出 Canva 设计
- 自动化品牌素材管理
- 将 Canva 集成到自动化工作流

## 依赖和前提条件
- Canva 开发者账户及 Integration
- `CANVA_CLIENT_ID` 和 `CANVA_CLIENT_SECRET` 环境变量
- jq 命令行工具

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| ORIGINAL_README.md | 原始说明文档 |
| scripts/canva-auth.sh | OAuth 认证脚本 |
| scripts/canva.sh | CLI 操作辅助脚本 |
| package.json | npm 依赖配置 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | shell 脚本执行 curl 和 jq，参数处理安全 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Canva 官方 API 通信 |
| SEC-03 凭证获取 | 🟡 Medium | 读取环境变量中的 Client ID/Secret，token 存储在 ~/.canva/tokens.json |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Canva 官方 API |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建 ~/.canva/ 目录并写入 token 文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 操作在 OAuth 授权范围内 |
| SEC-08 持久化机制 | 🟡 Medium | OAuth token 持久化到本地文件 |
| SEC-09 信息采集 | 🟢 Safe | 无额外信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** OAuth token 持久化到本地文件系统，需确保 Client Secret 安全

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
