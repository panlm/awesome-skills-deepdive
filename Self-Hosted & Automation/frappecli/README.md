# frappecli

> Frappe Framework / ERPNext 实例的命令行管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | frappecli |
| **作者** | pasogott |
| **ClawHub** | https://clawskills.sh/skills/pasogott-frappecli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pasogott/frappecli |
| **安全评级** | 🟡 Medium |

## 功能概述
- 管理 Frappe Framework 实例的文档 CRUD 操作
- 列出 Doctype、查看 Doctype 详情
- 文件上传/下载管理
- 运行和导出报表
- 调用自定义 RPC 方法
- 支持多站点配置

## 使用场景
- 通过 CLI 管理 ERPNext 业务数据
- 批量操作 Frappe 文档
- 自动化报表生成和导出

## 依赖和前提条件
- `frappecli` CLI（通过 Homebrew 或 pip 安装）
- Frappe API Key 和 Secret
- 配置文件 `~/.config/frappecli/config.yaml`

## 包含文件
- `SKILL.md` — 技能定义和完整命令参考
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 `frappecli` CLI 操作，无直接 shell 执行 |
| SEC-02 数据外泄 | 🟡 Medium | 可调用 RPC 方法和上传/下载文件到远程 Frappe 实例 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 config.yaml 中的 api_key 和 api_secret |
| SEC-04 供应链风险 | 🟢 Safe | 依赖外部 CLI 工具 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅下载文件到指定目录 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可进行文档创建/更新/删除操作，取决于 API 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 按需访问 Frappe 数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 SKILL.md 文档 |

**综合评级: 🟡 Medium**
**风险摘要:** 可对远程 ERP 系统进行 CRUD 操作和 RPC 调用，需注意 API 权限范围

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
