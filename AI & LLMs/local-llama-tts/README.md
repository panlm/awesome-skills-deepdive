# Local Llama TTS

> 基于本地 Llama 模型的文本转语音服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Local Llama TTS |
| **作者** | wuxxin |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/wuxxin-local-llama-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wuxxin/local-llama-tts |
| **安全评级** | 🟢 Low |

## 功能概述
- 使用本地部署的 Llama 模型进行文本转语音
- 无需云端 API，完全本地化运行保护隐私
- 支持多种语音风格和音色选择
- 提供低延迟的实时语音合成
- 支持自定义语音参数调节

## 使用场景
- 在隐私敏感场景中使用本地 TTS 避免数据外传
- 为 AI 助手添加语音输出能力，提升交互体验
- 离线环境下的文本转语音需求

## 依赖和前提条件
- 本地 Llama TTS 模型
- 足够的 GPU/CPU 计算资源
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
