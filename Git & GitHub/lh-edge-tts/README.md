# LH Edge TTS

> 使用 Microsoft Edge 神经网络 TTS 服务将文本转换为语音，支持多语言、多音色和字幕生成。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LH Edge TTS |
| **作者** | liuhedev |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/liuhedev-lh-edge-tts |

## 功能概述
- 使用 Python edge-tts 生成高质量神经网络语音
- 支持多种语言和音色选择（如中文小晓、英文 Aria 等）
- 可调节语速、音调和音量
- 支持生成 SRT/VTT 字幕文件
- 支持从文件读取文本进行批量转换
- 可设置代理和超时参数
- 自动过滤 TTS 关键词后进行转换

## 使用场景
- 将文档或报告转为音频，方便通勤或多任务场景收听
- 为视频内容快速生成旁白配音和同步字幕
- 为无障碍访问需求提供语音输出

## 依赖和前提条件
- Python 3
- `edge-tts` Python 包（需安装：`pip install edge-tts`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
