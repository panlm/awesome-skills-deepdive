# mac-clean-skill

> macOS 系统清理工具，清理缓存、垃圾箱和旧下载文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mac-clean-skill |
| **作者** | aadipapp |
| **ClawHub** | https://clawskills.sh/skills/aadipapp-mac-clean-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aadipapp/mac-clean-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 清空垃圾箱（~/.Trash）
- 清理超过 7 天的缓存文件
- 删除超过 30 天的下载文件
- 默认 DRY RUN 模式防止误删
- 需要 --force 标志才实际删除

## 使用场景
- 定期清理 Mac 磁盘空间
- 系统维护自动化

## 依赖和前提条件
- Python 3
- macOS

## 包含文件
SKILL.md, scripts/cleanup.py（清理脚本）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 os.remove 和 shutil.rmtree 删除文件 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外传 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 删除 ~/.Trash、~/Library/Caches、~/Downloads 中的文件，但默认 DRY RUN |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅操作用户目录 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅统计文件大小和数量 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，有 DRY RUN 保护 |

**综合评级: 🟡 Medium**
**风险摘要:** 删除用户文件的工具，但默认 DRY RUN 模式提供了安全保护

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
