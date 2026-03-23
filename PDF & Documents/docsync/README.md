# DocSync

> 文档同步工具，保持多处文档内容一致

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | DocSync |
| **作者** | suhteevah |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/suhteevah-docsync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/suhteevah/docsync |
| **安全评级** | 🟡 Medium |

## 功能概述
- 跨平台文档内容同步
- 变更追踪和版本管理
- 自动检测内容差异
- 支持多种文档格式

## 使用场景
- 在多个平台间保持文档内容同步更新
- 自动追踪文档变更并同步到所有副本

## 依赖和前提条件
- API 密钥
- Python 运行环境
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `config`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23