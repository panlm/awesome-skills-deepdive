# GitHub Action Generator

> 用自然语言描述需求，自动生成 GitHub Actions 工作流文件，告别从 StackOverflow 复制粘贴。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GitHub Action Generator |
| **作者** | branexp |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/branexp-gh-action-gen |

## 功能概述
- 根据自然语言描述自动生成 GitHub Actions 工作流 YAML 文件
- 支持直接写入 `.github/workflows/` 目录（`--install` 选项）
- 支持输出到指定文件（`-o` 选项）
- 通过 `npx` 直接运行，无需全局安装
- 支持复杂工作流描述（如测试+部署、Docker 构建+推送等）

## 使用场景
- 快速为新项目配置 CI/CD 流水线，无需手写复杂的 YAML 配置
- 根据项目需求用一句话生成 eslint 检查、Docker 构建、自动部署等工作流
- 批量为多个仓库创建标准化的 GitHub Actions 配置

## 依赖和前提条件
- Node.js / npm 环境
- 安装：`npm install -g ai-github-action`
- 环境变量 `OPENAI_API_KEY`：需要设置 OpenAI API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive skill 自动生成
