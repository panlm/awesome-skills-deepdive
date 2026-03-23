# Remote Skill Engine

> 从 ClawHub 和 GitHub 缓存远程 Skill 到本地，像已安装的 Skill 一样直接使用

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Remote Skill Engine |
| **作者** | oki3505f |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/oki3505f-remote-skill-engine |

## 功能概述
- 跨多个注册源（ClawHub、GitHub）搜索和发现 Skill
- 将远程 Skill 缓存到本地，工作方式与已安装的 Skill 完全一致
- 通过符号链接集成到 skills 目录，无缝触发使用
- 批量缓存管理：一次性缓存多个 Skill
- 智能同步和更新：检查更新、同步到最新版本
- 完整离线模式：缓存后无需网络即可使用
- 支持多种来源：ClawHub URL、GitHub URL、直接 URL

## 使用场景
- 快速试用 ClawHub 或 GitHub 上的社区 Skill，无需正式安装
- 在网络受限环境下预先缓存所需 Skill 实现离线使用
- 统一管理和更新多个远程 Skill 的本地缓存

## 依赖和前提条件
- ClawHub CLI（`clawhub`）或 GitHub CLI（`gh`）
- 需要网络访问 ClawHub/GitHub（首次缓存时）
- 缓存目录：`~/.openclaw/workspace/remote-skills-cache/`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23