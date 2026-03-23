# SiliconFlow Image Gen

> 使用 SiliconFlow API 生成图片，支持 FLUX.1、Stable Diffusion 等多种模型

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | SiliconFlow Image Gen |
| **作者** | lilei0311 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lilei0311-siliconflow-image-gen |

## 功能概述
- 支持多种图像生成模型：FLUX.1-schnell（免费）、FLUX.1-dev、Stable Diffusion 3.5
- 自动检测 API Key：从环境变量或 OpenClaw 配置文件读取
- 生成图片后自动下载保存到本地
- 支持命令行指定模型和输出路径
- 专为 OpenClaw Agent 集成设计，可通过自然语言触发图片生成

## 使用场景
- 通过文字描述快速生成插图、概念图或创意素材
- AI Agent 在对话中根据用户需求实时生成图片并返回
- 需要对比不同模型（免费 vs 付费）生成效果的图像创作场景

## 依赖和前提条件
- 环境变量 `SILICONFLOW_API_KEY`：SiliconFlow API 密钥（或配置在 `~/.openclaw/openclaw.json` 中）
- Python 3
- 通过 ClawHub 安装：`npx clawhub install siliconflow-image-gen`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
