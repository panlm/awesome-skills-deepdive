# ComfyUI TTS

> 使用 ComfyUI 的 Qwen-TTS 服务生成语音音频，在需要文本转语音或语音生成时调用。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ComfyUI TTS |
| **作者** | yhsi5358 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/yhsi5358-comfyui-tts |

## 功能概述
- 基础文本转语音：输入文本即可生成语音音频文件
- 支持多种语音角色（Girl/Boy 等）和说话风格（Emotional/Neutral 等）
- 提供三种模型尺寸选择：0.5B（快速）、1.7B（默认）、3B（高质量）
- 可调节生成参数：temperature、top-p、top-k 采样控制
- 自定义输出文件路径
- 完整工作流：构建 ComfyUI Workflow JSON → 提交任务 → 等待完成 → 下载音频

## 使用场景
- 将中文或多语言文本转换为自然语音音频
- 为内容创作生成不同角色和风格的配音
- 结合 ComfyUI 工作流进行批量语音生成

## 依赖和前提条件
- 运行中的 ComfyUI 服务器（含 Qwen-TTS 模型）
- curl、jq
- 环境变量：`COMFYUI_HOST`（默认 localhost）、`COMFYUI_PORT`（默认 8188）、`COMFYUI_OUTPUT_DIR`（可选）

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
