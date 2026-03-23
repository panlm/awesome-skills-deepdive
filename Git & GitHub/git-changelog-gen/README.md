# Git Changelog Generator

> 从 Git 提交记录生成变更日志，支持 Markdown、纯文本和 JSON 输出格式，可按日期范围和 Tag 过滤。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git Changelog Generator |
| **作者** | rogue-agent1 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/rogue-agent1-git-changelog-gen |

## 功能概述
- 通过 Bash 脚本从 Git 提交历史生成可读的变更日志
- 支持三种输出格式：Markdown（默认）、纯文本和 JSON
- 支持按日期范围过滤提交（`--since` 和 `--until`）
- 自动检测最新 Git Tag 作为起始点
- JSON 格式包含提交哈希、主题、作者、日期和约定式提交类型
- 支持按约定式提交类型分组（需要 Bash 4+）
- 自动排除合并提交以获得更清洁的输出

## 使用场景
- 快速生成指定时间段内的项目变更记录用于团队同步
- 以 JSON 格式导出提交数据用于自定义报告或集成到其他工具
- 为开源项目在发版时自动生成多格式变更日志

## 依赖和前提条件
- `git`：需要在 Git 仓库中运行
- `bash`：运行脚本（分组功能需要 Bash 4+，macOS 默认 3.2 需通过 `brew install bash` 升级）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
