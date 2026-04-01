# homebrew

> 通过 Homebrew 管理 macOS 软件包的安装和更新

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | homebrew |
| **作者** | thesethrose |
| **ClawHub** | https://clawskills.sh/skills/thesethrose-homebrew |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thesethrose/homebrew |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Installing packages or applications (`brew install X`)
- Searching for available packages (`brew search X`)
- Updating and upgrading existing packages
- Checking package information and dependencies
- Troubleshooting installation issues
- Managing installed packages

## 依赖和前提条件
- 
- Searching for available packages (`brew search X`)
- Updating and upgrading existing packages
- Examples:**
- Notes:**

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23