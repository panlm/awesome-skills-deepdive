# ModelReady

> 在聊天中即时启动本地或 Hugging Face 模型，无需离开对话界面

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ModelReady |
| **作者** | carol-gutianle |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/carol-gutianle-modelready |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/carol-gutianle/modelready |
| **安全评级** | 🟢 Low |

## 功能概述
- 一键启动本地或 Hugging Face 模型
- 将模型转化为 OpenAI 兼容的运行端点
- 直接在对话中与本地运行的模型聊天
- 使用 vLLM 在本地提供模型服务
- 暴露标准 OpenAI 格式的 API 端点

## 使用场景
- 快速测试和交互 Hugging Face 上的新模型
- 在本地部署私有模型并通过 OpenClaw 进行对话
- 开发阶段快速验证不同模型的表现

## 依赖和前提条件
- bash、curl 命令行工具
- URL 环境变量（模型端点）
- vLLM 本地安装

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
