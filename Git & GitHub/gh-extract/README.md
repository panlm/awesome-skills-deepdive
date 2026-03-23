# GitHub Extract

> 从 GitHub URL 提取文件内容，支持仓库、目录和文件链接。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GitHub Extract |
| **作者** | guoqiao |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/guoqiao-gh-extract |

## 功能概述
- 接受 GitHub URL（仓库/目录/文件链接），自动转换为 raw URL 提取内容
- 支持将文件内容输出到标准输出或保存到临时文件
- 自动检测仓库中的 README.md、SKILL.md 或 README.txt
- 支持 `/gh-extract <url>` 命令触发
- 支持 repo/tree/blob 三种 GitHub URL 格式

## 使用场景
- 快速提取并阅读公开 GitHub 仓库中的文件内容，无需克隆整个仓库
- 下载 GitHub 上的单个文件到本地进行分析或使用
- 批量提取多个 GitHub 项目的 README 用于内容汇总

## 依赖和前提条件
- `uv`（Python 包管理工具）
- `wget`（文件下载工具）
- 仅支持公开仓库

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
