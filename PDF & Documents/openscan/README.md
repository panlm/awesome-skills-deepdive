# OpenScan

> 开源文档扫描和数字化工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenScan |
| **作者** | dev-null321 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/dev-null321-openscan |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dev-null321/openscan |
| **安全评级** | 🔴 High |

## 功能概述
- 文档扫描和图像增强
- 自动裁剪和透视校正
- 多页文档合并为 PDF
- 图像质量优化处理

## 使用场景
- 将纸质文档快速扫描并数字化归档
- 批量处理手机拍摄的文档照片

## 依赖和前提条件
- Python 运行环境
- Node.js
- npm
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `lib`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23