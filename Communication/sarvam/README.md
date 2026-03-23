# Sarvam AI

> 使用 Sarvam AI 进行印度语言文字转语音、语音转文字和翻译

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sarvam AI |
| **作者** | iammhk |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/iammhk-sarvam |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iammhk/sarvam |
| **安全评级** | 🔴 High |

## 功能概述
- 印度多语言文字转语音（TTS）合成
- 印度语言语音转文字（STT）识别
- 印度语言间的文本翻译
- 支持印地语、泰米尔语、泰卢固语等多种印度语言
- 高质量本地化语音生成

## 使用场景
- 印度语言内容的语音合成和朗读
- 印度语言语音消息的文字转录
- 印度语言间的文档翻译

## 依赖和前提条件
- Sarvam AI API 密钥
- 配置语言和语音偏好设置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，4 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
