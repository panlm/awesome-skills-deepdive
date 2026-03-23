# grepwrapper

> 通过 grep.app 在公开的 GitHub 仓库中搜索精确的代码匹配，使用 grepwrapper CLI 工具。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | grepwrapper |
| **作者** | riprsa |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/riprsa-grepwrapper |

## 功能概述
- 通过 `grepwrapper search --q "查询内容"` 在公开 GitHub 仓库中搜索精确代码匹配
- 支持大小写敏感搜索（`--case`）
- 支持全词匹配模式（`--words`）
- 支持正则表达式搜索模式（`--regexp`）
- 支持分页浏览搜索结果（`--page`）
- 返回匹配摘要：耗时、总数、每条匹配的仓库和文件路径

## 使用场景
- 在全球公开 GitHub 仓库中搜索特定函数签名或 API 调用的使用示例
- 查找某个代码片段在哪些开源项目中被使用
- 通过正则表达式在 GitHub 代码库中进行模式匹配搜索

## 依赖和前提条件
- `grepwrapper` CLI 工具
- 安装方式：`npm i -g git+https://github.com/riprsa/grepwrapper.git`
- Node.js / npm 环境

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
