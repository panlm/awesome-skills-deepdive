# One API key. 70+ models. Route requests to GPT, Claude, Gemini, Qwen, Deepseek, Grok and more.

> 统一 LLM 网关——一个 API 密钥访问 70+ AI 模型，支持路由到 GPT、Claude、Gemini、Qwen、Deepseek、Grok 等。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | One API key. 70+ models. Route requests to GPT, Claude, Gemini, Qwen, Deepseek, Grok and more. |
| **作者** | renning22 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/renning22-asia-llm-router-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/renning22/asia-llm-router-skills |
| **安全评级** | 🔴 High |

## 功能概述
- 通过单一 API 密钥统一访问 70+ 大语言模型
- 支持 GPT、Claude、Gemini、Qwen、Deepseek、Grok 等主流模型
- 提供聊天补全和流式响应功能
- 支持视觉理解（图片分析）
- 提供完整的 Python 客户端脚本
- 统一 API 接口降低多模型集成复杂度

## 使用场景
- 在一个项目中需要使用多个不同的 LLM 模型
- 快速对比不同模型在同一任务上的表现
- 为 AI Agent 提供统一的模型访问网关

## 依赖和前提条件
- 需要 Python / pip
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
