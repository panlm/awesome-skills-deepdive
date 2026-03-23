# cicd-pipeline

> 使用 GitHub Actions 创建、调试和管理 CI/CD 流水线

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cicd-pipeline |
| **作者** | gitgoodordietrying |
| **ClawHub** | https://clawskills.sh/skills/gitgoodordietrying-cicd-pipeline |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/cicd-pipeline |
| **安全评级** | 🟢 Low |

## 功能概述
- 为 Node.js、Python、Go 等项目生成 CI/CD 工作流
- 配置自动测试、部署和发布流程
- 管理 Secrets 和环境变量
- 设置矩阵构建（跨平台测试）
- CI 缓存和并行优化
- 排查失败的 CI 工作流

## 使用场景
- 为新项目快速搭建 CI/CD 流水线
- 调试失败的 GitHub Actions 工作流
- 优化 CI 构建速度和资源使用

## 依赖和前提条件
- `gh` CLI 和 `git`
- GitHub 仓库

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含各种 CI/CD 模板 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，生成 YAML 配置文件 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外泄风险 |
| SEC-03 凭证获取 | 🟢 Safe | 指导使用 GitHub Secrets，不硬编码凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 引用的 Actions 均为官方/知名来源 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅在 .github/workflows/ 创建 YAML |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯指令型 CI/CD 配置生成器，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
