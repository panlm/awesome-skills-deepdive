# Audio Processing (Iyeque)

> 专业音频处理工具，支持转码、分割、合并和格式转换

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Audio Processing (Iyeque) |
| **作者** | iyeque |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/iyeque-iyeque-audio-processing |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iyeque/iyeque-audio-processing |
| **安全评级** | 🟢 Low |

## 功能概述
- 支持多种音频格式之间的转码和转换
- 提供音频文件的分割和合并功能
- 支持音频元数据的读取和编辑
- 提供音频波形分析和可视化
- 支持批量音频文件处理
- 可调整音频的采样率、比特率等参数

## 使用场景
- 批量处理播客或会议录音的格式转换
- 将长音频文件按时间或内容分割成多个片段
- 音频项目中的自动化后期处理流程

## 依赖和前提条件
- FFmpeg 或相关音频处理库
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
