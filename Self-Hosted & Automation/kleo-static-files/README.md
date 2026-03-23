# kleo-static-files

> 在子域名上托管静态文件，支持可选认证

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | kleo-static-files |
| **作者** | awaaate |
| **ClawHub** | https://clawskills.sh/skills/awaaate-kleo-static-files |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/awaaate/kleo-static-files |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在子域名（*.498as.com）上托管静态内容
- 自动 SSL 证书（通过 Caddy）
- 基本认证（用户名/密码）保护
- 文件上传和目录上传
- 站点创建/删除/列表管理
- 配额管理

## 使用场景
- 快速部署静态网站到子域名
- 创建受密码保护的文件共享
- 部署前端构建产物（Vite/React/Vue）

## 依赖和前提条件
- `sf` CLI 工具
- SF_API_URL 和 SF_API_KEY 环境变量

## 包含文件
- `SKILL.md` — 技能定义和命令参考
- `references/install.md` — 安装指南
- `scripts/sf-helper.sh` — 高级操作辅助脚本

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 sf CLI 操作 |
| SEC-02 数据外泄 | 🟡 Medium | 上传文件到外部托管服务（498as.com） |
| SEC-03 凭证获取 | 🟡 Medium | 使用 SF_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部 API 服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 操作在 API 权限范围内 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 将文件上传到第三方托管服务，需注意上传内容的敏感性

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
