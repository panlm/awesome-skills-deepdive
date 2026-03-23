# brew-audit

> 审计 Homebrew 安装状态 - 过期包、清理机会和健康检查

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | brew-audit |
| **作者** | rogue-agent1 |
| **ClawHub** | https://clawskills.sh/skills/rogue-agent1-brew-audit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rogue-agent1/brew-audit |
| **安全评级** | 🟢 Low |

## 功能概述
- 列出所有过期的 formulae 和 cask
- 计算可清理的旧版本和磁盘空间
- 运行 brew doctor 检测健康问题
- 支持 JSON 输出格式
- 汇总统计信息

## 使用场景
- 定期系统维护（周/月）
- 磁盘空间不足时清理
- 构建失败后的环境诊断

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
SKILL.md（技能定义）, scripts/brew-audit.sh（审计脚本）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 brew outdated/cleanup/doctor 等命令 |
| SEC-02 数据外泄 | 🟢 Safe | 所有数据本地处理 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用系统已安装的 brew |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读取信息，不修改系统（dry-run） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅执行用户级 brew 命令 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集包管理器状态信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简单清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 只读审计工具，不修改系统状态

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
