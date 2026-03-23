# Zhipu AI TTS

> 基于智谱 AI（BigModel）GLM-TTS 模型的中文语音合成工具，支持 7 种音色和语速调节

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zhipu AI TTS |
| **作者** | franklu0819-lang |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/franklu0819-lang-zhipu-tts |

## 功能概述
- 将中文文本转换为自然流畅的语音（24000 Hz 高采样率）
- 提供 7 种不同音色人设：彤彤、锤锤、小陈、Jam、Kazi、Douji、Luodo
- 支持 0.5x 到 2.0x 语速调节
- 支持 WAV 和 PCM 两种输出格式
- 单次最长支持 1024 个字符
- 针对普通话合成深度优化

## 使用场景
- 有声读物制作、游戏角色配音和视频旁白生成
- 智能客服和公告播报系统的语音合成
- 需要多种中文音色选择的语音内容生产

## 依赖和前提条件
- `jq` JSON 处理工具（`sudo apt-get install jq`）
- 环境变量 `ZHIPU_API_KEY`：智谱 AI 平台 API 密钥
- Bash 脚本运行环境

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
