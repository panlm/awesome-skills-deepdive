# communicate

> 在聊天中即时启动和使用本地或 Hugging Face 模型，提供 OpenAI 兼容端点

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | communicate |
| **作者** | kenblive |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/kenblive-communicate |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kenblive/communicate |
| **安全评级** | 🟢 Low |

## 功能概述
- 一键启动本地或 Hugging Face 模型服务器
- 使用 vLLM 在本地部署模型，提供 OpenAI API 兼容端点
- 支持直接在聊天中与运行中的模型对话
- 支持张量并行（tp）和数据类型（dtype）配置
- 提供服务器状态检查和停止功能
- 支持自定义 IP 和端口设置

## 使用场景
- 快速测试和对比不同的 Hugging Face 模型效果
- 在本地搭建私有 AI 推理服务器用于开发调试
- 通过聊天界面便捷地管理和交互多个模型实例

## 依赖和前提条件
- bash、curl
- vLLM（用于模型推理服务）
- URL 环境变量配置

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
