# Screen Vision

> 利用 AI 视觉能力捕获和理解屏幕内容

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Screen Vision |
| **作者** | ls18166407597-design |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ls18166407597-design-screen-vision |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ls18166407597-design/screen-vision |
| **安全评级** | 🟢 Low |

## 功能概述
- 捕获和分析屏幕截图内容
- 使用 AI 视觉模型理解屏幕界面
- 支持 OCR 文字识别和提取
- 实现屏幕内容的智能描述和交互
- 适用于辅助功能和自动化测试
- 支持多平台屏幕截图获取

## 使用场景
- 让 AI 助手「看到」屏幕内容并提供操作建议
- 自动化 UI 测试时捕获和分析界面状态
- 为视障用户提供屏幕内容语音描述

## 依赖和前提条件
- 无特殊依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
