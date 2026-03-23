# Music Generator

> 根据结构化作曲计划生成高质量音乐，带自动质量验证和失败重试机制

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Music Generator |
| **作者** | wells1137 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/wells1137-music-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wells1137/music-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- 接收结构化的作曲计划（Composition Plan）并生成音频文件
- 使用 AI 音乐模型生成高质量音频
- 自动验证输出音频质量
- 生成失败时自动重试，确保最终输出符合要求
- 作为音乐创作工作流中的执行引擎
- 支持自定义作曲参数和风格配置

## 使用场景
- 根据创意设计规格自动生成背景音乐
- 批量生成不同风格的音乐素材用于内容创作
- 在音乐创作 pipeline 中作为自动化执行环节

## 依赖和前提条件
- AI 音乐生成模型
- 音频处理相关依赖

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
