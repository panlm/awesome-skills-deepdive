# paperless-ngx

> 通过 REST API 与 Paperless-ngx 文档管理系统交互

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | paperless-ngx |
| **作者** | oskarstark |
| **ClawHub** | https://clawskills.sh/skills/oskarstark-paperless-ngx |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/oskarstark/paperless-ngx |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 REST API（curl）搜索和检索文档
- 上传/下载/删除文档
- 管理标签、通讯录、文档类型
- 更新文档元数据
- 支持原始和 OCR 版本下载

## 使用场景
- 通过 API 直接管理 Paperless-ngx 文档
- 自动化文档分类和元数据管理

## 依赖和前提条件
- curl
- PAPERLESS_URL、PAPERLESS_TOKEN 环境变量

## 包含文件
- `SKILL.md` — 技能定义和完整 API 参考
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl HTTP 请求 |
| SEC-02 数据外泄 | 🟡 Medium | 可上传文件到 Paperless-ngx |
| SEC-03 凭证获取 | 🟡 Medium | 使用 PAPERLESS_TOKEN 环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 curl 命令，无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅下载文件到指定路径 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可创建/更新/删除文档 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可搜索所有文档 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 SKILL.md 文档 |

**综合评级: 🟡 Medium**
**风险摘要:** 对文档管理系统进行 CRUD 操作，与 paperless skill 类似但使用原生 API

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
