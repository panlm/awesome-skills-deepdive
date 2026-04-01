# LLM Router Gateway

> 统一 LLM 网关——一个 API 密钥访问 70+ AI 模型，支持路由到 GPT、Claude、Gemini、Qwen、Deepseek、Grok 等。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LLM Router Gateway |
| **作者** | bowen-dotcom |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/bowen-dotcom-aisa-llm-router-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bowen-dotcom/aisa-llm-router-skill |
| **安全评级** | 🔴 High |

## 功能概述
- 通过单一 API 密钥访问 70+ 大语言模型
- 支持 GPT、Claude、Gemini、Qwen、Deepseek、Grok 等主流模型
- 提供文本聊天补全和流式响应
- 支持视觉分析（图片理解）功能
- 提供 Python 客户端脚本，开箱即用
- 统一的 API 接口，简化多模型集成

## 使用场景
- 需要在不同 LLM 之间灵活切换而不修改代码
- 希望通过统一接口对比不同模型的输出质量
- 构建需要多模型能力的 AI Agent 应用

## 依赖和前提条件
- 需要 Python 和 pip
- 需要 `AISA_API_KEY` 环境变量

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
